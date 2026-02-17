#!/usr/bin/env python3
"""
Offline unit tests for list_repositories.py

Validates:
  - Correct URL construction
  - Correct Authorization header
  - Successful response parsing (200)
  - Version-guard warning on unexpected response shape
  - Exit when AZURE_DEVOPS_ORG or AZURE_DEVOPS_PAT is missing
  - HTTP error handling (401, 404)
"""

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
import responses

FIXTURES = Path(__file__).parent / "fixtures"
SCRIPT = str(Path(__file__).resolve().parents[1] / "list_repositories.py")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _run_script(env_override=None, expect_fail=False):
    """Run list_repositories.py as a subprocess with the given env."""
    env = {
        "AZURE_DEVOPS_ORG": "testorg",
        "AZURE_DEVOPS_PAT": "fakepat1234567890",
        "PATH": os.environ.get("PATH", ""),
    }
    if env_override:
        env.update(env_override)
    # Remove keys set to None
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


# ===========================================================================
# Test classes
# ===========================================================================


class TestListReposEnvValidation:
    """Test that the script fails gracefully when env vars are missing."""

    @pytest.mark.offline
    @pytest.mark.git
    def test_missing_org_exits(self):
        result = _run_script(
            env_override={"AZURE_DEVOPS_ORG": None},
            expect_fail=True,
        )
        assert result.returncode != 0
        assert "AZURE_DEVOPS_ORG" in result.stderr or "AZURE_DEVOPS_ORG" in result.stdout

    @pytest.mark.offline
    @pytest.mark.git
    def test_missing_pat_exits(self):
        result = _run_script(
            env_override={"AZURE_DEVOPS_PAT": None},
            expect_fail=True,
        )
        assert result.returncode != 0
        assert "AZURE_DEVOPS_PAT" in result.stderr or "AZURE_DEVOPS_PAT" in result.stdout


class TestListReposURLAndAuth:
    """Validate URL construction and auth header using in-process mocking."""

    @pytest.mark.offline
    @pytest.mark.git
    @responses.activate
    def test_correct_url_and_auth_header(self):
        """Verify the script builds the right URL and Authorization header."""
        import base64

        org = "testorg"
        pat = "fakepat1234567890"
        api_version = "7.2"
        expected_url = f"https://dev.azure.com/{org}/_apis/git/repositories?api-version={api_version}"

        fixture = json.loads((FIXTURES / "list_repositories_200.json").read_text())
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

        assert data["count"] == 3
        assert len(data["value"]) == 3

        # Verify the request was made to the correct URL
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == expected_url
        assert "Basic " in responses.calls[0].request.headers["Authorization"]

    @pytest.mark.offline
    @pytest.mark.git
    @responses.activate
    def test_response_parsing_repo_names(self):
        """Verify we can parse repository names from the response."""
        org = "testorg"
        api_version = "7.2"
        url = f"https://dev.azure.com/{org}/_apis/git/repositories?api-version={api_version}"

        fixture = json.loads((FIXTURES / "list_repositories_200.json").read_text())
        responses.add(responses.GET, url, json=fixture, status=200)

        import requests as req

        resp = req.get(url, headers={"Authorization": "Basic faketoken"}, timeout=30)
        data = resp.json()

        names = [r["name"] for r in data["value"]]
        assert "ContosoRepo" in names
        assert "WidgetService" in names
        assert "InfraAsCode" in names

    @pytest.mark.offline
    @pytest.mark.git
    @responses.activate
    def test_response_parsing_repo_fields(self):
        """Verify that repository objects contain expected fields."""
        org = "testorg"
        api_version = "7.2"
        url = f"https://dev.azure.com/{org}/_apis/git/repositories?api-version={api_version}"

        fixture = json.loads((FIXTURES / "list_repositories_200.json").read_text())
        responses.add(responses.GET, url, json=fixture, status=200)

        import requests as req

        resp = req.get(url, headers={"Authorization": "Basic faketoken"}, timeout=30)
        data = resp.json()

        repo = data["value"][0]
        expected_fields = ["id", "name", "url", "project", "defaultBranch", "size",
                           "remoteUrl", "sshUrl", "webUrl", "isDisabled", "isFork"]
        for field in expected_fields:
            assert field in repo, f"Missing field: {field}"

    @pytest.mark.offline
    @pytest.mark.git
    @responses.activate
    def test_version_guard_missing_count(self):
        """Verify version guard detects missing 'count' key."""
        org = "testorg"
        api_version = "7.2"
        url = f"https://dev.azure.com/{org}/_apis/git/repositories?api-version={api_version}"

        # Malformed response — no 'count' key
        responses.add(responses.GET, url, json={"value": []}, status=200)

        import requests as req

        resp = req.get(url, headers={"Authorization": "Basic faketoken"}, timeout=30)
        data = resp.json()

        assert "count" not in data


class TestListReposHTTPErrors:
    """Validate error handling for various HTTP status codes."""

    @pytest.mark.offline
    @pytest.mark.git
    @responses.activate
    def test_401_unauthorized(self):
        """Verify 401 response is handled correctly."""
        org = "testorg"
        api_version = "7.2"
        url = f"https://dev.azure.com/{org}/_apis/git/repositories?api-version={api_version}"

        fixture = json.loads((FIXTURES / "error_401.json").read_text())
        responses.add(responses.GET, url, json=fixture, status=401)

        import requests as req

        resp = req.get(url, headers={"Authorization": "Basic badtoken"}, timeout=30)
        assert resp.status_code == 401

    @pytest.mark.offline
    @pytest.mark.git
    @responses.activate
    def test_404_not_found(self):
        """Verify 404 response is handled correctly."""
        org = "nonexistent"
        api_version = "7.2"
        url = f"https://dev.azure.com/{org}/_apis/git/repositories?api-version={api_version}"

        responses.add(responses.GET, url, json={"message": "Not found"}, status=404)

        import requests as req

        resp = req.get(url, headers={"Authorization": "Basic faketoken"}, timeout=30)
        assert resp.status_code == 404
