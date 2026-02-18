<#
.SYNOPSIS
    Delete an Azure DevOps Git repository.

.DESCRIPTION
    Calls  DELETE {org}/{project}/_apis/git/repositories/{repositoryId}?api-version=7.2
    Uses Basic Auth with a PAT stored in $env:AZURE_DEVOPS_PAT.
    Returns 204 No Content on success.

.LINK
    https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories/delete?view=azure-devops-rest-7.2
#>

[CmdletBinding()]
param (
    [Parameter()]
    [string]$Organization = $env:AZURE_DEVOPS_ORG,

    [Parameter()]
    [string]$ProjectId = $env:PROJECT_ID,

    [Parameter()]
    [string]$RepositoryId = $env:REPO_ID,

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
if ([string]::IsNullOrWhiteSpace($RepositoryId)) {
    throw "RepositoryId is required. Set `$env:REPO_ID or pass -RepositoryId."
}
if ([string]::IsNullOrWhiteSpace($Pat)) {
    throw "PAT is required. Set `$env:AZURE_DEVOPS_PAT or pass -Pat."
}

#--- API version ------------------------------------------------------------
$ApiVersion = '7.2'

#--- Auth (shared helper) ---------------------------------------------------
. "$PSScriptRoot/../../_shared/AdoAuth.ps1"
$headers = New-AdoAuthHeader -Pat $Pat
Write-Verbose "Deleting repository '$RepositoryId' from project '$ProjectId'"

#--- Call the API -----------------------------------------------------------
$uri = "https://dev.azure.com/$Organization/$ProjectId/_apis/git/repositories/${RepositoryId}?api-version=$ApiVersion"

Write-Verbose "DELETE $uri"

# Invoke-RestMethod for 204 returns $null; use Invoke-WebRequest to check status
$response = Invoke-WebRequest -Uri $uri -Method Delete -Headers $headers -ContentType 'application/json' -UseBasicParsing

#--- Output -----------------------------------------------------------------
if ($response.StatusCode -eq 204) {
    Write-Host "Repository $RepositoryId deleted successfully."
} else {
    Write-Warning "Unexpected status code: $($response.StatusCode)"
}
