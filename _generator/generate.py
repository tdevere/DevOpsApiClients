#!/usr/bin/env python3
"""
Azure DevOps API Client Code Generator

Generates Python, PowerShell, and Bash implementations + tests + fixtures
from a single YAML/JSON operation definition.

Usage:
    python -m _generator.generate --definition _generator/definitions/example.yaml
    python -m _generator.generate --definition _generator/definitions/example.yaml --lang python
    python -m _generator.generate --definition _generator/definitions/example.yaml --dry-run
"""

import argparse
import json
import sys
from pathlib import Path

from _generator.operation_def import load_definition
from _generator.templates.python_impl import render_python
from _generator.templates.powershell_impl import render_powershell
from _generator.templates.bash_impl import render_bash
from _generator.templates.python_test import render_python_test
from _generator.templates.pester_test import render_pester_test
from _generator.templates.bats_test import render_bats_test


def generate(definition_path: Path, output_dir: Path, languages: list, dry_run: bool = False):
    """Generate all files for an operation definition."""
    op = load_definition(definition_path)

    base = output_dir / op.domain / op.resource
    test_dir = base / "tests"
    fixture_dir = test_dir / "fixtures"

    files_to_write = {}

    # --- Implementation files ---
    if "python" in languages:
        files_to_write[base / op.python_script_name] = render_python(op)
    if "powershell" in languages:
        files_to_write[base / op.ps_script_name] = render_powershell(op)
    if "bash" in languages:
        files_to_write[base / op.bash_script_name] = render_bash(op)

    # --- Test files ---
    if "python" in languages:
        files_to_write[test_dir / f"test_{op.operation}.py"] = render_python_test(op)
    if "powershell" in languages:
        files_to_write[test_dir / f"{op.ps_verb}-{op.ps_noun}.Tests.ps1"] = render_pester_test(op)
    if "bash" in languages:
        files_to_write[test_dir / f"test_{op.operation}.bats"] = render_bats_test(op)

    # --- Fixtures ---
    if op.fixture_success:
        fixture_data = op.fixture_success
        # Wrap plain list fixtures in ADO paged format { count, value }.
        # Scripts use Set-StrictMode -Version Latest and access $response.value;
        # a bare array causes PropertyNotFoundException at runtime.
        if isinstance(fixture_data, list) and op.http_method.upper() == "GET":
            fixture_data = {"count": len(fixture_data), "value": fixture_data}
        files_to_write[fixture_dir / op.fixture_filename] = json.dumps(
            fixture_data, indent=2
        ) + "\n"
    if op.fixture_error_404:
        files_to_write[fixture_dir / f"{op.operation}_404.json"] = json.dumps(
            op.fixture_error_404, indent=2
        ) + "\n"

    # --- __init__.py files (ensure importability) ---
    for init_dir in [base, test_dir, output_dir / op.domain]:
        init_file = init_dir / "__init__.py"
        if not init_file.exists():
            files_to_write[init_file] = ""

    # --- Write files ---
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Generating {len(files_to_write)} files for {op.domain}/{op.resource}/{op.operation}:\n")

    for filepath, content in sorted(files_to_write.items()):
        rel = filepath.relative_to(output_dir)
        if dry_run:
            print(f"  [DRY] {rel}")
        else:
            filepath.parent.mkdir(parents=True, exist_ok=True)
            filepath.write_text(content, encoding="utf-8")
            # Make bash scripts executable
            if filepath.suffix == ".sh":
                filepath.chmod(0o755)
            print(f"  ✓ {rel}")

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Done. {len(files_to_write)} files {'would be ' if dry_run else ''}generated.")
    return files_to_write


def main():
    parser = argparse.ArgumentParser(
        description="Generate Azure DevOps API client implementations from a definition file."
    )
    parser.add_argument(
        "--definition", "-d",
        required=True,
        help="Path to the YAML/JSON operation definition file.",
    )
    parser.add_argument(
        "--output-dir", "-o",
        default=".",
        help="Root output directory (default: current directory).",
    )
    parser.add_argument(
        "--lang", "-l",
        nargs="+",
        choices=["python", "powershell", "bash", "all"],
        default=["all"],
        help="Languages to generate (default: all).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be generated without writing files.",
    )
    args = parser.parse_args()

    languages = args.lang
    if "all" in languages:
        languages = ["python", "powershell", "bash"]

    definition_path = Path(args.definition)
    if not definition_path.exists():
        sys.exit(f"ERROR: Definition file not found: {definition_path}")

    output_dir = Path(args.output_dir)
    generate(definition_path, output_dir, languages, args.dry_run)


if __name__ == "__main__":
    main()
