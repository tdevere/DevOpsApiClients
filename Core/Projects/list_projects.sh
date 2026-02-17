#!/usr/bin/env bash
# ============================================================================
# List all projects in an Azure DevOps organisation
#
# API:  GET {org}/_apis/projects?api-version=7.2-preview.4
# Auth: Basic (PAT)
#
# Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/core/projects/list?view=azure-devops-rest-7.2
# ============================================================================
set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
API_VERSION="7.2-preview.4"
ORG="${AZURE_DEVOPS_ORG:?ERROR: Set the AZURE_DEVOPS_ORG environment variable.}"
PAT="${AZURE_DEVOPS_PAT:?ERROR: Set the AZURE_DEVOPS_PAT environment variable.}"

# ---------------------------------------------------------------------------
# Auth — Base64-encode ":PAT"
# ---------------------------------------------------------------------------
AUTH=$(printf ':%s' "$PAT" | base64 -w0)

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
URL="https://dev.azure.com/${ORG}/_apis/projects?api-version=${API_VERSION}"

RESPONSE=$(curl --silent --fail --show-error \
    -X GET \
    -H "Authorization: Basic ${AUTH}" \
    -H "Content-Type: application/json" \
    "$URL")

# ---------------------------------------------------------------------------
# Version guard — simple check that the response contains "count"
# ---------------------------------------------------------------------------
if ! echo "$RESPONSE" | grep -q '"count"'; then
    echo "WARNING: Unexpected response — the server may not support api-version ${API_VERSION}." >&2
fi

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"
