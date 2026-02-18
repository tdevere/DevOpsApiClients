#!/usr/bin/env python3
"""
Create a new work item in an Azure DevOps project.

API:  POST {org}/{project}/_apis/wit/workitems/${type}?api-version=7.2
Auth: Basic (PAT)
Content-Type: application/json-patch+json

Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/work-items/create?view=azure-devops-rest-7.2
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
parser = argparse.ArgumentParser(description="Create a new work item.")
parser.add_argument("--type", required=True, dest="work_item_type",
                    help="Work item type (e.g., Task, Bug, User Story)")
parser.add_argument("--title", required=True,
                    help="Title for the new work item")
parser.add_argument("--description", default=None,
                    help="Description / repro steps (HTML supported)")
parser.add_argument("--assigned-to", default=None,
                    help="Display name or email of the assignee")
parser.add_argument("--priority", default=None, type=int, choices=[1, 2, 3, 4],
                    help="Priority (1=Critical … 4=Low)")
args = parser.parse_args()

# ---------------------------------------------------------------------------
# Auth header — note the special content type for JSON Patch
# ---------------------------------------------------------------------------
HEADERS = build_auth_header(PAT)
HEADERS["Content-Type"] = "application/json-patch+json"
logger = AdoLogger("create_work_item", PAT)
logger.info(f"Creating {args.work_item_type} in project '{PROJECT_ID}'")

# ---------------------------------------------------------------------------
# Build JSON Patch body
# ---------------------------------------------------------------------------
patch_document = [
    {"op": "add", "path": "/fields/System.Title", "value": args.title},
]

if args.description:
    patch_document.append(
        {"op": "add", "path": "/fields/System.Description", "value": args.description}
    )
if args.assigned_to:
    patch_document.append(
        {"op": "add", "path": "/fields/System.AssignedTo", "value": args.assigned_to}
    )
if args.priority:
    patch_document.append(
        {"op": "add", "path": "/fields/Microsoft.VSTS.Common.Priority", "value": args.priority}
    )

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
# The type is encoded into the URL path with a $ prefix
url = (
    f"https://dev.azure.com/{ORGANIZATION}/{PROJECT_ID}/_apis/wit/workitems"
    f"/${args.work_item_type}?api-version={API_VERSION}"
)
logger.info(f"POST {url}")

response = requests.post(url, headers=HEADERS, json=patch_document, timeout=30)

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
        f"ERROR: Insufficient permissions. Required PAT scope: Work Items (Read & Write).\n"
        f"URL: {url}\n"
        f"See https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate"
    )
if response.status_code == 404:
    sys.exit(
        f"ERROR: Resource not found. Verify AZURE_DEVOPS_ORG='{ORGANIZATION}', "
        f"PROJECT_ID='{PROJECT_ID}', and type='{args.work_item_type}' are correct.\n"
        f"URL: {url}"
    )
if response.status_code == 400:
    body_text = response.text[:500]
    sys.exit(
        f"ERROR: Bad request — check the work item type '{args.work_item_type}' exists "
        f"in project '{PROJECT_ID}'.\n"
        f"URL: {url}\nResponse: {body_text}"
    )

response.raise_for_status()
data = response.json()
logger.info(f"Work item #{data.get('id', 'N/A')} created successfully")

# ---------------------------------------------------------------------------
# Version guard
# ---------------------------------------------------------------------------
if "id" not in data or "fields" not in data:
    print(
        f"WARNING: Unexpected response shape — "
        f"the server may not support api-version {API_VERSION}.",
        file=sys.stderr,
    )

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
print(f"Work item created: #{data.get('id', 'N/A')} — {data.get('fields', {}).get('System.Title', 'N/A')}")
print(json.dumps(data, indent=2))
