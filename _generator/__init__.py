"""
Azure DevOps API Client Code Generator

Generates Python, PowerShell, and Bash implementations + tests + fixtures
from a single operation definition (YAML/JSON).

This is the 'Python-primary + auto-generate' approach recommended
in the sustainability analysis. Instead of maintaining 6+ files per
operation by hand, you define the operation once and generate the rest.

Usage:
    python -m _generator.generate \
        --definition _generator/definitions/core_list_teams.yaml \
        --output-dir .

    python -m _generator.generate \
        --definition _generator/definitions/core_list_teams.yaml \
        --output-dir . \
        --lang python          # generate only Python

See _generator/definitions/ for example operation definition files.
"""
