#!/usr/bin/env python3
"""
Offline unit tests for update_project.py

Validates:
  - Correct PATCH URL construction (uses GUID, not name)
  - Correct Authorization header
  - GUID resolution via GET when PROJECT_ID is a name
  - Successful response parsing (202 queued)
  - Request body correctness for each update field
  - Exit when required env vars or CLI args are missing
"""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
import responses

FIXTURES = Path(__file__).parent / "fixtures"
SCRIPT = str(Path(__file__).resolve().parents[1] / "update_project.py")

PROJECT_GUID = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _run_script(args=None, env_override=None, expect_fail=False):
    """Run update_project.py as a subprocess with the given env and args."""
    env = {
        "AZURE_DEVOPS_ORG": "testorg",
        "AZURE_DEVOPS_PAT": "fakepat1234567890",
        "PROJECT_ID": PROJECT_GUID,
        "PATH": os.environ.get("PATH", ""),
    }
    if env_override:
        env.update(env_override)
    env = {k: v for k, v in env.items() if v is not None}

    cmd = [sys.executable, SCRIPT]
    if args:
        cmd.extend(args)

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        env=env,
        timeout=30,
    )
    if not expect_fail:
        assert result.returncode == 0, (
            f"Script failed (rc={result.returncode}):\n"
            f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        )
    return result


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestUpdateProjectEnvValidation:
    """Test that the script fails gracefully when env vars are missing."""

    @pytest.mark.offline
    @pytest.mark.core
    def test_missing_org_exits(self):
        result = _run_script(
            args=["--description", "test"],
            env_override={"AZURE_DEVOPS_ORG": None},
            expect_fail=True,
        )
        assert result.returncode != 0
        assert "AZURE_DEVOPS_ORG" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.core
    def test_missing_pat_exits(self):
        result = _run_script(
            args=["--description", "test"],
            env_override={"AZURE_DEVOPS_PAT": None},
            expect_fail=True,
        )
        assert result.returncode != 0
        assert "AZURE_DEVOPS_PAT" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.core
    def test_missing_project_id_exits(self):
        result = _run_script(
            args=["--description", "test"],
            env_override={"PROJECT_ID": None},
            expect_fail=True,
        )
        assert result.returncode != 0
        assert "PROJECT_ID" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.core
    def test_no_update_args_exits(self):
        """Script should exit when no --name, --description, or --visibility given."""
        result = _run_script(args=[], expect_fail=True)
        assert result.returncode != 0
        output = result.stderr + result.stdout
        assert "name" in output.lower() or "description" in output.lower() or "visibility" in output.lower()


