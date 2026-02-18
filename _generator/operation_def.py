"""
Operation definition schema for the code generator.

An OperationDef is the single source of truth for an API endpoint.
All three language implementations are generated from it.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import json
import yaml
from pathlib import Path


@dataclass
class ParamDef:
    """A parameter for the API operation."""
    name: str                       # e.g., "project_id"
    env_var: str                    # e.g., "PROJECT_ID"
    description: str                # e.g., "Project name or GUID"
    required: bool = True
    cli_flag: Optional[str] = None  # e.g., "--name" (for argparse / ps param)
    ps_name: Optional[str] = None   # e.g., "ProjectId" (PascalCase for PS)
    default: Optional[str] = None


@dataclass
class BodyFieldDef:
    """A field in the request body."""
    json_path: str          # e.g., "name" or "project.id"
    source: str             # "param:<param_name>" or "literal:<value>"
    description: str = ""


@dataclass
class OperationDef:
    """
    Complete definition of an Azure DevOps API operation.

    This is the single source of truth from which Python, PowerShell,
    and Bash implementations (+ tests + fixtures) are generated.
    """
    # Identity
    domain: str             # e.g., "Core"
    resource: str           # e.g., "Teams"
    operation: str          # e.g., "list_teams" (snake_case)
    ps_verb: str            # e.g., "List" (PowerShell verb)
    ps_noun: str            # e.g., "Teams" (PowerShell noun)

    # API details
    http_method: str        # GET, POST, PATCH, PUT, DELETE
    url_path: str           # e.g., "_apis/projects/{project_id}/teams"
    api_version: str        # e.g., "7.2-preview.2"
    docs_url: str           # MS Learn link

    # Description
    synopsis: str           # One-line description
    description: str = ""   # Longer description

    # Parameters (env vars / CLI flags)
    params: List[ParamDef] = field(default_factory=list)

    # Request body (for POST/PATCH/PUT)
    body_fields: List[BodyFieldDef] = field(default_factory=list)

    # Response validation
    version_guard_keys: List[str] = field(default_factory=list)

    # Expected success status code (200, 201, 204, etc.)
    success_status: int = 200

    # Output formatting hints
    output_mode: str = "json"  # "json", "table", "message"
    output_message: str = ""   # e.g., "Repository created: {name}"
    table_columns: List[str] = field(default_factory=list)  # for table mode
    list_key: str = "value"  # JSON key holding the list in collection responses

    # Fixture: sample successful response
    fixture_success: Optional[Dict[str, Any]] = None
    fixture_error_404: Optional[Dict[str, Any]] = None

    # Whether this operation needs project scope in URL
    project_scoped: bool = False

    # Base hostname (default dev.azure.com; override for Graph, Release, etc.)
    base_host: str = "dev.azure.com"

    @property
    def ps_script_name(self) -> str:
        """PowerShell script name: Verb-Noun.ps1"""
        return f"{self.ps_verb}-{self.ps_noun}.ps1"

    @property
    def bash_script_name(self) -> str:
        """Bash script name: snake_case.sh"""
        return f"{self.operation}.sh"

    @property
    def python_script_name(self) -> str:
        """Python script name: snake_case.py"""
        return f"{self.operation}.py"

    @property
    def output_dir_path(self) -> str:
        """Relative path to the output directory: Domain/Resource/"""
        return f"{self.domain}/{self.resource}"

    @property
    def fixture_filename(self) -> str:
        """Fixture filename: operation_200.json"""
        return f"{self.operation}_{self.success_status}.json"


def load_definition(path: Path) -> OperationDef:
    """Load an operation definition from a YAML or JSON file."""
    text = path.read_text(encoding="utf-8")
    if path.suffix in (".yaml", ".yml"):
        raw = yaml.safe_load(text)
    else:
        raw = json.loads(text)

    # Parse params
    params = []
    for p in raw.get("params", []):
        params.append(ParamDef(**p))

    # Parse body fields
    body_fields = []
    for bf in raw.get("body_fields", []):
        body_fields.append(BodyFieldDef(**bf))

    return OperationDef(
        domain=raw["domain"],
        resource=raw["resource"],
        operation=raw["operation"],
        ps_verb=raw["ps_verb"],
        ps_noun=raw["ps_noun"],
        http_method=raw["http_method"],
        url_path=raw["url_path"],
        api_version=raw["api_version"],
        docs_url=raw["docs_url"],
        synopsis=raw["synopsis"],
        description=raw.get("description", ""),
        params=params,
        body_fields=body_fields,
        version_guard_keys=raw.get("version_guard_keys", []),
        success_status=raw.get("success_status", 200),
        output_mode=raw.get("output_mode", "json"),
        output_message=raw.get("output_message", ""),
        table_columns=raw.get("table_columns", []),
        list_key=raw.get("list_key", "value"),
        fixture_success=raw.get("fixture_success"),
        fixture_error_404=raw.get("fixture_error_404"),
        project_scoped=raw.get("project_scoped", False),
        base_host=raw.get("base_host", "dev.azure.com"),
    )
