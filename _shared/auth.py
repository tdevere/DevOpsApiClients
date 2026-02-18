"""
Shared authentication helpers for Azure DevOps API clients.

Provides PAT-based Basic Auth header construction and credential management.
All scripts share this logic — extracted per the ≥3 duplicate rule.
"""

import base64
import os
import sys
from typing import Dict, Optional


def get_env_or_exit(var_name: str, friendly: str = "") -> str:
    """Read an environment variable or exit with an actionable error."""
    value = os.environ.get(var_name)
    if not value:
        label = friendly or var_name
        sys.exit(f"ERROR: Set the {var_name} environment variable ({label}).")
    return value


def build_auth_header(pat: str) -> Dict[str, str]:
    """
    Build the HTTP headers for Azure DevOps Basic Auth.

    Returns a dict with Authorization and Content-Type headers.
    The PAT is Base64-encoded as `:<PAT>` per the ADO convention.
    """
    credentials = base64.b64encode(f":{pat}".encode("ascii")).decode("ascii")
    return {
        "Authorization": f"Basic {credentials}",
        "Content-Type": "application/json",
    }


def get_common_env() -> tuple:
    """
    Read the standard triple of (ORGANIZATION, PAT) from environment.

    Returns:
        (organization, pat) — both guaranteed non-empty.
    """
    org = get_env_or_exit("AZURE_DEVOPS_ORG", "organisation slug")
    pat = get_env_or_exit("AZURE_DEVOPS_PAT", "Personal Access Token")
    return org, pat


def redact_pat(pat: str) -> str:
    """Redact a PAT for safe logging — show only the first 4 characters."""
    if not pat or len(pat) <= 4:
        return "****"
    return pat[:4] + "****..."
