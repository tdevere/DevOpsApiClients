#!/usr/bin/env bats
# ============================================================================
# Offline unit tests for create_repository.sh
#
# Uses a stubbed curl function to intercept HTTP calls and return fixture data.
# ============================================================================

SCRIPT_DIR="$(cd "$(dirname "$BATS_TEST_FILENAME")/.." && pwd)"
FIXTURES_DIR="$(cd "$(dirname "$BATS_TEST_FILENAME")/fixtures" && pwd)"

PROJECT_ID_VAL="d1e2f3a4-b5c6-7890-1234-567890abcdef"

setup() {
    export AZURE_DEVOPS_ORG="testorg"
    export AZURE_DEVOPS_PAT="fakepat1234567890"
    export PROJECT_ID="$PROJECT_ID_VAL"
    export REPO_NAME="NewRepo"
    export FIXTURES_DIR
    export BATS_TMPDIR

    STUB_DIR="$(mktemp -d)"
    cat > "$STUB_DIR/curl" << STUBEOF
#!/usr/bin/env bash
echo "\$@" >> "${BATS_TMPDIR}/curl_args.log"
for arg in "\$@"; do
    if [[ "\$arg" == *"/_apis/git/repositories?api-version="* ]]; then
        cat "${FIXTURES_DIR}/create_repository_201.json"
        exit 0
    fi
done
echo '{"error": "no matching stub"}'
exit 1
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

@test "create_repository.sh: exits with error when AZURE_DEVOPS_ORG is unset" {
    unset AZURE_DEVOPS_ORG
    run bash "$SCRIPT_DIR/create_repository.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"AZURE_DEVOPS_ORG"* ]]
}

@test "create_repository.sh: exits with error when AZURE_DEVOPS_PAT is unset" {
    unset AZURE_DEVOPS_PAT
    run bash "$SCRIPT_DIR/create_repository.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"AZURE_DEVOPS_PAT"* ]]
}

@test "create_repository.sh: exits with error when PROJECT_ID is unset" {
    unset PROJECT_ID
    run bash "$SCRIPT_DIR/create_repository.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"PROJECT_ID"* ]]
}

@test "create_repository.sh: exits with error when REPO_NAME is unset" {
    unset REPO_NAME
    run bash "$SCRIPT_DIR/create_repository.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"REPO_NAME"* ]]
}

@test "create_repository.sh: calls correct URL with POST method" {
    run bash "$SCRIPT_DIR/create_repository.sh"
    [ "$status" -eq 0 ]

    curl_args=$(cat "${BATS_TMPDIR}/curl_args.log")
    [[ "$curl_args" == *"-X POST"* ]]
    [[ "$curl_args" == *"https://dev.azure.com/testorg/${PROJECT_ID_VAL}/_apis/git/repositories?api-version=7.2"* ]]
}

@test "create_repository.sh: outputs created repository details" {
    run bash "$SCRIPT_DIR/create_repository.sh"
    [ "$status" -eq 0 ]

    [[ "$output" == *"NewRepo"* ]]
    [[ "$output" == *"Repository created"* ]]
}
