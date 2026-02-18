#!/usr/bin/env bats
# ============================================================================
# Offline unit tests for create_work_item.sh
#
# Uses a stubbed curl function to intercept HTTP calls and return fixture data.
# ============================================================================

SCRIPT_DIR="$(cd "$(dirname "$BATS_TEST_FILENAME")/.." && pwd)"
FIXTURES_DIR="$(cd "$(dirname "$BATS_TEST_FILENAME")/fixtures" && pwd)"

setup() {
    export AZURE_DEVOPS_ORG="testorg"
    export AZURE_DEVOPS_PAT="fakepat1234567890"
    export PROJECT_ID="ProjectAlpha"
    export WORK_ITEM_TYPE="Task"
    export WORK_ITEM_TITLE="Add unit tests for auth module"
    export FIXTURES_DIR
    export BATS_TMPDIR

    STUB_DIR="$(mktemp -d)"
    cat > "$STUB_DIR/curl" << 'STUBEOF'
#!/usr/bin/env bash
echo "$@" >> "${BATS_TMPDIR}/curl_args.log"
for arg in "$@"; do
    if [[ "$arg" == *"/_apis/wit/workitems/"*"?api-version="* ]]; then
        # Write status code to stdout via --write-out, body to --output file
        for i in "${!args[@]}"; do :; done
        # Find the --output target
        output_file=""
        prev=""
        for a in "$@"; do
            if [[ "$prev" == "--output" ]]; then
                output_file="$a"
            fi
            prev="$a"
        done
        if [[ -n "$output_file" ]]; then
            cat "${FIXTURES_DIR}/create_work_item_200.json" > "$output_file"
            printf "200"
        else
            cat "${FIXTURES_DIR}/create_work_item_200.json"
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


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

@test "create_work_item.sh: exits with error when AZURE_DEVOPS_ORG is unset" {
    unset AZURE_DEVOPS_ORG
    run bash "$SCRIPT_DIR/create_work_item.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"AZURE_DEVOPS_ORG"* ]]
}

@test "create_work_item.sh: exits with error when AZURE_DEVOPS_PAT is unset" {
    unset AZURE_DEVOPS_PAT
    run bash "$SCRIPT_DIR/create_work_item.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"AZURE_DEVOPS_PAT"* ]]
}

@test "create_work_item.sh: exits with error when PROJECT_ID is unset" {
    unset PROJECT_ID
    run bash "$SCRIPT_DIR/create_work_item.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"PROJECT_ID"* ]]
}

@test "create_work_item.sh: exits with error when WORK_ITEM_TYPE is unset" {
    unset WORK_ITEM_TYPE
    run bash "$SCRIPT_DIR/create_work_item.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"WORK_ITEM_TYPE"* ]]
}

@test "create_work_item.sh: exits with error when WORK_ITEM_TITLE is unset" {
    unset WORK_ITEM_TITLE
    run bash "$SCRIPT_DIR/create_work_item.sh"
    [ "$status" -ne 0 ]
    [[ "$output" == *"WORK_ITEM_TITLE"* ]]
}

@test "create_work_item.sh: calls correct URL with dollar-type" {
    run bash "$SCRIPT_DIR/create_work_item.sh"
    [ "$status" -eq 0 ]

    curl_args=$(cat "${BATS_TMPDIR}/curl_args.log")
    [[ "$curl_args" == *"/_apis/wit/workitems/"*"Task?api-version=7.2"* ]]
}

@test "create_work_item.sh: sends json-patch+json content type" {
    run bash "$SCRIPT_DIR/create_work_item.sh"
    [ "$status" -eq 0 ]

    curl_args=$(cat "${BATS_TMPDIR}/curl_args.log")
    [[ "$curl_args" == *"application/json-patch+json"* ]]
}

@test "create_work_item.sh: request body contains System.Title" {
    run bash "$SCRIPT_DIR/create_work_item.sh"
    [ "$status" -eq 0 ]

    curl_args=$(cat "${BATS_TMPDIR}/curl_args.log")
    [[ "$curl_args" == *"System.Title"* ]]
}

@test "create_work_item.sh: outputs work item JSON on success" {
    run bash "$SCRIPT_DIR/create_work_item.sh"
    [ "$status" -eq 0 ]
    [[ "$output" == *'"id": 101'* ]] || [[ "$output" == *'"id":101'* ]]
}
