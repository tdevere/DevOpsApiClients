# Work Item Tracking API Area

Azure DevOps REST API 7.2 — **Work Item Tracking** area.

This area covers work items, queries, fields, and classification nodes.

> **Status:** In progress — see operations table below.

## Authentication

All scripts expect a **Personal Access Token (PAT)** supplied via the environment variable `AZURE_DEVOPS_PAT`. Basic Auth is used with an empty username and the PAT as the password.

## API Version

Every request targets **`api-version=7.2`**.

## Operations

### Work Items

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| Get Work Item | `GET` | `/{org}/{project}/_apis/wit/workitems/{id}` | ✅ `get_work_item.py` | ✅ `Get-WorkItem.ps1` | ✅ `get_work_item.sh` | ✅ pytest, Pester, bats |
| Create Work Item | `POST` | `/{org}/{project}/_apis/wit/workitems/${type}` | ✅ `create_work_item.py` | ✅ `Create-WorkItem.ps1` | ✅ `create_work_item.sh` | ✅ pytest, Pester, bats |
| Update Work Item | `PATCH` | `/{org}/{project}/_apis/wit/workitems/{id}` | ✅ `update_work_item.py` | ✅ `Update-WorkItem.ps1` | ✅ `update_work_item.sh` | ✅ pytest, Pester, bats |
| Batch Get Work Items | `POST` | `/{org}/{project}/_apis/wit/workitemsbatch` | ✅ `batch_get_work_items.py` | ✅ `Get-WorkItemsBatch.ps1` | ✅ `batch_get_work_items.sh` | ✅ pytest, Pester, bats |
| Delete Work Item | `DELETE` | `/{org}/{project}/_apis/wit/workitems/{id}` | ✅ `delete_work_item.py` | ✅ `Remove-WorkItem.ps1` | ✅ `delete_work_item.sh` | ✅ pytest, Pester, bats |

### WIQL (Work Item Query Language)

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| Query Work Items | `POST` | `/{org}/{project}/_apis/wit/wiql` | ✅ `query_work_items.py` | ✅ `Invoke-Wiql.ps1` | ✅ `query_work_items.sh` | ✅ pytest, Pester, bats |

### Fields

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Fields | `GET` | `/{org}/{project}/_apis/wit/fields` | ✅ `list_fields.py` | ✅ `List-Fields.ps1` | ✅ `list_fields.sh` | ✅ pytest, Pester, bats |

### Work Item Types

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Work Item Types | `GET` | `/{org}/{project}/_apis/wit/workitemtypes` | ✅ `list_work_item_types.py` | ✅ `List-WorkItemTypes.ps1` | ✅ `list_work_item_types.sh` | ✅ pytest, Pester, bats |

### Comments

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Comments | `GET` | `/{org}/{project}/_apis/wit/workitems/{id}/comments` | ✅ `list_comments.py` | ✅ `List-WorkItemComments.ps1` | ✅ `list_comments.sh` | ✅ pytest, Pester, bats |
| Add Comment | `POST` | `/{org}/{project}/_apis/wit/workitems/{id}/comments` | ✅ `add_comment.py` | ✅ `Add-WorkItemComment.ps1` | ✅ `add_comment.sh` | ✅ pytest, Pester, bats |

### Queries

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Queries | `GET` | `/{org}/{project}/_apis/wit/queries` | ✅ `list_queries.py` | ✅ `List-Queries.ps1` | ✅ `list_queries.sh` | ✅ pytest, Pester, bats |
| Get Query | `GET` | `/{org}/{project}/_apis/wit/queries/{queryId}` | ✅ `get_query.py` | ✅ `Get-Query.ps1` | ✅ `get_query.sh` | ✅ pytest, Pester, bats |
