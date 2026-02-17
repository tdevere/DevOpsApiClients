# Git API Area

Azure DevOps REST API 7.2 — **Git** area.

This area covers Git-specific resources such as repositories, pull requests, commits, and refs.

> **Status:** In progress — see operations table below.

## Authentication

All scripts expect a **Personal Access Token (PAT)** supplied via the environment variable `AZURE_DEVOPS_PAT`. Basic Auth is used with an empty username and the PAT as the password.

## API Version

Every request targets **`api-version=7.2`**.

## Operations

### Repositories

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Repositories | `GET` | `/{org}/_apis/git/repositories` | ✅ `list_repositories.py` | ✅ `List-Repositories.ps1` | ✅ `list_repositories.sh` | ✅ pytest, Pester, bats |
