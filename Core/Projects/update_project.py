#!/usr/bin/env python3
"""
Update an Azure DevOps project (name, description, or visibility).

API:  PATCH {org}/_apis/projects/{projectId}?api-version=7.2-preview.4
Auth: Basic (PAT)

The API is asynchronous — it returns an operation reference.
Poll the operation URL to track completion.

Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/core/projects/update?view=azure-devops-rest-7.2
"""

import argparse
import base64
import json
import os
import sys

import requests

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
# CLI arguments
# ---------------------------------------------------------------------------
parser = argparse.ArgumentParser(description="Update an Azure DevOps project.")
parser.add_argument("--name", help="New project name")
parser.add_argument("--description", help="New project description")
parser.add_argument(
    "--visibility",
    choices=["private", "public"],
    help="New project visibility",
)
args = parser.parse_args()

body: dict = {}
if args.name:
    body["name"] = args.name
if args.description:
    body["description"] = args.description
if args.visibility:
    body["visibility"] = args.visibility

if not body:
    sys.exit("ERROR: Provide at least one of --name, --description, or --visibility.")

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
url = (
    f"https://dev.azure.com/{ORGANIZATION}/_apis/projects/{PROJECT_ID}"
    f"?api-version={API_VERSION}"
)

response = requests.patch(url, headers=HEADERS, json=body, timeout=30)
response.raise_for_status()

data = response.json()

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
print("Update operation queued.")
print(json.dumps(data, indent=2))
