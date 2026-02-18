#!/usr/bin/env python3
"""
Spec-to-YAML Auto-Generator
============================
Reads cached Swagger 2.0 specs from _shared/specs/ and produces draft
YAML operation definitions for every endpoint.  Each YAML can then be
fed to the existing ``generate.py`` to produce Py / PS1 / Bash scripts
plus tests and fixtures.

Usage:
    python _generator/spec_to_yaml.py           # generate all
    python _generator/spec_to_yaml.py --domain git   # single domain
    python _generator/spec_to_yaml.py --dry-run      # preview only
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
SPEC_DIR = ROOT / "_shared" / "specs"
DEFS_DIR = ROOT / "_generator" / "definitions"
INVENTORY = ROOT / "_research" / "api_specs_full.json"

# ---------------------------------------------------------------------------
# Domain → directory name mapping (PascalCase as used in repo layout)
# ---------------------------------------------------------------------------
DOMAIN_DIR_MAP: Dict[str, str] = {
    "account": "Account",
    "advancedSecurity": "AdvancedSecurity",
    "approvalsAndChecks": "ApprovalsAndChecks",
    "artifacts": "Artifacts",
    "artifactsPackageTypes": "ArtifactsPackageTypes",
    "audit": "Audit",
    "build": "Build",
    "core": "Core",
    "dashboard": "Dashboard",
    "delegatedAuth": "DelegatedAuth",
    "distributedTask": "DistributedTask",
    "environments": "Environments",
    "extensionManagement": "ExtensionManagement",
    "favorite": "Favorite",
    "git": "Git",
    "governance": "Governance",
    "graph": "Graph",
    "hooks": "Hooks",
    "ims": "IMS",
    "memberEntitlementManagement": "MemberEntitlementManagement",
    "notification": "Notification",
    "operations": "Operations",
    "permissionsReport": "PermissionsReport",
    "pipelines": "Pipelines",
    "policy": "Policy",
    "processDefinitions": "ProcessDefinitions",
    "processadmin": "ProcessAdmin",
    "processes": "Processes",
    "profile": "Profile",
    "release": "Release",
    "resourceUsage": "ResourceUsage",
    "search": "Search",
    "security": "Security",
    "securityRoles": "SecurityRoles",
    "serviceEndpoint": "ServiceEndpoint",
    "status": "Status",
    "symbol": "Symbol",
    "test": "Test",
    "testPlan": "TestPlan",
    "testResults": "TestResults",
    "tfvc": "TFVC",
    "tokenAdmin": "TokenAdmin",
    "tokenAdministration": "TokenAdministration",
    "tokens": "Tokens",
    "wiki": "Wiki",
    "wit": "WorkItemTracking",
    "work": "Work",
}

# ---------------------------------------------------------------------------
# HTTP method → PS verb mapping
# ---------------------------------------------------------------------------
METHOD_VERB: Dict[str, str] = {
    "GET": "Get",
    "POST": "New",
    "PUT": "Set",
    "PATCH": "Update",
    "DELETE": "Remove",
    "HEAD": "Test",
    "OPTIONS": "Get",
}

# ---------------------------------------------------------------------------
# Parameter name → env var mapping overrides
# ---------------------------------------------------------------------------
PARAM_ENV_OVERRIDES: Dict[str, str] = {
    "organization": "__SKIP__",
    "project": "PROJECT_ID",
    "repositoryId": "REPO_ID",
    "buildId": "BUILD_ID",
    "definitionId": "DEFINITION_ID",
    "pipelineId": "PIPELINE_ID",
    "runId": "RUN_ID",
    "pullRequestId": "PULL_REQUEST_ID",
    "commitId": "COMMIT_ID",
    "threadId": "THREAD_ID",
    "workItemId": "WORK_ITEM_ID",
    "id": "RESOURCE_ID",
    "queryId": "QUERY_ID",
    "wikiIdentifier": "WIKI_IDENTIFIER",
    "groupId": "GROUP_ID",
    "environmentId": "ENVIRONMENT_ID",
    "poolId": "POOL_ID",
    "configurationId": "CONFIGURATION_ID",
    "subscriptionId": "SUBSCRIPTION_ID",
    "releaseId": "RELEASE_ID",
    "iterationId": "ITERATION_ID",
    "team": "TEAM_ID",
    "feedId": "FEED_ID",
    "packageId": "PACKAGE_ID",
    "versionId": "VERSION_ID",
    "planId": "PLAN_ID",
    "suiteId": "SUITE_ID",
    "testCaseId": "TEST_CASE_ID",
    "testPointIds": "TEST_POINT_IDS",
    "secretFieldName": "SECRET_FIELD_NAME",
    "endpointId": "ENDPOINT_ID",
    "typeId": "TYPE_ID",
    "requestId": "REQUEST_ID",
    "debugEntryId": "DEBUG_ENTRY_ID",
    "designtimeId": "DESIGNTIME_ID",
    "processId": "PROCESS_ID",
    "witRefName": "WIT_REF_NAME",
    "fieldRefName": "FIELD_REF_NAME",
    "groupName": "GROUP_NAME",
    "pageId": "PAGE_ID",
    "sectionId": "SECTION_ID",
    "stateId": "STATE_ID",
    "ruleId": "RULE_ID",
    "behaviorRefName": "BEHAVIOR_REF_NAME",
    "listId": "LIST_ID",
    "widgetId": "WIDGET_ID",
    "ownerId": "OWNER_ID",
    "memberId": "MEMBER_ID",
    "$top": "TOP",
    "$skip": "SKIP",
    "api-version": "__SKIP__",
}


# ===========================================================================
# Helpers
# ===========================================================================

def _load_spec(path: str) -> dict:
    """Load a Swagger JSON spec, handling BOM."""
    raw = open(path, "rb").read()
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    return json.loads(raw.decode("utf-8"))


def _safe_text(text: str, max_len: int = 120) -> str:
    """Sanitize text for safe embedding in generated code string literals.
    
    Removes newlines, escapes quotes, and truncates.
    """
    text = " ".join(text.split())  # flatten newlines/extra whitespace
    text = text.replace('"', "'").replace("\\", "/").replace("`", "'")
    text = text.replace("$", "").replace("!", "")
    if len(text) > max_len:
        text = text[:max_len - 3] + "..."
    return text


def _snake(name: str) -> str:
    """Convert camelCase / PascalCase to snake_case."""
    s1 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    s2 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1)
    return s2.lower().replace("-", "_").replace(".", "_").replace("$", "").replace(" ", "_")


def _pascal(name: str) -> str:
    """Convert snake_case / camelCase to PascalCase."""
    return "".join(w.capitalize() for w in re.split(r"[_\-. ]", name) if w)


def _env_var(param_name: str) -> str:
    """Convert a parameter name to an env var name."""
    if param_name in PARAM_ENV_OVERRIDES:
        return PARAM_ENV_OVERRIDES[param_name]
    return _snake(param_name).upper()


def _extract_operation_parts(operation_id: str) -> Tuple[str, str]:
    """
    Parse operationId like 'Pull Requests_Get Pull Request'
    or 'Repositories_List' into (resource, action).
    """
    if "_" in operation_id:
        parts = operation_id.split("_", 1)
        resource = parts[0].strip()
        action = parts[1].strip()
    else:
        resource = operation_id
        action = operation_id
    return resource, action


def _guess_ps_verb(method: str, action: str) -> str:
    """Determine PowerShell verb from HTTP method and action name."""
    action_lower = action.lower()
    if "list" in action_lower or "get all" in action_lower:
        return "Get"  # List operations still use Get- in PS
    if "create" in action_lower and method == "POST":
        return "New"
    if "delete" in action_lower or "remove" in action_lower:
        return "Remove"
    if "update" in action_lower:
        return "Update"
    if "set" in action_lower:
        return "Set"
    if "add" in action_lower:
        return "Add"
    if "query" in action_lower or "search" in action_lower:
        return "Invoke"
    if "run" in action_lower or "queue" in action_lower or "trigger" in action_lower:
        return "Start"
    return METHOD_VERB.get(method, "Invoke")


def _guess_ps_noun(resource: str, action: str, domain_dir: str) -> str:
    """Build PS noun from resource/action/domain."""
    # Clean up resource name
    noun = _pascal(resource.replace(" ", ""))
    # For list operations, keep plural; for get/create etc. use singular
    action_lower = action.lower()
    if not any(k in action_lower for k in ["list", "get all", "query", "search"]):
        # Try to singularize simple cases
        if noun.endswith("ies"):
            noun = noun[:-3] + "y"
        elif noun.endswith("ses"):
            pass  # keep as-is (e.g. Processes)
        elif noun.endswith("s") and not noun.endswith("ss"):
            noun = noun[:-1]
    return noun


def _operation_name(method: str, action: str, resource: str) -> str:
    """Generate a snake_case operation name."""
    action_lower = action.lower().replace(" ", "_")
    # Clean up common patterns
    action_lower = re.sub(r"^(get|list|create|update|delete|add|remove|set|query|run|queue)_", "", action_lower)
    
    verb_map = {
        "GET": "get",
        "POST": "create",
        "PUT": "set",
        "PATCH": "update",
        "DELETE": "delete",
        "HEAD": "head",
    }
    
    # Determine verb
    action_text = action.lower()
    if "list" in action_text or "get all" in action_text:
        verb = "list"
    elif "get" in action_text:
        verb = "get"
    elif "create" in action_text or "add" in action_text:
        verb = "create"
    elif "update" in action_text:
        verb = "update"
    elif "delete" in action_text or "remove" in action_text:
        verb = "delete"
    elif "query" in action_text or "search" in action_text:
        verb = "query"
    elif "run" in action_text or "queue" in action_text:
        verb = "run"
    elif "set" in action_text:
        verb = "set"
    else:
        verb = verb_map.get(method, "call")

    # Build the rest from action, cleaning up
    # Remove verb prefix from action
    rest = re.sub(
        r"^(get|list|create|update|delete|add|remove|set|query|run|queue|search)\s*",
        "",
        action.lower(),
    ).strip()
    
    if not rest:
        rest = _snake(resource)
    else:
        rest = _snake(rest.replace(" ", "_"))

    # Clean up duplicate words
    name = f"{verb}_{rest}"
    # Collapse multiple underscores, strip leading/trailing
    name = re.sub(r"_+", "_", name).strip("_")
    # Remove consecutive duplicate segments
    parts = name.split("_")
    deduped = [parts[0]]
    for p in parts[1:]:
        if p != deduped[-1]:
            deduped.append(p)
    return "_".join(deduped)


def _url_path_from_swagger(swagger_path: str) -> str:
    """
    Convert Swagger path like '/{organization}/{project}/_apis/git/repositories'
    to a url_path like '_apis/git/repositories' with {param_name} placeholders
    converted to snake_case.
    """
    # Strip the org/project prefix
    path = swagger_path
    path = re.sub(r"^/\{organization\}", "", path)
    path = re.sub(r"^/\{project\}", "", path)
    path = path.lstrip("/")
    
    # Convert {camelCase} to {snake_case}
    def _convert_param(m):
        name = m.group(1)
        if name in ("organization", "project"):
            return ""
        return "{" + _snake(name) + "}"
    
    path = re.sub(r"\{([^}]+)\}", _convert_param, path)
    # Clean up double slashes
    path = re.sub(r"//+", "/", path)
    return path


def _is_project_scoped(swagger_path: str) -> bool:
    """Check if the path includes {project}."""
    return "/{project}" in swagger_path or "/{project}/" in swagger_path


def _success_status(method: str, responses: dict) -> int:
    """Determine the success status code from responses."""
    if "201" in responses:
        return 201
    if "204" in responses:
        return 204
    if "200" in responses:
        return 200
    # Fallback
    for code in sorted(responses.keys()):
        if code.startswith("2"):
            return int(code)
    return 200


def _build_docs_url(domain: str, resource: str, action: str) -> str:
    """Build a plausible MS Learn docs URL."""
    domain_slug = _snake(domain).replace("_", "-")
    resource_slug = _snake(resource).replace("_", "-")
    action_slug = _snake(action).replace("_", "-")
    return (
        f"https://learn.microsoft.com/en-us/rest/api/azure/devops/"
        f"{domain_slug}/{resource_slug}/{action_slug}"
        f"?view=azure-devops-rest-7.2"
    )


def _resolve_schema_ref(ref: str, definitions: dict) -> dict:
    """Resolve a $ref to a definition."""
    if not ref or not ref.startswith("#/definitions/"):
        return {}
    name = ref.split("/")[-1]
    return definitions.get(name, {})


def _build_fixture(schema: dict, definitions: dict, depth: int = 0) -> Any:
    """Build a sample fixture from a JSON schema definition."""
    if depth > 3:
        return {}
    
    ref = schema.get("$ref")
    if ref:
        schema = _resolve_schema_ref(ref, definitions)
        if not schema:
            return {}
    
    schema_type = schema.get("type", "object")
    
    if schema_type == "string":
        fmt = schema.get("format", "")
        if fmt == "date-time":
            return "2026-01-15T10:30:00Z"
        if fmt == "uuid":
            return "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        enum = schema.get("enum")
        if enum:
            return enum[0]
        return "sample-string"
    elif schema_type == "integer":
        return 1
    elif schema_type == "number":
        return 1.0
    elif schema_type == "boolean":
        return True
    elif schema_type == "array":
        items = schema.get("items", {})
        return [_build_fixture(items, definitions, depth + 1)]
    elif schema_type == "object" or "properties" in schema:
        props = schema.get("properties", {})
        result = {}
        # Only include first 8 properties to keep fixtures manageable
        for i, (name, prop_schema) in enumerate(props.items()):
            if i >= 8:
                break
            if name.startswith("_"):
                continue
            result[name] = _build_fixture(prop_schema, definitions, depth + 1)
        return result
    return {}


def _build_version_guard_keys(schema: dict, definitions: dict) -> List[str]:
    """Pick 2-3 good version guard keys from a response schema."""
    ref = schema.get("$ref")
    if ref:
        schema = _resolve_schema_ref(ref, definitions)
    
    props = list(schema.get("properties", {}).keys())
    # Prefer id, name, then other scalar properties
    preferred = ["id", "name", "count", "value"]
    keys = []
    for p in preferred:
        if p in props:
            keys.append(p)
        if len(keys) >= 2:
            break
    # Fill with first available props
    for p in props:
        if p not in keys and not p.startswith("_"):
            keys.append(p)
        if len(keys) >= 2:
            break
    return keys


def _output_mode_heuristic(method: str, action: str, has_list_response: bool) -> str:
    """Determine output mode: json, table, or message."""
    if has_list_response:
        return "table"
    if method in ("POST", "PUT", "PATCH"):
        return "message"
    if method == "DELETE":
        return "message"
    if method == "GET" and "list" not in action.lower():
        return "message"
    return "json"


def _table_columns_from_schema(schema: dict, definitions: dict) -> List[str]:
    """Pick table columns from the items schema of a list response."""
    ref = schema.get("$ref")
    if ref:
        schema = _resolve_schema_ref(ref, definitions)
    
    props = list(schema.get("properties", {}).keys())
    # Prefer id, name, description, state/status, then others
    preferred = ["id", "name", "description", "state", "status", "url", "type"]
    cols = []
    for p in preferred:
        if p in props:
            cols.append(p)
        if len(cols) >= 4:
            break
    if len(cols) < 2:
        for p in props:
            if p not in cols and not p.startswith("_"):
                cols.append(p)
            if len(cols) >= 4:
                break
    return cols


# ===========================================================================
# Main generator
# ===========================================================================

def generate_yaml_for_endpoint(
    domain_key: str,
    host: str,
    swagger_path: str,
    method: str,
    details: dict,
    definitions: dict,
    api_version: str,
) -> Optional[dict]:
    """
    Generate a YAML-ready dict for a single endpoint.
    Returns None if the endpoint should be skipped.
    """
    operation_id = details.get("operationId", "")
    if not operation_id:
        return None

    resource_raw, action_raw = _extract_operation_parts(operation_id)
    domain_dir = DOMAIN_DIR_MAP.get(domain_key, _pascal(domain_key))
    resource_dir = _pascal(resource_raw.replace(" ", "_"))

    # Operation name
    op_name = _operation_name(method, action_raw, resource_raw)
    
    # PS naming
    ps_verb = _guess_ps_verb(method, action_raw)
    ps_noun = _guess_ps_noun(resource_raw, action_raw, domain_dir)
    
    # URL path
    url_path = _url_path_from_swagger(swagger_path)
    
    # Project scoped?
    project_scoped = _is_project_scoped(swagger_path)
    
    # Parameters
    params = []
    for p in details.get("parameters", []):
        p_name = p.get("name", "")
        p_in = p.get("in", "")
        
        if not p_name or p_in not in ("path", "query"):
            continue
        
        env = _env_var(p_name)
        if env == "__SKIP__":
            continue
        
        # Skip query params that are optional pagination/filtering
        if p_in == "query" and not p.get("required", False):
            continue
        
        snake_name = _snake(p_name)
        # Check if this param is in the URL path
        if "{" + snake_name + "}" not in url_path and p_in == "path":
            # It's a path param but not in our cleaned URL — skip (org/project)
            continue
        
        params.append({
            "name": snake_name,
            "env_var": env,
            "description": _safe_text((p.get("description") or f"{p_name}").strip(), 100),
            "required": p.get("required", p_in == "path"),
        })
    
    # Body fields (for POST/PATCH/PUT)
    body_fields = []
    if method in ("POST", "PATCH", "PUT"):
        for p in details.get("parameters", []):
            if p.get("in") == "body":
                body_schema = p.get("schema", {})
                ref = body_schema.get("$ref")
                if ref:
                    body_schema = _resolve_schema_ref(ref, definitions)
                body_props = body_schema.get("properties", {})
                for prop_name, prop_schema in list(body_props.items())[:6]:
                    if prop_name.startswith("_"):
                        continue
                    body_fields.append({
                        "json_path": prop_name,
                        "source": f"param:{_snake(prop_name)}",
                        "description": _safe_text((prop_schema.get("description") or prop_name), 80),
                    })
                    # Add a corresponding param for each body field
                    snake_body = _snake(prop_name)
                    env_body = _env_var(prop_name)
                    if env_body != "__SKIP__" and not any(
                        bp["name"] == snake_body for bp in params
                    ):
                        params.append({
                            "name": snake_body,
                            "env_var": env_body,
                            "description": _safe_text((prop_schema.get("description") or prop_name).strip(), 100),
                            "required": prop_name in body_schema.get("required", []),
                            "cli_flag": f"--{snake_body.replace('_', '-')}",
                        })
                break
    
    # Response handling
    responses = details.get("responses", {})
    success_code = _success_status(method, responses)
    
    # Response schema for version guard + fixture
    success_resp = responses.get(str(success_code), {})
    resp_schema = success_resp.get("schema", {})
    
    # Check if this is a list response (has "value" array)
    is_list = False
    list_key = "value"
    resolved_resp = resp_schema
    if resp_schema.get("$ref"):
        resolved_resp = _resolve_schema_ref(resp_schema["$ref"], definitions)
    if "value" in resolved_resp.get("properties", {}):
        is_list = True
    elif resp_schema.get("type") == "array":
        is_list = True
        list_key = "value"
    
    # Version guard keys
    guard_keys = _build_version_guard_keys(resp_schema, definitions)
    
    # Output mode
    output_mode = _output_mode_heuristic(method, action_raw, is_list)
    
    # Table columns
    table_columns = []
    if is_list and "value" in resolved_resp.get("properties", {}):
        value_schema = resolved_resp["properties"]["value"]
        items_schema = value_schema.get("items", {})
        table_columns = _table_columns_from_schema(items_schema, definitions)
    
    # Build fixtures
    fixture_success = None
    if resp_schema:
        fixture_success = _build_fixture(resp_schema, definitions)
        if isinstance(fixture_success, dict) and not fixture_success:
            fixture_success = None
    
    fixture_error_404 = {
        "message": f"{resource_raw} not found",
        "typeKey": f"{_pascal(resource_raw)}NotFoundException",
        "errorCode": 0,
    }
    
    # Output message
    output_message = ""
    if output_mode == "message" and success_code != 204:
        # Try to build from response properties
        if fixture_success and isinstance(fixture_success, dict):
            if "name" in fixture_success:
                output_message = f"{resource_raw}: {{name}}"
            elif "id" in fixture_success:
                output_message = f"{resource_raw} ID: {{id}}"
    if success_code == 204:
        output_message = f"{resource_raw} operation completed successfully."
    
    # Description
    synopsis = (details.get("description") or f"{action_raw} for {resource_raw}").strip()
    # Flatten to single line — newlines break string literals in generated code
    synopsis = " ".join(synopsis.split())
    # Truncate synopsis to first sentence
    if ". " in synopsis:
        synopsis = synopsis[:synopsis.index(". ") + 1]
    # Apply full sanitization
    synopsis = _safe_text(synopsis, 120)
    
    # Build the YAML dict
    yaml_dict: Dict[str, Any] = {
        "domain": domain_dir,
        "resource": resource_dir,
        "operation": op_name,
        "ps_verb": ps_verb,
        "ps_noun": ps_noun,
        "http_method": method,
        "url_path": url_path,
        "api_version": api_version,
        "docs_url": _build_docs_url(domain_key, resource_raw, action_raw),
        "synopsis": synopsis,
        "project_scoped": project_scoped,
    }
    
    if host != "dev.azure.com":
        yaml_dict["base_host"] = host
    
    if params:
        yaml_dict["params"] = params
    
    if body_fields:
        yaml_dict["body_fields"] = body_fields
    
    if guard_keys:
        yaml_dict["version_guard_keys"] = guard_keys
    
    if success_code != 200:
        yaml_dict["success_status"] = success_code
    
    yaml_dict["output_mode"] = output_mode
    if output_message:
        yaml_dict["output_message"] = output_message
    if table_columns:
        yaml_dict["table_columns"] = table_columns
    if list_key != "value" and is_list:
        yaml_dict["list_key"] = list_key
    
    if fixture_success:
        yaml_dict["fixture_success"] = fixture_success
    else:
        # Provide minimal fallback fixture so tests have something to mock
        yaml_dict["fixture_success"] = {"status": "ok"}
    yaml_dict["fixture_error_404"] = fixture_error_404
    
    return yaml_dict


def process_spec_file(spec_path: str, domain_key: str) -> List[Tuple[str, dict]]:
    """
    Process a single Swagger spec file and return list of
    (yaml_filename, yaml_dict) pairs.
    """
    spec = _load_spec(spec_path)
    host = spec.get("host", "dev.azure.com")
    api_version_raw = spec.get("info", {}).get("version", "7.2")
    # Normalize version: use just the major.minor
    api_version = re.sub(r"-.*$", "", api_version_raw)
    if not api_version:
        api_version = "7.2"
    
    definitions = spec.get("definitions", {})
    results = []
    
    for swagger_path, methods in spec.get("paths", {}).items():
        for method_lower, details in methods.items():
            method = method_lower.upper()
            if method not in ("GET", "POST", "PUT", "PATCH", "DELETE"):
                continue
            
            yaml_dict = generate_yaml_for_endpoint(
                domain_key, host, swagger_path, method, details, definitions, api_version,
            )
            if yaml_dict is None:
                continue
            
            # Build filename
            op_name = yaml_dict["operation"]
            domain_prefix = _snake(domain_key)
            yaml_filename = f"{domain_prefix}_{op_name}.yaml"
            # Sanitize filename (no spaces, no special chars)
            yaml_filename = re.sub(r"[^a-z0-9_.]", "_", yaml_filename)
            yaml_filename = re.sub(r"_+", "_", yaml_filename)
            
            results.append((yaml_filename, yaml_dict))
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Generate YAML definitions from Swagger specs")
    parser.add_argument("--domain", help="Process only this domain (e.g., 'git', 'build')")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, don't write files")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing YAML files")
    args = parser.parse_args()
    
    # Discover all cached spec files
    cache_files = sorted(glob.glob(str(SPEC_DIR / ".cache_*.json")))
    
    if not cache_files:
        print("ERROR: No cached spec files found in _shared/specs/", file=sys.stderr)
        sys.exit(1)
    
    # Map spec files to domains
    # Format: .cache_<domain>.json (old) or .cache_<domain>_<specfile>.json (new)
    spec_domain_map: Dict[str, List[str]] = {}
    for cf in cache_files:
        basename = os.path.basename(cf)
        # Remove .cache_ prefix and .json suffix
        name = basename.replace(".cache_", "").replace(".json", "")
        # For old-style files like .cache_core.json, domain = "core"
        # For new-style like .cache_account_accounts.json, domain = "account"
        # Try to match against known domains
        matched = False
        for domain in sorted(DOMAIN_DIR_MAP.keys(), key=len, reverse=True):
            if name == domain or name.startswith(domain + "_"):
                if domain not in spec_domain_map:
                    spec_domain_map[domain] = []
                spec_domain_map[domain].append(cf)
                matched = True
                break
        if not matched:
            print(f"  SKIP: Could not map {basename} to a domain", file=sys.stderr)
    
    # Filter to requested domain
    if args.domain:
        d = args.domain.lower()
        if d not in spec_domain_map:
            print(f"ERROR: Domain '{d}' not found. Available: {sorted(spec_domain_map.keys())}", file=sys.stderr)
            sys.exit(1)
        spec_domain_map = {d: spec_domain_map[d]}
    
    # Gather existing YAML definitions to check for collisions
    existing_yamls = set()
    for yf in DEFS_DIR.glob("*.yaml"):
        existing_yamls.add(yf.name)
    
    # Process all specs
    total_generated = 0
    total_skipped = 0
    total_existing = 0
    
    DEFS_DIR.mkdir(parents=True, exist_ok=True)
    
    for domain, spec_files in sorted(spec_domain_map.items()):
        domain_results = []
        for sf in spec_files:
            domain_results.extend(process_spec_file(sf, domain))
        
        # Deduplicate by operation name (same op may appear in multiple spec files)
        seen_ops = set()
        unique_results = []
        for filename, yaml_dict in domain_results:
            op = yaml_dict["operation"]
            if op in seen_ops:
                continue
            seen_ops.add(op)
            unique_results.append((filename, yaml_dict))
        
        for filename, yaml_dict in unique_results:
            if filename in existing_yamls and not args.overwrite:
                total_existing += 1
                continue
            
            if args.dry_run:
                print(f"  [DRY-RUN] {filename}: {yaml_dict['domain']}/{yaml_dict['resource']}/{yaml_dict['operation']}")
                total_generated += 1
                continue
            
            # Write YAML
            out_path = DEFS_DIR / filename
            header = "# AUTO-GENERATED by spec_to_yaml.py — review recommended\n"
            yaml_content = yaml.dump(yaml_dict, default_flow_style=False, sort_keys=False, allow_unicode=True)
            out_path.write_text(header + yaml_content, encoding="utf-8")
            total_generated += 1
        
        if unique_results:
            count = len([r for r in unique_results if r[0] not in existing_yamls or args.overwrite])
            if count > 0:
                print(f"  {DOMAIN_DIR_MAP.get(domain, domain)}: {count} definitions")
    
    print(f"\nSummary:")
    print(f"  Generated: {total_generated}")
    print(f"  Skipped (already exist): {total_existing}")
    print(f"  Total YAML files in {DEFS_DIR}: {len(list(DEFS_DIR.glob('*.yaml')))}")


if __name__ == "__main__":
    main()
