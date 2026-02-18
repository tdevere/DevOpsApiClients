<#
.SYNOPSIS
    Get a single Azure DevOps work item by ID.

.DESCRIPTION
    Calls  GET {org}/{project}/_apis/wit/workitems/{id}?api-version=7.2
    Uses Basic Auth with a PAT stored in $env:AZURE_DEVOPS_PAT.

.LINK
    https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/work-items/get-work-item?view=azure-devops-rest-7.2
#>

[CmdletBinding()]
param (
    [Parameter()]
    [string]$Organization = $env:AZURE_DEVOPS_ORG,

    [Parameter()]
    [string]$ProjectId = $env:PROJECT_ID,

    [Parameter()]
    [string]$WorkItemId = $env:WORK_ITEM_ID,

    [Parameter()]
    [string]$Pat = $env:AZURE_DEVOPS_PAT
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

#--- Validate inputs --------------------------------------------------------
if ([string]::IsNullOrWhiteSpace($Organization)) {
    throw "Organisation is required. Set `$env:AZURE_DEVOPS_ORG or pass -Organization."
}
if ([string]::IsNullOrWhiteSpace($ProjectId)) {
    throw "ProjectId is required. Set `$env:PROJECT_ID or pass -ProjectId."
}
if ([string]::IsNullOrWhiteSpace($WorkItemId)) {
    throw "WorkItemId is required. Set `$env:WORK_ITEM_ID or pass -WorkItemId."
}
if ([string]::IsNullOrWhiteSpace($Pat)) {
    throw "PAT is required. Set `$env:AZURE_DEVOPS_PAT or pass -Pat."
}

#--- API version ------------------------------------------------------------
$ApiVersion = '7.2'

#--- Auth (shared helper) ---------------------------------------------------
. "$PSScriptRoot/../../_shared/AdoAuth.ps1"
$headers = New-AdoAuthHeader -Pat $Pat
Write-Verbose "Getting work item #$WorkItemId in project '$ProjectId'"

#--- Call the API -----------------------------------------------------------
$uri = "https://dev.azure.com/$Organization/$ProjectId/_apis/wit/workitems/${WorkItemId}?api-version=$ApiVersion"

Write-Verbose "GET $uri"

$response = Invoke-RestMethod -Uri $uri -Method Get -Headers $headers -ContentType 'application/json'

#--- Version guard ----------------------------------------------------------
if (-not $response.id) {
    Write-Warning "Unexpected response — the server may not support api-version $ApiVersion."
}

#--- Output -----------------------------------------------------------------
$fields = $response.fields
[PSCustomObject]@{
    Id           = $response.id
    Rev          = $response.rev
    Title        = $fields.'System.Title'
    State        = $fields.'System.State'
    WorkItemType = $fields.'System.WorkItemType'
    AssignedTo   = $fields.'System.AssignedTo'.displayName
    AreaPath     = $fields.'System.AreaPath'
    IterationPath = $fields.'System.IterationPath'
    Priority     = $fields.'Microsoft.VSTS.Common.Priority'
    URL          = $response.url
} | Format-List
