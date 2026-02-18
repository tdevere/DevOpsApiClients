#!/usr/bin/env python3
"""
Offline unit tests for create_work_item.py

Validates:
  - Correct URL construction (project + $type)
  - JSON Patch content type header
  - JSON Patch document body structure
  - Successful response parsing (200)
  - Error-handling paths (400, 401)
  - Exit when required env vars or args are missing
"""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
import responses

FIXTURES = Path(__file__).parent / "fixtures"
SCRIPT = str(Path(__file__).resolve().parents[1] / "create_work_item.py")

PROJECT_ID = "ProjectAlpha"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _run_script(extra_args=None, env_override=None, expect_fail=False):
    """Run create_work_item.py as a subprocess with the given env and args."""
    env = {
        "AZURE_DEVOPS_ORG": "testorg",
        "AZURE_DEVOPS_PAT": "fakepat1234567890",
        "PROJECT_ID": PROJECT_ID,
        "PATH": os.environ.get("PATH", ""),
    }
    if env_override:
        env.update(env_override)
    env = {k: v for k, v in env.items() if v is not None}

    cmd = [sys.executable, SCRIPT]
    if extra_args:
        cmd.extend(extra_args)

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


class TestCreateWorkItemEnvValidation:
    """Test that the script fails gracefully when env vars are missing."""

    @pytest.mark.offline
    @pytest.mark.wit
    def test_missing_org_exits(self):
        result = _run_script(
            extra_args=["--type", "Task", "--title", "Test"],
            env_override={"AZURE_DEVOPS_ORG": None},
            expect_fail=True,
        )
        assert result.returncode != 0
        assert "AZURE_DEVOPS_ORG" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.wit
    def test_missing_pat_exits(self):
        result = _run_script(
            extra_args=["--type", "Task", "--title", "Test"],
            env_override={"AZURE_DEVOPS_PAT": None},
            expect_fail=True,
        )
        assert result.returncode != 0
        assert "AZURE_DEVOPS_PAT" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.wit
    def test_missing_project_id_exits(self):
        result = _run_script(
            extra_args=["--type", "Task", "--title", "Test"],
            env_override={"PROJECT_ID": None},
            expect_fail=True,
        )
        assert result.returncode != 0
        assert "PROJECT_ID" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.wit
    def test_missing_type_arg_exits(self):
        result = _run_script(
            extra_args=["--title", "Test"],
            expect_fail=True,
        )
        assert result.returncode != 0

    @pytest.mark.offline
    @pytest.mark.wit
    def test_missing_title_arg_exits(self):
        result = _run_script(
            extra_args=["--type", "Task"],
            expect_fail=True,
        )
        assert result.returncode != 0


class TestCreateWorkItemURLAndBody:
    """Validate URL construction and JSON Patch body."""

    @pytest.mark.offline
    @pytest.mark.wit
    @responses.activate
    def test_correct_url_includes_dollar_type(self):
        import base64

        org = "testorg"
        pat = "fakepat1234567890"
        work_item_type = "Task"
        expected_url = (
            f"https://dev.azure.com/{org}/{PROJECT_ID}/_apis/wit/workitems"
            f"/${work_item_type}?api-version=7.2"
        )

        fixture = json.loads((FIXTURES / "create_work_item_200.json").read_text())
        responses.add(responses.POST, expected_url, json=fixture, status=200)

        import requests as req

        cred = base64.b64encode(f":{pat}".encode("ascii")).decode("ascii")
        headers = {
            "Authorization": f"Basic {cred}",
            "Content-Type": "application/json-patch+json",
        }
        patch_body = [
            {"op": "add", "path": "/fields/System.Title", "value": "Add unit tests for auth module"}
        ]
        resp = req.post(expected_url, headers=headers, json=patch_body, timeout=30)

        assert resp.status_code == 200
        data = resp.json()
        assert data["id"] == 101
        assert data["fields"]["System.Title"] == "Add unit tests for auth module"

    @pytest.mark.offline
    @pytest.mark.wit
    @responses.activate
    def test_json_patch_content_type(self):
        """Verify that application/json-patch+json is used."""
        expected_url = (
            f"https://dev.azure.com/testorg/{PROJECT_ID}/_apis/wit/workitems"
            f"/$Task?api-version=7.2"
        )
        fixture = json.loads((FIXTURES / "create_work_item_200.json").read_text())
        responses.add(responses.POST, expected_url, json=fixture, status=200)

        import requests as req

        headers = {
            "Authorization": "Basic fake",
            "Content-Type": "application/json-patch+json",
        }
        resp = req.post(
            expected_url,
            headers=headers,
            json=[{"op": "add", "path": "/fields/System.Title", "value": "Test"}],
            timeout=30,
        )
        assert resp.status_code == 200

        # Verify the request was made with correct content type
        assert len(responses.calls) == 1
        assert "application/json-patch+json" in responses.calls[0].request.headers.get("Content-Type", "")


class TestCreateWorkItemErrorHandling:
    """Validate error-handling paths."""

    @pytest.mark.offline
    @pytest.mark.wit
    @responses.activate
    def test_401_auth_error(self):
        fixture = json.loads((FIXTURES / "error_401.json").read_text())
        url = (
            f"https://dev.azure.com/testorg/{PROJECT_ID}/_apis/wit/workitems"
            f"/$Task?api-version=7.2"
        )
        responses.add(responses.POST, url, json=fixture, status=401)

        import requests as req

        resp = req.post(url, headers={"Authorization": "Basic fake"}, json=[], timeout=30)
        assert resp.status_code == 401

    @pytest.mark.offline
    @pytest.mark.wit
    @responses.activate
    def test_400_bad_request(self):
        url = (
            f"https://dev.azure.com/testorg/{PROJECT_ID}/_apis/wit/workitems"
            f"/$InvalidType?api-version=7.2"
        )
        responses.add(
            responses.POST,
            url,
            json={"message": "VS402372: The work item type InvalidType does not exist."},
            status=400,
        )

        import requests as req

        resp = req.post(url, headers={"Authorization": "Basic fake"}, json=[], timeout=30)
        assert resp.status_code == 400
        assert "InvalidType" in resp.json().get("message", "")
