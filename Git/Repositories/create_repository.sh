#!/usr/bin/env bash
# ============================================================================
# Create a new Azure DevOps Git repository
#
# API:  POST {org}/{project}/_apis/git/repositories?api-version=7.2
# Auth: Basic (PAT)
#
# Usage: REPO_NAME="MyRepo" bash create_repository.sh
#
# Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories/create?view=azure-devops-rest-7.2
# ============================================================================
set -euo pipefail

# Source shared helpers
source "$(dirname "$0")/../../_shared/common.sh"

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
API_VERSION="7.2"
ORG="${AZURE_DEVOPS_ORG:?ERROR: Set the AZURE_DEVOPS_ORG environment variable.}"
PROJECT="${PROJECT_ID:?ERROR: Set the PROJECT_ID environment variable (name or GUID).}"
REPO_NAME="${REPO_NAME:?ERROR: Set the REPO_NAME environment variable.}"
PAT="${AZURE_DEVOPS_PAT:?ERROR: Set the AZURE_DEVOPS_PAT environment variable.}"

# ---------------------------------------------------------------------------
# Auth & logging
# ---------------------------------------------------------------------------
AUTH=$(ado_build_auth "$PAT")
ado_log_init "create_repository"
ado_log_info "Creating repository '${REPO_NAME}' in project '${PROJECT}'"

# ---------------------------------------------------------------------------
# Request body
# ---------------------------------------------------------------------------
BODY=$(cat <<EOF
{
  "name": "${REPO_NAME}",
  "project": {
    "id": "${PROJECT}"
  }
}
EOF
)

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
URL="https://dev.azure.com/${ORG}/${PROJECT}/_apis/git/repositories?api-version=${API_VERSION}"

RESPONSE=$(curl --silent --fail --show-error \
    -X POST \
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
echo "Repository created."
echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"
