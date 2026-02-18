# Azure DevOps REST API 7.2 — Complete Endpoint Inventory

Generated from: `MicrosoftDocs/vsts-rest-api-specs` (master branch)

## Summary

| # | Domain | Version | Spec Files | Endpoints |
|---|--------|---------|------------|-----------|
| 1 | [account](#account) | 7.2 | 1 | 1 |
| 2 | [advancedSecurity](#advancedsecurity) | 7.2 | 5 | 21 |
| 3 | [approvalsAndChecks](#approvalsandchecks) | 7.2 | 3 | 15 |
| 4 | [artifacts](#artifacts) | 7.2 | 3 | 37 |
| 5 | [artifactsPackageTypes](#artifactspackagetypes) | 7.2 | 6 | 73 |
| 6 | [audit](#audit) | 7.2 | 1 | 9 |
| 7 | [build](#build) | 7.2 | 1 | 87 |
| 8 | [core](#core) | 7.2 | 1 | 19 |
| 9 | [dashboard](#dashboard) | 7.2 | 1 | 16 |
| 10 | [delegatedAuth](#delegatedauth) | 7.2 | 1 | 2 |
| 11 | [distributedTask](#distributedtask) | 7.2 | 4 | 56 |
| 12 | [environments](#environments) | 7.2 | 1 | 17 |
| 13 | [extensionManagement](#extensionmanagement) | 7.2 | 1 | 5 |
| 14 | [favorite](#favorite) | 7.2 | 1 | 4 |
| 15 | [git](#git) | 7.2 | 1 | 108 |
| 16 | [governance](#governance) | 7.2 | 0 | 0 |
| 17 | [graph](#graph) | 7.2 | 1 | 29 |
| 18 | [hooks](#hooks) | 7.2 | 1 | 22 |
| 19 | [ims](#ims) | 7.2 | 1 | 1 |
| 20 | [memberEntitlementManagement](#memberentitlementmanagement) | 7.2 | 1 | 21 |
| 21 | [notification](#notification) | 7.2 | 1 | 17 |
| 22 | [operations](#operations) | 7.2 | 1 | 1 |
| 23 | [permissionsReport](#permissionsreport) | 7.2 | 1 | 4 |
| 24 | [pipelines](#pipelines) | 7.2 | 1 | 10 |
| 25 | [policy](#policy) | 7.2 | 1 | 12 |
| 26 | [processDefinitions](#processdefinitions) | 4.1 | 1 | 44 |
| 27 | [processadmin](#processadmin) | 7.2 | 1 | 4 |
| 28 | [processes](#processes) | 7.2 | 1 | 56 |
| 29 | [profile](#profile) | 7.2 | 1 | 1 |
| 30 | [release](#release) | 7.2 | 1 | 31 |
| 31 | [resourceUsage](#resourceusage) | 7.2 | 1 | 2 |
| 32 | [search](#search) | 7.2 | 1 | 6 |
| 33 | [security](#security) | 7.2 | 1 | 9 |
| 34 | [securityRoles](#securityroles) | 7.2 | 1 | 6 |
| 35 | [serviceEndpoint](#serviceendpoint) | 7.2 | 1 | 12 |
| 36 | [status](#status) | 7.2 | 1 | 1 |
| 37 | [symbol](#symbol) | 7.2 | 1 | 13 |
| 38 | [test](#test) | 7.2 | 1 | 36 |
| 39 | [testPlan](#testplan) | 7.2 | 1 | 42 |
| 40 | [testResults](#testresults) | 7.2 | 1 | 83 |
| 41 | [tfvc](#tfvc) | 7.2 | 1 | 15 |
| 42 | [tokenAdmin](#tokenadmin) | 7.2 | 1 | 3 |
| 43 | [tokenAdministration](#tokenadministration) | 5.2 | 1 | 3 |
| 44 | [tokens](#tokens) | 7.2 | 1 | 4 |
| 45 | [wiki](#wiki) | 7.2 | 1 | 15 |
| 46 | [wit](#wit) | 7.2 | 1 | 84 |
| 47 | [work](#work) | 7.2 | 1 | 59 |
| | **TOTAL** | | | **1116** |

---

## account

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2
- **Spec Files**: accounts.json
- **Endpoint Count**: 1

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/_apis/accounts` | Accounts_List |

---

## advancedSecurity

- **Target Version**: 7.2
- **All Versions**: 7.2
- **Spec Files**: advancedSecurity.Reporting.json, alert.json, management.json, managementInternal.json, reporting.json
- **Endpoint Count**: 21

### advancedSecurity.Reporting.json

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/reporting/summary/alerts` | Summary Dashboard_Get Alert Summary For Org |
| GET | `/{organization}/_apis/reporting/summary/alertsbatch` | Summary Dashboard_List |
| GET | `/{organization}/_apis/reporting/summary/enablement` | Summary Dashboard_Get Enablement Summary For Org |

### alert.json

| Method | Path | Operation ID |
|--------|------|-------------|
| POST | `/{organization}/{project}/_apis/alert/repositories/{repository}/AlertsBatch` | Alerts Batch_List |
| GET | `/{organization}/{project}/_apis/alert/repositories/{repository}/alerts` | Alerts_List |
| POST | `/{organization}/{project}/_apis/alert/repositories/{repository}/alerts/metadatabatch` | Metadata Batch_List |
| GET | `/{organization}/{project}/_apis/alert/repositories/{repository}/alerts/{alertId}` | Alerts_Get |
| PATCH | `/{organization}/{project}/_apis/alert/repositories/{repository}/alerts/{alertId}` | Alerts_Update |
| GET | `/{organization}/{project}/_apis/alert/repositories/{repository}/alerts/{alertId}/instances` | Instances_List |
| GET | `/{organization}/{project}/_apis/alert/repositories/{repository}/alerts/{alertId}/metadata` | Metadata2_Get |
| GET | `/{organization}/{project}/_apis/alert/repositories/{repository}/filters/branches` | Analysis_List |

### management.json

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/management/enablement` | Org Enablement_Get |
| PATCH | `/{organization}/_apis/management/enablement` | Org Enablement_Update |
| GET | `/{organization}/_apis/management/meterUsageEstimate/default` | Org Meter Usage Estimate_Get |
| GET | `/{organization}/_apis/management/meterusage/default` | Meter Usage_Get |
| GET | `/{organization}/{project}/_apis/management/enablement` | Project Enablement_Get |
| PATCH | `/{organization}/{project}/_apis/management/enablement` | Project Enablement_Update |
| GET | `/{organization}/{project}/_apis/management/meterUsageEstimate/default` | Project Meter Usage Estimate_Get |
| GET | `/{organization}/{project}/_apis/management/repositories/{repository}/enablement` | Repo Enablement_Get |
| PATCH | `/{organization}/{project}/_apis/management/repositories/{repository}/enablement` | Repo Enablement_Update |
| GET | `/{organization}/{project}/_apis/management/repositories/{repository}/meterUsageEstimate/default` | Repo Meter Usage Estimate_Get |

---

## approvalsAndChecks

- **Target Version**: 7.2
- **All Versions**: 6.1, 7.0, 7.1, 7.2, azure-devops-server-7.0, azure-devops-server-7.1
- **Spec Files**: pipelinePermissions.json, pipelinesChecks.json, pipelinesapproval.json
- **Endpoint Count**: 15

### pipelinePermissions.json

| Method | Path | Operation ID |
|--------|------|-------------|
| PATCH | `/{organization}/{project}/_apis/pipelines/pipelinepermissions` | Pipeline Permissions_Update Pipeline Permisions For Resources |
| GET | `/{organization}/{project}/_apis/pipelines/pipelinepermissions/{resourceType}/{resourceId}` | Pipeline Permissions_Get |
| PATCH | `/{organization}/{project}/_apis/pipelines/pipelinepermissions/{resourceType}/{resourceId}` | Pipeline Permissions_Update Pipeline Permisions For Resource |

### pipelinesChecks.json

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/{project}/_apis/pipelines/checks/configurations` | Check Configurations_List |
| POST | `/{organization}/{project}/_apis/pipelines/checks/configurations` | Check Configurations_Add |
| DELETE | `/{organization}/{project}/_apis/pipelines/checks/configurations/{id}` | Check Configurations_Delete |
| GET | `/{organization}/{project}/_apis/pipelines/checks/configurations/{id}` | Check Configurations_Get |
| PATCH | `/{organization}/{project}/_apis/pipelines/checks/configurations/{id}` | Check Configurations_Update |
| POST | `/{organization}/{project}/_apis/pipelines/checks/queryconfigurations` | Check Configurations_Query |
| POST | `/{organization}/{project}/_apis/pipelines/checks/runs` | Check Evaluations_Evaluate |
| GET | `/{organization}/{project}/_apis/pipelines/checks/runs/{checkSuiteId}` | Check Evaluations_Get |
| PATCH | `/{organization}/{project}/_apis/pipelines/checks/runs/{checkSuiteId}` | Check Evaluations_Update |

### pipelinesapproval.json

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/{project}/_apis/pipelines/approvals` | Approvals_Query |
| PATCH | `/{organization}/{project}/_apis/pipelines/approvals` | Approvals_Update |
| GET | `/{organization}/{project}/_apis/pipelines/approvals/{approvalId}` | Approvals_Get |

---

## artifacts

- **Target Version**: 7.2
- **All Versions**: 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1
- **Spec Files**: feed.json, provenance.json, sbom.json
- **Endpoint Count**: 37

### feed.json

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/packaging/globalpermissions` | Service  Settings_GetGlobalPermissions |
| PATCH | `/{organization}/_apis/packaging/globalpermissions` | Service  Settings_SetGlobalPermissions |
| GET | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/Packages/{packageId}/Versions/{packageVersionId}/provenance` | Artifact  Details_GetPackageVersionProvenance |
| POST | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/Packages/{packageId}/versionmetricsbatch` | Artifact  Details_Query Package Version Metrics |
| GET | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/Packages/{packageId}/versions` | Artifact  Details_Get Package Versions |
| GET | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/Packages/{packageId}/versions/{packageVersionId}` | Artifact  Details_Get Package Version |
| DELETE | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/RecycleBin/Packages` | Recycle  Bin_Empty Recycle Bin |
| GET | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/RecycleBin/Packages` | Recycle  Bin_Get Recycle Bin Packages |
| GET | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/RecycleBin/Packages/{packageId}` | Recycle  Bin_Get Recycle Bin Package |
| GET | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/RecycleBin/Packages/{packageId}/Versions` | Recycle  Bin_Get Recycle Bin Package Versions |
| GET | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/RecycleBin/Packages/{packageId}/Versions/{packageVersionId}` | Recycle  Bin_Get Recycle Bin Package Version |
| GET | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/packagechanges` | Change  Tracking_Get Package Changes |
| POST | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/packagemetricsbatch` | Artifact  Details_Query Package Metrics |
| GET | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/packages` | Artifact  Details_Get Packages |
| GET | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/packages/{packageId}` | Artifact  Details_Get Package |
| GET | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/permissions` | Feed  Management_Get Feed Permissions |
| PATCH | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/permissions` | Feed  Management_Set Feed Permissions |
| DELETE | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/retentionpolicies` | Retention  Policies_Delete Retention Policy |
| GET | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/retentionpolicies` | Retention  Policies_Get Retention Policy |
| PUT | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/retentionpolicies` | Retention  Policies_Set Retention Policy |
| GET | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/views` | Feed  Management_Get Feed Views |
| POST | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/views` | Feed  Management_Create Feed View |
| DELETE | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/views/{viewId}` | Feed  Management_Delete Feed View |
| GET | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/views/{viewId}` | Feed  Management_Get Feed View |
| PATCH | `/{organization}/{project}/_apis/packaging/Feeds/{feedId}/views/{viewId}` | Feed  Management_Update Feed View |
| GET | `/{organization}/{project}/_apis/packaging/feedchanges` | Change  Tracking_Get Feed Changes |
| GET | `/{organization}/{project}/_apis/packaging/feedchanges/{feedId}` | Change  Tracking_Get Feed Change |
| GET | `/{organization}/{project}/_apis/packaging/feedrecyclebin` | Feed Recycle Bin_List |
| DELETE | `/{organization}/{project}/_apis/packaging/feedrecyclebin/{feedId}` | Feed Recycle Bin_Permanent Delete Feed |
| PATCH | `/{organization}/{project}/_apis/packaging/feedrecyclebin/{feedId}` | Feed Recycle Bin_Restore Deleted Feed |
| GET | `/{organization}/{project}/_apis/packaging/feeds` | Feed  Management_Get Feeds |
| POST | `/{organization}/{project}/_apis/packaging/feeds` | Feed  Management_Create Feed |
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feedId}` | Feed  Management_Delete Feed |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}` | Feed  Management_Get Feed |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}` | Feed  Management_Update Feed |
| GET | `/{organization}/{project}/_apis/public/packaging/Feeds/{feedId}/Packages/{packageId}/badge` | Artifact  Details_Get Badge |

### provenance.json

| Method | Path | Operation ID |
|--------|------|-------------|
| POST | `/{organization}/{project}/_apis/provenance/session/{protocol}` | Provenance_CreateSession |

---

## artifactsPackageTypes

- **Target Version**: 7.2
- **All Versions**: 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1
- **Spec Files**: cargoApi-AzureArtifacts.json, maven.json, npm.json, nuGet.json, pyPiApi.json, universal.json
- **Endpoint Count**: 73

### cargoApi-AzureArtifacts.json

| Method | Path | Operation ID |
|--------|------|-------------|
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/cargo/RecycleBin/packages/{packageName}/versions/{packageVersion}` | Cargo_Delete Package Version From Recycle Bin |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/cargo/RecycleBin/packages/{packageName}/versions/{packageVersion}` | Cargo_GetPackageVersionFromRecycleBin |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/cargo/RecycleBin/packages/{packageName}/versions/{packageVersion}` | Cargo_Restore Package Version From Recycle Bin |
| POST | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/cargo/RecycleBin/packagesBatch` | Cargo_Update Recycle Bin Package Versions |
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/cargo/packages/{packageName}/versions/{packageVersion}` | Cargo_Delete Package Version |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/cargo/packages/{packageName}/versions/{packageVersion}` | Cargo_Get Package Version |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/cargo/packages/{packageName}/versions/{packageVersion}` | Cargo_Update Package Version |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feed}/cargo/packages/{packageName}/upstreaming` | Cargo_Get Upstreaming Behavior |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feed}/cargo/packages/{packageName}/upstreaming` | Cargo_Set Upstreaming Behavior |
| POST | `/{organization}/{project}/_packaging/packaging/feeds/{feedId}/cargo/packagesbatch` | Cargo_Update Package Versions |

### maven.json

| Method | Path | Operation ID |
|--------|------|-------------|
| POST | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/maven/packagesbatch` | Maven_Update Package Versions |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/maven/{groupId}/{artifactId}/{version}/{fileName}/content` | Maven_DownloadPackage |
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feed}/maven/RecycleBin/groups/{groupId}/artifacts/{artifactId}/versions/{version}` | Maven_DeletePackageVersionFromRecycleBin |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feed}/maven/RecycleBin/groups/{groupId}/artifacts/{artifactId}/versions/{version}` | Maven_GetPackageVersionFromRecycleBin |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feed}/maven/RecycleBin/groups/{groupId}/artifacts/{artifactId}/versions/{version}` | Maven_Restore Package Version From Recycle Bin |
| POST | `/{organization}/{project}/_apis/packaging/feeds/{feed}/maven/RecycleBin/packagesBatch` | Maven_Update Recycle Bin Packages |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feed}/maven/groups/{groupId}/artifacts/{artifactId}/upstreaming` | Maven_Get Upstreaming Behavior |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feed}/maven/groups/{groupId}/artifacts/{artifactId}/upstreaming` | Maven_Set Upstreaming Behavior |
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feed}/maven/groups/{groupId}/artifacts/{artifactId}/versions/{version}` | Maven_DeletePackageVersion |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feed}/maven/groups/{groupId}/artifacts/{artifactId}/versions/{version}` | Maven_Get Package Version |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feed}/maven/groups/{groupId}/artifacts/{artifactId}/versions/{version}` | Maven_Update Package Version |

### npm.json

| Method | Path | Operation ID |
|--------|------|-------------|
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/@{packageScope}/{unscopedPackageName}/versions/{packageVersion}` | Npm_Unpublish Scoped Package |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/@{packageScope}/{unscopedPackageName}/versions/{packageVersion}` | Npm_GetScopedPackageVersion |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/@{packageScope}/{unscopedPackageName}/versions/{packageVersion}` | Npm_Update Scoped Package |
| POST | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/RecycleBin/PackagesBatch` | Npm_Update Recycle Bin Packages |
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/RecycleBin/packages/@{packageScope}/{unscopedPackageName}/versions/{packageVersion}` | Npm_Delete Scoped Package Version From Recycle Bin |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/RecycleBin/packages/@{packageScope}/{unscopedPackageName}/versions/{packageVersion}` | Npm_GetScopedPackageVersionFromRecycleBin |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/RecycleBin/packages/@{packageScope}/{unscopedPackageName}/versions/{packageVersion}` | Npm_Restore Scoped Package Version From Recycle Bin |
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/RecycleBin/packages/{packageName}/versions/{packageVersion}` | Npm_Delete Package Version From Recycle Bin |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/RecycleBin/packages/{packageName}/versions/{packageVersion}` | Npm_GetPackageVersionFromRecycleBin |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/RecycleBin/packages/{packageName}/versions/{packageVersion}` | Npm_Restore Package Version From Recycle Bin |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/packages/@{packageScope}/{unscopedPackageName}/upstreaming` | Npm_GetPackageUpstreamingBehavior |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/packages/@{packageScope}/{unscopedPackageName}/upstreaming` | Npm_Set Scoped Upstreaming Behavior |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/packages/@{packageScope}/{unscopedPackageName}/versions/{packageVersion}/content` | Npm_DownloadScopedPackage |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/packages/@{packageScope}/{unscopedPackageName}/versions/{packageVersion}/readme` | Npm_GetScopedPackageReadme |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/packages/{packageName}/upstreaming` | Npm_GetScopedPackageUpstreamingBehavior |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/packages/{packageName}/upstreaming` | Npm_Set Upstreaming Behavior |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/packages/{packageName}/versions/{packageVersion}/content` | Npm_DownloadPackage |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/packages/{packageName}/versions/{packageVersion}/readme` | Npm_GetPackageReadme |
| POST | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/packagesbatch` | Npm_Update Packages |
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/{packageName}/versions/{packageVersion}` | Npm_Unpublish Package |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/{packageName}/versions/{packageVersion}` | Npm_GetPackageVersion |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/npm/{packageName}/versions/{packageVersion}` | Npm_Update Package |

### nuGet.json

| Method | Path | Operation ID |
|--------|------|-------------|
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/nuget/RecycleBin/packages/{packageName}/versions/{packageVersion}` | NuGet_Delete Package Version From Recycle Bin |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/nuget/RecycleBin/packages/{packageName}/versions/{packageVersion}` | NuGet_GetPackageVersionFromRecycleBin |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/nuget/RecycleBin/packages/{packageName}/versions/{packageVersion}` | NuGet_Restore Package Version From Recycle Bin |
| POST | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/nuget/RecycleBin/packagesBatch` | NuGet_Update Recycle Bin Package Versions |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/nuget/packages/{packageName}/upstreaming` | NuGet_Get Upstreaming Behavior |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/nuget/packages/{packageName}/upstreaming` | NuGet_Set Upstreaming Behavior |
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/nuget/packages/{packageName}/versions/{packageVersion}` | NuGet_Delete Package Version |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/nuget/packages/{packageName}/versions/{packageVersion}` | NuGet_Get Package Version |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/nuget/packages/{packageName}/versions/{packageVersion}` | NuGet_Update Package Version |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/nuget/packages/{packageName}/versions/{packageVersion}/content` | NuGet_Download Package |
| POST | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/nuget/packagesbatch` | NuGet_Update Package Versions |

### pyPiApi.json

| Method | Path | Operation ID |
|--------|------|-------------|
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/pypi/RecycleBin/packages/{packageName}/versions/{packageVersion}` | Python_Delete Package Version From Recycle Bin |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/pypi/RecycleBin/packages/{packageName}/versions/{packageVersion}` | Python_GetPackageVersionFromRecycleBin |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/pypi/RecycleBin/packages/{packageName}/versions/{packageVersion}` | Python_Restore Package Version From Recycle Bin |
| POST | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/pypi/RecycleBin/packagesBatch` | Python_Update Recycle Bin Package Versions |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/pypi/packages/{packageName}/upstreaming` | Python_Get Upstreaming Behavior |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/pypi/packages/{packageName}/upstreaming` | Python_Set Upstreaming Behavior |
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/pypi/packages/{packageName}/versions/{packageVersion}` | Python_Delete Package Version |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/pypi/packages/{packageName}/versions/{packageVersion}` | Python_Get Package Version |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/pypi/packages/{packageName}/versions/{packageVersion}` | Python_Update Package Version |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/pypi/packages/{packageName}/versions/{packageVersion}/{fileName}/content` | Python_Download Package |
| POST | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/pypi/packagesbatch` | Python_Update Package Versions |

### universal.json

| Method | Path | Operation ID |
|--------|------|-------------|
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/upack/RecycleBin/packages/{packageName}/versions/{packageVersion}` | Universal_Delete Package Version From Recycle Bin |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/upack/RecycleBin/packages/{packageName}/versions/{packageVersion}` | Universal_GetPackageVersionFromRecycleBin |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/upack/RecycleBin/packages/{packageName}/versions/{packageVersion}` | Universal_Restore Package Version From Recycle Bin |
| POST | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/upack/RecycleBin/packagesBatch` | Universal_Update Recycle Bin Package Versions |
| DELETE | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/upack/packages/{packageName}/versions/{packageVersion}` | Universal_Delete Package Version |
| GET | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/upack/packages/{packageName}/versions/{packageVersion}` | Universal_Get Package Version |
| PATCH | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/upack/packages/{packageName}/versions/{packageVersion}` | Universal_Update Package Version |
| POST | `/{organization}/{project}/_apis/packaging/feeds/{feedId}/upack/packagesbatch` | Universal_Update Package Versions |

---

## audit

- **Target Version**: 7.2
- **All Versions**: 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2
- **Spec Files**: audit.json
- **Endpoint Count**: 9

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/audit/actions` | Actions_List |
| GET | `/{organization}/_apis/audit/auditlog` | Audit Log_Query |
| GET | `/{organization}/_apis/audit/downloadlog` | Download Log_Download Log |
| GET | `/{organization}/_apis/audit/streams` | Streams_Query All Streams |
| POST | `/{organization}/_apis/audit/streams` | Streams_Create |
| PUT | `/{organization}/_apis/audit/streams` | Streams_Update Stream |
| DELETE | `/{organization}/_apis/audit/streams/{streamId}` | Streams_Delete |
| GET | `/{organization}/_apis/audit/streams/{streamId}` | Streams_Query Stream By Id |
| PUT | `/{organization}/_apis/audit/streams/{streamId}` | Streams_Update Status |

---

## build

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: build.json
- **Endpoint Count**: 87

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/build/controllers` | Controllers_List |
| GET | `/{organization}/_apis/build/controllers/{controllerId}` | Controllers_Get |
| GET | `/{organization}/_apis/build/resourceusage` | Resource Usage_Get |
| GET | `/{organization}/_apis/build/retention/history` | History_Get |
| GET | `/{organization}/_apis/public/build/definitions/{project}/{definitionId}/badge` | Badge_Get |
| GET | `/{organization}/{project}/_apis/build/authorizedresources` | Authorizedresources_List |
| PATCH | `/{organization}/{project}/_apis/build/authorizedresources` | Authorizedresources_Authorize Project Resources |
| GET | `/{organization}/{project}/_apis/build/builds` | Builds_List |
| PATCH | `/{organization}/{project}/_apis/build/builds` | Builds_Update Builds |
| POST | `/{organization}/{project}/_apis/build/builds` | Builds_Queue |
| DELETE | `/{organization}/{project}/_apis/build/builds/{buildId}` | Builds_Delete |
| GET | `/{organization}/{project}/_apis/build/builds/{buildId}` | Builds_Get |
| PATCH | `/{organization}/{project}/_apis/build/builds/{buildId}` | Builds_Update Build |
| GET | `/{organization}/{project}/_apis/build/builds/{buildId}/artifacts` | Artifacts_List |
| POST | `/{organization}/{project}/_apis/build/builds/{buildId}/artifacts` | Artifacts_Create |
| GET | `/{organization}/{project}/_apis/build/builds/{buildId}/attachments/{type}` | Attachments_List |
| GET | `/{organization}/{project}/_apis/build/builds/{buildId}/changes` | Builds_Get Build Changes |
| GET | `/{organization}/{project}/_apis/build/builds/{buildId}/leases` | Builds_Get Retention Leases For Build |
| GET | `/{organization}/{project}/_apis/build/builds/{buildId}/logs` | Builds_Get Build Logs |
| GET | `/{organization}/{project}/_apis/build/builds/{buildId}/logs/{logId}` | Builds_Get Build Log |
| GET | `/{organization}/{project}/_apis/build/builds/{buildId}/properties` | Properties_Get Build Properties |
| PATCH | `/{organization}/{project}/_apis/build/builds/{buildId}/properties` | Properties_Update Build Properties |
| GET | `/{organization}/{project}/_apis/build/builds/{buildId}/report` | Report_Get |
| PATCH | `/{organization}/{project}/_apis/build/builds/{buildId}/stages/{stageRefName}` | Stages_Update |
| GET | `/{organization}/{project}/_apis/build/builds/{buildId}/tags` | Tags_Get Build Tags |
| PATCH | `/{organization}/{project}/_apis/build/builds/{buildId}/tags` | Tags_Update Build Tags |
| POST | `/{organization}/{project}/_apis/build/builds/{buildId}/tags` | Tags_Add Build Tags |
| DELETE | `/{organization}/{project}/_apis/build/builds/{buildId}/tags/{tag}` | Tags_Delete Build Tag |
| PUT | `/{organization}/{project}/_apis/build/builds/{buildId}/tags/{tag}` | Tags_Add Build Tag |
| GET | `/{organization}/{project}/_apis/build/builds/{buildId}/timeline/{timelineId}` | Timeline_Get |
| GET | `/{organization}/{project}/_apis/build/builds/{buildId}/workitems` | Builds_Get Build Work Items Refs |
| POST | `/{organization}/{project}/_apis/build/builds/{buildId}/workitems` | Builds_Get Build Work Items Refs From Commits |
| GET | `/{organization}/{project}/_apis/build/builds/{buildId}/{timelineId}/{recordId}/attachments/{type}/{name}` | Attachments_Get |
| GET | `/{organization}/{project}/_apis/build/changes` | Builds_Get Changes Between Builds |
| GET | `/{organization}/{project}/_apis/build/definitions` | Definitions_List |
| POST | `/{organization}/{project}/_apis/build/definitions` | Definitions_Create |
| GET | `/{organization}/{project}/_apis/build/definitions/templates` | Templates_List |
| DELETE | `/{organization}/{project}/_apis/build/definitions/templates/{templateId}` | Templates_Delete |
| GET | `/{organization}/{project}/_apis/build/definitions/templates/{templateId}` | Templates_Get |
| PUT | `/{organization}/{project}/_apis/build/definitions/templates/{templateId}` | Templates_Save Template |
| GET | `/{organization}/{project}/_apis/build/definitions/{DefinitionId}/tags` | Tags_Get Definition Tags |
| PATCH | `/{organization}/{project}/_apis/build/definitions/{DefinitionId}/tags` | Tags_Update Definition Tags |
| POST | `/{organization}/{project}/_apis/build/definitions/{DefinitionId}/tags` | Tags_Add Definition Tags |
| DELETE | `/{organization}/{project}/_apis/build/definitions/{DefinitionId}/tags/{tag}` | Tags_Delete Definition Tag |
| PUT | `/{organization}/{project}/_apis/build/definitions/{DefinitionId}/tags/{tag}` | Tags_Add Definition Tag |
| DELETE | `/{organization}/{project}/_apis/build/definitions/{definitionId}` | Definitions_Delete |
| GET | `/{organization}/{project}/_apis/build/definitions/{definitionId}` | Definitions_Get |
| PATCH | `/{organization}/{project}/_apis/build/definitions/{definitionId}` | Definitions_Restore Definition |
| PUT | `/{organization}/{project}/_apis/build/definitions/{definitionId}` | Definitions_Update |
| GET | `/{organization}/{project}/_apis/build/definitions/{definitionId}/metrics` | Metrics_Get Definition Metrics |
| GET | `/{organization}/{project}/_apis/build/definitions/{definitionId}/properties` | Properties_Get Definition Properties |
| PATCH | `/{organization}/{project}/_apis/build/definitions/{definitionId}/properties` | Properties_Update Definition Properties |
| GET | `/{organization}/{project}/_apis/build/definitions/{definitionId}/resources` | Resources_List |
| PATCH | `/{organization}/{project}/_apis/build/definitions/{definitionId}/resources` | Resources_Authorize Definition Resources |
| GET | `/{organization}/{project}/_apis/build/definitions/{definitionId}/revisions` | Definitions_Get Definition Revisions |
| GET | `/{organization}/{project}/_apis/build/definitions/{definitionId}/yaml` | Yaml_Get |
| DELETE | `/{organization}/{project}/_apis/build/folders` | Folders_Delete |
| POST | `/{organization}/{project}/_apis/build/folders` | Folders_Update |
| PUT | `/{organization}/{project}/_apis/build/folders` | Folders_Create |
| GET | `/{organization}/{project}/_apis/build/folders/{path}` | Folders_List |
| GET | `/{organization}/{project}/_apis/build/generalsettings` | General Settings_Get |
| PATCH | `/{organization}/{project}/_apis/build/generalsettings` | General Settings_Update |
| GET | `/{organization}/{project}/_apis/build/latest/{definition}` | Latest_Get |
| GET | `/{organization}/{project}/_apis/build/metrics/{metricAggregationType}` | Metrics_Get Project Metrics |
| GET | `/{organization}/{project}/_apis/build/options` | Options_List |
| GET | `/{organization}/{project}/_apis/build/repos/{repoType}/badge` | Badge_Get Build Badge Data |
| GET | `/{organization}/{project}/_apis/build/retention` | Retention_Get |
| PATCH | `/{organization}/{project}/_apis/build/retention` | Retention_Update |
| DELETE | `/{organization}/{project}/_apis/build/retention/leases` | Leases_Delete |
| GET | `/{organization}/{project}/_apis/build/retention/leases` | Leases_Get Retention Leases By Minimal Retention Leases |
| POST | `/{organization}/{project}/_apis/build/retention/leases` | Leases_Add |
| GET | `/{organization}/{project}/_apis/build/retention/leases/{leaseId}` | Leases_Get |
| PATCH | `/{organization}/{project}/_apis/build/retention/leases/{leaseId}` | Leases_Update |
| GET | `/{organization}/{project}/_apis/build/settings` | Settings_Get |
| PATCH | `/{organization}/{project}/_apis/build/settings` | Settings_Update |
| GET | `/{organization}/{project}/_apis/build/status/{definition}` | Status_Get |
| GET | `/{organization}/{project}/_apis/build/tags` | Tags_Get Tags |
| DELETE | `/{organization}/{project}/_apis/build/tags/{tag}` | Tags_Delete Tag |
| GET | `/{organization}/{project}/_apis/build/workitems` | Builds_Get Work Items Between Builds |
| GET | `/{organization}/{project}/_apis/sourceProviders/{providerName}/branches` | Source Providers_List Branches |
| GET | `/{organization}/{project}/_apis/sourceProviders/{providerName}/filecontents` | Source Providers_Get File Contents |
| GET | `/{organization}/{project}/_apis/sourceProviders/{providerName}/pathcontents` | Source Providers_Get Path Contents |
| GET | `/{organization}/{project}/_apis/sourceProviders/{providerName}/pullrequests/{pullRequestId}` | Source Providers_Get Pull Request |
| GET | `/{organization}/{project}/_apis/sourceProviders/{providerName}/repositories` | Source Providers_List Repositories |
| GET | `/{organization}/{project}/_apis/sourceProviders/{providerName}/webhooks` | Source Providers_List Webhooks |
| POST | `/{organization}/{project}/_apis/sourceProviders/{providerName}/webhooks` | Source Providers_Restore Webhooks |
| GET | `/{organization}/{project}/_apis/sourceproviders` | Source Providers_List |

---

## core

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: core.json
- **Endpoint Count**: 19

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/process/processes` | Processes_List |
| GET | `/{organization}/_apis/process/processes/{processId}` | Processes_Get |
| GET | `/{organization}/_apis/projects` | Projects_List |
| POST | `/{organization}/_apis/projects` | Projects_Create |
| DELETE | `/{organization}/_apis/projects/{projectId}` | Projects_Delete |
| GET | `/{organization}/_apis/projects/{projectId}` | Projects_Get |
| PATCH | `/{organization}/_apis/projects/{projectId}` | Projects_Update |
| DELETE | `/{organization}/_apis/projects/{projectId}/avatar` | Avatar_Remove Project Avatar |
| PUT | `/{organization}/_apis/projects/{projectId}/avatar` | Avatar_Set Project Avatar |
| GET | `/{organization}/_apis/projects/{projectId}/categorizedteams/` | Categorized Teams_Get |
| GET | `/{organization}/_apis/projects/{projectId}/properties` | Projects_Get Project Properties |
| PATCH | `/{organization}/_apis/projects/{projectId}/properties` | Projects_Set Project Properties |
| GET | `/{organization}/_apis/projects/{projectId}/teams` | Teams_Get Teams |
| POST | `/{organization}/_apis/projects/{projectId}/teams` | Teams_Create |
| DELETE | `/{organization}/_apis/projects/{projectId}/teams/{teamId}` | Teams_Delete |
| GET | `/{organization}/_apis/projects/{projectId}/teams/{teamId}` | Teams_Get |
| PATCH | `/{organization}/_apis/projects/{projectId}/teams/{teamId}` | Teams_Update |
| GET | `/{organization}/_apis/projects/{projectId}/teams/{teamId}/members` | Teams_Get Team Members With Extended Properties |
| GET | `/{organization}/_apis/teams` | Teams_Get All Teams |

---

## dashboard

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: dashboard.json
- **Endpoint Count**: 16

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/{project}/_apis/dashboard/widgettypes` | Widget Types_Get Widget Types |
| GET | `/{organization}/{project}/_apis/dashboard/widgettypes/{contributionId}` | Widget Types_Get Widget Metadata |
| GET | `/{organization}/{project}/{team}/_apis/dashboard/dashboards` | Dashboards_List |
| POST | `/{organization}/{project}/{team}/_apis/dashboard/dashboards` | Dashboards_Create |
| PUT | `/{organization}/{project}/{team}/_apis/dashboard/dashboards` | Dashboards_Replace Dashboards |
| DELETE | `/{organization}/{project}/{team}/_apis/dashboard/dashboards/{dashboardId}` | Dashboards_Delete |
| GET | `/{organization}/{project}/{team}/_apis/dashboard/dashboards/{dashboardId}` | Dashboards_Get |
| PUT | `/{organization}/{project}/{team}/_apis/dashboard/dashboards/{dashboardId}` | Dashboards_Replace Dashboard |
| GET | `/{organization}/{project}/{team}/_apis/dashboard/dashboards/{dashboardId}/widgets` | Widgets_Get Widgets |
| PATCH | `/{organization}/{project}/{team}/_apis/dashboard/dashboards/{dashboardId}/widgets` | Widgets_Update Widgets |
| POST | `/{organization}/{project}/{team}/_apis/dashboard/dashboards/{dashboardId}/widgets` | Widgets_Create |
| PUT | `/{organization}/{project}/{team}/_apis/dashboard/dashboards/{dashboardId}/widgets` | Widgets_Replace Widgets |
| DELETE | `/{organization}/{project}/{team}/_apis/dashboard/dashboards/{dashboardId}/widgets/{widgetId}` | Widgets_Delete |
| GET | `/{organization}/{project}/{team}/_apis/dashboard/dashboards/{dashboardId}/widgets/{widgetId}` | Widgets_Get Widget |
| PATCH | `/{organization}/{project}/{team}/_apis/dashboard/dashboards/{dashboardId}/widgets/{widgetId}` | Widgets_Update Widget |
| PUT | `/{organization}/{project}/{team}/_apis/dashboard/dashboards/{dashboardId}/widgets/{widgetId}` | Widgets_Replace Widget |

---

## delegatedAuth

- **Target Version**: 7.2
- **All Versions**: 7.2
- **Spec Files**: delegatedAuthorization.json
- **Endpoint Count**: 2

| Method | Path | Operation ID |
|--------|------|-------------|
| POST | `/_apis/delegatedauth/registrationsecret/{registrationId}` | Registration Secret_Create |
| PUT | `/_apis/delegatedauth/registrationsecret/{registrationId}` | Registration Secret_Rotate Secret |

---

## distributedTask

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: dynamicPipelines.json, elastic.json, task.json, taskAgent.json
- **Endpoint Count**: 56

### elastic.json

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/distributedtask/elasticpools` | Elasticpools_List |
| POST | `/{organization}/_apis/distributedtask/elasticpools` | Elasticpools_Create |
| GET | `/{organization}/_apis/distributedtask/elasticpools/{poolId}` | Elasticpools_Get |
| PATCH | `/{organization}/_apis/distributedtask/elasticpools/{poolId}` | Elasticpools_Update |
| GET | `/{organization}/_apis/distributedtask/elasticpools/{poolId}/logs` | Elasticpoollogs_List |
| GET | `/{organization}/_apis/distributedtask/elasticpools/{poolId}/nodes` | Nodes_List |
| PATCH | `/{organization}/_apis/distributedtask/elasticpools/{poolId}/nodes/{elasticNodeId}` | Nodes_Update |

### task.json

| Method | Path | Operation ID |
|--------|------|-------------|
| POST | `/{organization}/_apis/public/distributedtask/webhooks/{webHookId}` | Webhooks_Receive External Event |
| POST | `/{organization}/{scopeIdentifier}/_apis/distributedtask/hubs/{hubName}/plans/{planId}/events` | Events_Post Event |
| POST | `/{organization}/{scopeIdentifier}/_apis/distributedtask/hubs/{hubName}/plans/{planId}/jobs/{jobId}/oidctoken` | Oidctoken_Create |
| POST | `/{organization}/{scopeIdentifier}/_apis/distributedtask/hubs/{hubName}/plans/{planId}/logs` | Logs_Create |
| POST | `/{organization}/{scopeIdentifier}/_apis/distributedtask/hubs/{hubName}/plans/{planId}/logs/{logId}` | Logs_Append Log Content |
| PATCH | `/{organization}/{scopeIdentifier}/_apis/distributedtask/hubs/{hubName}/plans/{planId}/timelines/{timelineId}/records` | Records_Update |

### taskAgent.json

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/distributedtask/agentclouds` | Agentclouds_List |
| POST | `/{organization}/_apis/distributedtask/agentclouds` | Agentclouds_Add |
| DELETE | `/{organization}/_apis/distributedtask/agentclouds/{agentCloudId}` | Agentclouds_Delete |
| GET | `/{organization}/_apis/distributedtask/agentclouds/{agentCloudId}` | Agentclouds_Get |
| PATCH | `/{organization}/_apis/distributedtask/agentclouds/{agentCloudId}` | Agentclouds_Update |
| GET | `/{organization}/_apis/distributedtask/agentclouds/{agentCloudId}/requests` | Requests_List |
| GET | `/{organization}/_apis/distributedtask/agentcloudtypes` | Agentcloudtypes_List |
| GET | `/{organization}/_apis/distributedtask/pools` | Pools_Get Agent Pools By Ids |
| POST | `/{organization}/_apis/distributedtask/pools` | Pools_Add |
| DELETE | `/{organization}/_apis/distributedtask/pools/{poolId}` | Pools_Delete |
| GET | `/{organization}/_apis/distributedtask/pools/{poolId}` | Pools_Get |
| PATCH | `/{organization}/_apis/distributedtask/pools/{poolId}` | Pools_Update |
| GET | `/{organization}/_apis/distributedtask/pools/{poolId}/agents` | Agents_List |
| POST | `/{organization}/_apis/distributedtask/pools/{poolId}/agents` | Agents_Add |
| DELETE | `/{organization}/_apis/distributedtask/pools/{poolId}/agents/{agentId}` | Agents_Delete |
| GET | `/{organization}/_apis/distributedtask/pools/{poolId}/agents/{agentId}` | Agents_Get |
| PATCH | `/{organization}/_apis/distributedtask/pools/{poolId}/agents/{agentId}` | Agents_Update |
| PUT | `/{organization}/_apis/distributedtask/pools/{poolId}/agents/{agentId}` | Agents_Replace Agent |
| GET | `/{organization}/_apis/distributedtask/pools/{poolId}/permissions/{permissions}` | Poolpermissions_Has Pool Permissions |
| PATCH | `/{organization}/_apis/distributedtask/variablegroups` | Variablegroups_Share Variable Group |
| POST | `/{organization}/_apis/distributedtask/variablegroups` | Variablegroups_Add |
| DELETE | `/{organization}/_apis/distributedtask/variablegroups/{groupId}` | Variablegroups_Delete |
| PUT | `/{organization}/_apis/distributedtask/variablegroups/{groupId}` | Variablegroups_Update |
| GET | `/{organization}/_apis/distributedtask/yamlschema` | Yamlschema_Get |
| GET | `/{organization}/{project}/_apis/distributedtask/deploymentgroups` | Deploymentgroups_List |
| POST | `/{organization}/{project}/_apis/distributedtask/deploymentgroups` | Deploymentgroups_Add |
| DELETE | `/{organization}/{project}/_apis/distributedtask/deploymentgroups/{deploymentGroupId}` | Deploymentgroups_Delete |
| GET | `/{organization}/{project}/_apis/distributedtask/deploymentgroups/{deploymentGroupId}` | Deploymentgroups_Get |
| PATCH | `/{organization}/{project}/_apis/distributedtask/deploymentgroups/{deploymentGroupId}` | Deploymentgroups_Update |
| GET | `/{organization}/{project}/_apis/distributedtask/deploymentgroups/{deploymentGroupId}/targets` | Targets_List |
| PATCH | `/{organization}/{project}/_apis/distributedtask/deploymentgroups/{deploymentGroupId}/targets` | Targets_Update |
| DELETE | `/{organization}/{project}/_apis/distributedtask/deploymentgroups/{deploymentGroupId}/targets/{targetId}` | Targets_Delete |
| GET | `/{organization}/{project}/_apis/distributedtask/deploymentgroups/{deploymentGroupId}/targets/{targetId}` | Targets_Get |
| GET | `/{organization}/{project}/_apis/distributedtask/queues` | Queues_Get Agent Queues For Pools |
| POST | `/{organization}/{project}/_apis/distributedtask/queues` | Queues_Add |
| DELETE | `/{organization}/{project}/_apis/distributedtask/queues/{queueId}` | Queues_Delete |
| GET | `/{organization}/{project}/_apis/distributedtask/queues/{queueId}` | Queues_Get |
| POST | `/{organization}/{project}/_apis/distributedtask/taskgroups` | Taskgroups_Add |
| DELETE | `/{organization}/{project}/_apis/distributedtask/taskgroups/{taskGroupId}` | Taskgroups_Delete |
| GET | `/{organization}/{project}/_apis/distributedtask/taskgroups/{taskGroupId}` | Taskgroups_List |
| PUT | `/{organization}/{project}/_apis/distributedtask/taskgroups/{taskGroupId}` | Taskgroups_Update |
| GET | `/{organization}/{project}/_apis/distributedtask/variablegroups` | Variablegroups_Get Variable Groups By Id |
| GET | `/{organization}/{project}/_apis/distributedtask/variablegroups/{groupId}` | Variablegroups_Get |

---

## environments

- **Target Version**: 7.2
- **All Versions**: 7.2
- **Spec Files**: environments.json
- **Endpoint Count**: 17

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/{project}/_apis/pipelines/environments` | Environments_List |
| POST | `/{organization}/{project}/_apis/pipelines/environments` | Environments_Add |
| POST | `/{organization}/{project}/_apis/pipelines/environments/environmentaccesstoken/{environmentId}` | Environmentaccesstoken_Generate Environment Access Token |
| DELETE | `/{organization}/{project}/_apis/pipelines/environments/{environmentId}` | Environments_Delete |
| GET | `/{organization}/{project}/_apis/pipelines/environments/{environmentId}` | Environments_Get |
| PATCH | `/{organization}/{project}/_apis/pipelines/environments/{environmentId}` | Environments_Update |
| GET | `/{organization}/{project}/_apis/pipelines/environments/{environmentId}/environmentdeploymentrecords` | Environmentdeploymentrecords_List |
| PATCH | `/{organization}/{project}/_apis/pipelines/environments/{environmentId}/providers/kubernetes` | Kubernetes_Update |
| POST | `/{organization}/{project}/_apis/pipelines/environments/{environmentId}/providers/kubernetes` | Kubernetes_Add |
| DELETE | `/{organization}/{project}/_apis/pipelines/environments/{environmentId}/providers/kubernetes/{resourceId}` | Kubernetes_Delete |
| GET | `/{organization}/{project}/_apis/pipelines/environments/{environmentId}/providers/kubernetes/{resourceId}` | Kubernetes_Get |
| GET | `/{organization}/{project}/_apis/pipelines/environments/{environmentId}/providers/virtualmachines` | Vmresource_List |
| PATCH | `/{organization}/{project}/_apis/pipelines/environments/{environmentId}/providers/virtualmachines` | Vmresource_Update |
| POST | `/{organization}/{project}/_apis/pipelines/environments/{environmentId}/providers/virtualmachines` | Vmresource_Add |
| PUT | `/{organization}/{project}/_apis/pipelines/environments/{environmentId}/providers/virtualmachines` | Vmresource_Replace Virtual Machine Resource |
| GET | `/{organization}/{project}/_apis/pipelines/environments/{environmentId}/providers/virtualmachines/pool` | Pool_Get |
| DELETE | `/{organization}/{project}/_apis/pipelines/environments/{environmentId}/providers/virtualmachines/{resourceId}` | Vmresource_Delete |

---

## extensionManagement

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: extensionManagement.json
- **Endpoint Count**: 5

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/extensionmanagement/installedextensions` | Installed Extensions_List |
| PATCH | `/{organization}/_apis/extensionmanagement/installedextensions` | Installed Extensions_Update |
| DELETE | `/{organization}/_apis/extensionmanagement/installedextensionsbyname/{publisherName}/{extensionName}` | Installed Extensions_Uninstall Extension By Name |
| GET | `/{organization}/_apis/extensionmanagement/installedextensionsbyname/{publisherName}/{extensionName}` | Installed Extensions_Get |
| POST | `/{organization}/_apis/extensionmanagement/installedextensionsbyname/{publisherName}/{extensionName}/{version}` | Installed Extensions_Install Extension By Name |

---

## favorite

- **Target Version**: 7.2
- **All Versions**: 7.1, 7.2, azure-devops-server-7.1
- **Spec Files**: favorite.json
- **Endpoint Count**: 4

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/favorite/favorites` | Favorites_Get Favorites |
| POST | `/{organization}/_apis/favorite/favorites` | Favorites_Create Favorite |
| DELETE | `/{organization}/_apis/favorite/favorites/{favoriteId}` | Favorites_Delete Favorite By Id |
| GET | `/{organization}/_apis/favorite/favorites/{favoriteId}` | Favorites_Get Favorite By Id |

---

## git

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: git.json
- **Endpoint Count**: 108

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/{project}/_apis/git/deletedrepositories` | Repositories_Get Deleted Repositories |
| GET | `/{organization}/{project}/_apis/git/favorites/refs` | Refs Favorites_List |
| POST | `/{organization}/{project}/_apis/git/favorites/refs` | Refs Favorites_Create |
| DELETE | `/{organization}/{project}/_apis/git/favorites/refs/{favoriteId}` | Refs Favorites_Delete |
| GET | `/{organization}/{project}/_apis/git/favorites/refs/{favoriteId}` | Refs Favorites_Get |
| GET | `/{organization}/{project}/_apis/git/favorites/refsForProject` | Refs Favorites For Project_List |
| GET | `/{organization}/{project}/_apis/git/policy/configurations` | Policy Configurations_Get |
| GET | `/{organization}/{project}/_apis/git/pullrequests` | Pull Requests_Get Pull Requests By Project |
| GET | `/{organization}/{project}/_apis/git/pullrequests/{pullRequestId}` | Pull Requests_Get Pull Request By Id |
| GET | `/{organization}/{project}/_apis/git/recycleBin/repositories` | Repositories_Get Recycle Bin Repositories |
| DELETE | `/{organization}/{project}/_apis/git/recycleBin/repositories/{repositoryId}` | Repositories_Delete Repository From Recycle Bin |
| PATCH | `/{organization}/{project}/_apis/git/recycleBin/repositories/{repositoryId}` | Repositories_Restore Repository From Recycle Bin |
| GET | `/{organization}/{project}/_apis/git/repositories` | Repositories_List |
| POST | `/{organization}/{project}/_apis/git/repositories` | Repositories_Create |
| DELETE | `/{organization}/{project}/_apis/git/repositories/{repositoryId}` | Repositories_Delete |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}` | Repositories_Get Repository |
| PATCH | `/{organization}/{project}/_apis/git/repositories/{repositoryId}` | Repositories_Update |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/annotatedtags` | Annotated Tags_Create |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/annotatedtags/{objectId}` | Annotated Tags_Get |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/blobs` | Blobs_Get Blobs Zip |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/blobs/{sha1}` | Blobs_Get Blob |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/cherryPicks` | Cherry Picks_Get Cherry Pick For Ref Name |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/cherryPicks` | Cherry Picks_Create |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/cherryPicks/{cherryPickId}` | Cherry Picks_Get Cherry Pick |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/commits` | Commits_Get Push Commits |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/commits/{commitId}` | Commits_Get |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/commits/{commitId}/changes` | Commits_Get Changes |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/commits/{commitId}/statuses` | Statuses_List |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/commits/{commitId}/statuses` | Statuses_Create |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/commitsbatch` | Commits_Get Commits Batch |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/diffs/commits` | Diffs_Get |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/importRequests` | Import Requests_Query |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/importRequests` | Import Requests_Create |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/importRequests/{importRequestId}` | Import Requests_Get |
| PATCH | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/importRequests/{importRequestId}` | Import Requests_Update |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/items` | Items_List |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/itemsbatch` | Items_Get Items Batch |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/attachments` | Pull Request Attachments_List |
| DELETE | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/attachments/{fileName}` | Pull Request Attachments_Delete |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/attachments/{fileName}` | Pull Request Attachments_Get |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/attachments/{fileName}` | Pull Request Attachments_Create |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/commits` | Pull Request Commits_Get Pull Request Commits |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/iterations` | Pull Request Iterations_List |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/iterations/{iterationId}` | Pull Request Iterations_Get |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/iterations/{iterationId}/changes` | Pull Request Iteration Changes_Get |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/iterations/{iterationId}/commits` | Pull Request Commits_Get Pull Request Iteration Commits |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/iterations/{iterationId}/statuses` | Pull Request Iteration Statuses_List |
| PATCH | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/iterations/{iterationId}/statuses` | Pull Request Iteration Statuses_Update |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/iterations/{iterationId}/statuses` | Pull Request Iteration Statuses_Create |
| DELETE | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/iterations/{iterationId}/statuses/{statusId}` | Pull Request Iteration Statuses_Delete |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/iterations/{iterationId}/statuses/{statusId}` | Pull Request Iteration Statuses_Get |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/labels` | Pull Request Labels_List |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/labels` | Pull Request Labels_Create |
| DELETE | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/labels/{labelIdOrName}` | Pull Request Labels_Delete |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/labels/{labelIdOrName}` | Pull Request Labels_Get |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/properties` | Pull Request Properties_List |
| PATCH | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/properties` | Pull Request Properties_Update |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/reviewers` | Pull Request Reviewers_List |
| PATCH | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/reviewers` | Pull Request Reviewers_Update Pull Request Reviewers |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/reviewers` | Pull Request Reviewers_Create Pull Request Reviewers |
| PUT | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/reviewers` | Pull Request Reviewers_Create Unmaterialized Pull Request Reviewer |
| DELETE | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/reviewers/{reviewerId}` | Pull Request Reviewers_Delete |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/reviewers/{reviewerId}` | Pull Request Reviewers_Get |
| PATCH | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/reviewers/{reviewerId}` | Pull Request Reviewers_Update Pull Request Reviewer |
| PUT | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/reviewers/{reviewerId}` | Pull Request Reviewers_Create Pull Request Reviewer |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/share` | Pull Request Share_Share Pull Request |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/statuses` | Pull Request Statuses_List |
| PATCH | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/statuses` | Pull Request Statuses_Update |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/statuses` | Pull Request Statuses_Create |
| DELETE | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/statuses/{statusId}` | Pull Request Statuses_Delete |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/statuses/{statusId}` | Pull Request Statuses_Get |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/threads` | Pull Request Threads_List |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/threads` | Pull Request Threads_Create |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/threads/{threadId}` | Pull Request Threads_Get |
| PATCH | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/threads/{threadId}` | Pull Request Threads_Update |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/threads/{threadId}/comments` | Pull Request Thread Comments_List |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/threads/{threadId}/comments` | Pull Request Thread Comments_Create |
| DELETE | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/threads/{threadId}/comments/{commentId}` | Pull Request Thread Comments_Delete |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/threads/{threadId}/comments/{commentId}` | Pull Request Thread Comments_Get |
| PATCH | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/threads/{threadId}/comments/{commentId}` | Pull Request Thread Comments_Update |
| DELETE | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/threads/{threadId}/comments/{commentId}/likes` | Pull Request Comment Likes_Delete |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/threads/{threadId}/comments/{commentId}/likes` | Pull Request Comment Likes_List |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/threads/{threadId}/comments/{commentId}/likes` | Pull Request Comment Likes_Create |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullRequests/{pullRequestId}/workitems` | Pull Request Work Items_List |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullrequestquery` | Pull Request Query_Get |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullrequests` | Pull Requests_Get Pull Requests |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullrequests` | Pull Requests_Create |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullrequests/{pullRequestId}` | Pull Requests_Get Pull Request |
| PATCH | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pullrequests/{pullRequestId}` | Pull Requests_Update |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pushes` | Pushes_List |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pushes` | Pushes_Create |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/pushes/{pushId}` | Pushes_Get |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/refs` | Refs_List |
| PATCH | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/refs` | Refs_Update Ref |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/refs` | Refs_Update Refs |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/reverts` | Reverts_Get Revert For Ref Name |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/reverts` | Reverts_Create |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/reverts/{revertId}` | Reverts_Get Revert |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/stats/branches` | Stats_List |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/suggestions` | Suggestions_List |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryId}/trees/{sha1}` | Trees_Get |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryNameOrId}/commits/{commitId}/mergebases` | Merge Bases_List |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryNameOrId}/forkSyncRequests` | Forks_Get Fork Sync Requests |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryNameOrId}/forkSyncRequests` | Forks_Create fork sync request |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryNameOrId}/forkSyncRequests/{forkSyncOperationId}` | Forks_Get fork sync request |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryNameOrId}/forks/{collectionId}` | Forks_List |
| POST | `/{organization}/{project}/_apis/git/repositories/{repositoryNameOrId}/merges` | Merges_Create |
| GET | `/{organization}/{project}/_apis/git/repositories/{repositoryNameOrId}/merges/{mergeOperationId}` | Merges_Get |

---

## governance

- **Target Version**: 7.2
- **All Versions**: 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1
- **Spec Files**: none
- **Endpoint Count**: 0

*No endpoints found in spec.*

---

## graph

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2
- **Spec Files**: graph.json
- **Endpoint Count**: 29

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/graph/Memberships/{subjectDescriptor}` | Memberships_List |
| DELETE | `/{organization}/_apis/graph/Subjects/{subjectDescriptor}/avatars` | Avatars_Delete |
| GET | `/{organization}/_apis/graph/Subjects/{subjectDescriptor}/avatars` | Avatars_Get |
| PUT | `/{organization}/_apis/graph/Subjects/{subjectDescriptor}/avatars` | Avatars_Set Avatar |
| GET | `/{organization}/_apis/graph/Users/{userDescriptor}/providerinfo` | Provider Info_Get |
| GET | `/{organization}/_apis/graph/descriptors/{storageKey}` | Descriptors_Get |
| GET | `/{organization}/_apis/graph/groups` | Groups_List |
| POST | `/{organization}/_apis/graph/groups` | Groups_Create |
| DELETE | `/{organization}/_apis/graph/groups/{groupDescriptor}` | Groups_Delete |
| GET | `/{organization}/_apis/graph/groups/{groupDescriptor}` | Groups_Get |
| PATCH | `/{organization}/_apis/graph/groups/{groupDescriptor}` | Groups_Update |
| DELETE | `/{organization}/_apis/graph/memberships/{subjectDescriptor}/{containerDescriptor}` | Memberships_Remove Membership |
| GET | `/{organization}/_apis/graph/memberships/{subjectDescriptor}/{containerDescriptor}` | Memberships_Get |
| HEAD | `/{organization}/_apis/graph/memberships/{subjectDescriptor}/{containerDescriptor}` | Memberships_Check Membership Existence |
| PUT | `/{organization}/_apis/graph/memberships/{subjectDescriptor}/{containerDescriptor}` | Memberships_Add |
| GET | `/{organization}/_apis/graph/membershipstates/{subjectDescriptor}` | Membership States_Get |
| POST | `/{organization}/_apis/graph/requestaccess` | Request Access_Request Access |
| GET | `/{organization}/_apis/graph/serviceprincipals` | Service Principals_List |
| POST | `/{organization}/_apis/graph/serviceprincipals` | Service Principals_Create |
| DELETE | `/{organization}/_apis/graph/serviceprincipals/{servicePrincipalDescriptor}` | Service Principals_Delete |
| GET | `/{organization}/_apis/graph/serviceprincipals/{servicePrincipalDescriptor}` | Service Principals_Get |
| GET | `/{organization}/_apis/graph/storagekeys/{subjectDescriptor}` | Storage Keys_Get |
| POST | `/{organization}/_apis/graph/subjectlookup` | Subject Lookup_Lookup Subjects |
| POST | `/{organization}/_apis/graph/subjectquery` | Subject Query_Query |
| GET | `/{organization}/_apis/graph/users` | Users_List |
| POST | `/{organization}/_apis/graph/users` | Users_Create |
| DELETE | `/{organization}/_apis/graph/users/{userDescriptor}` | Users_Delete |
| GET | `/{organization}/_apis/graph/users/{userDescriptor}` | Users_Get |
| PATCH | `/{organization}/_apis/graph/users/{userDescriptor}` | Users_Update |

---

## hooks

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: serviceHooks.json
- **Endpoint Count**: 22

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/hooks/consumers` | Consumers_List |
| GET | `/{organization}/_apis/hooks/consumers/{consumerId}` | Consumers_Get |
| GET | `/{organization}/_apis/hooks/consumers/{consumerId}/actions` | Consumers_List Consumer Actions |
| GET | `/{organization}/_apis/hooks/consumers/{consumerId}/actions/{consumerActionId}` | Consumers_Get Consumer Action |
| POST | `/{organization}/_apis/hooks/notificationsquery` | Notifications_Query |
| GET | `/{organization}/_apis/hooks/publishers` | Publishers_List |
| GET | `/{organization}/_apis/hooks/publishers/{publisherId}` | Publishers_Get |
| GET | `/{organization}/_apis/hooks/publishers/{publisherId}/eventtypes` | Publishers_List Event Types |
| GET | `/{organization}/_apis/hooks/publishers/{publisherId}/eventtypes/{eventTypeId}` | Publishers_Get Event Type |
| POST | `/{organization}/_apis/hooks/publishers/{publisherId}/inputValuesQuery` | Publishers_Query Input Values |
| POST | `/{organization}/_apis/hooks/publishersquery` | Publishers_Query Publishers |
| GET | `/{organization}/_apis/hooks/subscriptions` | Subscriptions_List |
| POST | `/{organization}/_apis/hooks/subscriptions` | Subscriptions_Create |
| DELETE | `/{organization}/_apis/hooks/subscriptions/{subscriptionId}` | Subscriptions_Delete |
| GET | `/{organization}/_apis/hooks/subscriptions/{subscriptionId}` | Subscriptions_Get |
| PUT | `/{organization}/_apis/hooks/subscriptions/{subscriptionId}` | Subscriptions_Replace Subscription |
| GET | `/{organization}/_apis/hooks/subscriptions/{subscriptionId}/diagnostics` | Diagnostics_Get |
| PUT | `/{organization}/_apis/hooks/subscriptions/{subscriptionId}/diagnostics` | Diagnostics_Update |
| GET | `/{organization}/_apis/hooks/subscriptions/{subscriptionId}/notifications` | Notifications_List |
| GET | `/{organization}/_apis/hooks/subscriptions/{subscriptionId}/notifications/{notificationId}` | Notifications_Get |
| POST | `/{organization}/_apis/hooks/subscriptionsquery` | Subscriptions_Create Subscriptions Query |
| POST | `/{organization}/_apis/hooks/testnotifications` | Notifications_Create |

---

## ims

- **Target Version**: 7.2
- **All Versions**: 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1
- **Spec Files**: identities.json
- **Endpoint Count**: 1

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/identities` | Identities_Read Identities |

---

## memberEntitlementManagement

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2
- **Spec Files**: memberEntitlementManagement.json
- **Endpoint Count**: 21

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/GroupEntitlements/{groupId}/members` | Members_Get |
| DELETE | `/{organization}/_apis/GroupEntitlements/{groupId}/members/{memberId}` | Members_Remove Member From Group |
| PUT | `/{organization}/_apis/GroupEntitlements/{groupId}/members/{memberId}` | Members_Add |
| GET | `/{organization}/_apis/groupentitlements` | Group Entitlements_List |
| POST | `/{organization}/_apis/groupentitlements` | Group Entitlements_Add |
| DELETE | `/{organization}/_apis/groupentitlements/{groupId}` | Group Entitlements_Delete |
| GET | `/{organization}/_apis/groupentitlements/{groupId}` | Group Entitlements_Get |
| PATCH | `/{organization}/_apis/groupentitlements/{groupId}` | Group Entitlements_Update |
| GET | `/{organization}/_apis/memberentitlements` | Member Entitlements_Search Member Entitlements |
| PATCH | `/{organization}/_apis/serviceprincipalentitlements` | Service Principal Entitlements_Update Service Principal Entitlements |
| POST | `/{organization}/_apis/serviceprincipalentitlements` | Service Principal Entitlements_Add |
| DELETE | `/{organization}/_apis/serviceprincipalentitlements/{servicePrincipalId}` | Service Principal Entitlements_Delete |
| GET | `/{organization}/_apis/serviceprincipalentitlements/{servicePrincipalId}` | Service Principal Entitlements_Get |
| PATCH | `/{organization}/_apis/serviceprincipalentitlements/{servicePrincipalId}` | Service Principal Entitlements_Update Service Principal Entitlement |
| GET | `/{organization}/_apis/userentitlements` | User Entitlements_Search User Entitlements |
| PATCH | `/{organization}/_apis/userentitlements` | User Entitlements_Update User Entitlements |
| POST | `/{organization}/_apis/userentitlements` | User Entitlements_Add |
| DELETE | `/{organization}/_apis/userentitlements/{userId}` | User Entitlements_Delete |
| GET | `/{organization}/_apis/userentitlements/{userId}` | User Entitlements_Get |
| PATCH | `/{organization}/_apis/userentitlements/{userId}` | User Entitlements_Update User Entitlement |
| GET | `/{organization}/_apis/userentitlementsummary` | User Entitlement Summary_Get |

---

## notification

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: notification.json
- **Endpoint Count**: 17

| Method | Path | Operation ID |
|--------|------|-------------|
| PUT | `/{organization}/_apis/notification/Subscriptions/{subscriptionId}/usersettings/{userId}` | Subscriptions_Update Subscription User Settings |
| GET | `/{organization}/_apis/notification/diagnosticlogs/{source}/entries/{entryId}` | Diagnostic Logs_List |
| GET | `/{organization}/_apis/notification/eventtypes` | Event Types_List |
| GET | `/{organization}/_apis/notification/eventtypes/{eventType}` | Event Types_Get |
| GET | `/{organization}/_apis/notification/settings` | Settings_Get |
| PATCH | `/{organization}/_apis/notification/settings` | Settings_Update |
| GET | `/{organization}/_apis/notification/subscribers/{subscriberId}` | Subscribers_Get |
| PATCH | `/{organization}/_apis/notification/subscribers/{subscriberId}` | Subscribers_Update |
| POST | `/{organization}/_apis/notification/subscriptionquery` | Subscriptions_Query |
| GET | `/{organization}/_apis/notification/subscriptions` | Subscriptions_List |
| POST | `/{organization}/_apis/notification/subscriptions` | Subscriptions_Create |
| DELETE | `/{organization}/_apis/notification/subscriptions/{subscriptionId}` | Subscriptions_Delete |
| GET | `/{organization}/_apis/notification/subscriptions/{subscriptionId}` | Subscriptions_Get |
| PATCH | `/{organization}/_apis/notification/subscriptions/{subscriptionId}` | Subscriptions_Update |
| GET | `/{organization}/_apis/notification/subscriptions/{subscriptionId}/diagnostics` | Diagnostics_Get |
| PUT | `/{organization}/_apis/notification/subscriptions/{subscriptionId}/diagnostics` | Diagnostics_Update |
| GET | `/{organization}/_apis/notification/subscriptiontemplates` | Subscriptions_Get Subscription Templates |

---

## operations

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: operations.json
- **Endpoint Count**: 1

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/operations/{operationId}` | Operations_Get |

---

## permissionsReport

- **Target Version**: 7.2
- **All Versions**: 6.0, 6.1, 7.0, 7.1, 7.2
- **Spec Files**: permissionsReport.json
- **Endpoint Count**: 4

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/permissionsreport` | Permissions Report_List |
| POST | `/{organization}/_apis/permissionsreport` | Permissions Report_Create |
| GET | `/{organization}/_apis/permissionsreport/{id}` | Permissions Report_Get |
| GET | `/{organization}/_apis/permissionsreport/{id}/download` | Permissions Report Download_Download |

---

## pipelines

- **Target Version**: 7.2
- **All Versions**: 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1
- **Spec Files**: pipelines.json
- **Endpoint Count**: 10

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/{project}/_apis/pipelines` | Pipelines_List |
| POST | `/{organization}/{project}/_apis/pipelines` | Pipelines_Create |
| GET | `/{organization}/{project}/_apis/pipelines/{pipelineId}` | Pipelines_Get |
| POST | `/{organization}/{project}/_apis/pipelines/{pipelineId}/preview` | Preview_Preview |
| GET | `/{organization}/{project}/_apis/pipelines/{pipelineId}/runs` | Runs_List |
| POST | `/{organization}/{project}/_apis/pipelines/{pipelineId}/runs` | Runs_Run Pipeline |
| GET | `/{organization}/{project}/_apis/pipelines/{pipelineId}/runs/{runId}` | Runs_Get |
| GET | `/{organization}/{project}/_apis/pipelines/{pipelineId}/runs/{runId}/artifacts` | Artifacts_Get |
| GET | `/{organization}/{project}/_apis/pipelines/{pipelineId}/runs/{runId}/logs` | Logs_List |
| GET | `/{organization}/{project}/_apis/pipelines/{pipelineId}/runs/{runId}/logs/{logId}` | Logs_Get |

---

## policy

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: policy.json
- **Endpoint Count**: 12

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/{project}/_apis/policy/configurations` | Configurations_List |
| POST | `/{organization}/{project}/_apis/policy/configurations` | Configurations_Create |
| DELETE | `/{organization}/{project}/_apis/policy/configurations/{configurationId}` | Configurations_Delete |
| GET | `/{organization}/{project}/_apis/policy/configurations/{configurationId}` | Configurations_Get |
| PUT | `/{organization}/{project}/_apis/policy/configurations/{configurationId}` | Configurations_Update |
| GET | `/{organization}/{project}/_apis/policy/configurations/{configurationId}/revisions` | Revisions_List |
| GET | `/{organization}/{project}/_apis/policy/configurations/{configurationId}/revisions/{revisionId}` | Revisions_Get |
| GET | `/{organization}/{project}/_apis/policy/evaluations` | Evaluations_List |
| GET | `/{organization}/{project}/_apis/policy/evaluations/{evaluationId}` | Evaluations_Get |
| PATCH | `/{organization}/{project}/_apis/policy/evaluations/{evaluationId}` | Evaluations_Requeue Policy Evaluation |
| GET | `/{organization}/{project}/_apis/policy/types` | Types_List |
| GET | `/{organization}/{project}/_apis/policy/types/{typeId}` | Types_Get |

---

## processDefinitions

- **Target Version**: 4.1
- **All Versions**: 4.1, tfs-4.1
- **Spec Files**: workItemTrackingProcessDefinitions.json
- **Endpoint Count**: 44

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/work/processdefinitions/lists` | List |
| POST | `/{organization}/_apis/work/processdefinitions/lists` | Create |
| DELETE | `/{organization}/_apis/work/processdefinitions/lists/{listId}` | Delete |
| GET | `/{organization}/_apis/work/processdefinitions/lists/{listId}` | Get |
| PUT | `/{organization}/_apis/work/processdefinitions/lists/{listId}` | Update |
| GET | `/{organization}/_apis/work/processdefinitions/{processId}/behaviors` | List |
| POST | `/{organization}/_apis/work/processdefinitions/{processId}/behaviors` | Create |
| DELETE | `/{organization}/_apis/work/processdefinitions/{processId}/behaviors/{behaviorId}` | Delete |
| GET | `/{organization}/_apis/work/processdefinitions/{processId}/behaviors/{behaviorId}` | Get |
| PUT | `/{organization}/_apis/work/processdefinitions/{processId}/behaviors/{behaviorId}` | Replace Behavior |
| PATCH | `/{organization}/_apis/work/processdefinitions/{processId}/fields` | Update |
| POST | `/{organization}/_apis/work/processdefinitions/{processId}/fields` | Create |
| GET | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefNameForFields}/fields` | List |
| POST | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefNameForFields}/fields` | Add |
| DELETE | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefNameForFields}/fields/{fieldRefName}` | Remove Field From Work Item Type |
| GET | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefNameForFields}/fields/{fieldRefName}` | Get |
| GET | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/layout` | Get |
| POST | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/layout/groups/{groupId}/controls` | Add |
| DELETE | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/layout/groups/{groupId}/controls/{controlId}` | Remove Control From Group |
| PATCH | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/layout/groups/{groupId}/controls/{controlId}` | Edit Control |
| PUT | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/layout/groups/{groupId}/controls/{controlId}` | Set Control In Group |
| PATCH | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/layout/pages` | Edit Page |
| POST | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/layout/pages` | Add |
| DELETE | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/layout/pages/{pageId}` | Remove Page |
| POST | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/layout/pages/{pageId}/sections/{sectionId}/groups` | Add |
| DELETE | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/layout/pages/{pageId}/sections/{sectionId}/groups/{groupId}` | Remove Group |
| PATCH | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/layout/pages/{pageId}/sections/{sectionId}/groups/{groupId}` | Edit Group |
| PUT | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/layout/pages/{pageId}/sections/{sectionId}/groups/{groupId}` | Set Group In Section |
| GET | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/states` | List |
| POST | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/states` | Create |
| DELETE | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/states/{stateId}` | Delete |
| GET | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/states/{stateId}` | Get |
| PATCH | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/states/{stateId}` | Update |
| PUT | `/{organization}/_apis/work/processdefinitions/{processId}/workItemTypes/{witRefName}/states/{stateId}` | Hide State Definition |
| GET | `/{organization}/_apis/work/processdefinitions/{processId}/workitemtypes` | Get Work Item Types |
| POST | `/{organization}/_apis/work/processdefinitions/{processId}/workitemtypes` | Create |
| GET | `/{organization}/_apis/work/processdefinitions/{processId}/workitemtypes/{witRefNameForBehaviors}/behaviors` | Get Behaviors For Work Item Type |
| PATCH | `/{organization}/_apis/work/processdefinitions/{processId}/workitemtypes/{witRefNameForBehaviors}/behaviors` | Update Behavior To Work Item Type |
| POST | `/{organization}/_apis/work/processdefinitions/{processId}/workitemtypes/{witRefNameForBehaviors}/behaviors` | Add |
| DELETE | `/{organization}/_apis/work/processdefinitions/{processId}/workitemtypes/{witRefNameForBehaviors}/behaviors/{behaviorRefName}` | Remove Behavior From Work Item Type |
| GET | `/{organization}/_apis/work/processdefinitions/{processId}/workitemtypes/{witRefNameForBehaviors}/behaviors/{behaviorRefName}` | Get Behavior For Work Item Type |
| DELETE | `/{organization}/_apis/work/processdefinitions/{processId}/workitemtypes/{witRefName}` | Delete |
| GET | `/{organization}/_apis/work/processdefinitions/{processId}/workitemtypes/{witRefName}` | Get Work Item Type |
| PATCH | `/{organization}/_apis/work/processdefinitions/{processId}/workitemtypes/{witRefName}` | Update Work Item Type |

---

## processadmin

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: workItemTrackingProcessTemplate.json
- **Endpoint Count**: 4

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/work/processadmin/processes/export/{id}` | Processes_Export Process Template |
| POST | `/{organization}/_apis/work/processadmin/processes/import` | Processes_Import Process Template |
| GET | `/{organization}/_apis/work/processadmin/processes/status/{id}` | Processes_Import Process Template Status |
| GET | `/{organization}/_apis/work/processadmin/{processId}/behaviors` | Behaviors_List |

---

## processes

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: workItemTrackingProcess.json
- **Endpoint Count**: 56

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/work/processes` | Processes_List |
| POST | `/{organization}/_apis/work/processes` | Processes_Create |
| GET | `/{organization}/_apis/work/processes/lists` | Lists_List |
| POST | `/{organization}/_apis/work/processes/lists` | Lists_Create |
| DELETE | `/{organization}/_apis/work/processes/lists/{listId}` | Lists_Delete |
| GET | `/{organization}/_apis/work/processes/lists/{listId}` | Lists_Get |
| PUT | `/{organization}/_apis/work/processes/lists/{listId}` | Lists_Update |
| GET | `/{organization}/_apis/work/processes/{processId}/behaviors` | Behaviors_List |
| POST | `/{organization}/_apis/work/processes/{processId}/behaviors` | Behaviors_Create |
| DELETE | `/{organization}/_apis/work/processes/{processId}/behaviors/{behaviorRefName}` | Behaviors_Delete |
| GET | `/{organization}/_apis/work/processes/{processId}/behaviors/{behaviorRefName}` | Behaviors_Get |
| PUT | `/{organization}/_apis/work/processes/{processId}/behaviors/{behaviorRefName}` | Behaviors_Update |
| GET | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/fields` | Fields_List |
| POST | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/fields` | Fields_Add |
| DELETE | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/fields/{fieldRefName}` | Fields_Remove Work Item Type Field |
| GET | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/fields/{fieldRefName}` | Fields_Get |
| PATCH | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/fields/{fieldRefName}` | Fields_Update |
| GET | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout` | Layout_Get |
| POST | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout/groups/{groupId}/controls` | Controls_Create |
| DELETE | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout/groups/{groupId}/controls/{controlId}` | Controls_Remove Control From Group |
| PATCH | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout/groups/{groupId}/controls/{controlId}` | Controls_Update |
| PUT | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout/groups/{groupId}/controls/{controlId}` | Controls_Move Control To Group |
| PATCH | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout/pages` | Pages_Update |
| POST | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout/pages` | Pages_Add |
| DELETE | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout/pages/{pageId}` | Pages_Remove Page |
| POST | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout/pages/{pageId}/sections/{sectionId}/groups` | Groups_Add |
| DELETE | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout/pages/{pageId}/sections/{sectionId}/groups/{groupId}` | Groups_Remove Group |
| PATCH | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout/pages/{pageId}/sections/{sectionId}/groups/{groupId}` | Groups_Update |
| PUT | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout/pages/{pageId}/sections/{sectionId}/groups/{groupId}` | Groups_Move Group To Section |
| GET | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout/systemcontrols` | System Controls_List |
| DELETE | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout/systemcontrols/{controlId}` | System Controls_Delete |
| PATCH | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/layout/systemcontrols/{controlId}` | System Controls_Update |
| GET | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/rules` | Rules_List |
| POST | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/rules` | Rules_Add |
| DELETE | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/rules/{ruleId}` | Rules_Delete |
| GET | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/rules/{ruleId}` | Rules_Get |
| PUT | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/rules/{ruleId}` | Rules_Update |
| GET | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/states` | States_List |
| POST | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/states` | States_Create |
| DELETE | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/states/{stateId}` | States_Delete |
| GET | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/states/{stateId}` | States_Get |
| PATCH | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/states/{stateId}` | States_Update |
| PUT | `/{organization}/_apis/work/processes/{processId}/workItemTypes/{witRefName}/states/{stateId}` | States_Hide State Definition |
| GET | `/{organization}/_apis/work/processes/{processId}/workitemtypes` | Work Item Types_List |
| POST | `/{organization}/_apis/work/processes/{processId}/workitemtypes` | Work Item Types_Create |
| DELETE | `/{organization}/_apis/work/processes/{processId}/workitemtypes/{witRefName}` | Work Item Types_Delete |
| GET | `/{organization}/_apis/work/processes/{processId}/workitemtypes/{witRefName}` | Work Item Types_Get |
| PATCH | `/{organization}/_apis/work/processes/{processId}/workitemtypes/{witRefName}` | Work Item Types_Update |
| GET | `/{organization}/_apis/work/processes/{processId}/workitemtypesbehaviors/{witRefNameForBehaviors}/behaviors` | Work Item Types Behaviors_List |
| PATCH | `/{organization}/_apis/work/processes/{processId}/workitemtypesbehaviors/{witRefNameForBehaviors}/behaviors` | Work Item Types Behaviors_Update |
| POST | `/{organization}/_apis/work/processes/{processId}/workitemtypesbehaviors/{witRefNameForBehaviors}/behaviors` | Work Item Types Behaviors_Add |
| DELETE | `/{organization}/_apis/work/processes/{processId}/workitemtypesbehaviors/{witRefNameForBehaviors}/behaviors/{behaviorRefName}` | Work Item Types Behaviors_Remove Behavior From Work Item Type |
| GET | `/{organization}/_apis/work/processes/{processId}/workitemtypesbehaviors/{witRefNameForBehaviors}/behaviors/{behaviorRefName}` | Work Item Types Behaviors_Get |
| DELETE | `/{organization}/_apis/work/processes/{processTypeId}` | Processes_Delete |
| GET | `/{organization}/_apis/work/processes/{processTypeId}` | Processes_Get |
| PATCH | `/{organization}/_apis/work/processes/{processTypeId}` | Processes_Edit Process |

---

## profile

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2
- **Spec Files**: profile.json
- **Endpoint Count**: 1

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/_apis/profile/profiles/{id}` | Profiles_Get |

---

## release

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: release.json
- **Endpoint Count**: 31

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/{project}/_apis/Release/definitions/{definitionId}/revisions` | Definitions_Get Release Definition History |
| GET | `/{organization}/{project}/_apis/Release/definitions/{definitionId}/revisions/{revision}` | Definitions_Get Definition Revision |
| GET | `/{organization}/{project}/_apis/Release/releases/{releaseId}/environments/{environmentId}` | Releases_Get Release Environment |
| PATCH | `/{organization}/{project}/_apis/Release/releases/{releaseId}/environments/{environmentId}` | Releases_Update Release Environment |
| GET | `/{organization}/{project}/_apis/Release/releases/{releaseId}/manualinterventions` | Manual Interventions_List |
| GET | `/{organization}/{project}/_apis/Release/releases/{releaseId}/manualinterventions/{manualInterventionId}` | Manual Interventions_Get |
| PATCH | `/{organization}/{project}/_apis/Release/releases/{releaseId}/manualinterventions/{manualInterventionId}` | Manual Interventions_Update |
| GET | `/{organization}/{project}/_apis/release/approvals` | Approvals_List |
| PATCH | `/{organization}/{project}/_apis/release/approvals/{approvalId}` | Approvals_Update |
| GET | `/{organization}/{project}/_apis/release/definitions` | Definitions_List |
| POST | `/{organization}/{project}/_apis/release/definitions` | Definitions_Create |
| PUT | `/{organization}/{project}/_apis/release/definitions` | Definitions_Update |
| DELETE | `/{organization}/{project}/_apis/release/definitions/{definitionId}` | Definitions_Delete |
| GET | `/{organization}/{project}/_apis/release/definitions/{definitionId}` | Definitions_Get |
| GET | `/{organization}/{project}/_apis/release/deployments` | Deployments_List |
| DELETE | `/{organization}/{project}/_apis/release/folders/{path}` | Folders_Delete |
| GET | `/{organization}/{project}/_apis/release/folders/{path}` | Folders_List |
| PATCH | `/{organization}/{project}/_apis/release/folders/{path}` | Folders_Update |
| POST | `/{organization}/{project}/_apis/release/folders/{path}` | Folders_Create |
| PATCH | `/{organization}/{project}/_apis/release/gates/{gateStepId}` | Gates_Update |
| GET | `/{organization}/{project}/_apis/release/releases` | Releases_List |
| POST | `/{organization}/{project}/_apis/release/releases` | Releases_Create |
| GET | `/{organization}/{project}/_apis/release/releases/{releaseId}` | Releases_Get Release Revision |
| PATCH | `/{organization}/{project}/_apis/release/releases/{releaseId}` | Releases_Update Release Resource |
| PUT | `/{organization}/{project}/_apis/release/releases/{releaseId}` | Releases_Update Release |
| GET | `/{organization}/{project}/_apis/release/releases/{releaseId}/environments/{environmentId}/attempts/{attemptId}/plan/{planId}/attachments/{type}` | Attachments_Get Release Task Attachments |
| GET | `/{organization}/{project}/_apis/release/releases/{releaseId}/environments/{environmentId}/attempts/{attemptId}/plan/{planId}/timelines/{timelineId}/records/{recordId}/attachments/{type}/{name}` | Attachments_Get Release Task Attachment Content |
| GET | `/{organization}/{project}/_apis/release/releases/{releaseId}/environments/{environmentId}/attempts/{attemptId}/timelines/{timelineId}/attachments/{type}` | Attachments_Get Task Attachments |
| GET | `/{organization}/{project}/_apis/release/releases/{releaseId}/environments/{environmentId}/attempts/{attemptId}/timelines/{timelineId}/records/{recordId}/attachments/{type}/{name}` | Attachments_Get Task Attachment Content |
| GET | `/{organization}/{project}/_apis/release/releases/{releaseId}/environments/{environmentId}/deployPhases/{releaseDeployPhaseId}/tasks/{taskId}/logs` | Releases_Get Task Log |
| GET | `/{organization}/{project}/_apis/release/releases/{releaseId}/logs` | Releases_Get Logs |

---

## resourceUsage

- **Target Version**: 7.2
- **All Versions**: 7.2
- **Spec Files**: resourceUsage.json
- **Endpoint Count**: 2

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/resourceusage` | Team Project Collection_List |
| GET | `/{organization}/{project}/_apis/resourceusage` | Project_List |

---

## search

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: search.json
- **Endpoint Count**: 6

| Method | Path | Operation ID |
|--------|------|-------------|
| POST | `/{organization}/_apis/search/packagesearchresults` | Package Search Results_Fetch Package Search Results |
| POST | `/{organization}/{project}/_apis/search/codesearchresults` | Code Search Results_Fetch Code Search Results |
| GET | `/{organization}/{project}/_apis/search/status/repositories/{repository}` | Repositories_Get |
| GET | `/{organization}/{project}/_apis/search/status/tfvc` | Tfvc_Get |
| POST | `/{organization}/{project}/_apis/search/wikisearchresults` | Wiki Search Results_Fetch Wiki Search Results |
| POST | `/{organization}/{project}/_apis/search/workitemsearchresults` | Work Item Search Results_Fetch Work Item Search Results |

---

## security

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: security.json
- **Endpoint Count**: 9

| Method | Path | Operation ID |
|--------|------|-------------|
| DELETE | `/{organization}/_apis/accesscontrolentries/{securityNamespaceId}` | Access Control Entries_Remove Access Control Entries |
| POST | `/{organization}/_apis/accesscontrolentries/{securityNamespaceId}` | Access Control Entries_Set Access Control Entries |
| DELETE | `/{organization}/_apis/accesscontrollists/{securityNamespaceId}` | Access Control Lists_Remove Access Control Lists |
| GET | `/{organization}/_apis/accesscontrollists/{securityNamespaceId}` | Access Control Lists_Query |
| POST | `/{organization}/_apis/accesscontrollists/{securityNamespaceId}` | Access Control Lists_Set Access Control Lists |
| DELETE | `/{organization}/_apis/permissions/{securityNamespaceId}/{permissions}` | Permissions_Remove Permission |
| GET | `/{organization}/_apis/permissions/{securityNamespaceId}/{permissions}` | Permissions_Has Permissions |
| POST | `/{organization}/_apis/security/permissionevaluationbatch` | Permissions_Has Permissions Batch |
| GET | `/{organization}/_apis/securitynamespaces/{securityNamespaceId}` | Security Namespaces_Query |

---

## securityRoles

- **Target Version**: 7.2
- **All Versions**: 6.1, 7.0, 7.1, 7.2, azure-devops-server-7.0, azure-devops-server-7.1
- **Spec Files**: securityRoles.json
- **Endpoint Count**: 6

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/securityroles/scopes/{scopeId}/roleassignments/resources/{resourceId}` | Roleassignments_List |
| PATCH | `/{organization}/_apis/securityroles/scopes/{scopeId}/roleassignments/resources/{resourceId}` | Roleassignments_Remove Role Assignments |
| PUT | `/{organization}/_apis/securityroles/scopes/{scopeId}/roleassignments/resources/{resourceId}` | Roleassignments_Set Role Assignments |
| DELETE | `/{organization}/_apis/securityroles/scopes/{scopeId}/roleassignments/resources/{resourceId}/{identityId}` | Roleassignments_Remove Role Assignment |
| PUT | `/{organization}/_apis/securityroles/scopes/{scopeId}/roleassignments/resources/{resourceId}/{identityId}` | Roleassignments_Set Role Assignment |
| GET | `/{organization}/_apis/securityroles/scopes/{scopeId}/roledefinitions` | Roledefinitions_List |

---

## serviceEndpoint

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: serviceEndpoint.json
- **Endpoint Count**: 12

| Method | Path | Operation ID |
|--------|------|-------------|
| POST | `/{organization}/_apis/serviceendpoint/endpoints` | Endpoints_Create |
| PUT | `/{organization}/_apis/serviceendpoint/endpoints` | Endpoints_Update Service Endpoints |
| DELETE | `/{organization}/_apis/serviceendpoint/endpoints/{endpointId}` | Endpoints_Delete |
| PATCH | `/{organization}/_apis/serviceendpoint/endpoints/{endpointId}` | Endpoints_Share Service Endpoint |
| PUT | `/{organization}/_apis/serviceendpoint/endpoints/{endpointId}` | Endpoints_Update Service Endpoint |
| GET | `/{organization}/_apis/serviceendpoint/types` | Types_Get Service Endpoint Types |
| POST | `/{organization}/_apis/serviceendpoint/types` | Types_Get Filtered Service Endpoint Types |
| POST | `/{organization}/{project}/_apis/serviceendpoint/endpointproxy` | Endpointproxy_Query |
| GET | `/{organization}/{project}/_apis/serviceendpoint/endpoints` | Endpoints_Get Service Endpoints By Names |
| POST | `/{organization}/{project}/_apis/serviceendpoint/endpoints` | Endpoints_Get Service Endpoints With Refreshed Authentication |
| GET | `/{organization}/{project}/_apis/serviceendpoint/endpoints/{endpointId}` | Endpoints_Get |
| GET | `/{organization}/{project}/_apis/serviceendpoint/{endpointId}/executionhistory` | Executionhistory_List |

---

## status

- **Target Version**: 7.2
- **All Versions**: 6.0, 6.1, 7.0, 7.1, 7.2
- **Spec Files**: status.json
- **Endpoint Count**: 1

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/_apis/status/health` | Health_Get |

---

## symbol

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2
- **Spec Files**: symbol.json
- **Endpoint Count**: 13

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/symbol/availability` | Availability_Check Availability |
| HEAD | `/{organization}/_apis/symbol/client` | Client_Head Client |
| GET | `/{organization}/_apis/symbol/client/{clientType}` | Client_Get |
| DELETE | `/{organization}/_apis/symbol/requests` | Requests_Delete Requests Request Name |
| GET | `/{organization}/_apis/symbol/requests` | Requests_Get Requests Request Name |
| PATCH | `/{organization}/_apis/symbol/requests` | Requests_Update Requests Request Name |
| POST | `/{organization}/_apis/symbol/requests` | Requests_Create Requests |
| DELETE | `/{organization}/_apis/symbol/requests/{requestId}` | Requests_Delete Requests Request Id |
| GET | `/{organization}/_apis/symbol/requests/{requestId}` | Requests_Get Requests Request Id |
| PATCH | `/{organization}/_apis/symbol/requests/{requestId}` | Requests_Update Requests Request Id |
| POST | `/{organization}/_apis/symbol/requests/{requestId}` | Requests_Create Requests Request Id Debug Entries |
| GET | `/{organization}/_apis/symbol/requests/{requestId}/contents/{debugEntryId}` | Contents_Get |
| GET | `/{organization}/_apis/symbol/symsrv/{debugEntryClientKey}` | Symsrv_Get |

---

## test

- **Target Version**: 7.2
- **All Versions**: 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1
- **Spec Files**: test.json
- **Endpoint Count**: 36

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/{project}/_apis/test/Plans/{planId}/Suites/{suiteId}/points` | Points_List |
| GET | `/{organization}/{project}/_apis/test/Plans/{planId}/Suites/{suiteId}/points/{pointIds}` | Points_Get Point |
| PATCH | `/{organization}/{project}/_apis/test/Plans/{planId}/Suites/{suiteId}/points/{pointIds}` | Points_Update |
| GET | `/{organization}/{project}/_apis/test/Plans/{planId}/suites/{suiteId}/testcases` | Test  Suites_List |
| DELETE | `/{organization}/{project}/_apis/test/Plans/{planId}/suites/{suiteId}/testcases/{testCaseIds}` | Test  Suites_Remove Test Cases From Suite Url |
| GET | `/{organization}/{project}/_apis/test/Plans/{planId}/suites/{suiteId}/testcases/{testCaseIds}` | Test  Suites_Get |
| PATCH | `/{organization}/{project}/_apis/test/Plans/{planId}/suites/{suiteId}/testcases/{testCaseIds}` | Test  Suites_Update |
| POST | `/{organization}/{project}/_apis/test/Plans/{planId}/suites/{suiteId}/testcases/{testCaseIds}` | Test  Suites_Add |
| POST | `/{organization}/{project}/_apis/test/Results/testhistory` | Test History_Query |
| GET | `/{organization}/{project}/_apis/test/Runs/{runId}/Results/{testCaseResultId}/attachments` | Attachments_Get Test Result Attachments |
| POST | `/{organization}/{project}/_apis/test/Runs/{runId}/Results/{testCaseResultId}/attachments` | Attachments_Create Test Result Attachment |
| GET | `/{organization}/{project}/_apis/test/Runs/{runId}/Results/{testCaseResultId}/attachments/{attachmentId}` | Attachments_Get Test Result Attachment Zip |
| GET | `/{organization}/{project}/_apis/test/Runs/{runId}/Results/{testCaseResultId}/iterations` | Iterations_List |
| GET | `/{organization}/{project}/_apis/test/Runs/{runId}/Results/{testCaseResultId}/iterations/{iterationId}` | Iterations_Get |
| GET | `/{organization}/{project}/_apis/test/Runs/{runId}/attachments` | Attachments_Get Test Run Attachments |
| POST | `/{organization}/{project}/_apis/test/Runs/{runId}/attachments` | Attachments_Create Test Run Attachment |
| GET | `/{organization}/{project}/_apis/test/Runs/{runId}/attachments/{attachmentId}` | Attachments_Get Test Run Attachment Zip |
| GET | `/{organization}/{project}/_apis/test/Runs/{runId}/codecoverage` | Code Coverage_Get Test Run Code Coverage |
| GET | `/{organization}/{project}/_apis/test/Runs/{runId}/results` | Results_List |
| PATCH | `/{organization}/{project}/_apis/test/Runs/{runId}/results` | Results_Update |
| POST | `/{organization}/{project}/_apis/test/Runs/{runId}/results` | Results_Add |
| GET | `/{organization}/{project}/_apis/test/Runs/{runId}/results/{testCaseResultId}` | Results_Get |
| GET | `/{organization}/{project}/_apis/test/codecoverage` | Code Coverage_Get Build Code Coverage |
| POST | `/{organization}/{project}/_apis/test/points` | Points_Get Points By Query |
| GET | `/{organization}/{project}/_apis/test/resultretentionsettings` | Result Retention Settings_Get |
| PATCH | `/{organization}/{project}/_apis/test/resultretentionsettings` | Result Retention Settings_Update |
| GET | `/{organization}/{project}/_apis/test/runs` | Runs_List |
| POST | `/{organization}/{project}/_apis/test/runs` | Runs_Create |
| DELETE | `/{organization}/{project}/_apis/test/runs/{runId}` | Runs_Delete |
| GET | `/{organization}/{project}/_apis/test/runs/{runId}` | Runs_Get Test Run By Id |
| PATCH | `/{organization}/{project}/_apis/test/runs/{runId}` | Runs_Update |
| GET | `/{organization}/{project}/_apis/test/runs/{runId}/Statistics` | Runs_Get Test Run Statistics |
| DELETE | `/{organization}/{project}/_apis/test/testcases/{testCaseId}` | Test Cases_Delete |
| GET | `/{organization}/{project}/{team}/_apis/test/session` | Session_List |
| PATCH | `/{organization}/{project}/{team}/_apis/test/session` | Session_Update |
| POST | `/{organization}/{project}/{team}/_apis/test/session` | Session_Create |

---

## testPlan

- **Target Version**: 7.2
- **All Versions**: 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1
- **Spec Files**: testPlan.json
- **Endpoint Count**: 42

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/testplan/suites` | Test  Suites_Get Suites By Test Case Id |
| POST | `/{organization}/{project}/_apis/testplan/Plans/CloneOperation` | Test Plan Clone_Clone Test Plan |
| GET | `/{organization}/{project}/_apis/testplan/Plans/CloneOperation/{cloneOperationId}` | Test Plan Clone_Get |
| DELETE | `/{organization}/{project}/_apis/testplan/Plans/{planId}/Suites/{suiteId}/TestCase` | Suite Test Case_Remove Test Cases List From Suite |
| GET | `/{organization}/{project}/_apis/testplan/Plans/{planId}/Suites/{suiteId}/TestCase` | Suite Test Case_Get Test Case List |
| PATCH | `/{organization}/{project}/_apis/testplan/Plans/{planId}/Suites/{suiteId}/TestCase` | Suite Test Case_Update |
| POST | `/{organization}/{project}/_apis/testplan/Plans/{planId}/Suites/{suiteId}/TestCase` | Suite Test Case_Add |
| GET | `/{organization}/{project}/_apis/testplan/Plans/{planId}/Suites/{suiteId}/TestCase/{testCaseId}` | Suite Test Case_Get Test Case |
| GET | `/{organization}/{project}/_apis/testplan/Plans/{planId}/Suites/{suiteId}/TestPoint` | Test Point_Get Points |
| PATCH | `/{organization}/{project}/_apis/testplan/Plans/{planId}/Suites/{suiteId}/TestPoint` | Test Point_Update |
| GET | `/{organization}/{project}/_apis/testplan/Plans/{planId}/suites` | Test  Suites_Get Test Suites For Plan |
| POST | `/{organization}/{project}/_apis/testplan/Plans/{planId}/suites` | Test  Suites_Create |
| DELETE | `/{organization}/{project}/_apis/testplan/Plans/{planId}/suites/{suiteId}` | Test  Suites_Delete |
| GET | `/{organization}/{project}/_apis/testplan/Plans/{planId}/suites/{suiteId}` | Test  Suites_Get |
| PATCH | `/{organization}/{project}/_apis/testplan/Plans/{planId}/suites/{suiteId}` | Test  Suites_Update |
| POST | `/{organization}/{project}/_apis/testplan/Suites/CloneOperation` | Test Suite Clone_Clone Test Suite |
| GET | `/{organization}/{project}/_apis/testplan/Suites/CloneOperation/{cloneOperationId}` | Test Suite Clone_Get |
| POST | `/{organization}/{project}/_apis/testplan/TestCases/CloneTestCaseOperation` | Test Case Clone_Clone Test Case |
| GET | `/{organization}/{project}/_apis/testplan/TestCases/CloneTestCaseOperation/{cloneOperationId}` | Test Case Clone_Get |
| DELETE | `/{organization}/{project}/_apis/testplan/configurations` | Configurations_Delete |
| GET | `/{organization}/{project}/_apis/testplan/configurations` | Configurations_List |
| PATCH | `/{organization}/{project}/_apis/testplan/configurations` | Configurations_Update |
| POST | `/{organization}/{project}/_apis/testplan/configurations` | Configurations_Create |
| GET | `/{organization}/{project}/_apis/testplan/configurations/{testConfigurationId}` | Configurations_Get |
| GET | `/{organization}/{project}/_apis/testplan/plans` | Test  Plans_List |
| POST | `/{organization}/{project}/_apis/testplan/plans` | Test  Plans_Create |
| DELETE | `/{organization}/{project}/_apis/testplan/plans/{planId}` | Test  Plans_Delete |
| GET | `/{organization}/{project}/_apis/testplan/plans/{planId}` | Test  Plans_Get |
| PATCH | `/{organization}/{project}/_apis/testplan/plans/{planId}` | Test  Plans_Update |
| GET | `/{organization}/{project}/_apis/testplan/recycleBin/TestPlan/{planId}/testsuite` | Test  Suite  Recycle  Bin  Operations_Get Deleted Test Suites For Plan |
| GET | `/{organization}/{project}/_apis/testplan/recycleBin/testplan` | Test  Plan  Recycle  Bin_List |
| PATCH | `/{organization}/{project}/_apis/testplan/recycleBin/testplan/{planId}` | Test  Plan  Recycle  Bin_Restore Deleted Test Plan |
| GET | `/{organization}/{project}/_apis/testplan/recycleBin/testsuite` | Test  Suite  Recycle  Bin  Operations_Get Deleted Test Suites For Project |
| PATCH | `/{organization}/{project}/_apis/testplan/recycleBin/testsuite/{suiteId}` | Test  Suite  Recycle  Bin  Operations_Restore Deleted Test Suite |
| GET | `/{organization}/{project}/_apis/testplan/suiteentry/{suiteId}` | Test  Suite  Entry_List |
| PATCH | `/{organization}/{project}/_apis/testplan/suiteentry/{suiteId}` | Test  Suite  Entry_Reorder Suite Entries |
| DELETE | `/{organization}/{project}/_apis/testplan/testcases/{testCaseId}` | Test Cases_Delete |
| GET | `/{organization}/{project}/_apis/testplan/variables` | Variables_List |
| POST | `/{organization}/{project}/_apis/testplan/variables` | Variables_Create |
| DELETE | `/{organization}/{project}/_apis/testplan/variables/{testVariableId}` | Variables_Delete |
| GET | `/{organization}/{project}/_apis/testplan/variables/{testVariableId}` | Variables_Get |
| PATCH | `/{organization}/{project}/_apis/testplan/variables/{testVariableId}` | Variables_Update |

---

## testResults

- **Target Version**: 7.2
- **All Versions**: 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1
- **Spec Files**: testResults.json
- **Endpoint Count**: 83

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/{project}/_apis/testresults/codecoverage` | Codecoverage_Get |
| POST | `/{organization}/{project}/_apis/testresults/codecoverage` | Codecoverage_Update |
| POST | `/{organization}/{project}/_apis/testresults/codecoverage/filecoverage` | Filecoverage_Get |
| GET | `/{organization}/{project}/_apis/testresults/codecoverage/sourceview` | Codecoverage_Fetch Source Code Coverage Report |
| GET | `/{organization}/{project}/_apis/testresults/codecoverage/status/{definition}` | Status_Get |
| GET | `/{organization}/{project}/_apis/testresults/extensionfields` | Extensionfields_Query |
| PATCH | `/{organization}/{project}/_apis/testresults/extensionfields` | Extensionfields_Update |
| POST | `/{organization}/{project}/_apis/testresults/extensionfields` | Extensionfields_Add |
| DELETE | `/{organization}/{project}/_apis/testresults/extensionfields/{testExtensionFieldId}` | Extensionfields_Delete |
| GET | `/{organization}/{project}/_apis/testresults/metrics` | Metrics_Get |
| GET | `/{organization}/{project}/_apis/testresults/resultdetailsbybuild` | Resultdetailsbybuild_Get |
| GET | `/{organization}/{project}/_apis/testresults/resultdetailsbyrelease` | Resultdetailsbyrelease_Get |
| GET | `/{organization}/{project}/_apis/testresults/resultgroupsbybuild` | Resultgroupsbybuild_List |
| GET | `/{organization}/{project}/_apis/testresults/resultgroupsbyrelease` | Resultgroupsbyrelease_List |
| POST | `/{organization}/{project}/_apis/testresults/results` | Results_Get Test Results By Query |
| POST | `/{organization}/{project}/_apis/testresults/results/history` | History_Query |
| POST | `/{organization}/{project}/_apis/testresults/results/query` | Results_Get Test Results By Query Wiql |
| POST | `/{organization}/{project}/_apis/testresults/results/resultmetadata` | Result Meta Data_Query |
| PATCH | `/{organization}/{project}/_apis/testresults/results/resultmetadata/{testCaseReferenceId}` | Result Meta Data_Update |
| POST | `/{organization}/{project}/_apis/testresults/results/testhistory` | Test History_Query |
| GET | `/{organization}/{project}/_apis/testresults/results/workitems` | Workitems_Query Test Result Work Items |
| GET | `/{organization}/{project}/_apis/testresults/resultsbybuild` | Resultsbybuild_List |
| GET | `/{organization}/{project}/_apis/testresults/resultsbypipeline` | Resultsbypipeline_List |
| GET | `/{organization}/{project}/_apis/testresults/resultsbyrelease` | Resultsbyrelease_List |
| GET | `/{organization}/{project}/_apis/testresults/resultsgroupdetails` | Resultsgroup Details_Test Results Group Details |
| GET | `/{organization}/{project}/_apis/testresults/resultsummarybybuild` | Resultsummarybybuild_Query |
| GET | `/{organization}/{project}/_apis/testresults/resultsummarybypipeline` | Resultsummarybypipeline_Query |
| GET | `/{organization}/{project}/_apis/testresults/resultsummarybyrelease` | Resultsummarybyrelease_Query Test Results Report For Release |
| POST | `/{organization}/{project}/_apis/testresults/resultsummarybyrelease` | Resultsummarybyrelease_Query Test Results Summary For Releases |
| POST | `/{organization}/{project}/_apis/testresults/resultsummarybyrequirement` | Resultsummarybyrequirement_Query |
| POST | `/{organization}/{project}/_apis/testresults/resulttrendbybuild` | Result Trend By Build_Query |
| POST | `/{organization}/{project}/_apis/testresults/resulttrendbyrelease` | Result Trend By Release_Query |
| GET | `/{organization}/{project}/_apis/testresults/runs` | Runs_List |
| POST | `/{organization}/{project}/_apis/testresults/runs` | Runs_Create |
| DELETE | `/{organization}/{project}/_apis/testresults/runs/{runId}` | Runs_Delete |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}` | Runs_Get |
| PATCH | `/{organization}/{project}/_apis/testresults/runs/{runId}` | Runs_Update |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/attachments` | Attachments_Get Test Run Attachments |
| POST | `/{organization}/{project}/_apis/testresults/runs/{runId}/attachments` | Attachments_Create Test Run Attachment |
| DELETE | `/{organization}/{project}/_apis/testresults/runs/{runId}/attachments/{attachmentId}` | Attachments_Delete Test Run Attachment |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/attachments/{attachmentId}` | Attachments_Get Test Run Attachment Zip |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/codecoverage` | Codecoverage_Get Test Run Code Coverage |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/messagelogs` | Message Logs_List |
| POST | `/{organization}/{project}/_apis/testresults/runs/{runId}/resultdocument` | Result Document_Publish Test Result Document |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/results` | Results_Get Test Results |
| PATCH | `/{organization}/{project}/_apis/testresults/runs/{runId}/results` | Results_Update |
| POST | `/{organization}/{project}/_apis/testresults/runs/{runId}/results` | Results_Add |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/results/{resultId}/testlog` | Testlog_Get Test Result Logs |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/results/{resultId}/testlogstoreendpoint` | Testlogstoreendpoint_Get Test Log Store Endpoint Details For Result Log |
| POST | `/{organization}/{project}/_apis/testresults/runs/{runId}/results/{resultId}/testlogstoreendpoint` | Testlogstoreendpoint_Test Log Store Endpoint Details For Result |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/results/{testCaseResultId}/attachments` | Attachments_Get Test Result Attachments |
| POST | `/{organization}/{project}/_apis/testresults/runs/{runId}/results/{testCaseResultId}/attachments` | Attachments_Create Test Result Attachment |
| DELETE | `/{organization}/{project}/_apis/testresults/runs/{runId}/results/{testCaseResultId}/attachments/{attachmentId}` | Attachments_Delete Test Result Attachment |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/results/{testCaseResultId}/attachments/{attachmentId}` | Attachments_Get Test Result Attachment Zip |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/results/{testCaseResultId}/bugs` | Bugs_List |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/results/{testCaseResultId}/workitems` | Workitems_List |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/results/{testResultId}` | Results_Get Test Result By Id |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/results/{testResultId}/similartestresults` | Similar Test Results_List |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/runsummary` | Runsummary_Get |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/statistics` | Statistics_Get |
| PATCH | `/{organization}/{project}/_apis/testresults/runs/{runId}/tags` | Tags_Update |
| DELETE | `/{organization}/{project}/_apis/testresults/runs/{runId}/testattachments` | Testattachments_Delete |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/testattachments` | Testattachments_List |
| POST | `/{organization}/{project}/_apis/testresults/runs/{runId}/testattachments` | Testattachments_Create Test Run Log Store Attachment |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/testlog` | Testlog_Get Test Run Logs |
| GET | `/{organization}/{project}/_apis/testresults/runs/{runId}/testlogstoreendpoint` | Testlogstoreendpoint_Get Test Log Store Endpoint Details For Run Log |
| POST | `/{organization}/{project}/_apis/testresults/runs/{runId}/testlogstoreendpoint` | Testlogstoreendpoint_Test Log Store Endpoint Details For Run |
| GET | `/{organization}/{project}/_apis/testresults/settings` | Settings_Get |
| PATCH | `/{organization}/{project}/_apis/testresults/settings` | Settings_Update |
| GET | `/{organization}/{project}/_apis/testresults/tags` | Tags_Get Test Tags For Build |
| GET | `/{organization}/{project}/_apis/testresults/tagsummary` | Tagsummary_Get Test Tag Summary For Build |
| GET | `/{organization}/{project}/_apis/testresults/testfailuretype` | Testfailuretype_List |
| POST | `/{organization}/{project}/_apis/testresults/testfailuretype` | Testfailuretype_Create |
| DELETE | `/{organization}/{project}/_apis/testresults/testfailuretype/{failureTypeId}` | Testfailuretype_Delete |
| GET | `/{organization}/{project}/_apis/testresults/testlog` | Testlog_Get Test Logs For Build |
| GET | `/{organization}/{project}/_apis/testresults/testlogstoreendpoint` | Testlogstoreendpoint_Get Test Log Store Endpoint Details For Build Log |
| POST | `/{organization}/{project}/_apis/testresults/testlogstoreendpoint` | Testlogstoreendpoint_Test Log Store Endpoint Details For Build |
| DELETE | `/{organization}/{project}/_apis/testresults/testmethods/workitems` | Workitems_Delete |
| POST | `/{organization}/{project}/_apis/testresults/testmethods/workitems` | Workitems_Add |
| DELETE | `/{organization}/{project}/_apis/testresults/testsettings` | Testsettings_Delete |
| GET | `/{organization}/{project}/_apis/testresults/testsettings` | Testsettings_Get |
| POST | `/{organization}/{project}/_apis/testresults/testsettings` | Testsettings_Create |
| POST | `/{organization}/{project}/_apis/testresults/uploadbuildattachments/{buildId}` | Testattachments_Create Build Attachment In Log Store |

---

## tfvc

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: tfvc.json
- **Endpoint Count**: 15

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/tfvc/changesets/{id}/changes` | Changesets_Get Changeset Changes |
| GET | `/{organization}/_apis/tfvc/changesets/{id}/workItems` | Changesets_Get Changeset Work Items |
| POST | `/{organization}/_apis/tfvc/changesetsbatch` | Changesets_Get Batched Changesets |
| GET | `/{organization}/_apis/tfvc/labels/{labelId}/items` | Labels_Get Label Items |
| GET | `/{organization}/_apis/tfvc/shelvesets` | Shelvesets_Get |
| GET | `/{organization}/_apis/tfvc/shelvesets/changes` | Shelvesets_Get Shelveset Changes |
| GET | `/{organization}/_apis/tfvc/shelvesets/workitems` | Shelvesets_Get Shelveset Work Items |
| GET | `/{organization}/{project}/_apis/tfvc/branches` | Branches_Get Branch Refs |
| GET | `/{organization}/{project}/_apis/tfvc/changesets` | Changesets_Get Changesets |
| POST | `/{organization}/{project}/_apis/tfvc/changesets` | Changesets_Create |
| GET | `/{organization}/{project}/_apis/tfvc/changesets/{id}` | Changesets_Get |
| POST | `/{organization}/{project}/_apis/tfvc/itembatch` | Items_Get Items Batch |
| GET | `/{organization}/{project}/_apis/tfvc/items` | Items_List |
| GET | `/{organization}/{project}/_apis/tfvc/labels` | Labels_List |
| GET | `/{organization}/{project}/_apis/tfvc/labels/{labelId}` | Labels_Get |

---

## tokenAdmin

- **Target Version**: 7.2
- **All Versions**: 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0
- **Spec Files**: tokenAdmin.json
- **Endpoint Count**: 3

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/tokenadmin/personalaccesstokens/{subjectDescriptor}` | Personal Access Tokens_List |
| POST | `/{organization}/_apis/tokenadmin/revocationrules` | Revocation Rules_Create |
| POST | `/{organization}/_apis/tokenadmin/revocations` | Revocations_Revoke Authorizations |

---

## tokenAdministration

- **Target Version**: 5.2
- **All Versions**: 5.0, 5.1, 5.2
- **Spec Files**: tokenAdministration.json
- **Endpoint Count**: 3

| Method | Path | Operation ID |
|--------|------|-------------|
| POST | `/_apis/tokenadministration/tokenlistglobalidentities` | List |
| POST | `/_apis/tokenadministration/tokenpersonalaccesstokens/{subjectDescriptor}` | List |
| POST | `/_apis/tokenadministration/tokenrevocations` | Revoke Authorizations |

---

## tokens

- **Target Version**: 7.2
- **All Versions**: 6.1, 7.0, 7.1, 7.2
- **Spec Files**: tokens.json
- **Endpoint Count**: 4

| Method | Path | Operation ID |
|--------|------|-------------|
| DELETE | `/{organization}/_apis/tokens/pats` | Pats_Revoke |
| GET | `/{organization}/_apis/tokens/pats` | Pats_Get |
| POST | `/{organization}/_apis/tokens/pats` | Pats_Create |
| PUT | `/{organization}/_apis/tokens/pats` | Pats_Update |

---

## wiki

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: wiki.json
- **Endpoint Count**: 15

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/{project}/_apis/wiki/wikis` | Wikis_List |
| POST | `/{organization}/{project}/_apis/wiki/wikis` | Wikis_Create |
| DELETE | `/{organization}/{project}/_apis/wiki/wikis/{wikiIdentifier}` | Wikis_Delete |
| GET | `/{organization}/{project}/_apis/wiki/wikis/{wikiIdentifier}` | Wikis_Get |
| PATCH | `/{organization}/{project}/_apis/wiki/wikis/{wikiIdentifier}` | Wikis_Update |
| PUT | `/{organization}/{project}/_apis/wiki/wikis/{wikiIdentifier}/attachments` | Attachments_Create |
| POST | `/{organization}/{project}/_apis/wiki/wikis/{wikiIdentifier}/pagemoves` | Page Moves_Create |
| DELETE | `/{organization}/{project}/_apis/wiki/wikis/{wikiIdentifier}/pages` | Pages_Delete Page |
| GET | `/{organization}/{project}/_apis/wiki/wikis/{wikiIdentifier}/pages` | Pages_Get Page |
| PUT | `/{organization}/{project}/_apis/wiki/wikis/{wikiIdentifier}/pages` | Pages_Create Or Update |
| DELETE | `/{organization}/{project}/_apis/wiki/wikis/{wikiIdentifier}/pages/{id}` | Pages_Delete Page By Id |
| GET | `/{organization}/{project}/_apis/wiki/wikis/{wikiIdentifier}/pages/{id}` | Pages_Get Page By Id |
| PATCH | `/{organization}/{project}/_apis/wiki/wikis/{wikiIdentifier}/pages/{id}` | Pages_Update |
| GET | `/{organization}/{project}/_apis/wiki/wikis/{wikiIdentifier}/pages/{pageId}/stats` | Page Stats_Get |
| POST | `/{organization}/{project}/_apis/wiki/wikis/{wikiIdentifier}/pagesbatch` | Pages Batch_Get |

---

## wit

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: workItemTracking.json
- **Endpoint Count**: 84

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/_apis/wit/artifactlinktypes` | Artifact Link Types_List |
| GET | `/{organization}/_apis/wit/workitemicons` | Work Item Icons_List |
| GET | `/{organization}/_apis/wit/workitemicons/{icon}` | Work Item Icons_Get |
| GET | `/{organization}/_apis/wit/workitemrelationtypes` | Work Item Relation Types_List |
| GET | `/{organization}/_apis/wit/workitemrelationtypes/{relation}` | Work Item Relation Types_Get |
| GET | `/{organization}/_apis/wit/workitemtransitions` | Work Item Transitions_List |
| GET | `/{organization}/_apis/work/accountmyworkrecentactivity` | Account My Work Recent Activity_List |
| GET | `/{organization}/{project}/_apis/githubconnections` | Github Connections_Get Github Connections |
| GET | `/{organization}/{project}/_apis/githubconnections/{connectionId}/repos` | Github Connections_Get Github Connection Repositories |
| POST | `/{organization}/{project}/_apis/githubconnections/{connectionId}/reposBatch` | Github Connections_Update |
| POST | `/{organization}/{project}/_apis/wit/artifacturiquery` | Artifact Uri Query_Query |
| POST | `/{organization}/{project}/_apis/wit/attachments` | Attachments_Create |
| DELETE | `/{organization}/{project}/_apis/wit/attachments/{id}` | Attachments_Delete |
| GET | `/{organization}/{project}/_apis/wit/attachments/{id}` | Attachments_Get |
| PUT | `/{organization}/{project}/_apis/wit/attachments/{id}` | Attachments_Upload Chunk |
| GET | `/{organization}/{project}/_apis/wit/classificationnodes` | Classification Nodes_Get Root Nodes |
| DELETE | `/{organization}/{project}/_apis/wit/classificationnodes/{structureGroup}/{path}` | Classification Nodes_Delete |
| GET | `/{organization}/{project}/_apis/wit/classificationnodes/{structureGroup}/{path}` | Classification Nodes_Get |
| PATCH | `/{organization}/{project}/_apis/wit/classificationnodes/{structureGroup}/{path}` | Classification Nodes_Update |
| POST | `/{organization}/{project}/_apis/wit/classificationnodes/{structureGroup}/{path}` | Classification Nodes_Create Or Update |
| GET | `/{organization}/{project}/_apis/wit/fields` | Fields_List |
| POST | `/{organization}/{project}/_apis/wit/fields` | Fields_Create |
| DELETE | `/{organization}/{project}/_apis/wit/fields/{fieldNameOrRefName}` | Fields_Delete |
| GET | `/{organization}/{project}/_apis/wit/fields/{fieldNameOrRefName}` | Fields_Get |
| PATCH | `/{organization}/{project}/_apis/wit/fields/{fieldNameOrRefName}` | Fields_Update |
| POST | `/{organization}/{project}/_apis/wit/projectprocessmigration` | Project Process Migration_Migrate Projects Process |
| GET | `/{organization}/{project}/_apis/wit/queries` | Queries_List |
| DELETE | `/{organization}/{project}/_apis/wit/queries/{query}` | Queries_Delete |
| GET | `/{organization}/{project}/_apis/wit/queries/{query}` | Queries_Get |
| PATCH | `/{organization}/{project}/_apis/wit/queries/{query}` | Queries_Update |
| POST | `/{organization}/{project}/_apis/wit/queries/{query}` | Queries_Create |
| POST | `/{organization}/{project}/_apis/wit/queriesbatch` | Queries_Get Queries Batch |
| GET | `/{organization}/{project}/_apis/wit/recyclebin` | Recyclebin_Get Deleted Work Item Shallow References |
| DELETE | `/{organization}/{project}/_apis/wit/recyclebin/{id}` | Recyclebin_Destroy Work Item |
| GET | `/{organization}/{project}/_apis/wit/recyclebin/{id}` | Recyclebin_Get |
| PATCH | `/{organization}/{project}/_apis/wit/recyclebin/{id}` | Recyclebin_Restore Work Item |
| GET | `/{organization}/{project}/_apis/wit/reporting/workItemRevisions/discussions` | Work Item Revisions Discussions_Read Reporting Discussions |
| GET | `/{organization}/{project}/_apis/wit/reporting/workitemlinks` | Reporting Work Item Links_Get |
| GET | `/{organization}/{project}/_apis/wit/reporting/workitemrevisions` | Reporting Work Item Revisions_Read Reporting Revisions Get |
| POST | `/{organization}/{project}/_apis/wit/reporting/workitemrevisions` | Reporting Work Item Revisions_Read Reporting Revisions Post |
| POST | `/{organization}/{project}/_apis/wit/sendmail` | Send Mail_Send Mail |
| GET | `/{organization}/{project}/_apis/wit/tags` | Tags_List |
| DELETE | `/{organization}/{project}/_apis/wit/tags/{tagIdOrName}` | Tags_Delete |
| GET | `/{organization}/{project}/_apis/wit/tags/{tagIdOrName}` | Tags_Get |
| PATCH | `/{organization}/{project}/_apis/wit/tags/{tagIdOrName}` | Tags_Update |
| POST | `/{organization}/{project}/_apis/wit/tempqueries` | Temp Queries_Create |
| GET | `/{organization}/{project}/_apis/wit/workItems/{id}/revisions` | Revisions_List |
| GET | `/{organization}/{project}/_apis/wit/workItems/{id}/revisions/{revisionNumber}` | Revisions_Get |
| GET | `/{organization}/{project}/_apis/wit/workItems/{id}/updates` | Updates_List |
| GET | `/{organization}/{project}/_apis/wit/workItems/{id}/updates/{updateNumber}` | Updates_Get |
| GET | `/{organization}/{project}/_apis/wit/workItems/{workItemId}/comments` | Comments_Get Comments Batch |
| POST | `/{organization}/{project}/_apis/wit/workItems/{workItemId}/comments` | Comments_Add Comment |
| DELETE | `/{organization}/{project}/_apis/wit/workItems/{workItemId}/comments/{commentId}` | Comments_Delete |
| GET | `/{organization}/{project}/_apis/wit/workItems/{workItemId}/comments/{commentId}` | Comments_Get Comment |
| PATCH | `/{organization}/{project}/_apis/wit/workItems/{workItemId}/comments/{commentId}` | Comments_Update Comment |
| GET | `/{organization}/{project}/_apis/wit/workItems/{workItemId}/comments/{commentId}/reactions` | Comments Reactions_List |
| DELETE | `/{organization}/{project}/_apis/wit/workItems/{workItemId}/comments/{commentId}/reactions/{reactionType}` | Comments Reactions_Delete |
| PUT | `/{organization}/{project}/_apis/wit/workItems/{workItemId}/comments/{commentId}/reactions/{reactionType}` | Comments Reactions_Create |
| GET | `/{organization}/{project}/_apis/wit/workItems/{workItemId}/comments/{commentId}/reactions/{reactionType}/users` | Comment Reactions Engaged Users_List |
| GET | `/{organization}/{project}/_apis/wit/workItems/{workItemId}/comments/{commentId}/versions` | Comments Versions_List |
| GET | `/{organization}/{project}/_apis/wit/workItems/{workItemId}/comments/{commentId}/versions/{version}` | Comments Versions_Get |
| GET | `/{organization}/{project}/_apis/wit/workitems` | Work Items_List |
| GET | `/{organization}/{project}/_apis/wit/workitems/${type}` | Work Items_Get Work Item Template |
| POST | `/{organization}/{project}/_apis/wit/workitems/${type}` | Work Items_Create |
| DELETE | `/{organization}/{project}/_apis/wit/workitems/{id}` | Work Items_Delete |
| GET | `/{organization}/{project}/_apis/wit/workitems/{id}` | Work Items_Get Work Item |
| PATCH | `/{organization}/{project}/_apis/wit/workitems/{id}` | Work Items_Update |
| POST | `/{organization}/{project}/_apis/wit/workitemsbatch` | Work Items_Get Work Items Batch |
| POST | `/{organization}/{project}/_apis/wit/workitemsdelete` | Work Items_Delete Work Items |
| GET | `/{organization}/{project}/_apis/wit/workitemtypecategories` | Work Item Type Categories_List |
| GET | `/{organization}/{project}/_apis/wit/workitemtypecategories/{category}` | Work Item Type Categories_Get |
| GET | `/{organization}/{project}/_apis/wit/workitemtypes` | Work Item Types_List |
| GET | `/{organization}/{project}/_apis/wit/workitemtypes/{type}` | Work Item Types_Get |
| GET | `/{organization}/{project}/_apis/wit/workitemtypes/{type}/fields` | Work Item Types Field_List |
| GET | `/{organization}/{project}/_apis/wit/workitemtypes/{type}/fields/{field}` | Work Item Types Field_Get |
| GET | `/{organization}/{project}/_apis/wit/workitemtypes/{type}/states` | Work Item Type States_List |
| GET | `/{organization}/{project}/{team}/_apis/wit/templates` | Templates_List |
| POST | `/{organization}/{project}/{team}/_apis/wit/templates` | Templates_Create |
| DELETE | `/{organization}/{project}/{team}/_apis/wit/templates/{templateId}` | Templates_Delete |
| GET | `/{organization}/{project}/{team}/_apis/wit/templates/{templateId}` | Templates_Get |
| PUT | `/{organization}/{project}/{team}/_apis/wit/templates/{templateId}` | Templates_Replace Template |
| POST | `/{organization}/{project}/{team}/_apis/wit/wiql` | Wiql_Query By Wiql |
| GET | `/{organization}/{project}/{team}/_apis/wit/wiql/{id}` | Wiql_Query By Id |
| HEAD | `/{organization}/{project}/{team}/_apis/wit/wiql/{id}` | Wiql_Get |

---

## work

- **Target Version**: 7.2
- **All Versions**: 4.1, 5.0, 5.1, 5.2, 6.0, 6.1, 7.0, 7.1, 7.2, azure-devops-server-5.0, azure-devops-server-6.0, azure-devops-server-7.0, azure-devops-server-7.1, tfs-4.1
- **Spec Files**: work.json
- **Endpoint Count**: 59

| Method | Path | Operation ID |
|--------|------|-------------|
| GET | `/{organization}/{project}/_apis/work/boardcolumns` | Boardcolumns_List |
| GET | `/{organization}/{project}/_apis/work/boardrows` | Boardrows_List |
| GET | `/{organization}/{project}/_apis/work/iterations/{iterationId}/iterationcapacities` | Iterationcapacities_Get |
| GET | `/{organization}/{project}/_apis/work/plans` | Plans_List |
| POST | `/{organization}/{project}/_apis/work/plans` | Plans_Create |
| DELETE | `/{organization}/{project}/_apis/work/plans/{id}` | Plans_Delete |
| GET | `/{organization}/{project}/_apis/work/plans/{id}` | Plans_Get |
| PUT | `/{organization}/{project}/_apis/work/plans/{id}` | Plans_Update |
| GET | `/{organization}/{project}/_apis/work/plans/{id}/deliverytimeline` | Deliverytimeline_Get |
| GET | `/{organization}/{project}/_apis/work/predefinedqueries` | Predefined Queries_List |
| GET | `/{organization}/{project}/_apis/work/predefinedqueries/{id}` | Predefined Queries_Get |
| GET | `/{organization}/{project}/_apis/work/processconfiguration` | Processconfiguration_Get |
| GET | `/{organization}/{project}/{team}/_apis/work/backlogconfiguration` | Backlogconfiguration_Get |
| GET | `/{organization}/{project}/{team}/_apis/work/backlogs` | Backlogs_List |
| GET | `/{organization}/{project}/{team}/_apis/work/backlogs/{backlogId}/workItems` | Backlogs_Get Backlog Level Work Items |
| GET | `/{organization}/{project}/{team}/_apis/work/backlogs/{id}` | Backlogs_Get Backlog |
| GET | `/{organization}/{project}/{team}/_apis/work/boards` | Boards_List |
| GET | `/{organization}/{project}/{team}/_apis/work/boards/boardparents` | Boardparents_List |
| GET | `/{organization}/{project}/{team}/_apis/work/boards/{board}/boardusersettings` | Boardusersettings_Get |
| PATCH | `/{organization}/{project}/{team}/_apis/work/boards/{board}/boardusersettings` | Boardusersettings_Update |
| GET | `/{organization}/{project}/{team}/_apis/work/boards/{board}/cardrulesettings` | Cardrulesettings_Get |
| PATCH | `/{organization}/{project}/{team}/_apis/work/boards/{board}/cardrulesettings` | Cardrulesettings_Update Board Card Rule Settings |
| GET | `/{organization}/{project}/{team}/_apis/work/boards/{board}/cardsettings` | Cardsettings_Get |
| PUT | `/{organization}/{project}/{team}/_apis/work/boards/{board}/cardsettings` | Cardsettings_Update Board Card Settings |
| GET | `/{organization}/{project}/{team}/_apis/work/boards/{board}/chartimages/{name}` | Chartimages_Get Board Chart Image |
| GET | `/{organization}/{project}/{team}/_apis/work/boards/{board}/charts` | Charts_List |
| GET | `/{organization}/{project}/{team}/_apis/work/boards/{board}/charts/{name}` | Charts_Get |
| PATCH | `/{organization}/{project}/{team}/_apis/work/boards/{board}/charts/{name}` | Charts_Update |
| GET | `/{organization}/{project}/{team}/_apis/work/boards/{board}/columns` | Columns_List |
| PUT | `/{organization}/{project}/{team}/_apis/work/boards/{board}/columns` | Columns_Update |
| GET | `/{organization}/{project}/{team}/_apis/work/boards/{board}/rows` | Rows_List |
| PUT | `/{organization}/{project}/{team}/_apis/work/boards/{board}/rows` | Rows_Update |
| GET | `/{organization}/{project}/{team}/_apis/work/boards/{id}` | Boards_Get |
| PUT | `/{organization}/{project}/{team}/_apis/work/boards/{id}` | Boards_Set Board Options |
| GET | `/{organization}/{project}/{team}/_apis/work/iterations/chartimages/{name}` | Chartimages_Get Iterations Chart Image |
| GET | `/{organization}/{project}/{team}/_apis/work/iterations/{iterationId}/chartimages/{name}` | Chartimages_Get Iteration Chart Image |
| PATCH | `/{organization}/{project}/{team}/_apis/work/iterations/{iterationId}/workitemsorder` | Workitemsorder_Reorder Iteration Work Items |
| PATCH | `/{organization}/{project}/{team}/_apis/work/taskboard/cardrulesettings` | Cardrulesettings_Update Taskboard Card Rule Settings |
| PUT | `/{organization}/{project}/{team}/_apis/work/taskboard/cardsettings` | Cardsettings_Update Taskboard Card Settings |
| GET | `/{organization}/{project}/{team}/_apis/work/taskboardcolumns` | Taskboard Columns_Get |
| PUT | `/{organization}/{project}/{team}/_apis/work/taskboardcolumns` | Taskboard Columns_Update |
| GET | `/{organization}/{project}/{team}/_apis/work/taskboardworkitems/{iterationId}` | Taskboard Work Items_List |
| PATCH | `/{organization}/{project}/{team}/_apis/work/taskboardworkitems/{iterationId}/{workItemId}` | Taskboard Work Items_Update |
| GET | `/{organization}/{project}/{team}/_apis/work/teamsettings` | Teamsettings_Get |
| PATCH | `/{organization}/{project}/{team}/_apis/work/teamsettings` | Teamsettings_Update |
| GET | `/{organization}/{project}/{team}/_apis/work/teamsettings/iterations` | Iterations_List |
| POST | `/{organization}/{project}/{team}/_apis/work/teamsettings/iterations` | Iterations_Post Team Iteration |
| DELETE | `/{organization}/{project}/{team}/_apis/work/teamsettings/iterations/{id}` | Iterations_Delete |
| GET | `/{organization}/{project}/{team}/_apis/work/teamsettings/iterations/{id}` | Iterations_Get |
| GET | `/{organization}/{project}/{team}/_apis/work/teamsettings/iterations/{iterationId}/capacities` | Capacities_Get Capacities With Identity Ref And Totals |
| PUT | `/{organization}/{project}/{team}/_apis/work/teamsettings/iterations/{iterationId}/capacities` | Capacities_Replace Capacities With Identity Ref |
| GET | `/{organization}/{project}/{team}/_apis/work/teamsettings/iterations/{iterationId}/capacities/{teamMemberId}` | Capacities_Get Capacity With Identity Ref |
| PATCH | `/{organization}/{project}/{team}/_apis/work/teamsettings/iterations/{iterationId}/capacities/{teamMemberId}` | Capacities_Update |
| GET | `/{organization}/{project}/{team}/_apis/work/teamsettings/iterations/{iterationId}/teamdaysoff` | Teamdaysoff_Get |
| PATCH | `/{organization}/{project}/{team}/_apis/work/teamsettings/iterations/{iterationId}/teamdaysoff` | Teamdaysoff_Update |
| GET | `/{organization}/{project}/{team}/_apis/work/teamsettings/iterations/{iterationId}/workitems` | Iterations_Get Iteration Work Items |
| GET | `/{organization}/{project}/{team}/_apis/work/teamsettings/teamfieldvalues` | Teamfieldvalues_Get |
| PATCH | `/{organization}/{project}/{team}/_apis/work/teamsettings/teamfieldvalues` | Teamfieldvalues_Update |
| PATCH | `/{organization}/{project}/{team}/_apis/work/workitemsorder` | Workitemsorder_Reorder Backlog Work Items |
