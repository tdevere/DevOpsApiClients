# Service Hooks API Area

Azure DevOps REST API 7.2 — **Service Hooks** area.

This area covers service hook subscriptions that trigger notifications (webhooks, Slack, Teams, etc.) when events occur in Azure DevOps.

> **Status:** In progress — see operations table below.

## Authentication

All scripts expect a **Personal Access Token (PAT)** supplied via the environment variable `AZURE_DEVOPS_PAT`. Basic Auth is used with an empty username and the PAT as the password.

## API Version

Every request targets **`api-version=7.2`**.

## Operations

### Subscriptions

| Operation | Method | Endpoint | Python | PowerShell | Bash | Tests |
|-----------|--------|----------|--------|------------|------|-------|
| List Subscriptions | `GET` | `/{org}/_apis/hooks/subscriptions` | ✅ `list_subscriptions.py` | ✅ `List-HookSubscriptions.ps1` | ✅ `list_subscriptions.sh` | ✅ pytest, Pester, bats |
| Get Subscription | `GET` | `/{org}/_apis/hooks/subscriptions/{subscriptionId}` | ✅ `get_subscription.py` | ✅ `Get-HookSubscription.ps1` | ✅ `get_subscription.sh` | ✅ pytest, Pester, bats |

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `AZURE_DEVOPS_ORG` | Yes | Azure DevOps organisation name |
| `AZURE_DEVOPS_PAT` | Yes | Personal Access Token |
| `SUBSCRIPTION_ID` | Get Subscription | Hook subscription ID (GUID) |
