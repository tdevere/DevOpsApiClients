<#
.SYNOPSIS
    Update an Azure DevOps project (name, description, or visibility).

.DESCRIPTION
    Calls  PATCH {org}/_apis/projects/{projectId}?api-version=7.2-preview.4
    Uses Basic Auth with a PAT stored in $env:AZURE_DEVOPS_PAT.

    The Update Projects API is an async operation. This script queues the
    update and returns the operation reference.  Poll the operation URL to
    track completion.

.LINK
    https://learn.microsoft.com/en-us/rest/api/azure/devops/core/projects/update?view=azure-devops-rest-7.2
#>

[CmdletBinding()]
param (
    [Parameter()]
    [string]$Organization = $env:AZURE_DEVOPS_ORG,

    [Parameter()]
    [string]$ProjectId = $env:PROJECT_ID,

    [Parameter()]
    [string]$Pat = $env:AZURE_DEVOPS_PAT,

    [Parameter()]
    [string]$NewName,

    [Parameter()]
    [string]$NewDescription,

    [Parameter()]
    [ValidateSet('private', 'public')]
    [string]$NewVisibility
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
if ([string]::IsNullOrWhiteSpace($NewName) -and
    [string]::IsNullOrWhiteSpace($NewDescription) -and
    [string]::IsNullOrWhiteSpace($NewVisibility)) {
    throw "Provide at least one update parameter: -NewName, -NewDescription, or -NewVisibility."
}

#--- API version check ------------------------------------------------------
$ApiVersion = '7.2-preview.4'

#--- Build auth header ------------------------------------------------------
$base64Auth = [Convert]::ToBase64String(
    [Text.Encoding]::ASCII.GetBytes(":$Pat")
)
$headers = @{
    Authorization  = "Basic $base64Auth"
    'Content-Type' = 'application/json'
}

#--- Build request body -----------------------------------------------------
$body = @{}
if ($NewName)        { $body['name']        = $NewName }
if ($NewDescription) { $body['description'] = $NewDescription }
if ($NewVisibility)  { $body['visibility']  = $NewVisibility }

$jsonBody = $body | ConvertTo-Json -Depth 5

#--- Call the API -----------------------------------------------------------
$uri = "https://dev.azure.com/$Organization/_apis/projects/${ProjectId}?api-version=$ApiVersion"

Write-Verbose "PATCH $uri"
Write-Verbose "Body: $jsonBody"

$response = Invoke-RestMethod -Uri $uri -Method Patch -Headers $headers -Body $jsonBody

#--- Version guard ----------------------------------------------------------
if (-not $response.id) {
    Write-Warning "Unexpected response — the server may not support api-version $ApiVersion."
}

#--- Output -----------------------------------------------------------------
Write-Output "Update operation queued."
[PSCustomObject]@{
    OperationId = $response.id
    Status      = $response.status
    URL         = $response.url
} | Format-List
