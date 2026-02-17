#!/usr/bin/env python3
"""
List all Git repositories in an Azure DevOps organisation.

API:  GET {org}/_apis/git/repositories?api-version=7.2
Auth: Basic (PAT)

Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories/list?view=azure-devops-rest-7.2
"""

import base64
import os
import sys

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
API_VERSION = "7.2"

ORGANIZATION = os.environ.get("AZURE_DEVOPS_ORG")
PAT = os.environ.get("AZURE_DEVOPS_PAT")

if not ORGANIZATION:
    sys.exit("ERROR: Set the AZURE_DEVOPS_ORG environment variable.")
if not PAT:
    sys.exit("ERROR: Set the AZURE_DEVOPS_PAT environment variable.")

# ---------------------------------------------------------------------------
# Auth header
# ---------------------------------------------------------------------------
credentials = base64.b64encode(f":{PAT}".encode("ascii")).decode("ascii")
HEADERS = {
    "Authorization": f"Basic {credentials}",
    "Content-Type": "application/json",
}

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
url = f"https://dev.azure.com/{ORGANIZATION}/_apis/git/repositories?api-version={API_VERSION}"

response = requests.get(url, headers=HEADERS, timeout=30)
response.raise_for_status()

data = response.json()

# ---------------------------------------------------------------------------
# Version guard — verify the response looks correct for 7.2
# ---------------------------------------------------------------------------
if "count" not in data:
    print(
        f"WARNING: Unexpected response shape — the server may not support api-version {API_VERSION}.",
        file=sys.stderr,
    )

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
print(f"Total repositories: {data.get('count', 'N/A')}\n")
for repo in data.get("value", []):
    project_name = repo.get("project", {}).get("name", "N/A")
    default_branch = repo.get("defaultBranch", "N/A")
    disabled = "DISABLED" if repo.get("isDisabled") else ""
    print(f"  {repo['name']:30s}  {project_name:20s}  {default_branch:25s}  {repo['id']}  {disabled}")
