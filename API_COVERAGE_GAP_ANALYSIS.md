# Azure DevOps REST API 7.2 — Endpoints NOT Available via `az devops` CLI

> **Generated**: 2026-02-17  
> **API Version**: 7.2  
> **CLI Extension**: `azure-devops` (latest)  
> **Total REST API Domains**: 47 | **Total Endpoints**: ~1,116  
> **CLI-Covered Endpoints**: ~120 | **Gap**: ~996 endpoints (~89%)

---

## Executive Summary

The Azure CLI `az devops` extension (and its sub-groups `az repos`, `az boards`, `az pipelines`, `az artifacts`) covers roughly **11% of the Azure DevOps REST API surface area**. The remaining **~89% of endpoints** have **no CLI equivalent** and must be accessed via direct REST calls, client libraries, or the generic `az devops invoke` escape hatch.

This document catalogues every REST API domain and identifies which endpoints lack a dedicated CLI command.

---

## How to Read This Document

| Symbol | Meaning |
|--------|---------|
| ✅ | Endpoint has a dedicated `az` CLI command |
| ⚠️ | Partial coverage — CLI command exists but covers limited parameters/functionality |
| ❌ | **No CLI command** — REST-only |

---

## Table of Contents

1. [Account](#1-account)
2. [Advanced Security](#2-advanced-security)
3. [Approvals and Checks](#3-approvals-and-checks)
4. [Artifacts (Feeds)](#4-artifacts-feeds)
5. [Artifacts Package Types](#5-artifacts-package-types)
6. [Audit](#6-audit)
7. [Build](#7-build)
8. [Core](#8-core)
9. [Dashboard](#9-dashboard)
10. [Delegated Auth](#10-delegated-auth)
11. [Distributed Task (Agents/Pools/Queues)](#11-distributed-task)
12. [Environments](#12-environments)
13. [Extension Management](#13-extension-management)
14. [Favorites](#14-favorites)
15. [Git](#15-git)
16. [Graph](#16-graph)
17. [Service Hooks](#17-service-hooks)
18. [Identity (IMS)](#18-identity-ims)
19. [Member Entitlement Management](#19-member-entitlement-management)
20. [Notification](#20-notification)
21. [Operations](#21-operations)
22. [Permissions Report](#22-permissions-report)
23. [Pipelines](#23-pipelines)
24. [Policy](#24-policy)
25. [Process Admin](#25-process-admin)
26. [Processes (Inherited)](#26-processes-inherited)
27. [Process Definitions (Legacy)](#27-process-definitions-legacy)
28. [Profile](#28-profile)
29. [Release](#29-release)
30. [Resource Usage](#30-resource-usage)
31. [Search](#31-search)
32. [Security](#32-security)
33. [Security Roles](#33-security-roles)
34. [Service Endpoint](#34-service-endpoint)
35. [Status](#35-status)
36. [Symbol](#36-symbol)
37. [Test (Legacy)](#37-test-legacy)
38. [Test Plans](#38-test-plans)
39. [Test Results](#39-test-results)
40. [TFVC](#40-tfvc)
41. [Token Admin](#41-token-admin)
42. [Tokens (PAT Lifecycle)](#42-tokens-pat-lifecycle)
43. [Wiki](#43-wiki)
44. [Work Item Tracking (WIT)](#44-work-item-tracking-wit)
45. [Work (Boards/Backlogs/Sprints)](#45-work-boardsbacklogsprints)

---

## 1. Account

**CLI Coverage: ❌ NONE**

| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/_apis/accounts` | ❌ |

> The CLI has no commands for listing or managing Azure DevOps accounts/organizations.

---

## 2. Advanced Security

**CLI Coverage: ❌ NONE** — Entire domain is REST-only

| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/{org}/_apis/alert/repositories/{repo}/alerts` | ❌ |
| GET | `/{org}/_apis/alert/repositories/{repo}/alerts/{alertId}` | ❌ |
| PATCH | `/{org}/_apis/alert/repositories/{repo}/alerts/{alertId}` | ❌ |
| GET | `/{org}/_apis/alert/repositories/{repo}/alerts/{alertId}/instances` | ❌ |
| GET | `/{org}/_apis/alert/repositories/{repo}/sarif/uploads/{sarifId}` | ❌ |
| POST | `/{org}/_apis/alert/repositories/{repo}/sarif/uploads` | ❌ |
| GET | `/{org}/_apis/management/enablement` | ❌ |
| PATCH | `/{org}/_apis/management/enablement` | ❌ |
| GET | `/{org}/_apis/management/enablement/{project}` | ❌ |
| PATCH | `/{org}/_apis/management/enablement/{project}` | ❌ |
| GET | `/{org}/_apis/management/enablement/{project}/{repo}` | ❌ |
| GET | `/{org}/_apis/management/meterUsageEstimate` | ❌ |
| GET | `/{org}/_apis/management/billingmode` | ❌ |
| PATCH | `/{org}/_apis/management/billingmode` | ❌ |
| GET | `/{org}/_apis/management/orgEnablement` | ❌ |
| PATCH | `/{org}/_apis/management/orgEnablement` | ❌ |
| GET | `/{org}/_apis/management/reporting/alerts` | ❌ |
| GET | `/{org}/_apis/management/reporting/alerts/{project}` | ❌ |
| GET | `/{org}/_apis/management/reporting/enablement` | ❌ |
| GET | `/{org}/_apis/management/reporting/enablement/{project}` | ❌ |
| GET | `/{org}/_apis/management/reporting/sarif` | ❌ |

---

## 3. Approvals and Checks

**CLI Coverage: ❌ NONE** — Entire domain is REST-only

| Method | Endpoint | CLI |
|--------|----------|-----|
| POST | `/{project}/_apis/pipelines/checks/configurations` | ❌ |
| GET | `/{project}/_apis/pipelines/checks/configurations` | ❌ |
| GET | `/{project}/_apis/pipelines/checks/configurations/{id}` | ❌ |
| PATCH | `/{project}/_apis/pipelines/checks/configurations/{id}` | ❌ |
| DELETE | `/{project}/_apis/pipelines/checks/configurations/{id}` | ❌ |
| POST | `/{project}/_apis/pipelines/checks/queryconfigurations` | ❌ |
| POST | `/{project}/_apis/pipelines/checks/runs` | ❌ |
| PATCH | `/{project}/_apis/pipelines/checks/runs/{approvalId}` | ❌ |
| POST | `/{project}/_apis/pipelines/pipelinepermissions` | ❌ |
| GET | `/{project}/_apis/pipelines/pipelinepermissions/{resourceType}/{resourceId}` | ❌ |
| PATCH | `/{project}/_apis/pipelines/pipelinepermissions/{resourceType}/{resourceId}` | ❌ |
| POST | `/{project}/_apis/pipelines/resources` | ❌ |
| GET | `/{project}/_apis/pipelines/resources` | ❌ |

> Pipeline approvals, checks, and resource authorization have zero CLI coverage. All approval workflows must be managed via REST.

---

## 4. Artifacts (Feeds)

**CLI Coverage: ⚠️ MINIMAL** — Only `az artifacts feed` has basic list/show/create

| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/{org}/_apis/packaging/feeds` | ⚠️ `az artifacts feed list` |
| POST | `/{org}/_apis/packaging/feeds` | ⚠️ `az artifacts feed create` |
| GET | `/{org}/_apis/packaging/feeds/{feedId}` | ⚠️ `az artifacts feed show` |
| PATCH | `/{org}/_apis/packaging/feeds/{feedId}` | ⚠️ `az artifacts feed update` |
| DELETE | `/{org}/_apis/packaging/feeds/{feedId}` | ❌ |
| GET | `/{org}/_apis/packaging/feeds/{feedId}/permissions` | ❌ |
| PATCH | `/{org}/_apis/packaging/feeds/{feedId}/permissions` | ❌ |
| GET | `/{org}/_apis/packaging/feeds/{feedId}/views` | ❌ |
| POST | `/{org}/_apis/packaging/feeds/{feedId}/views` | ❌ |
| GET | `/{org}/_apis/packaging/feeds/{feedId}/views/{viewId}` | ❌ |
| PATCH | `/{org}/_apis/packaging/feeds/{feedId}/views/{viewId}` | ❌ |
| DELETE | `/{org}/_apis/packaging/feeds/{feedId}/views/{viewId}` | ❌ |
| GET | `/{org}/_apis/packaging/feeds/{feedId}/retentionpolicies` | ❌ |
| PUT | `/{org}/_apis/packaging/feeds/{feedId}/retentionpolicies` | ❌ |
| DELETE | `/{org}/_apis/packaging/feeds/{feedId}/retentionpolicies` | ❌ |
| GET | `/{org}/_apis/packaging/feeds/{feedId}/packages` | ❌ |
| GET | `/{org}/_apis/packaging/feeds/{feedId}/packages/{packageId}` | ❌ |
| GET | `/{org}/_apis/packaging/feeds/{feedId}/packages/{packageId}/versions` | ❌ |
| GET | `/{org}/_apis/packaging/feeds/{feedId}/packages/{packageId}/versions/{versionId}` | ❌ |
| GET | `/{org}/_apis/packaging/feeds/{feedId}/RecycleBin/packages` | ❌ |
| GET | `/{org}/_apis/packaging/feeds/{feedId}/provenance` | ❌ |
| GET | `/{org}/_apis/packaging/globalpermissions` | ❌ |
| PATCH | `/{org}/_apis/packaging/globalpermissions` | ❌ |

> Feed delete, permissions, views, retention policies, package listing, provenance, and recycle bin — all REST-only.

---

## 5. Artifacts Package Types

**CLI Coverage: ⚠️ MINIMAL** — Only `az artifacts universal` (publish/download)

All protocol-specific package management is REST-only:

### NuGet (❌ all REST-only)
| Method | Endpoint | CLI |
|--------|----------|-----|
| GET/PUT/DELETE | `/_apis/packaging/feeds/{feedId}/nuget/packages/{packageName}/versions/{version}` | ❌ |
| POST | `/_apis/packaging/feeds/{feedId}/nuget/packagesbatch` | ❌ |
| GET | `/_apis/packaging/feeds/{feedId}/nuget/packages/{packageName}/versions/{version}/content` | ❌ |

### npm (❌ all REST-only)
| Method | Endpoint | CLI |
|--------|----------|-----|
| GET/PATCH/DELETE | `/_apis/packaging/feeds/{feedId}/npm/{packageName}/versions/{version}` | ❌ |
| POST | `/_apis/packaging/feeds/{feedId}/npm/packagesbatch` | ❌ |
| GET | `/_apis/packaging/feeds/{feedId}/npm/packages/{packageName}/versions/{version}/content` | ❌ |
| GET | `/_apis/packaging/feeds/{feedId}/npm/{scope}/{packageName}` (scoped) | ❌ |

### Maven (❌ all REST-only)
| Method | Endpoint | CLI |
|--------|----------|-----|
| GET/DELETE | `/_apis/packaging/feeds/{feedId}/maven/groups/{groupId}/artifacts/{artifactId}/versions/{version}` | ❌ |
| POST | `/_apis/packaging/feeds/{feedId}/maven/packagesbatch` | ❌ |
| GET | `/_apis/packaging/feeds/{feedId}/maven/{groupId}/{artifactId}/{version}/{fileName}/content` | ❌ |

### Python/PyPI (❌ all REST-only)
| Method | Endpoint | CLI |
|--------|----------|-----|
| GET/PATCH/DELETE | `/_apis/packaging/feeds/{feedId}/pypi/packages/{packageName}/versions/{version}` | ❌ |
| POST | `/_apis/packaging/feeds/{feedId}/pypi/packagesbatch` | ❌ |
| GET | `/_apis/packaging/feeds/{feedId}/pypi/packages/{packageName}/versions/{version}/content` | ❌ |

### Cargo (❌ all REST-only)
| Method | Endpoint | CLI |
|--------|----------|-----|
| GET/PATCH/DELETE | `/_apis/packaging/feeds/{feedId}/cargo/packages/{packageName}/versions/{version}` | ❌ |
| POST | `/_apis/packaging/feeds/{feedId}/cargo/packagesbatch` | ❌ |

### Universal Packages
| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/_apis/packaging/feeds/{feedId}/upack/packages/{packageName}/versions/{version}` | ⚠️ `az artifacts universal download` |
| PUT | `/_apis/packaging/feeds/{feedId}/upack/packages/{packageName}/versions/{version}` | ⚠️ `az artifacts universal publish` |
| PATCH/DELETE | (version management) | ❌ |
| POST | `/_apis/packaging/feeds/{feedId}/upack/packagesbatch` | ❌ |

> ~70+ package management endpoints across 6 protocols — CLI only covers universal publish/download.

---

## 6. Audit

**CLI Coverage: ❌ NONE**

| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/{org}/_apis/audit/streams` | ❌ |
| POST | `/{org}/_apis/audit/streams` | ❌ |
| GET | `/{org}/_apis/audit/streams/{streamId}` | ❌ |
| PUT | `/{org}/_apis/audit/streams/{streamId}` | ❌ |
| DELETE | `/{org}/_apis/audit/streams/{streamId}` | ❌ |
| GET | `/{org}/_apis/audit/auditlog` | ❌ |
| POST | `/{org}/_apis/audit/auditlog` | ❌ |
| GET | `/{org}/_apis/audit/downloadlog` | ❌ |
| GET | `/{org}/_apis/audit/actions` | ❌ |

> Zero audit log access from the CLI. All compliance/audit workflows require REST.

---

## 7. Build

**CLI Coverage: ⚠️ PARTIAL** (~15 of ~87 endpoints)

### Covered by CLI

| Endpoint Area | CLI Command |
|---------------|-------------|
| List builds | `az pipelines build list` |
| Show build | `az pipelines build show` |
| Queue build | `az pipelines build queue` |
| List definitions | `az pipelines build definition list` |
| Show definition | `az pipelines build definition show` |
| List build tags | `az pipelines build tag list` |
| Add build tag | `az pipelines build tag add` |
| Delete build tag | `az pipelines build tag delete` |

### ❌ NOT Available via CLI (~72 endpoints)

| Method | Endpoint | Notes |
|--------|----------|-------|
| POST | `/_apis/build/definitions` | Create build definition |
| PUT | `/_apis/build/definitions/{id}` | Update build definition |
| DELETE | `/_apis/build/definitions/{id}` | Delete build definition |
| GET | `/_apis/build/definitions/{id}/revisions` | Definition revision history |
| GET | `/_apis/build/definitions/{id}/resources` | Definition resources |
| PATCH | `/_apis/build/builds/{id}` | Update build (retry, cancel) |
| DELETE | `/_apis/build/builds/{id}` | Delete build |
| GET | `/_apis/build/builds/{id}/artifacts` | Get build artifacts |
| GET | `/_apis/build/builds/{id}/artifacts/{name}` | Get specific artifact |
| GET | `/_apis/build/builds/{id}/timeline` | Build timeline |
| GET | `/_apis/build/builds/{id}/timeline/{timelineId}` | Specific timeline |
| GET | `/_apis/build/builds/{id}/logs` | Build logs list |
| GET | `/_apis/build/builds/{id}/logs/{logId}` | Specific build log |
| GET | `/_apis/build/builds/{id}/changes` | Build changes/commits |
| GET | `/_apis/build/builds/{id}/workitems` | Build work items |
| GET | `/_apis/build/builds/{id}/report` | Build report |
| GET | `/_apis/build/builds/{id}/leases` | Retention leases |
| POST | `/_apis/build/retention/leases` | Create retention lease |
| GET | `/_apis/build/retention/leases` | List retention leases |
| DELETE | `/_apis/build/retention/leases` | Delete retention lease |
| GET | `/_apis/build/retention` | Retention settings |
| PATCH | `/_apis/build/retention` | Update retention settings |
| GET | `/_apis/build/folders` | List folders |
| PUT | `/_apis/build/folders/{path}` | Create/update folder |
| DELETE | `/_apis/build/folders/{path}` | Delete folder |
| GET | `/_apis/build/properties` | Build properties |
| PATCH | `/_apis/build/properties` | Update build properties |
| GET | `/_apis/build/definitions/{id}/properties` | Definition properties |
| GET | `/_apis/build/options` | Build options |
| GET | `/_apis/build/resources/usage` | Resource usage |
| GET | `/_apis/build/settings` | Build settings |
| PATCH | `/_apis/build/settings` | Update build settings |
| GET | `/_apis/build/status/{definition}` | Build status badge |
| POST | `/_apis/build/definitions/{id}/templates` | Save as template |
| GET | `/_apis/build/definitions/templates` | List templates |
| GET | `/_apis/build/definitions/templates/{templateId}` | Get template |
| DELETE | `/_apis/build/definitions/templates/{templateId}` | Delete template |
| POST | `/_apis/build/definitions/{id}/metrics` | Definition metrics |
| GET | `/_apis/build/metrics` | Project build metrics |
| GET | `/_apis/build/generalSettings` | General settings |
| PATCH | `/_apis/build/generalSettings` | Update general settings |
| GET | `/_apis/build/sourceProviders` | Source providers |
| GET | `/_apis/build/sourceProviders/{providerName}/repositories` | List repos from provider |
| GET | `/_apis/build/sourceProviders/{providerName}/branches` | List branches from provider |
| GET | `/_apis/build/sourceProviders/{providerName}/webhooks` | Provider webhooks |
| GET | `/_apis/build/latest/{definition}` | Latest build for definition |
| GET | `/_apis/build/controllers` | Build controllers |
| GET | `/_apis/build/ResourceAuthorization` | Authorized resources |
| PATCH | `/_apis/build/ResourceAuthorization` | Authorize resources |
| GET | `/_apis/build/definitions/{id}/yaml` | Get YAML |
| POST | `/_apis/build/builds/{id}/stages/{stageRefName}` | Retry stage |

---

## 8. Core

**CLI Coverage: ⚠️ PARTIAL** (~8 of ~19 endpoints)

### Covered by CLI

| Endpoint | CLI Command |
|----------|-------------|
| List projects | `az devops project list` |
| Get project | `az devops project show` |
| Create project | `az devops project create` |
| Delete project | `az devops project delete` |
| List teams | `az devops team list` |
| Show team | `az devops team show` |
| Create team | `az devops team create` |
| Delete team | `az devops team delete` |

### ❌ NOT Available via CLI

| Method | Endpoint | Notes |
|--------|----------|-------|
| PATCH | `/_apis/projects/{id}` | Update project properties |
| GET | `/_apis/projects/{id}/properties` | Project properties |
| PATCH | `/_apis/projects/{id}/properties` | Set project properties |
| GET | `/_apis/teams/{teamId}/members` | ⚠️ `az devops team list-member` exists |
| PATCH | `/_apis/teams/{teamId}` | Update team |
| GET | `/_apis/processes` | List processes |
| GET | `/_apis/processes/{processId}` | Get process |
| GET | `/_apis/connectedServices` | Connected services |
| POST | `/_apis/connectedServices` | Create connected service |
| GET | `/_apis/projects/{id}/teams/{teamId}/members` | Team members |
| GET | `/_apis/operations/{operationId}` | Operation status |

---

## 9. Dashboard

**CLI Coverage: ❌ NONE** — Entire domain is REST-only

| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/{project}/{team}/_apis/dashboard/dashboards` | ❌ |
| POST | `/{project}/{team}/_apis/dashboard/dashboards` | ❌ |
| GET | `/{project}/{team}/_apis/dashboard/dashboards/{id}` | ❌ |
| PUT | `/{project}/{team}/_apis/dashboard/dashboards/{id}` | ❌ |
| DELETE | `/{project}/{team}/_apis/dashboard/dashboards/{id}` | ❌ |
| PATCH | `/{project}/{team}/_apis/dashboard/dashboards/{id}` | ❌ |
| GET | `/{project}/{team}/_apis/dashboard/dashboards/{id}/widgets` | ❌ |
| POST | `/{project}/{team}/_apis/dashboard/dashboards/{id}/widgets` | ❌ |
| GET | `/{project}/{team}/_apis/dashboard/dashboards/{id}/widgets/{widgetId}` | ❌ |
| PUT | `/{project}/{team}/_apis/dashboard/dashboards/{id}/widgets/{widgetId}` | ❌ |
| PATCH | `/{project}/{team}/_apis/dashboard/dashboards/{id}/widgets/{widgetId}` | ❌ |
| DELETE | `/{project}/{team}/_apis/dashboard/dashboards/{id}/widgets/{widgetId}` | ❌ |
| GET | `/_apis/dashboard/widgettypes` | ❌ |
| GET | `/_apis/dashboard/widgettypes/{contributionId}` | ❌ |
| PATCH | `/{project}/{team}/_apis/dashboard/dashboards/{id}/widgets` | ❌ Replace widgets |
| PUT | `/{project}/{team}/_apis/dashboard/dashboards` | ❌ Replace dashboards |

---

## 10. Delegated Auth

**CLI Coverage: ❌ NONE**

| Method | Endpoint | CLI |
|--------|----------|-----|
| POST | `/_apis/delegatedauthorization/registration` | ❌ |
| GET | `/_apis/delegatedauthorization/registration` | ❌ |

---

## 11. Distributed Task

**CLI Coverage: ⚠️ MINIMAL** (~6 of ~56 endpoints)

### Covered by CLI

| Endpoint | CLI Command |
|----------|-------------|
| List pools | `az pipelines pool list` |
| Show pool | `az pipelines pool show` |
| List agents | `az pipelines agent list` |
| Show agent | `az pipelines agent show` |
| List queues | `az pipelines queue list` |
| Show queue | `az pipelines queue show` |

### ❌ NOT Available via CLI (~50 endpoints)

| Method | Endpoint | Notes |
|--------|----------|-------|
| POST | `/_apis/distributedtask/pools` | Create pool |
| PATCH | `/_apis/distributedtask/pools/{poolId}` | Update pool |
| DELETE | `/_apis/distributedtask/pools/{poolId}` | Delete pool |
| PATCH | `/_apis/distributedtask/pools/{poolId}/agents/{agentId}` | Update agent |
| PUT | `/_apis/distributedtask/pools/{poolId}/agents/{agentId}` | Replace agent |
| DELETE | `/_apis/distributedtask/pools/{poolId}/agents/{agentId}` | Delete/remove agent |
| GET | `/_apis/distributedtask/pools/{poolId}/agents/{agentId}/useragent` | Agent user capabilities |
| PUT | `/_apis/distributedtask/pools/{poolId}/agents/{agentId}/usercapabilities` | Set user capabilities |
| GET | `/_apis/distributedtask/pools/{poolId}/jobrequests` | Job requests |
| PATCH | `/_apis/distributedtask/pools/{poolId}/jobrequests/{requestId}` | Update job request |
| GET/POST/DELETE | `/_apis/distributedtask/variablegroups` | Variable groups (full CRUD) |
| GET | `/_apis/distributedtask/variablegroups/{id}` | Get variable group |
| PUT | `/_apis/distributedtask/variablegroups/{id}` | Update variable group |
| GET/POST/DELETE | `/_apis/distributedtask/securefiles` | Secure files (full CRUD) |
| GET | `/_apis/distributedtask/securefiles/{id}` | Get secure file |
| GET | `/_apis/distributedtask/securefiles/{id}/download` | Download secure file |
| DELETE | `/_apis/distributedtask/securefiles/{id}` | Delete secure file |
| GET/POST | `/_apis/distributedtask/deploymentgroups` | Deployment groups |
| GET | `/_apis/distributedtask/deploymentgroups/{id}` | Get deployment group |
| PATCH | `/_apis/distributedtask/deploymentgroups/{id}` | Update deployment group |
| DELETE | `/_apis/distributedtask/deploymentgroups/{id}` | Delete deployment group |
| GET | `/_apis/distributedtask/deploymentgroups/{id}/targets` | Deployment targets |
| PATCH | `/_apis/distributedtask/deploymentgroups/{id}/targets` | Update targets |
| DELETE | `/_apis/distributedtask/deploymentgroups/{id}/targets/{targetId}` | Delete target |
| GET | `/_apis/distributedtask/pools/{poolId}/messages` | Agent messages |
| POST | `/_apis/distributedtask/pools/{poolId}/messages` | Send message to agent |
| DELETE | `/_apis/distributedtask/pools/{poolId}/messages/{messageId}` | Delete message |
| GET | `/_apis/distributedtask/tasks` | List task definitions |
| GET | `/_apis/distributedtask/tasks/{taskId}` | Get task definition |
| GET | `/_apis/distributedtask/tasks/{taskId}/{versionString}` | Get task version |
| GET | `/_apis/distributedtask/serviceendpointtypes` | Endpoint types |
| GET/POST/PUT/DELETE | `/_apis/distributedtask/elasticpools` | Elastic pools (VMSS agents) |
| GET | `/_apis/distributedtask/elasticpools/{poolId}/logs` | Elastic pool logs |
| GET | `/_apis/distributedtask/elasticpools/{poolId}/nodes` | Elastic pool nodes |
| GET | `/_apis/distributedtask/pools/{poolId}/maintenancedefinitions` | Maintenance definitions |
| POST | `/_apis/distributedtask/pools/{poolId}/maintenancedefinitions` | Create maintenance definition |
| GET | `/_apis/distributedtask/pools/{poolId}/maintenancejobs` | Maintenance jobs |

> Secure files, deployment groups, task definitions, elastic pools, agent messaging — all REST-only.

---

## 12. Environments

**CLI Coverage: ❌ NONE** — Entire domain is REST-only

| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/{project}/_apis/pipelines/environments` | ❌ |
| POST | `/{project}/_apis/pipelines/environments` | ❌ |
| GET | `/{project}/_apis/pipelines/environments/{environmentId}` | ❌ |
| PATCH | `/{project}/_apis/pipelines/environments/{environmentId}` | ❌ |
| DELETE | `/{project}/_apis/pipelines/environments/{environmentId}` | ❌ |
| GET | `/{project}/_apis/pipelines/environments/{environmentId}/providers/kubernetes` | ❌ |
| POST | `/{project}/_apis/pipelines/environments/{environmentId}/providers/kubernetes` | ❌ |
| GET | `/{project}/_apis/pipelines/environments/{environmentId}/providers/kubernetes/{resourceId}` | ❌ |
| DELETE | `/{project}/_apis/pipelines/environments/{environmentId}/providers/kubernetes/{resourceId}` | ❌ |
| GET | `/{project}/_apis/pipelines/environments/{environmentId}/providers/virtualmachines` | ❌ |
| POST | `/{project}/_apis/pipelines/environments/{environmentId}/providers/virtualmachines` | ❌ |
| GET | `/{project}/_apis/pipelines/environments/{environmentId}/providers/virtualmachines/{resourceId}` | ❌ |
| DELETE | `/{project}/_apis/pipelines/environments/{environmentId}/providers/virtualmachines/{resourceId}` | ❌ |
| GET | `/{project}/_apis/pipelines/environments/{environmentId}/environmentdeploymentrecords` | ❌ |
| GET | `/{project}/_apis/pipelines/environments/{environmentId}/checks` | ❌ |

> Pipeline environments (Kubernetes, VM resources, deployment records) — zero CLI support.

---

## 13. Extension Management

**CLI Coverage: ⚠️ PARTIAL** (~3 of ~5 endpoints)

### Covered by CLI

| Endpoint | CLI Command |
|----------|-------------|
| List installed extensions | `az devops extension list` |
| Show extension | `az devops extension show` |
| Install extension | `az devops extension install` |
| Uninstall extension | `az devops extension uninstall` |
| Enable/disable | `az devops extension enable/disable` |

### ❌ NOT Available via CLI

| Method | Endpoint | Notes |
|--------|----------|-------|
| PATCH | `/_apis/extensionmanagement/installedextensions/{publisherId}/{extensionId}` | Update extension settings/config |
| GET | `/_apis/extensionmanagement/installedextensions/{publisherId}/{extensionId}/data/scopes/{scope}/collections/{collection}/documents` | Extension data |
| POST | `/_apis/extensionmanagement/requests` | Request extension installation |
| GET | `/_apis/extensionmanagement/requests` | List installation requests |
| DELETE | `/_apis/extensionmanagement/requests/{publisherId}/{extensionId}/{requesterId}` | Delete request |

---

## 14. Favorites

**CLI Coverage: ❌ NONE**

| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/_apis/favorites` | ❌ |
| POST | `/_apis/favorites` | ❌ |
| DELETE | `/_apis/favorites/{favoriteId}` | ❌ |
| GET | `/_apis/favorites/{favoriteId}` | ❌ |

---

## 15. Git

**CLI Coverage: ⚠️ PARTIAL** (~25 of ~108 endpoints)

### Covered by CLI

| Endpoint Area | CLI Commands |
|---------------|-------------|
| Repositories | `az repos list/show/create/delete/update` |
| Branches/Refs | `az repos ref list/create/delete/lock` |
| Pull Requests | `az repos pr create/update/show/list/complete/abandon/set-vote/checkout` |
| PR Reviewers | `az repos pr reviewer add/list/remove` |
| PR Work Items | `az repos pr work-item add/list/remove` |
| PR Policies | `az repos pr policy list/queue` |
| Import | `az repos import create` |
| Branch Policies | `az repos policy list/show/create/update/delete` + type-specific |

### ❌ NOT Available via CLI (~83 endpoints)

| Method | Endpoint | Notes |
|--------|----------|-------|
| **Commits** | | |
| GET | `/_apis/git/repositories/{repo}/commits` | List commits |
| GET | `/_apis/git/repositories/{repo}/commits/{commitId}` | Get commit |
| GET | `/_apis/git/repositories/{repo}/commits/{commitId}/changes` | Commit changes |
| GET | `/_apis/git/repositories/{repo}/commits/{commitId}/statuses` | Commit statuses |
| POST | `/_apis/git/repositories/{repo}/commits/{commitId}/statuses` | Create commit status |
| GET | `/_apis/git/repositories/{repo}/commitsBatch` | Batch commit lookup |
| **Pushes** | | |
| GET | `/_apis/git/repositories/{repo}/pushes` | List pushes |
| GET | `/_apis/git/repositories/{repo}/pushes/{pushId}` | Get push |
| POST | `/_apis/git/repositories/{repo}/pushes` | Create push (create/edit/delete files) |
| **Items (File Content)** | | |
| GET | `/_apis/git/repositories/{repo}/items` | List items (files/dirs) |
| GET | `/_apis/git/repositories/{repo}/items/{path}` | Get file content |
| POST | `/_apis/git/repositories/{repo}/itemsBatch` | Batch item download |
| **Blobs** | | |
| GET | `/_apis/git/repositories/{repo}/blobs/{sha1}` | Get blob |
| POST | `/_apis/git/repositories/{repo}/blobs` | Get blobs in batch |
| **Trees** | | |
| GET | `/_apis/git/repositories/{repo}/trees/{sha1}` | Get tree |
| **Diffs** | | |
| GET | `/_apis/git/repositories/{repo}/diffs/commits` | Diff between commits |
| **Stats** | | |
| GET | `/_apis/git/repositories/{repo}/stats/branches` | Branch statistics |
| **Pull Request Threads** | | |
| GET | `/_apis/git/repositories/{repo}/pullRequests/{prId}/threads` | PR comments/threads |
| POST | `/_apis/git/repositories/{repo}/pullRequests/{prId}/threads` | Create PR thread |
| GET | `/_apis/git/repositories/{repo}/pullRequests/{prId}/threads/{threadId}` | Get thread |
| PATCH | `/_apis/git/repositories/{repo}/pullRequests/{prId}/threads/{threadId}` | Update thread |
| POST | `/_apis/git/repositories/{repo}/pullRequests/{prId}/threads/{threadId}/comments` | Add comment |
| GET | `/_apis/git/repositories/{repo}/pullRequests/{prId}/threads/{threadId}/comments/{commentId}` | Get comment |
| PATCH | `/_apis/git/repositories/{repo}/pullRequests/{prId}/threads/{threadId}/comments/{commentId}` | Update comment |
| DELETE | `/_apis/git/repositories/{repo}/pullRequests/{prId}/threads/{threadId}/comments/{commentId}` | Delete comment |
| **Pull Request Iterations** | | |
| GET | `/_apis/git/repositories/{repo}/pullRequests/{prId}/iterations` | PR iterations |
| GET | `/_apis/git/repositories/{repo}/pullRequests/{prId}/iterations/{iterationId}` | Get iteration |
| GET | `/_apis/git/repositories/{repo}/pullRequests/{prId}/iterations/{iterationId}/changes` | Iteration changes |
| GET | `/_apis/git/repositories/{repo}/pullRequests/{prId}/iterations/{iterationId}/statuses` | Iteration statuses |
| **Pull Request Statuses** | | |
| GET | `/_apis/git/repositories/{repo}/pullRequests/{prId}/statuses` | PR statuses |
| POST | `/_apis/git/repositories/{repo}/pullRequests/{prId}/statuses` | Create PR status |
| GET | `/_apis/git/repositories/{repo}/pullRequests/{prId}/statuses/{statusId}` | Get status |
| PATCH | `/_apis/git/repositories/{repo}/pullRequests/{prId}/statuses/{statusId}` | Update status |
| DELETE | `/_apis/git/repositories/{repo}/pullRequests/{prId}/statuses/{statusId}` | Delete status |
| **Pull Request Labels** | | |
| GET | `/_apis/git/repositories/{repo}/pullRequests/{prId}/labels` | PR labels |
| POST | `/_apis/git/repositories/{repo}/pullRequests/{prId}/labels` | Add PR label |
| DELETE | `/_apis/git/repositories/{repo}/pullRequests/{prId}/labels/{labelIdOrName}` | Remove PR label |
| **Pull Request Commits** | | |
| GET | `/_apis/git/repositories/{repo}/pullRequests/{prId}/commits` | PR commits |
| **Pull Request Properties** | | |
| GET | `/_apis/git/repositories/{repo}/pullRequests/{prId}/properties` | PR properties |
| PATCH | `/_apis/git/repositories/{repo}/pullRequests/{prId}/properties` | Update PR properties |
| **Forks** | | |
| GET | `/_apis/git/repositories/{repo}/forks` | List forks |
| POST | `/_apis/git/repositories/{repo}/forks` | Create fork |
| GET | `/_apis/git/repositories/{repo}/forks/{collection}/{repo}` | Sync status |
| **Annotated Tags** | | |
| GET | `/_apis/git/repositories/{repo}/annotatedtags/{objectId}` | Get annotated tag |
| POST | `/_apis/git/repositories/{repo}/annotatedtags` | Create annotated tag |
| **Cherry-Picks** | | |
| POST | `/_apis/git/repositories/{repo}/cherryPicks` | Initiate cherry-pick |
| GET | `/_apis/git/repositories/{repo}/cherryPicks/{cherryPickId}` | Get cherry-pick status |
| **Reverts** | | |
| POST | `/_apis/git/repositories/{repo}/reverts` | Initiate revert |
| GET | `/_apis/git/repositories/{repo}/reverts/{revertId}` | Get revert status |
| **Merges** | | |
| POST | `/_apis/git/repositories/{repo}/merges` | Create merge |
| GET | `/_apis/git/repositories/{repo}/merges/{mergeOperationId}` | Get merge status |
| **Import Requests** | | |
| GET | `/_apis/git/repositories/{repo}/importRequests` | List imports |
| GET | `/_apis/git/repositories/{repo}/importRequests/{importRequestId}` | Get import status |
| PATCH | `/_apis/git/repositories/{repo}/importRequests/{importRequestId}` | Update import |
| **Recycle Bin** | | |
| GET | `/_apis/git/recycleBin/repositories` | List soft-deleted repos |
| PATCH | `/_apis/git/recycleBin/repositories/{repositoryId}` | Restore/delete repo |
| **Repository Statistics** | | |
| GET | `/_apis/git/repositories/{repo}/stats` | Repo statistics |

---

## 16. Graph

**CLI Coverage: ❌ NONE** — Entire domain is REST-only (~29 endpoints)

| Method | Endpoint | Notes |
|--------|----------|-------|
| GET | `/_apis/graph/users` | List users |
| POST | `/_apis/graph/users` | Create user |
| GET | `/_apis/graph/users/{userDescriptor}` | Get user |
| PATCH | `/_apis/graph/users/{userDescriptor}` | Update user |
| DELETE | `/_apis/graph/users/{userDescriptor}` | Delete user |
| GET | `/_apis/graph/groups` | List groups |
| POST | `/_apis/graph/groups` | Create group |
| GET | `/_apis/graph/groups/{groupDescriptor}` | Get group |
| PATCH | `/_apis/graph/groups/{groupDescriptor}` | Update group |
| DELETE | `/_apis/graph/groups/{groupDescriptor}` | Delete group |
| GET | `/_apis/graph/memberships/{subjectDescriptor}` | List memberships for subject |
| PUT | `/_apis/graph/memberships/{subjectDescriptor}/{containerDescriptor}` | Add membership |
| DELETE | `/_apis/graph/memberships/{subjectDescriptor}/{containerDescriptor}` | Remove membership |
| GET | `/_apis/graph/memberships/{subjectDescriptor}/{containerDescriptor}` | Check membership |
| POST | `/_apis/graph/membershipstates/{subjectDescriptor}` | Get membership state |
| POST | `/_apis/graph/subjectlookup` | Lookup subjects by descriptor |
| GET | `/_apis/graph/descriptors/{storageKey}` | Get descriptor from storage key |
| GET | `/_apis/graph/storagekeys/{subjectDescriptor}` | Get storage key from descriptor |
| GET | `/_apis/graph/serviceprincipals` | List service principals |
| POST | `/_apis/graph/serviceprincipals` | Create service principal |
| GET | `/_apis/graph/serviceprincipals/{spDescriptor}` | Get service principal |
| DELETE | `/_apis/graph/serviceprincipals/{spDescriptor}` | Delete service principal |
| GET | `/_apis/graph/scopes` | List scopes |
| GET | `/_apis/graph/scopes/{scopeDescriptor}` | Get scope |

> The entire Graph API (identity, group, membership management) has zero CLI support.

---

## 17. Service Hooks

**CLI Coverage: ❌ NONE** — Entire domain is REST-only (~22 endpoints)

| Method | Endpoint | Notes |
|--------|----------|-------|
| GET | `/_apis/hooks/subscriptions` | List subscriptions |
| POST | `/_apis/hooks/subscriptions` | Create subscription |
| GET | `/_apis/hooks/subscriptions/{id}` | Get subscription |
| PUT | `/_apis/hooks/subscriptions/{id}` | Update subscription |
| DELETE | `/_apis/hooks/subscriptions/{id}` | Delete subscription |
| POST | `/_apis/hooks/subscriptionsquery` | Query subscriptions |
| GET | `/_apis/hooks/notifications` | List notifications |
| GET | `/_apis/hooks/notifications/{id}` | Get notification |
| POST | `/_apis/hooks/notificationsquery` | Query notifications |
| GET | `/_apis/hooks/publishers` | List publishers |
| GET | `/_apis/hooks/publishers/{publisherId}` | Get publisher |
| GET | `/_apis/hooks/publishers/{publisherId}/eventtypes` | Event types |
| GET | `/_apis/hooks/publishers/{publisherId}/inputvaluesquery` | Input options |
| GET | `/_apis/hooks/consumers` | List consumers |
| GET | `/_apis/hooks/consumers/{consumerId}` | Get consumer |
| GET | `/_apis/hooks/consumers/{consumerId}/actions` | Consumer actions |
| GET | `/_apis/hooks/consumers/{consumerId}/actions/{actionId}` | Get action |
| GET | `/_apis/hooks/consumers/{consumerId}/inputvaluesquery` | Action input options |
| POST | `/_apis/hooks/testnotifications` | Test notification delivery |
| POST | `/_apis/hooks/subscriptions/{id}/testnotifications` | Test specific subscription |
| GET | `/_apis/hooks/diagnostics` | Diagnostics |

---

## 18. Identity (IMS)

**CLI Coverage: ❌ NONE**

| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/_apis/identities` | ❌ |

---

## 19. Member Entitlement Management

**CLI Coverage: ⚠️ PARTIAL** — `az devops user` covers basic user ops

### Covered by CLI

| Endpoint | CLI Command |
|----------|-------------|
| List user entitlements | `az devops user list` |
| Show user entitlement | `az devops user show` |
| Add user entitlement | `az devops user add` |
| Remove user entitlement | `az devops user remove` |
| Update user entitlement | `az devops user update` |

### ❌ NOT Available via CLI (~16 endpoints)

| Method | Endpoint | Notes |
|--------|----------|-------|
| POST | `/_apis/memberentitlementmanagement/userentitlements` | Batch add users |
| PATCH | `/_apis/memberentitlementmanagement/userentitlements` | Batch update users |
| GET | `/_apis/memberentitlementmanagement/userentitlements/summary` | Entitlement summary |
| GET | `/_apis/memberentitlementmanagement/groupentitlements` | List group entitlements |
| POST | `/_apis/memberentitlementmanagement/groupentitlements` | Create group entitlement |
| GET | `/_apis/memberentitlementmanagement/groupentitlements/{id}` | Get group entitlement |
| PATCH | `/_apis/memberentitlementmanagement/groupentitlements/{id}` | Update group entitlement |
| DELETE | `/_apis/memberentitlementmanagement/groupentitlements/{id}` | Delete group entitlement |
| GET | `/_apis/memberentitlementmanagement/groupentitlements/{id}/members` | Group members |
| POST | `/_apis/memberentitlementmanagement/userentitlements/search` | Search user entitlements |
| PATCH | `/_apis/memberentitlementmanagement/serviceprincipals` | Service principal entitlements |
| GET | `/_apis/memberentitlementmanagement/serviceprincipals` | List SP entitlements |
| GET | `/_apis/memberentitlementmanagement/serviceprincipals/{id}` | Get SP entitlement |
| DELETE | `/_apis/memberentitlementmanagement/serviceprincipals/{id}` | Delete SP entitlement |

---

## 20. Notification

**CLI Coverage: ❌ NONE** — Entire domain is REST-only (~17 endpoints)

| Method | Endpoint | Notes |
|--------|----------|-------|
| GET | `/_apis/notification/subscriptions` | List subscriptions |
| POST | `/_apis/notification/subscriptions` | Create subscription |
| GET | `/_apis/notification/subscriptions/{id}` | Get subscription |
| PATCH | `/_apis/notification/subscriptions/{id}` | Update subscription |
| DELETE | `/_apis/notification/subscriptions/{id}` | Delete subscription |
| POST | `/_apis/notification/subscriptionquery` | Query subscriptions |
| GET | `/_apis/notification/eventtypes` | List event types |
| GET | `/_apis/notification/eventtypes/{eventType}` | Get event type |
| GET | `/_apis/notification/diagnostics` | Notification diagnostics |
| PUT | `/_apis/notification/diagnostics` | Update diagnostics settings |
| GET | `/_apis/notification/settings` | Get global settings |
| PATCH | `/_apis/notification/settings` | Update global settings |
| GET | `/_apis/notification/subscribers/{subscriberId}` | Get subscriber |
| PATCH | `/_apis/notification/subscribers/{subscriberId}` | Update subscriber |
| POST | `/_apis/notification/subscriptiontemplates` | List templates |
| GET | `/_apis/notification/subscriptiontemplates` | Get templates |
| POST | `/_apis/notification/subscriptionevaluationrequests` | Test subscription |

---

## 21. Operations

**CLI Coverage: ❌ NONE**

| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/_apis/operations/{operationId}` | ❌ |

---

## 22. Permissions Report

**CLI Coverage: ❌ NONE**

| Method | Endpoint | CLI |
|--------|----------|-----|
| POST | `/_apis/permissionsreport` | ❌ Create report |
| GET | `/_apis/permissionsreport` | ❌ List reports |
| GET | `/_apis/permissionsreport/{id}` | ❌ Get report |
| GET | `/_apis/permissionsreport/{id}/download` | ❌ Download report |

---

## 23. Pipelines

**CLI Coverage: ⚠️ PARTIAL** (~4 of ~10 endpoints)

### Covered by CLI

| Endpoint | CLI Command |
|----------|-------------|
| List pipelines | `az pipelines list` |
| Show pipeline | `az pipelines show` |
| Create pipeline | `az pipelines create` |
| Run pipeline | `az pipelines run` |

### ❌ NOT Available via CLI

| Method | Endpoint | Notes |
|--------|----------|-------|
| PATCH | `/_apis/pipelines/{pipelineId}` | Update pipeline |
| DELETE | `/_apis/pipelines/{pipelineId}` | Delete pipeline |
| GET | `/_apis/pipelines/{pipelineId}/runs` | List runs |
| GET | `/_apis/pipelines/{pipelineId}/runs/{runId}` | Get run details |
| GET | `/_apis/pipelines/{pipelineId}/runs/{runId}/log` | Run logs |
| GET | `/_apis/pipelines/{pipelineId}/runs/{runId}/artifacts` | Run artifacts |
| POST | `/_apis/pipelines/preview` | Preview YAML pipeline |

---

## 24. Policy

**CLI Coverage: ⚠️ PARTIAL** — via `az repos policy`

### Covered by CLI

Branch policies for specific types (approver count, build validation, comment resolution, etc.) are covered. But:

### ❌ NOT Available via CLI

| Method | Endpoint | Notes |
|--------|----------|-------|
| GET | `/_apis/policy/types` | List all policy types |
| GET | `/_apis/policy/types/{typeId}` | Get policy type |
| GET | `/_apis/policy/evaluations` | Policy evaluations |
| GET | `/_apis/policy/evaluations/{evaluationId}` | Get evaluation |
| PATCH | `/_apis/policy/evaluations/{evaluationId}` | Requeue evaluation |

---

## 25. Process Admin

**CLI Coverage: ❌ NONE**

| Method | Endpoint | CLI |
|--------|----------|-----|
| POST | `/_apis/work/processadmin/processes/export` | ❌ Export process |
| POST | `/_apis/work/processadmin/processes/import` | ❌ Import process |
| GET | `/_apis/work/processadmin/processes/status/{id}` | ❌ Import status |
| POST | `/_apis/work/processadmin/processes/migrate/{processId}` | ❌ Migrate process |

---

## 26. Processes (Inherited)

**CLI Coverage: ❌ NONE** — Entire domain is REST-only (~56 endpoints)

This covers the entire Inherited Process Model customization API:

| Category | Endpoints | CLI |
|----------|-----------|-----|
| Processes (list, create, get, update, delete) | 5 | ❌ |
| Work Item Types (list, create, get, update, delete) | 5 | ❌ |
| Fields (list, create, get, update, remove) | 5 | ❌ |
| States (list, create, get, update, delete, hide) | 6 | ❌ |
| Rules (list, create, get, update, delete) | 5 | ❌ |
| Behaviors (list, create, get, update, delete) | 5 | ❌ |
| Pages / Layout (list, create, get, update, delete) | 5 | ❌ |
| Groups / Layout (list, create, get, update, delete, move) | 6 | ❌ |
| Controls / Layout (list, create, get, update, delete, move) | 6 | ❌ |
| Lists (picklists — list, create, get, update, delete) | 5 | ❌ |
| System Controls | 3 | ❌ |

> The entire process customization API (custom fields, states, rules, form layout) has zero CLI coverage.

---

## 27. Process Definitions (Legacy)

**CLI Coverage: ❌ NONE** — Legacy API (~44 endpoints, superseded by Processes domain)

---

## 28. Profile

**CLI Coverage: ❌ NONE**

| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/_apis/profile/profiles/me` | ❌ |

---

## 29. Release

**CLI Coverage: ⚠️ MINIMAL** (~5 of ~31 endpoints)

### Covered by CLI

| Endpoint | CLI Command |
|----------|-------------|
| List releases | `az pipelines release list` |
| Show release | `az pipelines release show` |
| Create release | `az pipelines release create` |
| List release definitions | `az pipelines release definition list` |
| Show release definition | `az pipelines release definition show` |

### ❌ NOT Available via CLI (~26 endpoints)

| Method | Endpoint | Notes |
|--------|----------|-------|
| POST | `/_apis/release/definitions` | Create release definition |
| PUT | `/_apis/release/definitions/{id}` | Update release definition |
| DELETE | `/_apis/release/definitions/{id}` | Delete release definition |
| GET | `/_apis/release/definitions/{id}/revisions` | Definition revisions |
| GET | `/_apis/release/definitions/{id}/environments/...` | Environment templates |
| PUT | `/_apis/release/releases/{id}` | Update release |
| PATCH | `/_apis/release/releases/{id}/environments/{envId}` | Update environment (deploy/cancel) |
| GET | `/_apis/release/releases/{id}/environments/{envId}/attempts` | Deployment attempts |
| PATCH | `/_apis/release/releases/{id}/environments/{envId}/deployPhases/.../tasks/{taskId}` | Update manual intervention |
| GET | `/_apis/release/approvals` | List pending approvals |
| PATCH | `/_apis/release/approvals/{approvalId}` | Approve/reject |
| PATCH | `/_apis/release/approvals` | Bulk approve/reject |
| GET | `/_apis/release/releases/{id}/logs` | Release logs |
| GET | `/_apis/release/releases/{id}/environments/{envId}/deployPhases/.../logs` | Task logs |
| GET | `/_apis/release/deployments` | List deployments |
| GET | `/_apis/release/releases/{id}/manualinterventions` | Manual interventions |
| PATCH | `/_apis/release/releases/{id}/manualinterventions/{id}` | Respond to intervention |
| GET | `/_apis/release/releases/{id}/gates/{gateStepId}` | Gate status |
| PATCH | `/_apis/release/releases/{id}/gates/{gateStepId}` | Ignore gate |
| GET | `/_apis/release/folders/{path}` | Release folders |
| POST | `/_apis/release/folders/{path}` | Create folder |
| PATCH | `/_apis/release/folders/{path}` | Update folder |
| DELETE | `/_apis/release/folders/{path}` | Delete folder |
| GET | `/_apis/release/releases/{id}/tasks` | Release tasks |
| DELETE | `/_apis/release/releases/{id}` | Delete release |
| PUT | `/_apis/release/releases/{id}/environments/{envId}/cancel` | Cancel deployment |

> Release definition CRUD, approvals/rejections, manual interventions, deployment management — all REST-only.

---

## 30. Resource Usage

**CLI Coverage: ❌ NONE**

| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/_apis/resourceusage/usage` | ❌ |
| GET | `/_apis/resourceusage/usage/pipelines` | ❌ |

---

## 31. Search

**CLI Coverage: ❌ NONE** — Entire domain is REST-only

| Method | Endpoint | CLI |
|--------|----------|-----|
| POST | `/_apis/search/codesearchresults` | ❌ Code search |
| POST | `/_apis/search/workitemsearchresults` | ❌ Work item search |
| POST | `/_apis/search/wikisearchresults` | ❌ Wiki search |
| POST | `/_apis/search/packagesearchresults` | ❌ Package search |
| POST | `/_apis/search/repositoriessearchresults` | ❌ Repository search |
| GET | `/_apis/search/status/{area}` | ❌ Search index status |

---

## 32. Security

**CLI Coverage: ⚠️ PARTIAL** — `az devops security permission` covers some

### Covered by CLI

| Endpoint | CLI Command |
|----------|-------------|
| List security namespaces | `az devops security permission namespace list` |
| Show permissions | `az devops security permission namespace show` |
| List permissions for token | `az devops security permission list` |
| Update permission | `az devops security permission update` |
| Reset permission | `az devops security permission reset` |
| Reset all permissions | `az devops security permission reset-all` |

### ❌ NOT Available via CLI

| Method | Endpoint | Notes |
|--------|----------|-------|
| GET | `/_apis/securitynamespaces` | List security namespaces (partially covered) |
| GET | `/_apis/accesscontrollists/{securityNamespaceId}` | Query ACLs |
| POST | `/_apis/accesscontrollists/{securityNamespaceId}` | Set ACLs |
| DELETE | `/_apis/accesscontrollists/{securityNamespaceId}` | Remove ACLs |
| POST | `/_apis/accesscontrolentries/{securityNamespaceId}` | Set ACEs |
| DELETE | `/_apis/accesscontrolentries/{securityNamespaceId}` | Remove ACEs |
| GET | `/_apis/permissions/{securityNamespaceId}/{permissions}` | Has permissions |
| DELETE | `/_apis/permissions/{securityNamespaceId}/{permissions}` | Remove permissions |
| POST | `/_apis/security/permissionevaluationbatch` | Batch evaluate |

---

## 33. Security Roles

**CLI Coverage: ❌ NONE**

| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/_apis/securityroles/scopes/{scopeId}/roleassignments/resources/{resourceId}` | ❌ |
| PUT | `/_apis/securityroles/scopes/{scopeId}/roleassignments/resources/{resourceId}` | ❌ |
| PATCH | `/_apis/securityroles/scopes/{scopeId}/roleassignments/resources/{resourceId}` | ❌ |
| DELETE | `/_apis/securityroles/scopes/{scopeId}/roleassignments/resources/{resourceId}/{identityId}` | ❌ |
| GET | `/_apis/securityroles/scopes/{scopeId}/roledefinitions` | ❌ |
| GET | `/_apis/securityroles/scopes` | ❌ |

---

## 34. Service Endpoint

**CLI Coverage: ⚠️ PARTIAL** — `az devops service-endpoint` covers basic CRUD

### Covered by CLI

| Endpoint | CLI Command |
|----------|-------------|
| List endpoints | `az devops service-endpoint list` |
| Show endpoint | `az devops service-endpoint show` |
| Create endpoint | `az devops service-endpoint create` (generic) |
| Create Azure RM | `az devops service-endpoint azurerm create` |
| Create GitHub | `az devops service-endpoint github create` |
| Delete endpoint | `az devops service-endpoint delete` |
| Update endpoint | `az devops service-endpoint update` |

### ❌ NOT Available via CLI

| Method | Endpoint | Notes |
|--------|----------|-------|
| GET | `/_apis/serviceendpoint/types` | Endpoint types |
| POST | `/_apis/serviceendpoint/endpoints/{id}/executionhistory` | Execution history |
| GET | `/_apis/serviceendpoint/endpoints/{id}/executionhistory` | Get execution history |
| POST | `/_apis/serviceendpoint/endpointproxy` | Execute endpoint proxy |
| POST | `/_apis/serviceendpoint/endpoints/{id}/share` | Share with project |

---

## 35. Status

**CLI Coverage: ❌ NONE**

| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/_apis/status/health` | ❌ |

---

## 36. Symbol

**CLI Coverage: ❌ NONE** — Entire domain is REST-only (~13 endpoints)

| Method | Endpoint | Notes |
|--------|----------|-------|
| POST | `/_apis/symbol/requests` | Create symbol request |
| GET | `/_apis/symbol/requests` | List requests |
| GET | `/_apis/symbol/requests/{requestId}` | Get request |
| PATCH | `/_apis/symbol/requests/{requestId}` | Update request |
| DELETE | `/_apis/symbol/requests/{requestId}` | Delete request |
| GET | `/_apis/symbol/symsrv/{debugEntryClientKey}` | Get debug entry (by client key) |
| POST | `/_apis/symbol/requests/{requestId}/debug/entries` | Create debug entry |
| POST | `/_apis/symbol/requests/{requestId}/debug/entries/batch` | Create batch debug entries |
| GET | `/_apis/symbol/requests/{requestId}/debug/entries` | List debug entries |
| POST | `/_apis/symbol/availability` | Check availability |
| GET | `/_apis/symbol/client` | Get client |
| HEAD | `/_apis/symbol/symsrv/{debugEntryClientKey}` | Check debug entry exists |
| GET | `/_apis/symbol/symsrv/{debugEntryClientKey}/{fileName}` | Download debug entry content |

---

## 37. Test (Legacy)

**CLI Coverage: ❌ NONE** — Entire domain is REST-only (~36 endpoints)

| Category | Endpoints | CLI |
|----------|-----------|-----|
| Test Runs (list, create, get, update, delete) | 5 | ❌ |
| Test Results (list, add, get, update) | 4 | ❌ |
| Test Attachments (create for run/result, list, get) | 6 | ❌ |
| Test Suites (list, add test cases, remove, get points) | 5 | ❌ |
| Test Points (list, update) | 2 | ❌ |
| Test Configurations (list, create, get, update, delete) | 5 | ❌ |
| Test Plans (list, create, get, update, delete) — legacy | 5 | ❌ |
| Code Coverage (summary, modules) | 4 | ❌ |

---

## 38. Test Plans

**CLI Coverage: ❌ NONE** — Entire domain is REST-only (~42 endpoints)

| Category | Endpoints | CLI |
|----------|-----------|-----|
| Test Plans (list, create, get, update, delete, clone) | 6 | ❌ |
| Test Suites (list, create, get, update, delete, clone) | 6 | ❌ |
| Test Cases (list, add, remove, get, update, order) | 6 | ❌ |
| Test Configurations (list, create, get, update, delete) | 5 | ❌ |
| Test Variables (list, create, get, update, delete) | 5 | ❌ |
| Test Points (list, get, update) | 3 | ❌ |
| Test Suites Entry (list, reorder) | 2 | ❌ |
| Suite Test Case (list, get, remove, update) | 4 | ❌ |
| Test Plan Clone (status) | 2 | ❌ |
| Test Suite Clone (status) | 2 | ❌ |
| Shared Parameters | 1 | ❌ |

---

## 39. Test Results

**CLI Coverage: ❌ NONE** — Entire domain is REST-only (~83 endpoints)

| Category | Endpoints | CLI |
|----------|-----------|-----|
| Test Run Statistics | 3 | ❌ |
| Test Result Details | 8 | ❌ |
| Test Result Attachments | 6 | ❌ |
| Test Result Trend | 3 | ❌ |
| Test Session | 4 | ❌ |
| Test Log Store | 5 | ❌ |
| Code Coverage | 6 | ❌ |
| Result Meta Data | 4 | ❌ |
| Flaky Detection | 3 | ❌ |
| Test History | 4 | ❌ |
| Test Analytics | 15+ | ❌ |
| Build Coverage | 4 | ❌ |
| Test Summary | 5+ | ❌ |
| Result Grouping | 5+ | ❌ |
| Custom Fields | 3+ | ❌ |

> The entire Test domain (legacy + new plans + results) — approximately **161 combined endpoints** — has zero CLI support. This is the largest uncovered area.

---

## 40. TFVC

**CLI Coverage: ❌ NONE** — Entire domain is REST-only (~15 endpoints)

| Method | Endpoint | Notes |
|--------|----------|-------|
| GET | `/_apis/tfvc/changesets` | List changesets |
| GET | `/_apis/tfvc/changesets/{id}` | Get changeset |
| GET | `/_apis/tfvc/changesets/{id}/changes` | Changeset changes |
| GET | `/_apis/tfvc/changesets/{id}/workItems` | Changeset work items |
| POST | `/_apis/tfvc/changesetsBatch` | Batch changeset lookup |
| GET | `/_apis/tfvc/shelvesets` | List shelvesets |
| GET | `/_apis/tfvc/shelvesets/{shelvesetId}` | Get shelveset |
| GET | `/_apis/tfvc/shelvesets/{shelvesetId}/changes` | Shelveset changes |
| GET | `/_apis/tfvc/shelvesets/{shelvesetId}/workItems` | Shelveset work items |
| GET | `/_apis/tfvc/items` | List/get items |
| GET | `/_apis/tfvc/items/{path}` | Get item content |
| POST | `/_apis/tfvc/itemBatch` | Batch item download |
| GET | `/_apis/tfvc/labels` | List labels |
| GET | `/_apis/tfvc/labels/{labelId}` | Get label |
| GET | `/_apis/tfvc/branches` | Branches/hierarchy |

---

## 41. Token Admin

**CLI Coverage: ❌ NONE**

| Method | Endpoint | CLI |
|--------|----------|-----|
| GET | `/_apis/tokenadmin/personalaccesstokens/{subjectDescriptor}` | ❌ List PATs for user |
| POST | `/_apis/tokenadmin/revocations` | ❌ Revoke token |
| POST | `/_apis/tokenadmin/revocationrules` | ❌ Create revocation rule |

---

## 42. Tokens (PAT Lifecycle)

**CLI Coverage: ❌ NONE**

| Method | Endpoint | CLI |
|--------|----------|-----|
| POST | `/_apis/tokens/pats` | ❌ Create PAT |
| GET | `/_apis/tokens/pats` | ❌ List PATs |
| PUT | `/_apis/tokens/pats` | ❌ Update PAT |
| DELETE | `/_apis/tokens/pats` | ❌ Revoke PAT |

> PAT lifecycle management (create, list, rotate, revoke) is completely REST-only.

---

## 43. Wiki

**CLI Coverage: ⚠️ PARTIAL** (~6 of ~15 endpoints)

### Covered by CLI

| Endpoint | CLI Command |
|----------|-------------|
| List wikis | `az devops wiki list` |
| Show wiki | `az devops wiki show` |
| Create wiki | `az devops wiki create` |
| Delete wiki | `az devops wiki delete` |
| Create page | `az devops wiki page create` |
| Show page | `az devops wiki page show` |
| Update page | `az devops wiki page update` |
| Delete page | `az devops wiki page delete` |

### ❌ NOT Available via CLI

| Method | Endpoint | Notes |
|--------|----------|-------|
| PATCH | `/_apis/wiki/wikis/{wikiIdentifier}` | Update wiki settings |
| GET | `/_apis/wiki/wikis/{wikiIdentifier}/pages/{pageId}/stats` | Page stats |
| GET | `/_apis/wiki/wikis/{wikiIdentifier}/pagesbatch` | Batch pages |
| POST | `/_apis/wiki/wikis/{wikiIdentifier}/pagesbatch` | Batch page operations |
| POST | `/_apis/wiki/wikis/{wikiIdentifier}/attachments` | Upload attachment |
| GET | `/_apis/wiki/wikis/{wikiIdentifier}/attachments/{name}` | Get attachment |
| POST | `/_apis/wiki/wikis/{wikiIdentifier}/pages/{id}/moves` | Move/rename page |
| GET | `/_apis/wiki/wikis/{wikiIdentifier}/pagesstats` | Wiki-wide page stats |

---

## 44. Work Item Tracking (WIT)

**CLI Coverage: ⚠️ PARTIAL** (~15 of ~84 endpoints)

### Covered by CLI

| Endpoint Area | CLI Commands |
|---------------|-------------|
| Work Items | `az boards work-item create/show/update/delete` |
| Queries (run) | `az boards query -id {queryId} --wiql {wiql}` |
| Relations | `az boards relation add/remove/show` |
| Area paths | `az boards area project/team list/create/update/delete` |
| Iteration paths | `az boards iteration project/team list/create/update/delete` |

### ❌ NOT Available via CLI (~69 endpoints)

| Method | Endpoint | Notes |
|--------|----------|-------|
| **Batch Operations** | | |
| POST | `/_apis/wit/workitemsbatch` | Batch get work items |
| POST | `/_apis/wit/workitems` | Batch create work items |
| PATCH | `/_apis/wit/workitems` | Batch update work items |
| DELETE | `/_apis/wit/workitems/{id}` (with `destroy=true`) | Permanent delete |
| **WIQL** | | |
| POST | `/_apis/wit/wiql` | Full WIQL execution (⚠️ limited CLI coverage) |
| **Queries (CRUD)** | | |
| GET | `/_apis/wit/queries` | List saved queries |
| POST | `/_apis/wit/queries/{path}` | Create saved query |
| GET | `/_apis/wit/queries/{id}` | Get saved query |
| PATCH | `/_apis/wit/queries/{id}` | Update saved query |
| DELETE | `/_apis/wit/queries/{id}` | Delete saved query |
| **Fields** | | |
| GET | `/_apis/wit/fields` | List all fields |
| POST | `/_apis/wit/fields` | Create custom field |
| GET | `/_apis/wit/fields/{fieldNameOrRef}` | Get field |
| PATCH | `/_apis/wit/fields/{fieldNameOrRef}` | Update field |
| DELETE | `/_apis/wit/fields/{fieldNameOrRef}` | Delete field |
| **Work Item Types** | | |
| GET | `/_apis/wit/workitemtypes` | List work item types |
| GET | `/_apis/wit/workitemtypes/{type}` | Get work item type |
| GET | `/_apis/wit/workitemtypes/{type}/states` | States for type |
| GET | `/_apis/wit/workitemtypes/{type}/fields` | Fields for type |
| **Classification Nodes** (partial CLI coverage) | | |
| GET | `/_apis/wit/classificationnodes` | Get full tree |
| POST | `/_apis/wit/classificationnodes/{structureGroup}/{path}` | Create node |
| PATCH | `/_apis/wit/classificationnodes/{structureGroup}/{path}` | Update node |
| DELETE | `/_apis/wit/classificationnodes/{structureGroup}/{path}` | Delete node |
| POST | `/_apis/wit/classificationnodes/{structureGroup}/{path}` | Move node |
| **Attachments** | | |
| POST | `/_apis/wit/attachments` | Upload attachment |
| GET | `/_apis/wit/attachments/{id}` | Download attachment |
| **Comments** | | |
| GET | `/_apis/wit/workitems/{id}/comments` | List comments |
| POST | `/_apis/wit/workitems/{id}/comments` | Add comment |
| GET | `/_apis/wit/workitems/{id}/comments/{commentId}` | Get comment |
| PATCH | `/_apis/wit/workitems/{id}/comments/{commentId}` | Update comment |
| DELETE | `/_apis/wit/workitems/{id}/comments/{commentId}` | Delete comment |
| GET | `/_apis/wit/workitems/{id}/comments/{commentId}/reactions` | Comment reactions |
| POST | `/_apis/wit/workitems/{id}/comments/{commentId}/reactions/{reactionType}` | Add reaction |
| DELETE | `/_apis/wit/workitems/{id}/comments/{commentId}/reactions/{reactionType}` | Remove reaction |
| **Updates & Revisions** | | |
| GET | `/_apis/wit/workitems/{id}/updates` | Work item updates |
| GET | `/_apis/wit/workitems/{id}/updates/{updateNumber}` | Get specific update |
| GET | `/_apis/wit/workitems/{id}/revisions` | Work item revisions |
| GET | `/_apis/wit/workitems/{id}/revisions/{revisionNumber}` | Get specific revision |
| **Tags** | | |
| GET | `/_apis/wit/tags` | List all tags |
| GET | `/_apis/wit/tags/{tagId}` | Get tag |
| PATCH | `/_apis/wit/tags/{tagId}` | Update tag |
| DELETE | `/_apis/wit/tags/{tagId}` | Delete tag |
| **Recycle Bin** | | |
| GET | `/_apis/wit/recyclebin` | List recycled work items |
| GET | `/_apis/wit/recyclebin/{id}` | Get recycled item |
| PATCH | `/_apis/wit/recyclebin/{id}` | Restore item |
| DELETE | `/_apis/wit/recyclebin/{id}` | Permanently delete |
| **Templates** | | |
| GET | `/_apis/wit/templates` | List templates |
| POST | `/_apis/wit/templates` | Create template |
| GET | `/_apis/wit/templates/{id}` | Get template |
| PUT | `/_apis/wit/templates/{id}` | Update template |
| DELETE | `/_apis/wit/templates/{id}` | Delete template |
| **Reporting** | | |
| GET | `/_apis/wit/reporting/workitemrevisions` | Reporting revisions (OData-like) |
| GET | `/_apis/wit/reporting/workitemlinks` | Reporting links |
| **Account-Wide** | | |
| GET | `/_apis/wit/workitemsearch` | Work item search |
| GET | `/_apis/wit/workitemicons` | Work item type icons |
| GET | `/_apis/wit/workitemtypecategories` | Type categories |
| GET | `/_apis/wit/workitemrelationtypes` | Relation types |
| GET | `/_apis/wit/accountmyworkrecentactivity` | Recent activity |

---

## 45. Work (Boards/Backlogs/Sprints)

**CLI Coverage: ❌ NONE** — Entire domain is REST-only (~59 endpoints)

| Category | Endpoints | CLI |
|----------|-----------|-----|
| **Team Settings** | | |
| GET/PATCH | `/_apis/work/teamsettings` | 2 | ❌ |
| **Iterations** | | |
| GET | `/_apis/work/teamsettings/iterations` | ❌ List team iterations |
| POST | `/_apis/work/teamsettings/iterations` | ❌ Add iteration to team |
| GET | `/_apis/work/teamsettings/iterations/{id}` | ❌ Get team iteration |
| DELETE | `/_apis/work/teamsettings/iterations/{id}` | ❌ Remove from team |
| GET | `/_apis/work/teamsettings/iterations/{id}/capacities` | ❌ Sprint capacities |
| GET | `/_apis/work/teamsettings/iterations/{id}/capacities/{memberId}` | ❌ Member capacity |
| PATCH | `/_apis/work/teamsettings/iterations/{id}/capacities/{memberId}` | ❌ Update capacity |
| PUT | `/_apis/work/teamsettings/iterations/{id}/capacities` | ❌ Replace capacities |
| GET | `/_apis/work/teamsettings/iterations/{id}/workitems` | ❌ Iteration work items |
| **Boards** | | |
| GET | `/_apis/work/boards` | ❌ List boards |
| GET | `/_apis/work/boards/{id}` | ❌ Get board |
| GET | `/_apis/work/boards/{id}/columns` | ❌ Board columns |
| PUT | `/_apis/work/boards/{id}/columns` | ❌ Update columns |
| GET | `/_apis/work/boards/{id}/rows` | ❌ Board rows |
| PUT | `/_apis/work/boards/{id}/rows` | ❌ Update rows |
| GET | `/_apis/work/boards/{id}/cardsettings` | ❌ Card settings |
| PUT | `/_apis/work/boards/{id}/cardsettings` | ❌ Update card settings |
| GET | `/_apis/work/boards/{id}/cardrulesettings` | ❌ Card rules |
| PUT | `/_apis/work/boards/{id}/cardrulesettings` | ❌ Update card rules |
| GET | `/_apis/work/boards/{id}/charts` | ❌ Board charts (CFD, burndown) |
| GET | `/_apis/work/boards/{id}/charts/{chartName}` | ❌ Get chart |
| PATCH | `/_apis/work/boards/{id}/charts/{chartName}` | ❌ Update chart |
| GET | `/_apis/work/boardparents` | ❌ Board parents |
| GET | `/_apis/work/boardusersettings/{id}` | ❌ User board settings |
| PUT | `/_apis/work/boardusersettings/{id}` | ❌ Update user settings |
| PATCH | `/_apis/work/boards/{id}/items/{itemid}` | ❌ Move item on board |
| **Backlogs** | | |
| GET | `/_apis/work/backlogs` | ❌ List backlogs |
| GET | `/_apis/work/backlogs/{id}` | ❌ Get backlog |
| GET | `/_apis/work/backlogs/{id}/workitems` | ❌ Backlog items |
| **Plans (Delivery Plans)** | | |
| GET | `/_apis/work/plans` | ❌ List plans |
| POST | `/_apis/work/plans` | ❌ Create plan |
| GET | `/_apis/work/plans/{id}` | ❌ Get plan |
| PUT | `/_apis/work/plans/{id}` | ❌ Update plan |
| DELETE | `/_apis/work/plans/{id}` | ❌ Delete plan |
| GET | `/_apis/work/plans/{id}/deliverytimeline` | ❌ Delivery timeline |
| **Process Configuration** | | |
| GET | `/_apis/work/processconfiguration` | ❌ |
| **Taskboard** | | |
| GET | `/_apis/work/taskboardcolumns` | ❌ |
| PUT | `/_apis/work/taskboardcolumns` | ❌ |
| GET | `/_apis/work/taskboardworkitems` | ❌ |
| PATCH | `/_apis/work/taskboardworkitems/{workItemId}` | ❌ |

> The entire Boards/Backlogs/Sprint planning/Delivery Plans API — zero CLI coverage.

---

## Summary: Top Uncovered Areas by Impact

| Priority | API Domain | Endpoints | Impact |
|----------|-----------|-----------|--------|
| 🔴 Critical | **Test Plans + Test Results + Test (legacy)** | ~161 | Zero test management from CLI |
| 🔴 Critical | **Processes (Inherited)** | ~56 | Cannot customize work item types, fields, states, rules |
| 🔴 Critical | **Work (Boards/Backlogs)** | ~59 | Cannot manage boards, sprints, capacities, delivery plans |
| 🔴 Critical | **Git (advanced)** | ~83 | No commits, pushes, PR threads/comments, cherry-picks, forks |
| 🟠 High | **Build (advanced)** | ~72 | No definition CRUD, artifacts, logs, retention, templates |
| 🟠 High | **Release (advanced)** | ~26 | No definition CRUD, approvals, manual interventions |
| 🟠 High | **Graph** | ~29 | No user/group/membership management |
| 🟠 High | **Distributed Task** | ~50 | No secure files, deployment groups, elastic pools |
| 🟠 High | **Approvals & Checks** | ~15 | No pipeline approval/check management |
| 🟠 High | **Environments** | ~17 | No pipeline environment management |
| 🟡 Medium | **Artifacts (Package Types)** | ~73 | Only universal packages; no NuGet/npm/Maven/PyPI/Cargo |
| 🟡 Medium | **Audit** | ~9 | No audit log access |
| 🟡 Medium | **Service Hooks** | ~22 | No webhook/subscription management |
| 🟡 Medium | **Notification** | ~17 | No notification subscription management |
| 🟡 Medium | **Dashboard** | ~16 | No dashboard/widget management |
| 🟡 Medium | **Search** | ~6 | No code/work item/wiki search from CLI |
| 🟡 Medium | **Security Roles** | ~6 | No role assignment management |
| 🟡 Medium | **Token Admin / PAT** | ~7 | No PAT lifecycle management |
| 🟢 Low | **TFVC** | ~15 | Legacy version control |
| 🟢 Low | **Symbol** | ~13 | Debug symbol server |
| 🟢 Low | **Wiki (advanced)** | ~8 | Missing: attachments, page stats, moves |
| 🟢 Low | **Favorites** | ~4 | Bookmark management |
| 🟢 Low | **Profile** | ~1 | User profile |
| 🟢 Low | **Status** | ~1 | Service health |
| 🟢 Low | **Resource Usage** | ~2 | Consumption reporting |
| 🟢 Low | **Delegated Auth** | ~2 | OAuth app registration |
| 🟢 Low | **Permissions Report** | ~4 | Permission reporting |
| 🟢 Low | **Process Admin** | ~4 | Process export/import |

---

## Prioritized Implementation Roadmap for This Repository

Based on the gap analysis, here is the suggested order for building REST API clients in this repository:

### Phase 1 — Foundation (Current)
- [x] Core/Projects (list, get, update)
- [x] Git/Repositories (list)
- [ ] Git/Repositories (get, create, delete, update)

### Phase 2 — Git Advanced
- [ ] Git/Commits (list, get, changes)
- [ ] Git/Pushes (list, get, create)
- [ ] Git/Items (list, get — file content)
- [ ] Git/PullRequests (threads, iterations, statuses, labels)
- [ ] Git/CherryPicks and Reverts
- [ ] Git/Forks

### Phase 3 — Build & Pipelines
- [ ] Build/Definitions (CRUD)
- [ ] Build/Artifacts
- [ ] Build/Logs and Timeline
- [ ] Build/Retention
- [ ] Pipelines/Runs (list, get, logs)
- [ ] Environments (CRUD, Kubernetes, VM)
- [ ] Approvals & Checks

### Phase 4 — Work Item Tracking Deep
- [ ] WIT/Queries (CRUD for saved queries)
- [ ] WIT/Fields (list, create)
- [ ] WIT/Comments
- [ ] WIT/Attachments
- [ ] WIT/Updates and Revisions
- [ ] WIT/Tags
- [ ] WIT/Recycle Bin
- [ ] WIT/Templates
- [ ] WIT/Batch Operations

### Phase 5 — Boards & Planning
- [ ] Work/Boards (columns, rows, cards)
- [ ] Work/Backlogs
- [ ] Work/Iterations (team capacities)
- [ ] Work/Plans (Delivery Plans)

### Phase 6 — Process Customization
- [ ] Processes (inherited process model)
- [ ] Work Item Types, Fields, States, Rules, Layout

### Phase 7 — Test Management
- [ ] Test Plans (CRUD)
- [ ] Test Suites, Test Cases, Test Points
- [ ] Test Runs, Test Results
- [ ] Code Coverage

### Phase 8 — Identity & Security
- [ ] Graph (users, groups, memberships)
- [ ] Security (ACLs, ACEs, permissions)
- [ ] Member Entitlement Management
- [ ] Token Admin / PAT Lifecycle

### Phase 9 — Release & Artifacts
- [ ] Release Definitions (CRUD)
- [ ] Release Approvals, Manual Interventions
- [ ] Artifacts Package Types (NuGet, npm, Maven, PyPI, Cargo)
- [ ] Artifacts Feed Management (permissions, views, retention)

### Phase 10 — Observability & Admin
- [ ] Audit Logs
- [ ] Service Hooks
- [ ] Notifications
- [ ] Dashboards & Widgets
- [ ] Search (code, work items, wiki)
- [ ] TFVC
- [ ] Symbol Server

---

## Notes

1. **`az devops invoke`** is a generic escape hatch that can call any REST endpoint, but it provides no parameter validation, response formatting, or error handling — it is not a substitute for dedicated commands.

2. **Azure DevOps Server (on-prem)** may have fewer APIs available than Azure DevOps Services (cloud). This analysis targets the cloud service.

3. **Preview APIs**: Some endpoints are only available as `-preview` sub-versions. These are subject to change and are noted where applicable.

4. **Endpoint counts are approximate** — some endpoints support multiple HTTP methods (GET + PATCH on the same path count as 2), and nested resources add more paths.
