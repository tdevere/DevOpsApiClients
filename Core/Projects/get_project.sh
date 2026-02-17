#!/usr/bin/env bash
# ============================================================================
# Get a single Azure DevOps project by ID or name
#
# API:  GET {org}/_apis/projects/{projectId}?api-version=7.2-preview.4
# Auth: Basic (PAT)
#
# Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/core/projects/get?view=azure-devops-rest-7.2
# ============================================================================
set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
API_VERSION="7.2-preview.4"
ORG="${AZURE_DEVOPS_ORG:?ERROR: Set the AZURE_DEVOPS_ORG environment variable.}"
PROJECT="${PROJECT_ID:?ERROR: Set the PROJECT_ID environment variable (name or GUID).}"
PAT="${AZURE_DEVOPS_PAT:?ERROR: Set the AZURE_DEVOPS_PAT environment variable.}"

# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------
AUTH=$(printf ':%s' "$PAT" | base64 -w0)

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
URL="https://dev.azure.com/${ORG}/_apis/projects/${PROJECT}?api-version=${API_VERSION}"

RESPONSE=$(curl --silent --fail --show-error \
    -X GET \
    -H "Authorization: Basic ${AUTH}" \
    -H "Content-Type: application/json" \
    "$URL")

# ---------------------------------------------------------------------------
# Version guard
# ---------------------------------------------------------------------------
if ! echo "$RESPONSE" | grep -q '"id"'; then
    echo "WARNING: Unexpected response — the server may not support api-version ${API_VERSION}." >&2
fi

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"
