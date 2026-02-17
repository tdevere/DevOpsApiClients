<#
.SYNOPSIS
    Get a single Azure DevOps project by ID or name.

.DESCRIPTION
    Calls  GET {org}/_apis/projects/{projectId}?api-version=7.2-preview.4
    Uses Basic Auth with a PAT stored in $env:AZURE_DEVOPS_PAT.

.LINK
    https://learn.microsoft.com/en-us/rest/api/azure/devops/core/projects/get?view=azure-devops-rest-7.2
#>

[CmdletBinding()]
param (
    [Parameter()]
    [string]$Organization = $env:AZURE_DEVOPS_ORG,

    [Parameter()]
    [string]$ProjectId = $env:PROJECT_ID,

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
if ([string]::IsNullOrWhiteSpace($Pat)) {
    throw "PAT is required. Set `$env:AZURE_DEVOPS_PAT or pass -Pat."
}

#--- API version check ------------------------------------------------------
$ApiVersion = '7.2-preview.4'

#--- Build auth header ------------------------------------------------------
$base64Auth = [Convert]::ToBase64String(
    [Text.Encoding]::ASCII.GetBytes(":$Pat")
)
$headers = @{
    Authorization = "Basic $base64Auth"
}

#--- Call the API -----------------------------------------------------------
$uri = "https://dev.azure.com/$Organization/_apis/projects/${ProjectId}?api-version=$ApiVersion"

Write-Verbose "GET $uri"

$response = Invoke-RestMethod -Uri $uri -Method Get -Headers $headers -ContentType 'application/json'

#--- Version guard ----------------------------------------------------------
if (-not $response.id) {
    Write-Warning "Unexpected response — the server may not support api-version $ApiVersion."
}

#--- Output -----------------------------------------------------------------
[PSCustomObject]@{
    Id          = $response.id
    Name        = $response.name
    Description = $response.description
    State       = $response.state
    Revision    = $response.revision
    Visibility  = $response.visibility
    URL         = $response.url
} | Format-List
