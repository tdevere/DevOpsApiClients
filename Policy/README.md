# Policy API Area

Azure DevOps REST API 7.2 — **Policy** area.

This area covers policy configurations used to enforce branch policies, required reviewers, build validation, and other governance rules.

> **Status:** In progress — see operations table below.

## Authentication

All scripts expect a **Personal Access Token (PAT)** supplied via the environment variable `AZURE_DEVOPS_PAT`. Basic Auth is used with an empty username and the PAT as the password.

## API Version

Every request targets **`api-version=7.2`**.

## Operations

### Configurations

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Configurations | `GET` | `/{org}/{project}/_apis/policy/configurations` | ✅ `list_configurations.py` | ✅ `List-PolicyConfigurations.ps1` | ✅ `list_configurations.sh` | ✅ pytest, Pester, bats |
| Get Configuration | `GET` | `/{org}/{project}/_apis/policy/configurations/{configurationId}` | ✅ `get_configuration.py` | ✅ `Get-PolicyConfiguration.ps1` | ✅ `get_configuration.sh` | ✅ pytest, Pester, bats |

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `AZURE_DEVOPS_ORG` | Yes | Azure DevOps organisation name |
| `AZURE_DEVOPS_PAT` | Yes | Personal Access Token |
| `PROJECT_ID` | Yes | Project name or GUID |
| `CONFIGURATION_ID` | Get Configuration | Policy configuration ID (integer) |
