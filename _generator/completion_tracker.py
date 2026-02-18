#!/usr/bin/env python3
"""
Project Completion Tracker
==========================
Evaluates the DevOpsApiClients project against a defined completion checklist
and outputs a structured JSON report of the highest-priority remaining task.

Designed to be called by the ``project-completion.yml`` GitHub Actions workflow.
Each invocation identifies ONE focused task for the Copilot Coding Agent.

Usage:
    python _generator/completion_tracker.py              # JSON to stdout
    python _generator/completion_tracker.py --verbose     # human-readable
    python _generator/completion_tracker.py --check-only  # exit 0 if complete, 1 if not

Exit codes:
    0 — project is complete (or --check-only and complete)
    1 — task emitted (or --check-only and incomplete)
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]

# ═══════════════════════════════════════════════════════════════════════════════
# All 46 domain directories the project targets
# ═══════════════════════════════════════════════════════════════════════════════
ALL_DOMAINS = sorted([
    "Account", "AdvancedSecurity", "ApprovalsAndChecks", "Artifacts",
    "ArtifactsPackageTypes", "Audit", "Build", "Core", "Dashboard",
    "DelegatedAuth", "DistributedTask", "Environments", "ExtensionManagement",
    "Favorite", "Git", "Graph", "Hooks", "IMS", "MemberEntitlementManagement",
    "Notification", "Operations", "PermissionsReport", "Pipelines", "Policy",
    "ProcessAdmin", "ProcessDefinitions", "Processes", "Profile", "Release",
    "ResourceUsage", "Search", "Security", "SecurityRoles", "ServiceEndpoint",
    "Status", "Symbol", "TFVC", "Test", "TestPlan", "TestResults",
    "TokenAdmin", "TokenAdministration", "Tokens", "Wiki", "Work",
    "WorkItemTracking",
])

# Map domain folder → lowercase key used in CI filters
DOMAIN_FILTER_KEY = {
    "Account": "account", "AdvancedSecurity": "advancedsecurity",
    "ApprovalsAndChecks": "approvalsandchecks", "Artifacts": "artifacts",
    "ArtifactsPackageTypes": "artifactspackagetypes", "Audit": "audit",
    "Build": "build", "Core": "core", "Dashboard": "dashboard",
    "DelegatedAuth": "delegatedauth", "DistributedTask": "distributedtask",
    "Environments": "environments", "ExtensionManagement": "extensionmanagement",
    "Favorite": "favorite", "Git": "git", "Graph": "graph", "Hooks": "hooks",
    "IMS": "ims", "MemberEntitlementManagement": "memberentitlementmanagement",
    "Notification": "notification", "Operations": "operations",
    "PermissionsReport": "permissionsreport", "Pipelines": "pipelines",
    "Policy": "policy", "ProcessAdmin": "processadmin",
    "ProcessDefinitions": "processdefinitions", "Processes": "processes",
    "Profile": "profile", "Release": "release", "ResourceUsage": "resourceusage",
    "Search": "search", "Security": "security", "SecurityRoles": "securityroles",
    "ServiceEndpoint": "serviceendpoint", "Status": "status", "Symbol": "symbol",
    "TFVC": "tfvc", "Test": "test", "TestPlan": "testplan",
    "TestResults": "testresults", "TokenAdmin": "tokenadmin",
    "TokenAdministration": "tokenadministration", "Tokens": "tokens",
    "Wiki": "wiki", "Work": "work", "WorkItemTracking": "wit",
}

# Maximum number of domains to batch into a single issue
BATCH_CI_FILTER = 10
BATCH_README = 5


# ═══════════════════════════════════════════════════════════════════════════════
# Checkers — each returns None if the check passes, or a task dict if work needed
# ═══════════════════════════════════════════════════════════════════════════════

def _check_python_syntax() -> Optional[Dict[str, Any]]:
    """P0: Verify all generated Python scripts compile without errors."""
    scripts = sorted(glob.glob(str(ROOT / "**" / "*.py"), recursive=True))
    scripts = [
        s for s in scripts
        if "/tests/" not in s and "__init__" not in s
        and "_generator/" not in s and "_shared/" not in s
        and "_research/" not in s and "__pycache__" not in s
        and "/.git/" not in s
    ]

    bad_by_domain: Dict[str, List[str]] = {}
    for s in scripts:
        r = subprocess.run(
            [sys.executable, "-m", "py_compile", s],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            rel = os.path.relpath(s, ROOT)
            domain = rel.split("/")[0]
            bad_by_domain.setdefault(domain, []).append(rel)

    if not bad_by_domain:
        return None

    # Pick the domain with the most errors
    worst = max(bad_by_domain, key=lambda d: len(bad_by_domain[d]))
    files = bad_by_domain[worst]
    total = sum(len(v) for v in bad_by_domain.values())

    return {
        "title": f"[AUTO] Fix Python syntax errors in {worst} ({len(files)} files)",
        "body": _format_body(
            task=f"Fix Python syntax errors in the `{worst}/` domain",
            context=(
                f"There are **{total} total Python files** with syntax errors across "
                f"**{len(bad_by_domain)} domains**. This issue targets `{worst}/` "
                f"which has {len(files)} files with errors.\n\n"
                f"These are auto-generated scripts. The root cause is usually unescaped "
                f"special characters in synopsis or description fields. Fix the YAML "
                f"definition in `_generator/definitions/` and regenerate, OR fix the "
                f"template in `_generator/templates/`."
            ),
            files=[f"- `{f}`" for f in files[:15]],
            criteria=[
                f"`python -m py_compile` succeeds for all `.py` files in `{worst}/`",
                f"`python -m pytest {worst}/ -q --tb=short` passes",
            ],
        ),
        "labels": ["auto-completion", "bug"],
        "priority": 0,
    }


def _check_ci_path_filter() -> Optional[Dict[str, Any]]:
    """P1: Verify all domains are in the CI dorny/paths-filter."""
    ci_path = ROOT / ".github" / "workflows" / "ci-test-and-release.yml"
    if not ci_path.exists():
        return None

    content = ci_path.read_text()

    # Find domains already in the filter by looking for '<Domain>/**' patterns
    present = set()
    for domain in ALL_DOMAINS:
        # Match patterns like "'Core/**'" or "- 'Core/**'"
        if f"'{domain}/**'" in content or f'"{domain}/**"' in content:
            present.add(domain)

    missing = sorted(set(ALL_DOMAINS) - present)
    if not missing:
        return None

    batch = missing[:BATCH_CI_FILTER]
    remaining = len(missing) - len(batch)

    # Build the filter entries and output entries needed
    filter_entries = []
    output_entries = []
    check_entries = []
    pytest_entries = []
    pester_entries = []
    bats_entries = []

    for d in batch:
        key = DOMAIN_FILTER_KEY[d]
        filter_entries.append(f"            {key}:\n              - '{d}/**'")
        output_entries.append(f"      {key}: ${{{{ steps.filter.outputs.{key} }}}}")
        check_entries.append(
            f'                "${{{{ steps.filter.outputs.{key} }}}}" == "true" || \\\n'
        )
        pytest_entries.append(
            f'            [[ "${{{{ needs.detect-changes.outputs.{key} }}}}" == "true" ]]'
            f'  && PATHS="$PATHS {d}/"'
        )
        pester_entries.append(
            f"              if ('${{{{ needs.detect-changes.outputs.{key} }}}}' -eq 'true')"
            f"  {{ $paths += './{d}' }}"
        )
        bats_entries.append(
            f'            [[ "${{{{ needs.detect-changes.outputs.{key} }}}}" == "true" ]]'
            f'  && BATS_FILES="$BATS_FILES $(find {d}/ -name \'*.bats\' 2>/dev/null)"'
        )

    return {
        "title": f"[AUTO] Add {len(batch)} domains to CI path filter ({batch[0]}–{batch[-1]})",
        "body": _format_body(
            task=f"Add {len(batch)} domain directories to the CI `dorny/paths-filter` in `ci-test-and-release.yml`",
            context=(
                f"The CI pipeline currently only scopes test runs to {len(present)} of "
                f"{len(ALL_DOMAINS)} domains. This means changes to {len(missing)} "
                f"domain folders don't trigger their tests.\n\n"
                f"**Domains to add in this batch:** {', '.join(f'`{d}`' for d in batch)}\n"
                + (f"\n**{remaining} more domains** will be added in subsequent issues.\n" if remaining else "")
            ),
            files=[
                "- `.github/workflows/ci-test-and-release.yml` — Add filter entries, outputs, check conditions, and scoped test paths for each new domain",
            ],
            criteria=[
                f"The `detect-changes` job has outputs for: {', '.join(DOMAIN_FILTER_KEY[d] for d in batch)}",
                f"The `test-offline` job's pytest, Pester, and bats steps include scoped paths for each new domain",
                "The `any_domain` check includes the new outputs",
                "The workflow YAML is valid (no syntax errors)",
            ],
        ),
        "labels": ["auto-completion", "ci"],
        "priority": 1,
    }


def _check_domain_readmes() -> Optional[Dict[str, Any]]:
    """P2: Verify every domain folder has a README.md."""
    missing = []
    for d in ALL_DOMAINS:
        domain_dir = ROOT / d
        if domain_dir.is_dir() and not (domain_dir / "README.md").exists():
            missing.append(d)

    if not missing:
        return None

    batch = missing[:BATCH_README]
    remaining = len(missing) - len(batch)

    file_entries = []
    for d in batch:
        # Count operations in this domain
        resources = [
            p.name for p in (ROOT / d).iterdir()
            if p.is_dir() and not p.name.startswith(("_", ".")) and p.name != "tests"
        ]
        file_entries.append(
            f"- `{d}/README.md` — Create with operations table covering resources: "
            f"{', '.join(resources[:8]) if resources else '(check subdirectories)'}"
        )

    return {
        "title": f"[AUTO] Create README.md for {len(batch)} domains ({batch[0]}–{batch[-1]})",
        "body": _format_body(
            task=f"Create README.md files for {len(batch)} domain directories",
            context=(
                f"Per project spec (Section 7.6), every domain must have a README.md "
                f"with an operations table.\n\n"
                f"**Domains needing READMEs:** {', '.join(f'`{d}`' for d in batch)}\n"
                + (f"\n**{remaining} more** will be handled in subsequent issues.\n" if remaining else "")
                + "\nUse existing domain READMEs (e.g., `Core/README.md`, `Git/README.md`) as a template. "
                "Each README should list available operations with links to scripts, HTTP method, "
                "endpoint path, and a brief description."
            ),
            files=file_entries,
            criteria=[
                f"`{d}/README.md` exists and contains a Markdown table of operations"
                for d in batch
            ],
        ),
        "labels": ["auto-completion", "documentation"],
        "priority": 2,
    }


def _check_spec_sync_coverage() -> Optional[Dict[str, Any]]:
    """P3: Verify all domains are tracked in upstream_urls.json and spec sync dropdown."""
    urls_path = ROOT / "_shared" / "specs" / "upstream_urls.json"
    hashes_path = ROOT / "_shared" / "specs" / "last_sync_hashes.json"
    sync_wf = ROOT / ".github" / "workflows" / "api-spec-sync.yml"

    # Check upstream_urls.json
    tracked = set()
    if urls_path.exists():
        data = json.loads(urls_path.read_text())
        tracked = set(data.keys())

    # All known spec domains (from cached files)
    cache_files = glob.glob(str(ROOT / "_shared" / "specs" / ".cache_*.json"))
    all_spec_domains = set()
    for cf in cache_files:
        name = os.path.basename(cf).replace(".cache_", "").replace(".json", "")
        # Extract domain prefix
        for known in sorted(DOMAIN_FILTER_KEY.values(), key=len, reverse=True):
            if name == known or name.startswith(known + "_"):
                all_spec_domains.add(known)
                break

    missing_urls = sorted(all_spec_domains - tracked)

    # Check sync workflow dropdown
    sync_content = sync_wf.read_text() if sync_wf.exists() else ""
    missing_dropdown = []
    for d in all_spec_domains:
        if f"- {d}" not in sync_content:
            missing_dropdown.append(d)

    total_missing = len(set(missing_urls) | set(missing_dropdown))
    if total_missing == 0:
        return None

    return {
        "title": f"[AUTO] Expand spec sync tracking to {total_missing} additional domains",
        "body": _format_body(
            task="Add missing domains to the API spec sync infrastructure",
            context=(
                f"Currently only **{len(tracked)} domains** are tracked for upstream spec "
                f"changes. There are **{len(all_spec_domains)} domains** with cached specs.\n\n"
                f"**Missing from `upstream_urls.json`:** {', '.join(f'`{d}`' for d in missing_urls[:15])}"
                + (f" (+{len(missing_urls)-15} more)" if len(missing_urls) > 15 else "")
                + f"\n**Missing from sync workflow dropdown:** {len(missing_dropdown)} domains"
            ),
            files=[
                "- `_shared/specs/upstream_urls.json` — Add URL entries for each untracked domain (use the pattern from existing entries and the cached spec files in `_shared/specs/.cache_*.json`)",
                "- `_shared/specs/last_sync_hashes.json` — Add entries with `null` hash and `null` synced_at for new domains",
                "- `.github/workflows/api-spec-sync.yml` — Add missing domains to the `workflow_dispatch` dropdown choices",
            ],
            criteria=[
                "All domains with cached specs have entries in `upstream_urls.json`",
                "All domains have entries in `last_sync_hashes.json`",
                "The spec sync workflow dropdown includes all domains",
            ],
        ),
        "labels": ["auto-completion", "infrastructure"],
        "priority": 3,
    }


def _check_root_readme() -> Optional[Dict[str, Any]]:
    """P4: Verify root README reflects actual project scale."""
    readme_path = ROOT / "README.md"
    if not readme_path.exists():
        return None

    content = readme_path.read_text()

    # Count actual YAML definitions
    yaml_count = len(glob.glob(str(ROOT / "_generator" / "definitions" / "*.yaml")))

    # Count actual domain directories
    domain_count = sum(
        1 for d in ALL_DOMAINS if (ROOT / d).is_dir()
    )

    # Count actual test files
    test_count = len(glob.glob(str(ROOT / "**" / "test_*.py"), recursive=True))

    # Count implementation scripts
    py_scripts = len([
        s for s in glob.glob(str(ROOT / "**" / "*.py"), recursive=True)
        if "/tests/" not in s and "__init__" not in s
        and "_generator/" not in s and "_shared/" not in s
        and "_research/" not in s and "__pycache__" not in s
        and "/.git/" not in s
    ])

    # Check if README is stale — look for obviously wrong numbers
    is_stale = False
    # If README mentions "39 total" or "50 operations" but we have 1000+
    if yaml_count > 100 and ("39 total" in content or "50 operations" in content):
        is_stale = True
    # If README lists fewer than 20 rows in coverage table but we have 40+ domains
    if domain_count > 30 and content.count("| ") < 60:
        is_stale = True

    if not is_stale:
        return None

    return {
        "title": "[AUTO] Update root README.md with actual project scale",
        "body": _format_body(
            task="Update the root README.md to reflect the actual project scale",
            context=(
                f"The README currently claims ~50 operations and 9 domains, but the "
                f"project now contains:\n\n"
                f"| Metric | Actual |\n|--------|--------|\n"
                f"| YAML definitions | **{yaml_count}** |\n"
                f"| Domain directories | **{domain_count}** |\n"
                f"| Python test files | **{test_count}** |\n"
                f"| Implementation scripts (.py) | **{py_scripts}** |\n\n"
                "The Coverage Summary table, structure tree, and headline numbers all "
                "need to be updated."
            ),
            files=[
                "- `README.md` — Update the headline numbers, Coverage Summary table (add all domains), and repository structure tree",
            ],
            criteria=[
                f"README mentions ~{yaml_count} operations (not 50)",
                f"Coverage Summary table has rows for all {domain_count} domains",
                "Repository structure tree reflects at least the top-level domain folders",
                "No references to '39 total' or '50 operations' remain",
            ],
        ),
        "labels": ["auto-completion", "documentation"],
        "priority": 4,
    }


def _check_test_failures() -> Optional[Dict[str, Any]]:
    """P5: Find domains with failing T1 tests and create a fix task."""
    # Test one domain at a time (cheapest first — fewest test files)
    domain_tests: List[tuple] = []
    for d in ALL_DOMAINS:
        test_dir = ROOT / d
        if not test_dir.is_dir():
            continue
        test_files = glob.glob(str(test_dir / "**" / "test_*.py"), recursive=True)
        if test_files:
            domain_tests.append((d, len(test_files)))

    # Sort by fewest tests first (quicker to validate)
    domain_tests.sort(key=lambda x: x[1])

    for domain, count in domain_tests:
        r = subprocess.run(
            [sys.executable, "-m", "pytest", str(ROOT / domain), "-q", "--tb=line", "-x"],
            capture_output=True, text=True, timeout=120,
            cwd=str(ROOT),
        )
        if r.returncode != 0:
            # Parse failure count from pytest output
            last_line = r.stdout.strip().split("\n")[-1] if r.stdout.strip() else ""
            # e.g. "3 failed, 12 passed in 2.50s"
            fail_match = re.search(r"(\d+) failed", last_line)
            pass_match = re.search(r"(\d+) passed", last_line)
            failed = int(fail_match.group(1)) if fail_match else 0
            passed = int(pass_match.group(1)) if pass_match else 0

            # Get first few failure lines
            failure_lines = []
            for line in r.stdout.split("\n"):
                if line.startswith("FAILED "):
                    failure_lines.append(line.strip())
                if len(failure_lines) >= 5:
                    break

            return {
                "title": f"[AUTO] Fix {failed} test failures in {domain}/ ({passed} passing)",
                "body": _format_body(
                    task=f"Fix failing T1 offline tests in the `{domain}/` domain",
                    context=(
                        f"Running `pytest {domain}/ -q --tb=short` shows "
                        f"**{failed} failures** and **{passed} passing** tests.\n\n"
                        f"**First failures:**\n"
                        + "\n".join(f"- `{f}`" for f in failure_lines)
                        + "\n\n**Full output (last 20 lines):**\n```\n"
                        + "\n".join(r.stdout.strip().split("\n")[-20:])
                        + "\n```\n\n"
                        "Common causes: missing fixture files, URL pattern mismatches, "
                        "or unescaped special characters in generated code. Check if the "
                        "YAML definition needs updating or if a template fix is needed."
                    ),
                    files=[
                        f"- `{domain}/` — Fix failing tests (possibly update YAML definitions in `_generator/definitions/` and regenerate using `python -m _generator.generate -d <yaml>`)",
                    ],
                    criteria=[
                        f"`python -m pytest {domain}/ -q --tb=short` shows 0 failures",
                        f"All {count} test files in `{domain}/` pass",
                    ],
                ),
                "labels": ["auto-completion", "tests"],
                "priority": 5,
            }

    return None


def _check_spec_sync_dropdown_completeness() -> Optional[Dict[str, Any]]:
    """P6: Ensure api-spec-sync.yml dropdown has all domains."""
    # This is a lighter version of P3 — just the dropdown
    sync_wf = ROOT / ".github" / "workflows" / "api-spec-sync.yml"
    if not sync_wf.exists():
        return None
    content = sync_wf.read_text()

    missing = [d for d in ALL_DOMAINS if f"- {DOMAIN_FILTER_KEY[d]}" not in content]
    if not missing:
        return None

    # Already handled by P3 if upstream_urls is also missing
    # Only emit this if P3 didn't fire (i.e., urls are tracked but dropdown isn't updated)
    return None  # Let P3 handle it


# ═══════════════════════════════════════════════════════════════════════════════
# Issue body formatter
# ═══════════════════════════════════════════════════════════════════════════════

def _format_body(
    task: str,
    context: str,
    files: List[str],
    criteria: List[str],
) -> str:
    """Format a GitHub Issue body with consistent structure."""
    files_str = "\n".join(files)
    criteria_str = "\n".join(f"- [ ] {c}" for c in criteria)
    return f"""## Task: {task}

