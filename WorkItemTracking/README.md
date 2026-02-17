# Work Item Tracking API Area

Azure DevOps REST API 7.2 — **Work Item Tracking** area.

This area covers work items, queries, fields, and classification nodes.

> **Status:** Scaffold — implementations coming soon.

## Authentication

All scripts expect a **Personal Access Token (PAT)** supplied via the environment variable `AZURE_DEVOPS_PAT`. Basic Auth is used with an empty username and the PAT as the password.

## API Version

Every request targets **`api-version=7.2-preview`**.
