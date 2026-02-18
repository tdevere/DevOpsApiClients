#!/usr/bin/env bash
# ============================================================================
# Delete an Azure DevOps Git repository
#
# API:  DELETE {org}/{project}/_apis/git/repositories/{repositoryId}?api-version=7.2
# Auth: Basic (PAT)
#
# Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories/delete?view=azure-devops-rest-7.2
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
REPO="${REPO_ID:?ERROR: Set the REPO_ID environment variable (repository GUID).}"
PAT="${AZURE_DEVOPS_PAT:?ERROR: Set the AZURE_DEVOPS_PAT environment variable.}"

# ---------------------------------------------------------------------------
# Auth & logging
# ---------------------------------------------------------------------------
AUTH=$(ado_build_auth "$PAT")
ado_log_init "delete_repository"
ado_log_info "Deleting repository '${REPO}' from project '${PROJECT}'"

# ---------------------------------------------------------------------------
# API call — expect 204 No Content
# ---------------------------------------------------------------------------
URL="https://dev.azure.com/${ORG}/${PROJECT}/_apis/git/repositories/${REPO}?api-version=${API_VERSION}"

HTTP_CODE=$(curl --silent --output /dev/null --write-out "%{http_code}" \
    -X DELETE \
    -H "Authorization: Basic ${AUTH}" \
    -H "Content-Type: application/json" \
    "$URL")

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
if [ "$HTTP_CODE" = "204" ]; then
    echo "Repository ${REPO} deleted successfully."
else
    echo "ERROR: Unexpected HTTP status $HTTP_CODE" >&2
    exit 1
fi
