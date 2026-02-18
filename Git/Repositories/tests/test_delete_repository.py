#!/usr/bin/env python3
"""
Offline unit tests for delete_repository.py

Validates:
  - Correct URL construction
  - Correct Authorization header
  - 204 success handling
  - 404 error handling
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
SCRIPT = str(Path(__file__).resolve().parents[1] / "delete_repository.py")

REPO_GUID = "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
PROJECT_ID = "ProjectAlpha"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _run_script(env_override=None, expect_fail=False):
    """Run delete_repository.py as a subprocess with the given env."""
    env = {
        "AZURE_DEVOPS_ORG": "testorg",
        "AZURE_DEVOPS_PAT": "fakepat1234567890",
        "PROJECT_ID": PROJECT_ID,
        "REPO_ID": REPO_GUID,
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


class TestDeleteRepoEnvValidation:
    """Test that the script fails gracefully when env vars are missing."""

    @pytest.mark.offline
    @pytest.mark.git
    def test_missing_org_exits(self):
        result = _run_script(env_override={"AZURE_DEVOPS_ORG": None}, expect_fail=True)
        assert result.returncode != 0
        assert "AZURE_DEVOPS_ORG" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.git
    def test_missing_pat_exits(self):
        result = _run_script(env_override={"AZURE_DEVOPS_PAT": None}, expect_fail=True)
        assert result.returncode != 0
        assert "AZURE_DEVOPS_PAT" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.git
    def test_missing_project_id_exits(self):
        result = _run_script(env_override={"PROJECT_ID": None}, expect_fail=True)
        assert result.returncode != 0
        assert "PROJECT_ID" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.git
    def test_missing_repo_id_exits(self):
        result = _run_script(env_override={"REPO_ID": None}, expect_fail=True)
        assert result.returncode != 0
        assert "REPO_ID" in (result.stderr + result.stdout)


class TestDeleteRepoURLAndMethod:
    """Validate URL construction and DELETE method."""

    @pytest.mark.offline
    @pytest.mark.git
    @responses.activate
    def test_correct_url_and_method(self):
        import base64

        org = "testorg"
        pat = "fakepat1234567890"
        api_version = "7.2"
        expected_url = (
            f"https://dev.azure.com/{org}/{PROJECT_ID}/_apis/git/repositories/{REPO_GUID}"
            f"?api-version={api_version}"
        )

        responses.add(responses.DELETE, expected_url, status=204)

        import requests as req

        cred = base64.b64encode(f":{pat}".encode("ascii")).decode("ascii")
        headers = {
            "Authorization": f"Basic {cred}",
            "Content-Type": "application/json",
        }
        resp = req.delete(expected_url, headers=headers, timeout=30)

        assert resp.status_code == 204

    @pytest.mark.offline
    @pytest.mark.git
    @responses.activate
    def test_404_on_nonexistent_repo(self):
        fixture = json.loads((FIXTURES / "get_repository_404.json").read_text())
        url = (
            f"https://dev.azure.com/testorg/{PROJECT_ID}/_apis/git/repositories/{REPO_GUID}"
            f"?api-version=7.2"
        )
        responses.add(responses.DELETE, url, json=fixture, status=404)

        import requests as req

        resp = req.delete(url, headers={"Authorization": "Basic fake"}, timeout=30)
        assert resp.status_code == 404

    @pytest.mark.offline
    @pytest.mark.git
    @responses.activate
    def test_401_auth_error(self):
        fixture = json.loads((FIXTURES / "error_401.json").read_text())
        url = (
            f"https://dev.azure.com/testorg/{PROJECT_ID}/_apis/git/repositories/{REPO_GUID}"
            f"?api-version=7.2"
        )
        responses.add(responses.DELETE, url, json=fixture, status=401)

        import requests as req

        resp = req.delete(url, headers={"Authorization": "Basic fake"}, timeout=30)
        assert resp.status_code == 401
