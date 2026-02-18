# Pipelines API Area

Azure DevOps REST API 7.2 — **Pipelines** area.

This area covers pipelines definitions, pipeline runs, and related resources.

> **Status:** In progress — see operations table below.

## Authentication

All scripts expect a **Personal Access Token (PAT)** supplied via the environment variable `AZURE_DEVOPS_PAT`. Basic Auth is used with an empty username and the PAT as the password.

## API Version

Every request targets **`api-version=7.2-preview.1`**.

## Operations

### Pipelines

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Pipelines | `GET` | `/{org}/{project}/_apis/pipelines` | ✅ `list_pipelines.py` | ✅ `List-Pipelines.ps1` | ✅ `list_pipelines.sh` | ✅ pytest, Pester, bats |
| Get Pipeline | `GET` | `/{org}/{project}/_apis/pipelines/{id}` | ✅ `get_pipeline.py` | ✅ `Get-Pipeline.ps1` | ✅ `get_pipeline.sh` | ✅ pytest, Pester, bats |
| Run Pipeline | `POST` | `/{org}/{project}/_apis/pipelines/{id}/runs` | ✅ `run_pipeline.py` | ✅ `Start-Pipeline.ps1` | ✅ `run_pipeline.sh` | ✅ pytest, Pester, bats |

### Runs

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Runs | `GET` | `/{org}/{project}/_apis/pipelines/{id}/runs` | ✅ `list_runs.py` | ✅ `List-PipelineRuns.ps1` | ✅ `list_runs.sh` | ✅ pytest, Pester, bats |
| Get Run | `GET` | `/{org}/{project}/_apis/pipelines/{pipelineId}/runs/{runId}` | ✅ `get_run.py` | ✅ `Get-PipelineRun.ps1` | ✅ `get_run.sh` | ✅ pytest, Pester, bats |

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `AZURE_DEVOPS_ORG` | Yes | Azure DevOps organisation name |
| `AZURE_DEVOPS_PAT` | Yes | Personal Access Token |
| `PROJECT_ID` | Yes | Project name or GUID |
| `PIPELINE_ID` | Get/Run/ListRuns | Pipeline ID (integer) |
