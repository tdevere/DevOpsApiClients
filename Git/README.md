# Git API Area

Azure DevOps REST API 7.2 — **Git** area.

This area covers Git-specific resources such as repositories, pull requests, commits, and refs.

> **Status:** Scaffold — implementations coming soon.

## Authentication

All scripts expect a **Personal Access Token (PAT)** supplied via the environment variable `AZURE_DEVOPS_PAT`. Basic Auth is used with an empty username and the PAT as the password.

## API Version

Every request targets **`api-version=7.2-preview`**.
