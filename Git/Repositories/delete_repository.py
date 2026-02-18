#!/usr/bin/env python3
"""
Delete an Azure DevOps Git repository.

API:  DELETE {org}/{project}/_apis/git/repositories/{repositoryId}?api-version=7.2
Auth: Basic (PAT)

Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories/delete?view=azure-devops-rest-7.2
"""

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
REPO_ID = os.environ.get("REPO_ID")
PAT = os.environ.get("AZURE_DEVOPS_PAT")

if not ORGANIZATION:
    sys.exit("ERROR: Set the AZURE_DEVOPS_ORG environment variable.")
if not PROJECT_ID:
    sys.exit("ERROR: Set the PROJECT_ID environment variable (name or GUID).")
if not REPO_ID:
    sys.exit("ERROR: Set the REPO_ID environment variable (repository GUID).")
if not PAT:
    sys.exit("ERROR: Set the AZURE_DEVOPS_PAT environment variable.")

# ---------------------------------------------------------------------------
# Auth header & logging
# ---------------------------------------------------------------------------
HEADERS = build_auth_header(PAT)
logger = AdoLogger("delete_repository", PAT)
logger.info(f"Deleting repository '{REPO_ID}' from project '{PROJECT_ID}'")

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
url = (
    f"https://dev.azure.com/{ORGANIZATION}/{PROJECT_ID}/_apis/git/repositories/{REPO_ID}"
    f"?api-version={API_VERSION}"
)
logger.info(f"DELETE {url}")

response = requests.delete(url, headers=HEADERS, timeout=30)
response.raise_for_status()
logger.info(f"Repository {REPO_ID} deleted successfully")

# ---------------------------------------------------------------------------
# Output — DELETE returns 204 No Content on success
# ---------------------------------------------------------------------------
if response.status_code == 204:
    print(f"Repository {REPO_ID} deleted successfully.")
else:
    print(f"Unexpected status code: {response.status_code}", file=sys.stderr)
    if response.text:
        print(response.text)
