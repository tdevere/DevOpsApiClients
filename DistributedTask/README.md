# Distributed Task API Area

Azure DevOps REST API 7.2 — **Distributed Task** area.

This area covers agent pools, variable groups, and environments used for pipeline execution.

> **Status:** In progress — see operations table below.

## Authentication

All scripts expect a **Personal Access Token (PAT)** supplied via the environment variable `AZURE_DEVOPS_PAT`. Basic Auth is used with an empty username and the PAT as the password.

## API Version

Every request targets **`api-version=7.2`**.

## Operations

### Pools (Agent Pools)

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Pools | `GET` | `/{org}/_apis/distributedtask/pools` | ✅ `list_pools.py` | ✅ `List-AgentPools.ps1` | ✅ `list_pools.sh` | ✅ pytest, Pester, bats |

### Variable Groups

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Variable Groups | `GET` | `/{org}/{project}/_apis/distributedtask/variablegroups` | ✅ `list_variable_groups.py` | ✅ `List-VariableGroups.ps1` | ✅ `list_variable_groups.sh` | ✅ pytest, Pester, bats |
| Get Variable Group | `GET` | `/{org}/{project}/_apis/distributedtask/variablegroups/{groupId}` | ✅ `get_variable_group.py` | ✅ `Get-VariableGroup.ps1` | ✅ `get_variable_group.sh` | ✅ pytest, Pester, bats |

### Environments

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Environments | `GET` | `/{org}/{project}/_apis/distributedtask/environments` | ✅ `list_environments.py` | ✅ `List-Environments.ps1` | ✅ `list_environments.sh` | ✅ pytest, Pester, bats |
| Get Environment | `GET` | `/{org}/{project}/_apis/distributedtask/environments/{environmentId}` | ✅ `get_environment.py` | ✅ `Get-Environment.ps1` | ✅ `get_environment.sh` | ✅ pytest, Pester, bats |

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `AZURE_DEVOPS_ORG` | Yes | Azure DevOps organisation name |
| `AZURE_DEVOPS_PAT` | Yes | Personal Access Token |
| `PROJECT_ID` | Variable Groups, Environments | Project name or GUID |
| `VARIABLE_GROUP_ID` | Get Variable Group | Variable group ID (integer) |
| `ENVIRONMENT_ID` | Get Environment | Environment ID (integer) |
