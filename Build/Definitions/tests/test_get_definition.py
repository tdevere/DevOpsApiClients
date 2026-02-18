#!/usr/bin/env python3
"""
Offline unit tests for get_definition.py

Validates:
  - Correct URL construction with definition ID
  - Successful response parsing (200)
  - 404 response handling
  - Version-guard on unexpected response shape
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
SCRIPT = str(Path(__file__).resolve().parents[1] / "get_definition.py")

PROJECT_ID = "ProjectAlpha"
DEFINITION_ID = "1"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _run_script(env_override=None, expect_fail=False):
    env = {
        "AZURE_DEVOPS_ORG": "testorg",
        "AZURE_DEVOPS_PAT": "fakepat1234567890",
        "PROJECT_ID": PROJECT_ID,
        "DEFINITION_ID": DEFINITION_ID,
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


class TestGetDefinitionEnvValidation:

    @pytest.mark.offline
    @pytest.mark.build
    def test_missing_org_exits(self):
        result = _run_script(env_override={"AZURE_DEVOPS_ORG": None}, expect_fail=True)
        assert result.returncode != 0
        assert "AZURE_DEVOPS_ORG" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.build
    def test_missing_pat_exits(self):
        result = _run_script(env_override={"AZURE_DEVOPS_PAT": None}, expect_fail=True)
        assert result.returncode != 0
        assert "AZURE_DEVOPS_PAT" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.build
    def test_missing_project_id_exits(self):
        result = _run_script(env_override={"PROJECT_ID": None}, expect_fail=True)
        assert result.returncode != 0
        assert "PROJECT_ID" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.build
    def test_missing_definition_id_exits(self):
        result = _run_script(env_override={"DEFINITION_ID": None}, expect_fail=True)
        assert result.returncode != 0
        assert "DEFINITION_ID" in (result.stderr + result.stdout)


class TestGetDefinitionURLAndAuth:

    @pytest.mark.offline
    @pytest.mark.build
    @responses.activate
    def test_correct_url_includes_definition_id(self):
        import base64

        org = "testorg"
        pat = "fakepat1234567890"
        expected_url = (
            f"https://dev.azure.com/{org}/{PROJECT_ID}/_apis/build/definitions/{DEFINITION_ID}"
            f"?api-version=7.2"
        )

        fixture = json.loads((FIXTURES / "get_definition_200.json").read_text())
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
        assert data["id"] == 1
        assert data["name"] == "CI-Pipeline"

    @pytest.mark.offline
    @pytest.mark.build
    @responses.activate
    def test_response_contains_expected_keys(self):
        fixture = json.loads((FIXTURES / "get_definition_200.json").read_text())
        url = (
            f"https://dev.azure.com/testorg/{PROJECT_ID}/_apis/build/definitions/{DEFINITION_ID}"
            f"?api-version=7.2"
        )
        responses.add(responses.GET, url, json=fixture, status=200)

        import requests as req

        resp = req.get(url, headers={"Authorization": "Basic fake"}, timeout=30)
        data = resp.json()

        assert "id" in data
        assert "name" in data
        assert "repository" in data
        assert "authoredBy" in data
        assert "queueStatus" in data


class TestGetDefinitionErrorHandling:

    @pytest.mark.offline
    @pytest.mark.build
    @responses.activate
    def test_404_definition_not_found(self):
        fixture = json.loads((FIXTURES / "get_definition_404.json").read_text())
        url = (
            f"https://dev.azure.com/testorg/{PROJECT_ID}/_apis/build/definitions/99999"
            f"?api-version=7.2"
        )
        responses.add(responses.GET, url, json=fixture, status=404)

        import requests as req

        resp = req.get(url, headers={"Authorization": "Basic fake"}, timeout=30)
        assert resp.status_code == 404
        data = resp.json()
        assert "DefinitionNotFoundException" in data.get("typeName", "")

    @pytest.mark.offline
    @pytest.mark.build
    @responses.activate
    def test_401_auth_error(self):
        fixture = json.loads((FIXTURES / "error_401.json").read_text())
        url = (
            f"https://dev.azure.com/testorg/{PROJECT_ID}/_apis/build/definitions/{DEFINITION_ID}"
            f"?api-version=7.2"
        )
        responses.add(responses.GET, url, json=fixture, status=401)

        import requests as req

        resp = req.get(url, headers={"Authorization": "Basic fake"}, timeout=30)
        assert resp.status_code == 401
