<#
.SYNOPSIS
    List all Git repositories in an Azure DevOps organisation.

.DESCRIPTION
    Calls  GET {org}/_apis/git/repositories?api-version=7.2
    Uses Basic Auth with a PAT stored in $env:AZURE_DEVOPS_PAT.

.LINK
    https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories/list?view=azure-devops-rest-7.2
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

#--- API version ------------------------------------------------------------
$ApiVersion = '7.2'

#--- Build auth header ------------------------------------------------------
$base64Auth = [Convert]::ToBase64String(
    [Text.Encoding]::ASCII.GetBytes(":$Pat")
)
$headers = @{
    Authorization = "Basic $base64Auth"
}

#--- Call the API -----------------------------------------------------------
$uri = "https://dev.azure.com/$Organization/_apis/git/repositories?api-version=$ApiVersion"

Write-Verbose "GET $uri"

$response = Invoke-RestMethod -Uri $uri -Method Get -Headers $headers -ContentType 'application/json'

#--- Version guard ----------------------------------------------------------
if ($response.PSObject.Properties.Name -notcontains 'count') {
    Write-Warning "Unexpected response shape — the server may not support api-version $ApiVersion."
}

#--- Output -----------------------------------------------------------------
Write-Output "Total repositories: $($response.count)"
$response.value | ForEach-Object {
    [PSCustomObject]@{
        Id            = $_.id
        Name          = $_.name
        Project       = $_.project.name
        DefaultBranch = $_.defaultBranch
        Size          = $_.size
        IsDisabled    = $_.isDisabled
    }
} | Format-Table -AutoSize
