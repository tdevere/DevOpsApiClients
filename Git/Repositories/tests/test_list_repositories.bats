#!/usr/bin/env bats
# ============================================================================
# Offline unit tests for list_repositories.sh
#
# Uses a stubbed curl function to intercept HTTP calls and return fixture data.
# Requires: bats-core (https://github.com/bats-core/bats-core)
# ============================================================================

SCRIPT_DIR="$(cd "$(dirname "$BATS_TEST_FILENAME")/.." && pwd)"
FIXTURES_DIR="$(cd "$(dirname "$BATS_TEST_FILENAME")/fixtures" && pwd)"

# ---------------------------------------------------------------------------
# Stub curl — returns fixture data instead of making real HTTP calls
# ---------------------------------------------------------------------------
setup() {
    export AZURE_DEVOPS_ORG="testorg"
    export AZURE_DEVOPS_PAT="fakepat1234567890"
    export FIXTURES_DIR
    export BATS_TMPDIR

    # Create a temporary bin directory with a fake curl
    STUB_DIR="$(mktemp -d)"
    cat > "$STUB_DIR/curl" << STUBEOF
#!/usr/bin/env bash
# Capture all arguments for assertion
echo "\$@" >> "${BATS_TMPDIR}/curl_args.log"
# Return the fixture based on URL pattern
for arg in "\$@"; do
    if [[ "\$arg" == *"/_apis/git/repositories?"* ]]; then
        cat "${FIXTURES_DIR}/list_repositories_200.json"
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

@test "list_repositories.sh: exits with error when AZURE_DEVOPS_ORG is unset" {
    unset AZURE_DEVOPS_ORG
    run bash "$SCRIPT_DIR/list_repositories.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"AZURE_DEVOPS_ORG"* ]]
}

@test "list_repositories.sh: exits with error when AZURE_DEVOPS_PAT is unset" {
    unset AZURE_DEVOPS_PAT
    run bash "$SCRIPT_DIR/list_repositories.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"AZURE_DEVOPS_PAT"* ]]
}

@test "list_repositories.sh: calls correct URL with api-version" {
    run bash "$SCRIPT_DIR/list_repositories.sh"
    [ "$status" -eq 0 ]

    # Verify curl was called with the correct URL
    curl_args=$(cat "${BATS_TMPDIR}/curl_args.log")
    [[ "$curl_args" == *"https://dev.azure.com/testorg/_apis/git/repositories?api-version=7.2"* ]]
}

@test "list_repositories.sh: sends Authorization header" {
    run bash "$SCRIPT_DIR/list_repositories.sh"
    [ "$status" -eq 0 ]

    curl_args=$(cat "${BATS_TMPDIR}/curl_args.log")
    [[ "$curl_args" == *"Authorization: Basic"* ]]
}

@test "list_repositories.sh: outputs valid JSON response" {
    run bash "$SCRIPT_DIR/list_repositories.sh"
    [ "$status" -eq 0 ]

    # Output should contain repository data from fixture
    [[ "$output" == *"count"* ]]
    [[ "$output" == *"ContosoRepo"* ]]
}

@test "list_repositories.sh: output contains all repository names" {
    run bash "$SCRIPT_DIR/list_repositories.sh"
    [ "$status" -eq 0 ]

    [[ "$output" == *"ContosoRepo"* ]]
    [[ "$output" == *"WidgetService"* ]]
    [[ "$output" == *"InfraAsCode"* ]]
}