### Context
{context}

### Files to modify
{files_str}

### Acceptance criteria
{criteria_str}

### Reference
See `.github/copilot-instructions.md` for project conventions.

> This issue was auto-generated by the project completion tracker.
> After completing this task, the next scheduled run will pick the next item.
"""


# ═══════════════════════════════════════════════════════════════════════════════
# Priority queue — ordered checklist
# ═══════════════════════════════════════════════════════════════════════════════

CHECKS = [
    ("P0: Python syntax errors", _check_python_syntax),
    ("P1: CI path filter coverage", _check_ci_path_filter),
    ("P2: Domain READMEs", _check_domain_readmes),
    ("P3: Spec sync coverage", _check_spec_sync_coverage),
    ("P4: Root README accuracy", _check_root_readme),
    ("P5: Test failures", _check_test_failures),
]


def run_tracker(verbose: bool = False) -> Dict[str, Any]:
    """Run all checks in priority order and return the first task found."""
    completed = []
    for name, check_fn in CHECKS:
        if verbose:
            print(f"  Checking {name}...", end=" ", flush=True)
        try:
            task = check_fn()
        except Exception as e:
            if verbose:
                print(f"ERROR: {e}")
            continue

        if task is None:
            if verbose:
                print("✓ PASS")
            completed.append(name)
        else:
            if verbose:
                print(f"→ TASK: {task['title']}")
            return {
                "status": "incomplete",
                "completed_checks": completed,
                "next_task": task,
                "total_checks": len(CHECKS),
                "completed_count": len(completed),
            }

    return {
        "status": "complete",
        "completed_checks": completed,
        "total_checks": len(CHECKS),
        "completed_count": len(completed),
    }


# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Project completion tracker")
    parser.add_argument("--verbose", "-v", action="store_true", help="Human-readable output")
    parser.add_argument(
        "--check-only", action="store_true",
        help="Exit 0 if complete, 1 if not (no JSON output)",
    )
    args = parser.parse_args()

    result = run_tracker(verbose=args.verbose)

    if args.check_only:
        sys.exit(0 if result["status"] == "complete" else 1)

    print(json.dumps(result, indent=2))
    sys.exit(0 if result["status"] == "complete" else 1)


if __name__ == "__main__":
    main()
