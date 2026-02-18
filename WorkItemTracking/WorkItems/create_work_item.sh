#!/usr/bin/env bash
# ============================================================================
# Create a new work item in an Azure DevOps project.
#
# API:  POST {org}/{project}/_apis/wit/workitems/${type}?api-version=7.2
# Auth: Basic (PAT)
# Content-Type: application/json-patch+json
#
# Docs: https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/work-items/create?view=azure-devops-rest-7.2
#
# Required environment variables:
#   AZURE_DEVOPS_ORG   — Organization name
#   AZURE_DEVOPS_PAT   — Personal Access Token
#   PROJECT_ID         — Project name or GUID
#   WORK_ITEM_TYPE     — Work item type (e.g., Task, Bug, "User Story")
#   WORK_ITEM_TITLE    — Title for the new work item
#
# Optional environment variables:
#   WORK_ITEM_DESCRIPTION — Description (HTML supported)
#   WORK_ITEM_ASSIGNED_TO — Display name or email of assignee
#   WORK_ITEM_PRIORITY    — Priority (1-4)
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
: "${WORK_ITEM_TYPE:?ERROR: Set the WORK_ITEM_TYPE environment variable (e.g., Task, Bug).}"
: "${WORK_ITEM_TITLE:?ERROR: Set the WORK_ITEM_TITLE environment variable.}"

# ---------------------------------------------------------------------------
# Auth & logging
# ---------------------------------------------------------------------------
AUTH_HEADER=$(ado_build_auth "$AZURE_DEVOPS_PAT")
ado_log_init "create_work_item"
ado_log_info "Creating ${WORK_ITEM_TYPE} in project '${PROJECT_ID}'"

# ---------------------------------------------------------------------------
# Build JSON Patch body
# ---------------------------------------------------------------------------
# Start with the required title operation
PATCH_BODY=$(cat <<JSON
[
  {"op": "add", "path": "/fields/System.Title", "value": "${WORK_ITEM_TITLE}"}
JSON
)

# Append optional fields
if [[ -n "${WORK_ITEM_DESCRIPTION:-}" ]]; then
    PATCH_BODY="${PATCH_BODY},"$'\n'"  {\"op\": \"add\", \"path\": \"/fields/System.Description\", \"value\": \"${WORK_ITEM_DESCRIPTION}\"}"
fi

if [[ -n "${WORK_ITEM_ASSIGNED_TO:-}" ]]; then
    PATCH_BODY="${PATCH_BODY},"$'\n'"  {\"op\": \"add\", \"path\": \"/fields/System.AssignedTo\", \"value\": \"${WORK_ITEM_ASSIGNED_TO}\"}"
fi

if [[ -n "${WORK_ITEM_PRIORITY:-}" ]]; then
    PATCH_BODY="${PATCH_BODY},"$'\n'"  {\"op\": \"add\", \"path\": \"/fields/Microsoft.VSTS.Common.Priority\", \"value\": ${WORK_ITEM_PRIORITY}}"
fi

PATCH_BODY="${PATCH_BODY}"$'\n'"]"

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
URL="https://dev.azure.com/${AZURE_DEVOPS_ORG}/${PROJECT_ID}/_apis/wit/workitems/\$${WORK_ITEM_TYPE}?api-version=${API_VERSION}"

HTTP_CODE=$(curl --silent --show-error --write-out "%{http_code}" \
    --output /tmp/ado_create_workitem_response.json \
    --request POST \
    --header "Authorization: Basic ${AUTH_HEADER}" \
    --header "Content-Type: application/json-patch+json" \
    --data "${PATCH_BODY}" \
    "${URL}")

BODY=$(cat /tmp/ado_create_workitem_response.json)
rm -f /tmp/ado_create_workitem_response.json

# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------
case "$HTTP_CODE" in
    200|201)
        ;;
    400)
        echo "ERROR: Bad request (400). Verify work item type '${WORK_ITEM_TYPE}' exists in project '${PROJECT_ID}'." >&2
        echo "URL: $URL" >&2
        echo "Response: ${BODY:0:500}" >&2
        exit 1
        ;;
    401)
        echo "ERROR: Authentication failed (401). Verify AZURE_DEVOPS_PAT is valid and not expired." >&2
        echo "URL: $URL" >&2
        exit 1
        ;;
    403)
        echo "ERROR: Insufficient permissions (403). Required PAT scope: Work Items (Read & Write)." >&2
        echo "URL: $URL" >&2
        exit 1
        ;;
    404)
        echo "ERROR: Resource not found (404). Verify org='${AZURE_DEVOPS_ORG}', project='${PROJECT_ID}', type='${WORK_ITEM_TYPE}'." >&2
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
