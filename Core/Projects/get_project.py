#!/usr/bin/env python3
"""
Get a single Azure DevOps project by ID or name.

API:  GET {org}/_apis/projects/{projectId}?api-version=7.2-preview.4
Auth: Basic (PAT)

Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/core/projects/get?view=azure-devops-rest-7.2
"""

import json
import os
import sys

# Add project root to path for shared helpers
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))

import requests

from _shared.auth import build_auth_header
from _shared.logging_utils import AdoLogger

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
API_VERSION = "7.2-preview.4"

ORGANIZATION = os.environ.get("AZURE_DEVOPS_ORG")
PROJECT_ID = os.environ.get("PROJECT_ID")
PAT = os.environ.get("AZURE_DEVOPS_PAT")

if not ORGANIZATION:
    sys.exit("ERROR: Set the AZURE_DEVOPS_ORG environment variable.")
if not PROJECT_ID:
    sys.exit("ERROR: Set the PROJECT_ID environment variable (name or GUID).")
if not PAT:
    sys.exit("ERROR: Set the AZURE_DEVOPS_PAT environment variable.")

# ---------------------------------------------------------------------------
# Auth header & logging
# ---------------------------------------------------------------------------
HEADERS = build_auth_header(PAT)
logger = AdoLogger("get_project", PAT)
logger.info(f"Getting project '{PROJECT_ID}' in org '{ORGANIZATION}'")

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
url = (
    f"https://dev.azure.com/{ORGANIZATION}/_apis/projects/{PROJECT_ID}"
    f"?api-version={API_VERSION}"
)
logger.info(f"GET {url}")

response = requests.get(url, headers=HEADERS, timeout=30)
response.raise_for_status()

data = response.json()
logger.info("Project retrieved successfully")

# ---------------------------------------------------------------------------
# Version guard
# ---------------------------------------------------------------------------
if "id" not in data:
    print(
        f"WARNING: Unexpected response — the server may not support api-version {API_VERSION}.",
        file=sys.stderr,
    )

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
print(json.dumps(data, indent=2))
