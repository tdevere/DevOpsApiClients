# Core / Projects Module

Azure DevOps REST API 7.2 — **Projects** resource under the Core area.

| Operation | Verb    | Endpoint                                                         | Script Files                                         |
|-----------|---------|------------------------------------------------------------------|------------------------------------------------------|
| List      | `GET`   | `{org}/_apis/projects?api-version=7.2-preview.4`                 | `List-Projects.ps1` · `list_projects.py` · `list_projects.sh` |
| Get       | `GET`   | `{org}/_apis/projects/{id}?api-version=7.2-preview.4`            | `Get-Project.ps1` · `get_project.py` · `get_project.sh`       |
| Update    | `PATCH` | `{org}/_apis/projects/{id}?api-version=7.2-preview.4`            | `Update-Project.ps1` · `update_project.py` · `update_project.sh` |

## Required Environment Variables

| Variable              | Description                                                |
|-----------------------|------------------------------------------------------------|
| `AZURE_DEVOPS_PAT`   | Personal Access Token with appropriate scopes              |
| `AZURE_DEVOPS_ORG`   | Azure DevOps organisation name (e.g. `my-org`)             |
| `PROJECT_ID`         | *(Get / Update only)* GUID or name of the target project   |

## Quick Start

```bash
export AZURE_DEVOPS_PAT="<your-pat>"
export AZURE_DEVOPS_ORG="<your-org>"

# List all projects
python list_projects.py

# Get a single project
export PROJECT_ID="<project-name-or-guid>"
./get_project.sh
```
