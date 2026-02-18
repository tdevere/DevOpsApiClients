# DevOpsApiClients

> A growing reference library of **tested** Azure DevOps **REST API 7.2** client examples — Python, PowerShell, and cURL, organised by API area.

[![API Version](https://img.shields.io/badge/Azure%20DevOps%20API-7.2--preview-blue)](https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.2)

---

## Repository Structure

```
DevOpsApiClients/
├── Core/                          # Core area (org-level resources)
│   ├── Projects/                  # List, Get, Update
│   └── Teams/                     # List
├── Git/                           # Git area
│   ├── Repositories/              # List, Get, Create, Delete
│   ├── PullRequests/              # List, Get, Create, Update
│   ├── PullRequestThreads/        # List
│   ├── Commits/                   # List, Get
│   ├── Pushes/                    # List
│   └── Refs/                      # List (branches/tags)
├── Build/                         # Build area
│   ├── Definitions/               # List, Get
│   ├── Builds/                    # List, Get
│   └── Artifacts/                 # List
├── Pipelines/                     # Pipelines area
│   ├── Pipelines/                 # List, Get, Run
│   └── Runs/                      # List, Get
├── WorkItemTracking/              # Work Item Tracking area
│   ├── WorkItems/                 # Get, Create, Update, Batch Get, Delete
│   ├── Wiql/                      # Query (WIQL)
│   ├── Fields/                    # List
│   ├── WorkItemTypes/             # List
│   ├── Comments/                  # List, Add
│   └── Queries/                   # List, Get
├── DistributedTask/               # Distributed Task area
│   ├── Pools/                     # List
│   ├── VariableGroups/            # List, Get
│   └── Environments/              # List, Get
├── Policy/                        # Policy area
│   └── Configurations/            # List, Get
├── Hooks/                         # Service Hooks area
│   └── Subscriptions/             # List, Get
├── Wiki/                          # Wiki area
│   └── Wikis/                     # List, Get
├── _generator/                    # Code generator (YAML → all 3 languages)
│   ├── definitions/               # YAML operation definitions (39 total)
│   └── templates/                 # Python, PowerShell, Bash templates
└── _shared/                       # Shared helpers (auth, logging, HTTP)
    ├── auth.py / AdoAuth.ps1 / common.sh
    ├── logging_utils.py
    └── http_client.py / AdoHttp.ps1
```

All generated scripts use the `_shared/` helpers for authentication, logging, and HTTP handling — ensuring consistent error messages, PAT redaction, and retry logic across languages.

## Coverage Summary

| Domain | Resource | Operations | Languages | Offline Tests |
|--------|----------|-----------|-----------|---------------|
| **Core** | Projects | List, Get, Update | Py, PS, Bash | ✅ |
| **Core** | Teams | List | Py, PS, Bash | ✅ |
| **Git** | Repositories | List, Get, Create, Delete | Py, PS, Bash | ✅ |
| **Git** | PullRequests | List, Get, Create, Update | Py, PS, Bash | ✅ |
| **Git** | PullRequestThreads | List | Py, PS, Bash | ✅ |
| **Git** | Commits | List, Get | Py, PS, Bash | ✅ |
| **Git** | Pushes | List | Py, PS, Bash | ✅ |
| **Git** | Refs | List | Py, PS, Bash | ✅ |
| **Build** | Definitions | List, Get | Py, PS, Bash | ✅ |
| **Build** | Builds | List, Get | Py, PS, Bash | ✅ |
| **Build** | Artifacts | List | Py, PS, Bash | ✅ |
| **Pipelines** | Pipelines | List, Get, Run | Py, PS, Bash | ✅ |
| **Pipelines** | Runs | List, Get | Py, PS, Bash | ✅ |
| **WorkItemTracking** | WorkItems | Get, Create, Update, Batch Get, Delete | Py, PS, Bash | ✅ |
| **WorkItemTracking** | Wiql | Query | Py, PS, Bash | ✅ |
| **WorkItemTracking** | Fields | List | Py, PS, Bash | ✅ |
| **WorkItemTracking** | WorkItemTypes | List | Py, PS, Bash | ✅ |
| **WorkItemTracking** | Comments | List, Add | Py, PS, Bash | ✅ |
| **WorkItemTracking** | Queries | List, Get | Py, PS, Bash | ✅ |
| **DistributedTask** | Pools | List | Py, PS, Bash | ✅ |
| **DistributedTask** | VariableGroups | List, Get | Py, PS, Bash | ✅ |
| **DistributedTask** | Environments | List, Get | Py, PS, Bash | ✅ |
| **Policy** | Configurations | List, Get | Py, PS, Bash | ✅ |
| **Hooks** | Subscriptions | List, Get | Py, PS, Bash | ✅ |
| **Wiki** | Wikis | List, Get | Py, PS, Bash | ✅ |

**Totals:** 50 operations × 3 languages = 150 scripts, 997+ offline tests (pytest + Pester + bats)

## Authentication

All scripts authenticate via **Basic Auth** using a Personal Access Token (PAT).

| Variable            | Description                                           |
|---------------------|-------------------------------------------------------|
| `AZURE_DEVOPS_PAT`  | PAT with appropriate scopes (set as GitHub Secret)    |
| `AZURE_DEVOPS_ORG`  | Your Azure DevOps organisation name                   |
| `PROJECT_ID`        | *(where needed)* Project name or GUID                 |

**Basic Auth scheme:** the PAT is Base64-encoded as `:<PAT>` and sent in the `Authorization: Basic <token>` header.

## API Versioning

Every script in this repository explicitly targets **`api-version=7.2-preview`** (resource-specific sub-versions like `7.2-preview.4` where applicable). Each script includes a **version guard** that validates the response shape to detect version mismatches early.

## Quick Start

### PowerShell

```powershell
$env:AZURE_DEVOPS_PAT = "<your-pat>"
$env:AZURE_DEVOPS_ORG = "<your-org>"

./Core/Projects/List-Projects.ps1
```

### Python

```bash
export AZURE_DEVOPS_PAT="<your-pat>"
export AZURE_DEVOPS_ORG="<your-org>"

pip install requests
python Core/Projects/list_projects.py
```

### cURL / Bash

```bash
export AZURE_DEVOPS_PAT="<your-pat>"
export AZURE_DEVOPS_ORG="<your-org>"

bash Core/Projects/list_projects.sh
```

## GitHub Actions Usage

Store `AZURE_DEVOPS_PAT` and `AZURE_DEVOPS_ORG` as **repository secrets**, then reference them in your workflow:

```yaml
env:
  AZURE_DEVOPS_PAT: ${{ secrets.AZURE_DEVOPS_PAT }}
  AZURE_DEVOPS_ORG: ${{ secrets.AZURE_DEVOPS_ORG }}
```

## API Reference

- [Azure DevOps REST API 7.2 Documentation](https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.2)
- [Core — Projects](https://learn.microsoft.com/en-us/rest/api/azure/devops/core/projects?view=azure-devops-rest-7.2)
- [Git — Repositories](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories?view=azure-devops-rest-7.2)
- [Git — Pull Requests](https://learn.microsoft.com/en-us/rest/api/azure/devops/git/pull-requests?view=azure-devops-rest-7.2)
- [Build — Definitions](https://learn.microsoft.com/en-us/rest/api/azure/devops/build/definitions?view=azure-devops-rest-7.2)
- [Build — Builds](https://learn.microsoft.com/en-us/rest/api/azure/devops/build/builds?view=azure-devops-rest-7.2)
- [Pipelines](https://learn.microsoft.com/en-us/rest/api/azure/devops/pipelines/pipelines?view=azure-devops-rest-7.2)
- [Work Item Tracking](https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/work-items?view=azure-devops-rest-7.2)
- [Distributed Task — Pools](https://learn.microsoft.com/en-us/rest/api/azure/devops/distributedtask/pools?view=azure-devops-rest-7.2)
- [Policy — Configurations](https://learn.microsoft.com/en-us/rest/api/azure/devops/policy/configurations?view=azure-devops-rest-7.2)
- [Service Hooks — Subscriptions](https://learn.microsoft.com/en-us/rest/api/azure/devops/hooks/subscriptions?view=azure-devops-rest-7.2)
- [Wiki — Wikis](https://learn.microsoft.com/en-us/rest/api/azure/devops/wiki/wikis?view=azure-devops-rest-7.2)

## License

See repository license.