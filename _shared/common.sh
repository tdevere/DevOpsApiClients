#!/usr/bin/env bash
# ============================================================================
# Shared helpers for Azure DevOps API Bash/cURL clients.
#
# Source this file:  source "$(dirname "$0")/../../_shared/common.sh"
# ============================================================================

# ---------------------------------------------------------------------------
# Auth helper — Base64-encode ":PAT"
# ---------------------------------------------------------------------------
ado_build_auth() {
    local pat="${1:?ERROR: PAT argument required}"
    printf ':%s' "$pat" | base64 -w0 2>/dev/null || printf ':%s' "$pat" | base64
}

# ---------------------------------------------------------------------------
# URL builder
# ---------------------------------------------------------------------------
ado_build_url() {
    # Usage: ado_build_url <org> <path> <api_version> [project] [base_host]
    local org="${1:?}" path="${2:?}" api_version="${3:?}" project="${4:-}" base_host="${5:-dev.azure.com}"
    local base="https://${base_host}/${org}"
    if [[ -n "$project" ]]; then
        base="${base}/${project}"
    fi
    local sep="?"
    if [[ "$path" == *"?"* ]]; then
        sep="&"
    fi
    echo "${base}/${path}${sep}api-version=${api_version}"
}

# ---------------------------------------------------------------------------
# Environment validation
# ---------------------------------------------------------------------------
ado_require_env() {
    # Usage: ado_require_env VAR_NAME "friendly description"
    local var_name="${1:?}" friendly="${2:-$1}"
    local value="${!var_name:-}"
    if [[ -z "$value" ]]; then
        echo "ERROR: Set the ${var_name} environment variable (${friendly})." >&2
        exit 1
    fi
    echo "$value"
}

# ---------------------------------------------------------------------------
# PAT redaction
# ---------------------------------------------------------------------------
ado_redact_pat() {
    local pat="${1:-}"
    if [[ ${#pat} -le 4 ]]; then
        echo "****"
    else
        echo "${pat:0:4}****..."
    fi
}

# ---------------------------------------------------------------------------
# Version guard — check JSON response for expected keys
# ---------------------------------------------------------------------------
ado_version_guard() {
    # Usage: ado_version_guard "$RESPONSE" "key1" "key2" ...
    local response="$1"; shift
    local api_version="${API_VERSION:-7.2}"
    for key in "$@"; do
        if ! echo "$response" | grep -q "\"${key}\""; then
            echo "WARNING: Unexpected response — missing '${key}'. The server may not support api-version ${api_version}." >&2
        fi
    done
}

# ---------------------------------------------------------------------------
# Error handler — parse HTTP status from curl and provide actionable errors
# ---------------------------------------------------------------------------
ado_handle_error() {
    local status_code="${1:?}" url="${2:-unknown}" body="${3:-}"
    case "$status_code" in
        401) echo "ERROR: Authentication failed (HTTP 401). Verify AZURE_DEVOPS_PAT is valid and not expired. URL: ${url}" >&2 ;;
        403) echo "ERROR: Insufficient permissions (HTTP 403). Check PAT scopes. URL: ${url}" >&2 ;;
        404) echo "ERROR: Resource not found (HTTP 404). Verify org and resource identifiers. URL: ${url}" >&2 ;;
        429) echo "WARN: Rate limited (HTTP 429). Retry after a delay. URL: ${url}" >&2 ;;
        5*) echo "ERROR: Server error (HTTP ${status_code}). Check https://status.dev.azure.com. URL: ${url}" >&2 ;;
        *) echo "ERROR: Unexpected HTTP ${status_code}. URL: ${url}" >&2 ;;
    esac
    exit 1
}

# ---------------------------------------------------------------------------
# Logging helpers
# ---------------------------------------------------------------------------
_ADO_LOG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/logs"

ado_log_init() {
    # Usage: ado_log_init "operation_name"
    _ADO_OPERATION="${1:?}"
    mkdir -p "$_ADO_LOG_DIR"
}

_ado_log() {
    local level="$1" message="$2"
    local ts
    ts=$(date -u +"%Y-%m-%dT%H:%M:%S.%6NZ" 2>/dev/null || date -u +"%Y-%m-%dT%H:%M:%SZ")

    # Redact PAT from message
    local pat="${AZURE_DEVOPS_PAT:-}"
    if [[ -n "$pat" && ${#pat} -gt 4 ]]; then
        local redacted
        redacted=$(ado_redact_pat "$pat")
        message="${message//$pat/$redacted}"
    fi

    # Human-readable log
    echo "[${ts}] [${level}] ${message}" >> "${_ADO_LOG_DIR}/${_ADO_OPERATION}.log"

    # Structured JSON log
    printf '{"timestamp":"%s","level":"%s","operation":"%s","message":"%s"}\n' \
        "$ts" "$level" "$_ADO_OPERATION" "$message" >> "${_ADO_LOG_DIR}/${_ADO_OPERATION}.json"

    # Console
    echo "[${level}] ${message}" >&2

    # GitHub Actions annotations
    if [[ "${CI:-}" == "true" ]]; then
        case "$level" in
            ERROR) echo "::error::${message}" ;;
            WARN)  echo "::warning::${message}" ;;
        esac
    fi
}

ado_log_info()  { _ado_log "INFO"  "$1"; }
ado_log_warn()  { _ado_log "WARN"  "$1"; }
ado_log_error() { _ado_log "ERROR" "$1"; }
