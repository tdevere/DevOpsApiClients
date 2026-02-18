<#
.SYNOPSIS
    Create a new work item in an Azure DevOps project.

.DESCRIPTION
    Calls POST {org}/{project}/_apis/wit/workitems/${type}?api-version=7.2
    Uses JSON Patch (application/json-patch+json) content type.

.PARAMETER Organization
    Azure DevOps organization name. Falls back to $env:AZURE_DEVOPS_ORG.

.PARAMETER ProjectId
    Project name or GUID. Falls back to $env:PROJECT_ID.

.PARAMETER WorkItemType
    Work item type (e.g., Task, Bug, "User Story"). Falls back to $env:WORK_ITEM_TYPE.

.PARAMETER Title
    Title for the new work item.

.PARAMETER Description
    Optional description / repro steps (HTML supported).

.PARAMETER AssignedTo
    Optional display name or email of the assignee.

.PARAMETER Priority
    Optional priority (1–4).

.PARAMETER Pat
    Personal Access Token. Falls back to $env:AZURE_DEVOPS_PAT.
#>

[CmdletBinding()]
param(
    [string]$Organization = $env:AZURE_DEVOPS_ORG,
    [string]$ProjectId    = $env:PROJECT_ID,
    [string]$WorkItemType = $env:WORK_ITEM_TYPE,
    [string]$Title,
    [string]$Description,
    [string]$AssignedTo,
    [int]$Priority,
    [string]$Pat          = $env:AZURE_DEVOPS_PAT
)

# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------
if ([string]::IsNullOrWhiteSpace($Organization)) {
    throw "Organisation is required. Supply -Organization or set `$env:AZURE_DEVOPS_ORG."
}
if ([string]::IsNullOrWhiteSpace($ProjectId)) {
    throw "ProjectId is required. Supply -ProjectId or set `$env:PROJECT_ID."
}
if ([string]::IsNullOrWhiteSpace($WorkItemType)) {
    throw "WorkItemType is required. Supply -WorkItemType or set `$env:WORK_ITEM_TYPE."
}
if ([string]::IsNullOrWhiteSpace($Title)) {
    throw "Title is required. Supply -Title."
}
if ([string]::IsNullOrWhiteSpace($Pat)) {
    throw "PAT is required. Supply -Pat or set `$env:AZURE_DEVOPS_PAT."
}

# ---------------------------------------------------------------------------
# Auth (shared helper) — note special content type for JSON Patch
# ---------------------------------------------------------------------------
. "$PSScriptRoot/../../_shared/AdoAuth.ps1"
$headers = New-AdoAuthHeader -Pat $Pat
$headers['Content-Type'] = 'application/json-patch+json'
Write-Verbose "Creating $WorkItemType in project '$ProjectId'"

# ---------------------------------------------------------------------------
# Build JSON Patch document
# ---------------------------------------------------------------------------
$patchOps = @(
    @{ op = 'add'; path = '/fields/System.Title'; value = $Title }
)

if (-not [string]::IsNullOrWhiteSpace($Description)) {
    $patchOps += @{ op = 'add'; path = '/fields/System.Description'; value = $Description }
}
if (-not [string]::IsNullOrWhiteSpace($AssignedTo)) {
    $patchOps += @{ op = 'add'; path = '/fields/System.AssignedTo'; value = $AssignedTo }
}
if ($Priority -gt 0) {
    $patchOps += @{ op = 'add'; path = '/fields/Microsoft.VSTS.Common.Priority'; value = $Priority }
}

$body = $patchOps | ConvertTo-Json -Depth 5

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
$apiVersion = '7.2'
$uri = "https://dev.azure.com/$Organization/$ProjectId/_apis/wit/workitems/`$$($WorkItemType)?api-version=$apiVersion"

try {
    $result = Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $body -TimeoutSec 30
}
catch {
    $statusCode = $_.Exception.Response.StatusCode.value__
    switch ($statusCode) {
        401 { throw "ERROR: Authentication failed (401). Verify AZURE_DEVOPS_PAT is valid." }
        403 { throw "ERROR: Insufficient permissions (403). Required scope: Work Items (Read & Write)." }
        404 { throw "ERROR: Resource not found (404). Verify org='$Organization', project='$ProjectId', type='$WorkItemType'." }
        400 { throw "ERROR: Bad request (400). Verify work item type '$WorkItemType' exists in project '$ProjectId'." }
        default { throw $_ }
    }
}

# ---------------------------------------------------------------------------
# Version guard
# ---------------------------------------------------------------------------
if (-not $result.id -or -not $result.fields) {
    Write-Warning "Unexpected response shape — the server may not support api-version $apiVersion."
}

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
Write-Output "Work item created: #$($result.id)"
Write-Output ("  Type      : {0}" -f $result.fields.'System.WorkItemType')
Write-Output ("  Title     : {0}" -f $result.fields.'System.Title')
Write-Output ("  State     : {0}" -f $result.fields.'System.State')
if ($result.fields.'System.AssignedTo') {
    Write-Output ("  Assigned  : {0}" -f $result.fields.'System.AssignedTo'.displayName)
}
if ($result.fields.'Microsoft.VSTS.Common.Priority') {
    Write-Output ("  Priority  : {0}" -f $result.fields.'Microsoft.VSTS.Common.Priority')
}
Write-Output ""
$result | ConvertTo-Json -Depth 10
