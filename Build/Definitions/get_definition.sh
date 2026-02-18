#!/usr/bin/env bash
# ============================================================================
# Get a single build definition by ID from an Azure DevOps project.
#
# API:  GET {org}/{project}/_apis/build/definitions/{definitionId}?api-version=7.2
# Auth: Basic (PAT)
#
# Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/build/definitions/get?view=azure-devops-rest-7.2
#
# Required environment variables:
#   AZURE_DEVOPS_ORG  — Organization name
#   AZURE_DEVOPS_PAT  — Personal Access Token
#   PROJECT_ID        — Project name or GUID
#   DEFINITION_ID     — Build definition ID
# ============================================================================
set -euo pipefail

# Source shared helpers
source "$(dirname "$0")/../../_shared/common.sh"

API_VERSION="7.2"

# ---------------------------------------------------------------------------
# Validate required env vars
# ---------------------------------------------------------------------------
: "${AZURE_DEVOPS_ORG:?ERROR: Set the AZURE_DEVOPS_ORG environment variable.}"
: "${AZURE_DEVOPS_PAT:?ERROR: Set the AZURE_DEVOPS_PAT environment variable.}"
: "${PROJECT_ID:?ERROR: Set the PROJECT_ID environment variable.}"
: "${DEFINITION_ID:?ERROR: Set the DEFINITION_ID environment variable.}"

# ---------------------------------------------------------------------------
# Auth & logging
# ---------------------------------------------------------------------------
AUTH_HEADER=$(ado_build_auth "$AZURE_DEVOPS_PAT")
ado_log_init "get_definition"
ado_log_info "Getting build definition '${DEFINITION_ID}' in project '${PROJECT_ID}'"

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
URL="https://dev.azure.com/${AZURE_DEVOPS_ORG}/${PROJECT_ID}/_apis/build/definitions/${DEFINITION_ID}?api-version=${API_VERSION}"

HTTP_CODE=$(curl --silent --show-error --write-out "%{http_code}" \
    --output /tmp/ado_get_definition_response.json \
    --header "Authorization: Basic ${AUTH_HEADER}" \
    --header "Content-Type: application/json" \
    "${URL}")

BODY=$(cat /tmp/ado_get_definition_response.json)
rm -f /tmp/ado_get_definition_response.json

# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------
case "$HTTP_CODE" in
    200)
        ;;
    401)
        echo "ERROR: Authentication failed (401). Verify AZURE_DEVOPS_PAT is valid and not expired." >&2
        echo "URL: $URL" >&2
        exit 1
        ;;
    403)
        echo "ERROR: Insufficient permissions (403). Required PAT scope: Build (Read)." >&2
        echo "URL: $URL" >&2
        exit 1
        ;;
    404)
        echo "ERROR: Build definition not found (404). Verify org='${AZURE_DEVOPS_ORG}', project='${PROJECT_ID}', definitionId='${DEFINITION_ID}'." >&2
        echo "URL: $URL" >&2
        exit 1
        ;;
    *)
        echo "ERROR: Unexpected HTTP status $HTTP_CODE." >&2
        echo "URL: $URL" >&2
        echo "Response: ${BODY:0:500}" >&2
        exit 1
        ;;
esac

# ---------------------------------------------------------------------------
# Version guard
# ---------------------------------------------------------------------------
if ! echo "$BODY" | grep -q '"id"'; then
    echo "WARNING: Unexpected response shape — server may not support api-version ${API_VERSION}." >&2
fi

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
echo "$BODY"
