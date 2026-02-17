#!/usr/bin/env bats
# ============================================================================
# Offline unit tests for update_project.sh
#
# Uses a stubbed curl function to intercept HTTP calls and return fixture data.
# ============================================================================

SCRIPT_DIR="$(cd "$(dirname "$BATS_TEST_FILENAME")/.." && pwd)"
FIXTURES_DIR="$(cd "$(dirname "$BATS_TEST_FILENAME")/fixtures" && pwd)"

PROJECT_GUID="a1b2c3d4-e5f6-7890-abcd-ef1234567890"

setup() {
    export AZURE_DEVOPS_ORG="testorg"
    export AZURE_DEVOPS_PAT="fakepat1234567890"
    export PROJECT_ID="$PROJECT_GUID"
    export FIXTURES_DIR
    export BATS_TMPDIR

    STUB_DIR="$(mktemp -d)"
    # The update script may call curl twice: GET (resolve GUID) + PATCH (update)
    cat > "$STUB_DIR/curl" << STUBEOF
#!/usr/bin/env bash
echo "\$@" >> "${BATS_TMPDIR}/curl_args.log"
for arg in "\$@"; do
    # PATCH call
    if [[ "\$arg" == *"/_apis/projects/"*"?api-version="* ]]; then
        cat "${FIXTURES_DIR}/update_project_202.json"
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

@test "update_project.sh: exits with error when AZURE_DEVOPS_ORG is unset" {
    unset AZURE_DEVOPS_ORG
    run bash "$SCRIPT_DIR/update_project.sh" '{"description":"test"}'
    [ "$status" -ne 0 ]
    [[ "$output" == *"AZURE_DEVOPS_ORG"* ]]
}

@test "update_project.sh: exits with error when AZURE_DEVOPS_PAT is unset" {
    unset AZURE_DEVOPS_PAT
    run bash "$SCRIPT_DIR/update_project.sh" '{"description":"test"}'
    [ "$status" -ne 0 ]
    [[ "$output" == *"AZURE_DEVOPS_PAT"* ]]
}

@test "update_project.sh: exits with error when PROJECT_ID is unset" {
    unset PROJECT_ID
    run bash "$SCRIPT_DIR/update_project.sh" '{"description":"test"}'
    [ "$status" -ne 0 ]
    [[ "$output" == *"PROJECT_ID"* ]]
}

@test "update_project.sh: exits with error when no JSON body is passed" {
    run bash "$SCRIPT_DIR/update_project.sh"
    [ "$status" -ne 0 ]
}

@test "update_project.sh: calls PATCH with correct URL when PROJECT_ID is a GUID" {
    run bash "$SCRIPT_DIR/update_project.sh" '{"description":"Updated by test"}'
    [ "$status" -eq 0 ]

    curl_args=$(cat "${BATS_TMPDIR}/curl_args.log")
    [[ "$curl_args" == *"PATCH"* ]]
    [[ "$curl_args" == *"https://dev.azure.com/testorg/_apis/projects/${PROJECT_GUID}?api-version=7.2-preview.4"* ]]
}

@test "update_project.sh: sends Authorization header" {
    run bash "$SCRIPT_DIR/update_project.sh" '{"description":"test"}'
    [ "$status" -eq 0 ]

    curl_args=$(cat "${BATS_TMPDIR}/curl_args.log")
    [[ "$curl_args" == *"Authorization: Basic"* ]]
}

@test "update_project.sh: outputs 'Update operation queued'" {
    run bash "$SCRIPT_DIR/update_project.sh" '{"description":"test"}'
    [ "$status" -eq 0 ]

    [[ "$output" == *"Update operation queued"* ]]
}

@test "update_project.sh: resolves project name to GUID via GET before PATCH" {
    # Set PROJECT_ID to a name (not a GUID) to trigger resolution
    export PROJECT_ID="ProjectAlpha"

    # Need the curl stub to handle both GET (resolve) and PATCH (update)
    cat > "$STUB_DIR/curl" << STUBEOF2
#!/usr/bin/env bash
echo "\$@" >> "${BATS_TMPDIR}/curl_args.log"
METHOD=""
for i in "\$@"; do
    if [[ "\$prev" == "-X" ]]; then
        METHOD="\$i"
    fi
    prev="\$i"
done
for arg in "\$@"; do
    if [[ "\$arg" == *"/_apis/projects/"*"?api-version="* ]]; then
        if [[ "\$METHOD" == "GET" ]]; then
            cat "${FIXTURES_DIR}/get_project_200.json"
        else
            cat "${FIXTURES_DIR}/update_project_202.json"
        fi
        exit 0
    fi
done
echo '{"error": "no matching stub"}'
exit 1
STUBEOF2
    chmod +x "$STUB_DIR/curl"

    run bash "$SCRIPT_DIR/update_project.sh" '{"description":"Updated"}'
    [ "$status" -eq 0 ]

    # Should see both GET and PATCH in the curl args log
    curl_args=$(cat "${BATS_TMPDIR}/curl_args.log")
    [[ "$curl_args" == *"GET"* ]]
    [[ "$curl_args" == *"PATCH"* ]]
}
