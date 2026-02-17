<#
.SYNOPSIS
    List all projects in an Azure DevOps organisation.

.DESCRIPTION
    Calls  GET {org}/_apis/projects?api-version=7.2-preview.4
    Uses Basic Auth with a PAT stored in $env:AZURE_DEVOPS_PAT.

.LINK
    https://learn.microsoft.com/en-us/rest/api/azure/devops/core/projects/list?view=azure-devops-rest-7.2
#>

[CmdletBinding()]
param (
    [Parameter()]
    [string]$Organization = $env:AZURE_DEVOPS_ORG,

    [Parameter()]
    [string]$Pat = $env:AZURE_DEVOPS_PAT
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

#--- Validate inputs --------------------------------------------------------
if ([string]::IsNullOrWhiteSpace($Organization)) {
    throw "Organisation is required. Set `$env:AZURE_DEVOPS_ORG or pass -Organization."
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
$uri = "https://dev.azure.com/$Organization/_apis/projects?api-version=$ApiVersion"

Write-Verbose "GET $uri"

$response = Invoke-RestMethod -Uri $uri -Method Get -Headers $headers -ContentType 'application/json'

#--- Version guard ----------------------------------------------------------
# Validate that the server responded with the expected API version family.
if ($response.PSObject.Properties.Name -notcontains 'count') {
    Write-Warning "Unexpected response shape — the server may not support api-version $ApiVersion."
}

#--- Output -----------------------------------------------------------------
Write-Output "Total projects: $($response.count)"
$response.value | ForEach-Object {
    [PSCustomObject]@{
        Id    = $_.id
        Name  = $_.name
        State = $_.state
        URL   = $_.url
    }
} | Format-Table -AutoSize
