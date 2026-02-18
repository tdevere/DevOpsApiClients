#!/usr/bin/env python3
"""
Update an Azure DevOps project (name, description, or visibility).

API:  PATCH {org}/_apis/projects/{projectId}?api-version=7.2-preview.4
Auth: Basic (PAT)

The PATCH endpoint requires a project GUID (not a name).  If a name is
supplied, the script automatically resolves it to a GUID via a GET call.

The API is asynchronous — it returns an operation reference.
Poll the operation URL to track completion.

Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/core/projects/update?view=azure-devops-rest-7.2
"""

import argparse
import json
import os
import re
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
GUID_RE = re.compile(
    r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)

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
# Auth header & logging
# ---------------------------------------------------------------------------
HEADERS = build_auth_header(PAT)
logger = AdoLogger("update_project", PAT)
logger.info(f"Updating project '{PROJECT_ID}' in org '{ORGANIZATION}' with {body}")

# ---------------------------------------------------------------------------
# Resolve project GUID — PATCH requires a GUID, not a name
# ---------------------------------------------------------------------------
if not GUID_RE.match(PROJECT_ID):
    print(f"Resolving project name '{PROJECT_ID}' to GUID...", file=sys.stderr)
    get_url = (
        f"https://dev.azure.com/{ORGANIZATION}/_apis/projects/{PROJECT_ID}"
        f"?api-version={API_VERSION}"
    )
    get_resp = requests.get(get_url, headers=HEADERS, timeout=30)
    get_resp.raise_for_status()
    PROJECT_ID = get_resp.json()["id"]
    print(f"Resolved to GUID: {PROJECT_ID}", file=sys.stderr)

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
url = (
    f"https://dev.azure.com/{ORGANIZATION}/_apis/projects/{PROJECT_ID}"
    f"?api-version={API_VERSION}"
)
logger.info(f"PATCH {url}")

response = requests.patch(url, headers=HEADERS, json=body, timeout=30)
response.raise_for_status()

data = response.json()
logger.info("Update operation queued successfully")

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
