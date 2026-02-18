#!/usr/bin/env bats
# ============================================================================
# Offline unit tests for get_definition.sh
# ============================================================================

SCRIPT_DIR="$(cd "$(dirname "$BATS_TEST_FILENAME")/.." && pwd)"
FIXTURES_DIR="$(cd "$(dirname "$BATS_TEST_FILENAME")/fixtures" && pwd)"

DEFINITION_ID="1"

setup() {
    export AZURE_DEVOPS_ORG="testorg"
    export AZURE_DEVOPS_PAT="fakepat1234567890"
    export PROJECT_ID="ProjectAlpha"
    export DEFINITION_ID="$DEFINITION_ID"
    export FIXTURES_DIR
    export BATS_TMPDIR

    STUB_DIR="$(mktemp -d)"
    cat > "$STUB_DIR/curl" << 'STUBEOF'
#!/usr/bin/env bash
echo "$@" >> "${BATS_TMPDIR}/curl_args.log"
for arg in "$@"; do
    if [[ "$arg" == *"/_apis/build/definitions/"*"?api-version="* ]]; then
        output_file=""
        prev=""
        for a in "$@"; do
            if [[ "$prev" == "--output" ]]; then
                output_file="$a"
            fi
            prev="$a"
        done
        if [[ -n "$output_file" ]]; then
            cat "${FIXTURES_DIR}/get_definition_200.json" > "$output_file"
            printf "200"
        else
            cat "${FIXTURES_DIR}/get_definition_200.json"
        fi
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


@test "get_definition.sh: exits with error when AZURE_DEVOPS_ORG is unset" {
    unset AZURE_DEVOPS_ORG
    run bash "$SCRIPT_DIR/get_definition.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"AZURE_DEVOPS_ORG"* ]]
}

@test "get_definition.sh: exits with error when AZURE_DEVOPS_PAT is unset" {
    unset AZURE_DEVOPS_PAT
    run bash "$SCRIPT_DIR/get_definition.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"AZURE_DEVOPS_PAT"* ]]
}

@test "get_definition.sh: exits with error when PROJECT_ID is unset" {
    unset PROJECT_ID
    run bash "$SCRIPT_DIR/get_definition.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"PROJECT_ID"* ]]
}

@test "get_definition.sh: exits with error when DEFINITION_ID is unset" {
    unset DEFINITION_ID
    run bash "$SCRIPT_DIR/get_definition.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"DEFINITION_ID"* ]]
}

@test "get_definition.sh: calls correct URL with definition ID" {
    run bash "$SCRIPT_DIR/get_definition.sh"
    [ "$status" -eq 0 ]

    curl_args=$(cat "${BATS_TMPDIR}/curl_args.log")
    [[ "$curl_args" == *"https://dev.azure.com/testorg/ProjectAlpha/_apis/build/definitions/1?api-version=7.2"* ]]
}

@test "get_definition.sh: outputs definition data" {
    run bash "$SCRIPT_DIR/get_definition.sh"
    [ "$status" -eq 0 ]
    [[ "$output" == *"CI-Pipeline"* ]]
}
