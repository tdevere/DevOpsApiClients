# Core API Area

Azure DevOps REST API 7.2 — **Core** area.

This area covers fundamental organizational resources:

| Module   | Operations                         | Description                        |
|----------|------------------------------------|------------------------------------|
| Projects | List, Get, Update                  | Manage projects in the organisation |
| Teams    | List                               | List teams within a project         |

## Authentication

All scripts expect a **Personal Access Token (PAT)** supplied via the environment variable `AZURE_DEVOPS_PAT` (or GitHub Actions secret of the same name). Basic Auth is used with an empty username and the PAT as the password.

## API Version

Every request targets **`api-version=7.2-preview`** and validates the response to confirm the server honours this version.
