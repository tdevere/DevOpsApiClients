#!/usr/bin/env python3
"""
Create a new Git repository in an Azure DevOps project.

API:  POST {org}/{project}/_apis/git/repositories?api-version=7.2
Auth: Basic (PAT)

Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories/create?view=azure-devops-rest-7.2
"""

import argparse
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
API_VERSION = "7.2"

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
# CLI arguments
# ---------------------------------------------------------------------------
parser = argparse.ArgumentParser(description="Create a new Git repository.")
parser.add_argument("--name", required=True, help="Repository name")
args = parser.parse_args()

# ---------------------------------------------------------------------------
# Auth header & logging
# ---------------------------------------------------------------------------
HEADERS = build_auth_header(PAT)
logger = AdoLogger("create_repository", PAT)
logger.info(f"Creating repository '{args.name}' in project '{PROJECT_ID}'")

# ---------------------------------------------------------------------------
# Request body
# ---------------------------------------------------------------------------
body = {
    "name": args.name,
    "project": {
        "id": PROJECT_ID,
    },
}

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
url = (
    f"https://dev.azure.com/{ORGANIZATION}/{PROJECT_ID}/_apis/git/repositories"
    f"?api-version={API_VERSION}"
)
logger.info(f"POST {url}")

response = requests.post(url, headers=HEADERS, json=body, timeout=30)
response.raise_for_status()

data = response.json()
logger.info(f"Repository '{data.get('name', 'N/A')}' created successfully")

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
print(f"Repository created: {data.get('name', 'N/A')}")
print(json.dumps(data, indent=2))
