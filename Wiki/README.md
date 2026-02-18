# Wiki API Area

Azure DevOps REST API 7.2 — **Wiki** area.

This area covers wiki resources — project wikis and code wikis.

> **Status:** In progress — see operations table below.

## Authentication

All scripts expect a **Personal Access Token (PAT)** supplied via the environment variable `AZURE_DEVOPS_PAT`. Basic Auth is used with an empty username and the PAT as the password.

## API Version

Every request targets **`api-version=7.2`**.

## Operations

### Wikis

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Wikis | `GET` | `/{org}/{project}/_apis/wiki/wikis` | ✅ `list_wikis.py` | ✅ `List-Wikis.ps1` | ✅ `list_wikis.sh` | ✅ pytest, Pester, bats |
| Get Wiki | `GET` | `/{org}/{project}/_apis/wiki/wikis/{wikiIdentifier}` | ✅ `get_wiki.py` | ✅ `Get-Wiki.ps1` | ✅ `get_wiki.sh` | ✅ pytest, Pester, bats |

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `AZURE_DEVOPS_ORG` | Yes | Azure DevOps organisation name |
| `AZURE_DEVOPS_PAT` | Yes | Personal Access Token |
| `PROJECT_ID` | Yes | Project name or GUID |
| `WIKI_IDENTIFIER` | Get Wiki | Wiki name or ID |
