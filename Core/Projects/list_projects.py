#!/usr/bin/env python3
"""
List all projects in an Azure DevOps organisation.

API:  GET {org}/_apis/projects?api-version=7.2-preview.4
Auth: Basic (PAT)

Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/core/projects/list?view=azure-devops-rest-7.2
"""

import base64
import os
import sys

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
API_VERSION = "7.2-preview.4"

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
url = f"https://dev.azure.com/{ORGANIZATION}/_apis/projects?api-version={API_VERSION}"

response = requests.get(url, headers=HEADERS, timeout=30)
response.raise_for_status()

data = response.json()

# ---------------------------------------------------------------------------
# Version guard — verify the response looks correct for 7.2-preview
# ---------------------------------------------------------------------------
if "count" not in data:
    print(
        f"WARNING: Unexpected response shape — the server may not support api-version {API_VERSION}.",
        file=sys.stderr,
    )

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
print(f"Total projects: {data.get('count', 'N/A')}\n")
for project in data.get("value", []):
    print(f"  {project['name']:30s}  {project['state']:12s}  {project['id']}")
