#!/usr/bin/env bash
# ============================================================================
# Update an Azure DevOps project (name, description, or visibility)
#
# API:  PATCH {org}/_apis/projects/{projectId}?api-version=7.2-preview.4
# Auth: Basic (PAT)
#
# The PATCH endpoint requires a project GUID (not a name).  If a name is
# supplied, the script automatically resolves it to a GUID via a GET call.
#
# The API is asynchronous — it returns an operation reference.
#
# Usage:
#   ./update_project.sh '{"description":"New desc","visibility":"private"}'
#
# Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/core/projects/update?view=azure-devops-rest-7.2
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
# Request body — passed as the first positional argument (JSON string)
# ---------------------------------------------------------------------------
BODY="${1:?ERROR: Pass a JSON body as the first argument, e.g. '{\"description\":\"New description\"}'}"

# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------
AUTH=$(printf ':%s' "$PAT" | base64 -w0)

# ---------------------------------------------------------------------------
# Resolve project GUID — PATCH requires a GUID, not a name
# ---------------------------------------------------------------------------
GUID_RE='^[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}$'
if ! [[ "$PROJECT" =~ $GUID_RE ]]; then
    echo "Resolving project name '${PROJECT}' to GUID..." >&2
    GET_URL="https://dev.azure.com/${ORG}/_apis/projects/${PROJECT}?api-version=${API_VERSION}"
    GET_RESP=$(curl --silent --fail --show-error \
        -X GET \
        -H "Authorization: Basic ${AUTH}" \
        -H "Content-Type: application/json" \
        "$GET_URL")
    PROJECT=$(echo "$GET_RESP" | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")
    echo "Resolved to GUID: ${PROJECT}" >&2
fi

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
URL="https://dev.azure.com/${ORG}/_apis/projects/${PROJECT}?api-version=${API_VERSION}"

RESPONSE=$(curl --silent --fail --show-error \
    -X PATCH \
    -H "Authorization: Basic ${AUTH}" \
    -H "Content-Type: application/json" \
    -d "$BODY" \
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
echo "Update operation queued."
echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"
