# Build API Area

Azure DevOps REST API 7.2 — **Build** area.

This area covers build definitions, builds, timelines, and artifacts.

> **Status:** In progress — see operations table below.

## Authentication

All scripts expect a **Personal Access Token (PAT)** supplied via the environment variable `AZURE_DEVOPS_PAT`. Basic Auth is used with an empty username and the PAT as the password.

## API Version

Every request targets **`api-version=7.2`**.

## Operations

### Definitions

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Definitions | `GET` | `/{org}/{project}/_apis/build/definitions` | ✅ `list_definitions.py` | ✅ `List-Definitions.ps1` | ✅ `list_definitions.sh` | ✅ pytest, Pester, bats |
| Get Definition | `GET` | `/{org}/{project}/_apis/build/definitions/{id}` | ✅ `get_definition.py` | ✅ `Get-Definition.ps1` | ✅ `get_definition.sh` | ✅ pytest, Pester, bats |

### Builds

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Builds | `GET` | `/{org}/{project}/_apis/build/builds` | ✅ `list_builds.py` | ✅ `List-Builds.ps1` | ✅ `list_builds.sh` | ✅ pytest, Pester, bats |
| Get Build | `GET` | `/{org}/{project}/_apis/build/builds/{buildId}` | ✅ `get_build.py` | ✅ `Get-Build.ps1` | ✅ `get_build.sh` | ✅ pytest, Pester, bats |

### Artifacts

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Artifacts | `GET` | `/{org}/{project}/_apis/build/builds/{buildId}/artifacts` | ✅ `list_artifacts.py` | ✅ `List-BuildArtifacts.ps1` | ✅ `list_artifacts.sh` | ✅ pytest, Pester, bats |
