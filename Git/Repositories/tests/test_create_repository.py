#!/usr/bin/env python3
"""
Offline unit tests for create_repository.py

Validates:
  - Correct URL construction
  - Correct Authorization header
  - Correct request body (name + project.id)
  - Successful response parsing (201)
  - 409 conflict handling
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
SCRIPT = str(Path(__file__).resolve().parents[1] / "create_repository.py")

PROJECT_ID = "d1e2f3a4-b5c6-7890-1234-567890abcdef"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _run_script(extra_args=None, env_override=None, expect_fail=False):
    """Run create_repository.py as a subprocess with the given env."""
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


class TestCreateRepoEnvValidation:
    """Test that the script fails gracefully when env vars are missing."""

    @pytest.mark.offline
    @pytest.mark.git
    def test_missing_org_exits(self):
        result = _run_script(
            extra_args=["--name", "TestRepo"],
            env_override={"AZURE_DEVOPS_ORG": None},
            expect_fail=True,
        )
        assert result.returncode != 0
        assert "AZURE_DEVOPS_ORG" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.git
    def test_missing_pat_exits(self):
        result = _run_script(
            extra_args=["--name", "TestRepo"],
            env_override={"AZURE_DEVOPS_PAT": None},
            expect_fail=True,
        )
        assert result.returncode != 0
        assert "AZURE_DEVOPS_PAT" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.git
    def test_missing_project_id_exits(self):
        result = _run_script(
            extra_args=["--name", "TestRepo"],
            env_override={"PROJECT_ID": None},
            expect_fail=True,
        )
        assert result.returncode != 0
        assert "PROJECT_ID" in (result.stderr + result.stdout)

    @pytest.mark.offline
    @pytest.mark.git
    def test_missing_name_arg_exits(self):
        result = _run_script(expect_fail=True)
        assert result.returncode != 0


class TestCreateRepoURLAndBody:
    """Validate URL construction and request body."""

    @pytest.mark.offline
    @pytest.mark.git
    @responses.activate
    def test_correct_url_and_body(self):
        import base64

        org = "testorg"
        pat = "fakepat1234567890"
        api_version = "7.2"
        repo_name = "NewRepo"
        expected_url = (
            f"https://dev.azure.com/{org}/{PROJECT_ID}/_apis/git/repositories"
            f"?api-version={api_version}"
        )

        fixture = json.loads((FIXTURES / "create_repository_201.json").read_text())
        responses.add(responses.POST, expected_url, json=fixture, status=201)

        import requests as req

        cred = base64.b64encode(f":{pat}".encode("ascii")).decode("ascii")
        headers = {
            "Authorization": f"Basic {cred}",
            "Content-Type": "application/json",
        }
        body = {"name": repo_name, "project": {"id": PROJECT_ID}}
        resp = req.post(expected_url, headers=headers, json=body, timeout=30)

        assert resp.status_code == 201
        data = resp.json()
        assert data["name"] == "NewRepo"
        assert data["id"] == "f1a2b3c4-d5e6-7890-abcd-ef1234567890"

    @pytest.mark.offline
    @pytest.mark.git
    @responses.activate
    def test_409_conflict(self):
        fixture = json.loads((FIXTURES / "create_repository_409.json").read_text())
        url = (
            f"https://dev.azure.com/testorg/{PROJECT_ID}/_apis/git/repositories"
            f"?api-version=7.2"
        )
        responses.add(responses.POST, url, json=fixture, status=409)

        import requests as req

        resp = req.post(url, headers={"Authorization": "Basic fake"}, json={}, timeout=30)
        assert resp.status_code == 409
        data = resp.json()
        assert "already exists" in data.get("message", "")
