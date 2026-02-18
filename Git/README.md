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
| Get Repository | `GET` | `/{org}/{project}/_apis/git/repositories/{repoId}` | ✅ `get_repository.py` | ✅ `Get-Repository.ps1` | ✅ `get_repository.sh` | ✅ pytest, Pester, bats |
| Create Repository | `POST` | `/{org}/{project}/_apis/git/repositories` | ✅ `create_repository.py` | ✅ `Create-Repository.ps1` | ✅ `create_repository.sh` | ✅ pytest, Pester, bats |
| Delete Repository | `DELETE` | `/{org}/{project}/_apis/git/repositories/{repoId}` | ✅ `delete_repository.py` | ✅ `Delete-Repository.ps1` | ✅ `delete_repository.sh` | ✅ pytest, Pester, bats |

### Pull Requests

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Pull Requests | `GET` | `/{org}/{project}/_apis/git/repositories/{repoId}/pullrequests` | ✅ `list_pull_requests.py` | ✅ `List-PullRequests.ps1` | ✅ `list_pull_requests.sh` | ✅ pytest, Pester, bats |
| Get Pull Request | `GET` | `/{org}/{project}/_apis/git/repositories/{repoId}/pullrequests/{pullRequestId}` | ✅ `get_pull_request.py` | ✅ `Get-PullRequest.ps1` | ✅ `get_pull_request.sh` | ✅ pytest, Pester, bats |
| Create Pull Request | `POST` | `/{org}/{project}/_apis/git/repositories/{repoId}/pullrequests` | ✅ `create_pull_request.py` | ✅ `New-PullRequest.ps1` | ✅ `create_pull_request.sh` | ✅ pytest, Pester, bats |
| Update Pull Request | `PATCH` | `/{org}/{project}/_apis/git/repositories/{repoId}/pullrequests/{pullRequestId}` | ✅ `update_pull_request.py` | ✅ `Update-PullRequest.ps1` | ✅ `update_pull_request.sh` | ✅ pytest, Pester, bats |

### Pull Request Threads

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Threads | `GET` | `/{org}/{project}/_apis/git/repositories/{repoId}/pullrequests/{pullRequestId}/threads` | ✅ `list_pr_threads.py` | ✅ `List-PullRequestThreads.ps1` | ✅ `list_pr_threads.sh` | ✅ pytest, Pester, bats |

### Commits

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Commits | `GET` | `/{org}/{project}/_apis/git/repositories/{repoId}/commits` | ✅ `list_commits.py` | ✅ `List-Commits.ps1` | ✅ `list_commits.sh` | ✅ pytest, Pester, bats |
| Get Commit | `GET` | `/{org}/{project}/_apis/git/repositories/{repoId}/commits/{commitId}` | ✅ `get_commit.py` | ✅ `Get-Commit.ps1` | ✅ `get_commit.sh` | ✅ pytest, Pester, bats |

### Pushes

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Pushes | `GET` | `/{org}/{project}/_apis/git/repositories/{repoId}/pushes` | ✅ `list_pushes.py` | ✅ `List-Pushes.ps1` | ✅ `list_pushes.sh` | ✅ pytest, Pester, bats |

### Refs (Branches/Tags)

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Refs | `GET` | `/{org}/{project}/_apis/git/repositories/{repoId}/refs` | ✅ `list_refs.py` | ✅ `List-Refs.ps1` | ✅ `list_refs.sh` | ✅ pytest, Pester, bats |
