# DevOpsApiClients

> Definitive Azure DevOps **REST API 7.2** client library — multi-language examples organised by API Area.

[![API Version](https://img.shields.io/badge/Azure%20DevOps%20API-7.2--preview-blue)](https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.2)

---

## Repository Structure

```
DevOpsApiClients/
├── Core/                          # Core area (org-level resources)
│   ├── README.md
│   └── Projects/                  # Projects module
│       ├── README.md
│       ├── List-Projects.ps1      # PowerShell — List projects
│       ├── list_projects.py       # Python     — List projects
│       ├── list_projects.sh       # cURL/Bash  — List projects
│       ├── Get-Project.ps1        # PowerShell — Get single project
│       ├── get_project.py         # Python     — Get single project
│       ├── get_project.sh         # cURL/Bash  — Get single project
│       ├── Update-Project.ps1     # PowerShell — Update project
│       ├── update_project.py      # Python     — Update project
│       └── update_project.sh      # cURL/Bash  — Update project
├── Git/                           # Git area (repos, PRs, commits)
│   └── README.md
├── Build/                         # Build area (definitions, builds)
│   └── README.md
└── WorkItemTracking/              # Work Item Tracking area
    └── README.md
```

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

## License

See repository license.