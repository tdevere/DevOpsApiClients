#!/usr/bin/env bats
# ============================================================================
# Offline unit tests for delete_repository.sh
#
# Uses a stubbed curl function to intercept HTTP calls.
# ============================================================================

SCRIPT_DIR="$(cd "$(dirname "$BATS_TEST_FILENAME")/.." && pwd)"
FIXTURES_DIR="$(cd "$(dirname "$BATS_TEST_FILENAME")/fixtures" && pwd)"

REPO_GUID="a1b2c3d4-e5f6-7890-abcd-ef1234567890"
PROJECT_ID_VAL="ProjectAlpha"

setup() {
    export AZURE_DEVOPS_ORG="testorg"
    export AZURE_DEVOPS_PAT="fakepat1234567890"
    export PROJECT_ID="$PROJECT_ID_VAL"
    export REPO_ID="$REPO_GUID"
    export FIXTURES_DIR
    export BATS_TMPDIR

    STUB_DIR="$(mktemp -d)"
    # Stub curl to return 204 for DELETE calls
    cat > "$STUB_DIR/curl" << 'STUBEOF'
#!/usr/bin/env bash
echo "$@" >> "${BATS_TMPDIR}/curl_args.log"
# Check for --write-out (used by the script for status code)
for arg in "$@"; do
    if [[ "$arg" == *"%{http_code}"* ]]; then
        echo "204"
        exit 0
    fi
done
exit 0
STUBEOF
    chmod +x "$STUB_DIR/curl"
    export ORIGINAL_PATH="$PATH"
    export PATH="$STUB_DIR:$PATH"
    export STUB_DIR
    : > "${BATS_TMPDIR}/curl_args.log"
}

teardown() {
    export PATH="$ORIGINAL_PATH"
    rm -rf "$STUB_DIR"
    rm -f "${BATS_TMPDIR}/curl_args.log"
}


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

@test "delete_repository.sh: exits with error when AZURE_DEVOPS_ORG is unset" {
    unset AZURE_DEVOPS_ORG
    run bash "$SCRIPT_DIR/delete_repository.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"AZURE_DEVOPS_ORG"* ]]
}

@test "delete_repository.sh: exits with error when AZURE_DEVOPS_PAT is unset" {
    unset AZURE_DEVOPS_PAT
    run bash "$SCRIPT_DIR/delete_repository.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"AZURE_DEVOPS_PAT"* ]]
}

@test "delete_repository.sh: exits with error when PROJECT_ID is unset" {
    unset PROJECT_ID
    run bash "$SCRIPT_DIR/delete_repository.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"PROJECT_ID"* ]]
}

@test "delete_repository.sh: exits with error when REPO_ID is unset" {
    unset REPO_ID
    run bash "$SCRIPT_DIR/delete_repository.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"REPO_ID"* ]]
}

@test "delete_repository.sh: calls correct URL with DELETE method" {
    run bash "$SCRIPT_DIR/delete_repository.sh"
    [ "$status" -eq 0 ]

    curl_args=$(cat "${BATS_TMPDIR}/curl_args.log")
    [[ "$curl_args" == *"-X DELETE"* ]]
    [[ "$curl_args" == *"https://dev.azure.com/testorg/ProjectAlpha/_apis/git/repositories/${REPO_GUID}?api-version=7.2"* ]]
}

@test "delete_repository.sh: outputs success message on 204" {
    run bash "$SCRIPT_DIR/delete_repository.sh"
    [ "$status" -eq 0 ]

    [[ "$output" == *"deleted successfully"* ]]
}
