#!/usr/bin/env python3
"""
Get a single build definition by ID from an Azure DevOps project.

API:  GET {org}/{project}/_apis/build/definitions/{definitionId}?api-version=7.2
Auth: Basic (PAT)

Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/build/definitions/get?view=azure-devops-rest-7.2
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
API_VERSION = "7.2"

ORGANIZATION = os.environ.get("AZURE_DEVOPS_ORG")
PROJECT_ID = os.environ.get("PROJECT_ID")
PAT = os.environ.get("AZURE_DEVOPS_PAT")
DEFINITION_ID = os.environ.get("DEFINITION_ID")

if not ORGANIZATION:
    sys.exit("ERROR: Set the AZURE_DEVOPS_ORG environment variable.")
if not PROJECT_ID:
    sys.exit("ERROR: Set the PROJECT_ID environment variable (name or GUID).")
if not PAT:
    sys.exit("ERROR: Set the AZURE_DEVOPS_PAT environment variable.")
if not DEFINITION_ID:
    sys.exit("ERROR: Set the DEFINITION_ID environment variable.")

# ---------------------------------------------------------------------------
# Auth header & logging
# ---------------------------------------------------------------------------
HEADERS = build_auth_header(PAT)
logger = AdoLogger("get_definition", PAT)
logger.info(f"Getting build definition '{DEFINITION_ID}' in project '{PROJECT_ID}'")

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
url = (
    f"https://dev.azure.com/{ORGANIZATION}/{PROJECT_ID}/_apis/build/definitions/{DEFINITION_ID}"
    f"?api-version={API_VERSION}"
)
logger.info(f"GET {url}")

response = requests.get(url, headers=HEADERS, timeout=30)

# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------
if response.status_code == 401:
    sys.exit(
        f"ERROR: Authentication failed. Verify AZURE_DEVOPS_PAT is valid and not expired.\n"
        f"URL: {url}"
    )
if response.status_code == 403:
    sys.exit(
        f"ERROR: Insufficient permissions. Required PAT scope: Build (Read).\n"
        f"URL: {url}\n"
        f"See https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate"
    )
if response.status_code == 404:
    sys.exit(
        f"ERROR: Build definition not found. Verify AZURE_DEVOPS_ORG='{ORGANIZATION}', "
        f"PROJECT_ID='{PROJECT_ID}', and DEFINITION_ID='{DEFINITION_ID}' are correct.\n"
        f"URL: {url}"
    )

response.raise_for_status()
data = response.json()
logger.info(f"Build definition [{data.get('id', '?')}] '{data.get('name', 'N/A')}' retrieved")

# ---------------------------------------------------------------------------
# Version guard
# ---------------------------------------------------------------------------
if "id" not in data or "name" not in data:
    print(
        f"WARNING: Unexpected response shape — "
        f"the server may not support api-version {API_VERSION}.",
        file=sys.stderr,
    )

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
print(f"Build Definition: [{data.get('id', '?')}] {data.get('name', 'N/A')}")
print(f"  Path       : {data.get('path', 'N/A')}")
print(f"  Status     : {data.get('queueStatus', 'N/A')}")
print(f"  Revision   : {data.get('revision', 'N/A')}")
author = data.get("authoredBy", {})
print(f"  Author     : {author.get('displayName', 'N/A')}")
repo = data.get("repository", {})
if repo:
    print(f"  Repository : {repo.get('name', 'N/A')} ({repo.get('type', 'N/A')})")
print()
print(json.dumps(data, indent=2))
