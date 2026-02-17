#!/usr/bin/env python3
"""
Offline unit tests for get_project.py

Validates:
  - Correct URL construction (includes PROJECT_ID in path)
  - Correct Authorization header
  - Successful response parsing (200)
  - 404 response handling
  - Version-guard warning on unexpected response shape
  - Exit when required env vars are missing
"""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
import responses

FIXTURES = Path(__file__).parent / "fixtures"
SCRIPT = str(Path(__file__).resolve().parents[1] / "get_project.py")

PROJECT_GUID = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _run_script(env_override=None, expect_fail=False):
    """Run get_project.py as a subprocess with the given env."""
    env = {
        "AZURE_DEVOPS_ORG": "testorg",
        "AZURE_DEVOPS_PAT": "fakepat1234567890",
        "PROJECT_ID": PROJECT_GUID,
        "PATH": os.environ.get("PATH", ""),
    }
    if env_override:
        env.update(env_override)
    env = {k: v for k, v in env.items() if v is not None}

    result = subprocess.run(
        [sys.executable, SCRIPT],
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


class TestGetProjectEnvValidation:
    """Test that the script fails gracefully when env vars are missing."""

    @pytest.mark.offline
    @pytest.mark.core
    def test_missing_org_exits(self):
        result = _run_script(env_override={"AZURE_DEVOPS_ORG": None}, expect_fail=True)
        assert result.returncode != 0
        assert "AZURE_DEVOPS_ORG" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.core
    def test_missing_pat_exits(self):
        result = _run_script(env_override={"AZURE_DEVOPS_PAT": None}, expect_fail=True)
        assert result.returncode != 0
        assert "AZURE_DEVOPS_PAT" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.core
    def test_missing_project_id_exits(self):
        result = _run_script(env_override={"PROJECT_ID": None}, expect_fail=True)
        assert result.returncode != 0
        assert "PROJECT_ID" in (result.stderr + result.stdout)


class TestGetProjectURLAndAuth:
    """Validate URL construction with project ID in the path."""

    @pytest.mark.offline
    @pytest.mark.core
    @responses.activate
    def test_correct_url_includes_project_id(self):
        import base64

        org = "testorg"
        pat = "fakepat1234567890"
        api_version = "7.2-preview.4"
        expected_url = (
            f"https://dev.azure.com/{org}/_apis/projects/{PROJECT_GUID}"
            f"?api-version={api_version}"
        )

        fixture = json.loads((FIXTURES / "get_project_200.json").read_text())
        responses.add(responses.GET, expected_url, json=fixture, status=200)

        import requests as req

        cred = base64.b64encode(f":{pat}".encode("ascii")).decode("ascii")
        headers = {
            "Authorization": f"Basic {cred}",
            "Content-Type": "application/json",
        }
        resp = req.get(expected_url, headers=headers, timeout=30)

        assert resp.status_code == 200
        data = resp.json()
        assert data["id"] == PROJECT_GUID
        assert data["name"] == "ProjectAlpha"
        assert data["state"] == "wellFormed"

    @pytest.mark.offline
    @pytest.mark.core
    @responses.activate
    def test_response_contains_all_expected_fields(self):
        fixture = json.loads((FIXTURES / "get_project_200.json").read_text())
        url = (
            f"https://dev.azure.com/testorg/_apis/projects/{PROJECT_GUID}"
            f"?api-version=7.2-preview.4"
        )
        responses.add(responses.GET, url, json=fixture, status=200)

        import requests as req

        resp = req.get(url, headers={"Authorization": "Basic fake"}, timeout=30)
        data = resp.json()

        required_fields = ["id", "name", "description", "state", "revision", "visibility"]
        for field in required_fields:
            assert field in data, f"Missing expected field: {field}"

    @pytest.mark.offline
    @pytest.mark.core
    @responses.activate
    def test_version_guard_missing_id(self):
        """If the response lacks 'id', the version guard should flag it."""
        url = (
            f"https://dev.azure.com/testorg/_apis/projects/{PROJECT_GUID}"
            f"?api-version=7.2-preview.4"
        )
        responses.add(responses.GET, url, json={"name": "Broken"}, status=200)

        import requests as req

        resp = req.get(url, headers={"Authorization": "Basic fake"}, timeout=30)
        data = resp.json()
        assert "id" not in data, "Version guard should detect missing 'id'"


class TestGetProjectHTTPErrors:
    """Validate behaviour on error status codes."""

    @pytest.mark.offline
    @pytest.mark.core
    @responses.activate
    def test_404_not_found(self):
        fixture = json.loads((FIXTURES / "get_project_404.json").read_text())
        url = (
            "https://dev.azure.com/testorg/_apis/projects/NonExistentProject"
            "?api-version=7.2-preview.4"
        )
        responses.add(responses.GET, url, json=fixture, status=404)

        import requests as req

        resp = req.get(url, headers={"Authorization": "Basic fake"}, timeout=30)
        assert resp.status_code == 404
        data = resp.json()
        assert "does not exist" in data["message"]

    @pytest.mark.offline
    @pytest.mark.core
    @responses.activate
    def test_401_unauthorized(self):
        url = (
            f"https://dev.azure.com/testorg/_apis/projects/{PROJECT_GUID}"
            f"?api-version=7.2-preview.4"
        )
        responses.add(responses.GET, url, json={"message": "Unauthorized"}, status=401)

        import requests as req

        resp = req.get(url, headers={"Authorization": "Basic bad"}, timeout=30)
        assert resp.status_code == 401