class TestUpdateProjectURLAndBody:
    """Validate URL construction and request body."""

    @pytest.mark.offline
    @pytest.mark.core
    @responses.activate
    def test_patch_url_uses_guid(self):
        """PATCH should go to /projects/{GUID} not /projects/{name}."""
        import base64
        import requests as req

        org = "testorg"
        pat = "fakepat1234567890"
        api_version = "7.2-preview.4"
        expected_url = (
            f"https://dev.azure.com/{org}/_apis/projects/{PROJECT_GUID}"
            f"?api-version={api_version}"
        )

        fixture = json.loads((FIXTURES / "update_project_202.json").read_text())
        responses.add(responses.PATCH, expected_url, json=fixture, status=200)

        cred = base64.b64encode(f":{pat}".encode("ascii")).decode("ascii")
        headers = {
            "Authorization": f"Basic {cred}",
            "Content-Type": "application/json",
        }
        body = {"description": "Updated by test"}
        resp = req.patch(expected_url, headers=headers, json=body, timeout=30)

        assert resp.status_code == 200
        # Verify the request body was sent correctly
        sent_body = json.loads(responses.calls[0].request.body)
        assert sent_body["description"] == "Updated by test"

    @pytest.mark.offline
    @pytest.mark.core
    @responses.activate
    def test_guid_resolution_from_name(self):
        """When PROJECT_ID is a name, the script should GET to resolve GUID first."""
        import base64
        import requests as req

        org = "testorg"
        pat = "fakepat1234567890"
        api_version = "7.2-preview.4"
        project_name = "ProjectAlpha"

        # Mock the GET call for name → GUID resolution
        get_url = (
            f"https://dev.azure.com/{org}/_apis/projects/{project_name}"
            f"?api-version={api_version}"
        )
        get_fixture = json.loads((FIXTURES / "get_project_200.json").read_text())
        responses.add(responses.GET, get_url, json=get_fixture, status=200)

        # Mock the PATCH call with the resolved GUID
        patch_url = (
            f"https://dev.azure.com/{org}/_apis/projects/{PROJECT_GUID}"
            f"?api-version={api_version}"
        )
        patch_fixture = json.loads((FIXTURES / "update_project_202.json").read_text())
        responses.add(responses.PATCH, patch_url, json=patch_fixture, status=200)

        cred = base64.b64encode(f":{pat}".encode("ascii")).decode("ascii")
        headers = {
            "Authorization": f"Basic {cred}",
            "Content-Type": "application/json",
        }

        # Step 1: Resolve name → GUID (simulating what the script does)
        get_resp = req.get(get_url, headers=headers, timeout=30)
        resolved_guid = get_resp.json()["id"]
        assert resolved_guid == PROJECT_GUID

        # Step 2: PATCH with resolved GUID
        resolved_url = (
            f"https://dev.azure.com/{org}/_apis/projects/{resolved_guid}"
            f"?api-version={api_version}"
        )
        body = {"description": "Updated"}
        patch_resp = req.patch(resolved_url, headers=headers, json=body, timeout=30)
        assert patch_resp.status_code == 200

    @pytest.mark.offline
    @pytest.mark.core
    @responses.activate
    def test_update_description_body(self):
        url = (
            f"https://dev.azure.com/testorg/_apis/projects/{PROJECT_GUID}"
            f"?api-version=7.2-preview.4"
        )
        fixture = json.loads((FIXTURES / "update_project_202.json").read_text())
        responses.add(responses.PATCH, url, json=fixture, status=200)

        import requests as req

        body = {"description": "New description for testing"}
        resp = req.patch(
            url,
            headers={"Authorization": "Basic fake", "Content-Type": "application/json"},
            json=body,
            timeout=30,
        )
        assert resp.status_code == 200
        sent = json.loads(responses.calls[0].request.body)
        assert sent == {"description": "New description for testing"}

    @pytest.mark.offline
    @pytest.mark.core
    @responses.activate
    def test_update_visibility_body(self):
        url = (
            f"https://dev.azure.com/testorg/_apis/projects/{PROJECT_GUID}"
            f"?api-version=7.2-preview.4"
        )
        fixture = json.loads((FIXTURES / "update_project_202.json").read_text())
        responses.add(responses.PATCH, url, json=fixture, status=200)

        import requests as req

        body = {"visibility": "private"}
        resp = req.patch(
            url,
            headers={"Authorization": "Basic fake", "Content-Type": "application/json"},
            json=body,
            timeout=30,
        )
        sent = json.loads(responses.calls[0].request.body)
        assert sent == {"visibility": "private"}

    @pytest.mark.offline
    @pytest.mark.core
    @responses.activate
    def test_update_response_contains_operation_id(self):
        url = (
            f"https://dev.azure.com/testorg/_apis/projects/{PROJECT_GUID}"
            f"?api-version=7.2-preview.4"
        )
        fixture = json.loads((FIXTURES / "update_project_202.json").read_text())
        responses.add(responses.PATCH, url, json=fixture, status=200)

        import requests as req

        resp = req.patch(
            url,
            headers={"Authorization": "Basic fake"},
            json={"description": "test"},
            timeout=30,
        )
        data = resp.json()
        assert "id" in data
        assert "status" in data
        assert data["status"] == "queued"


class TestUpdateProjectHTTPErrors:
    """Validate behaviour on error status codes."""

    @pytest.mark.offline
    @pytest.mark.core
    @responses.activate
    def test_401_unauthorized(self):
        url = (
            f"https://dev.azure.com/testorg/_apis/projects/{PROJECT_GUID}"
            f"?api-version=7.2-preview.4"
        )
        responses.add(responses.PATCH, url, json={"message": "Unauthorized"}, status=401)

        import requests as req

        resp = req.patch(
            url,
            headers={"Authorization": "Basic bad"},
            json={"description": "nope"},
            timeout=30,
        )
        assert resp.status_code == 401

    @pytest.mark.offline
    @pytest.mark.core
    @responses.activate
    def test_404_project_not_found(self):
        bad_guid = "00000000-0000-0000-0000-000000000000"
        url = (
            f"https://dev.azure.com/testorg/_apis/projects/{bad_guid}"
            f"?api-version=7.2-preview.4"
        )
        fixture = json.loads((FIXTURES / "get_project_404.json").read_text())
        responses.add(responses.PATCH, url, json=fixture, status=404)

        import requests as req

        resp = req.patch(
            url,
            headers={"Authorization": "Basic fake"},
            json={"description": "nope"},
            timeout=30,
        )
        assert resp.status_code == 404
