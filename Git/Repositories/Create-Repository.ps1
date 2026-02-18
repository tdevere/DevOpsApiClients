<#
.SYNOPSIS
    Create a new Azure DevOps Git repository.

.DESCRIPTION
    Calls  POST {org}/{project}/_apis/git/repositories?api-version=7.2
    Uses Basic Auth with a PAT stored in $env:AZURE_DEVOPS_PAT.

.LINK
    https://learn.microsoft.com/en-us/rest/api/azure/devops/git/repositories/create?view=azure-devops-rest-7.2
#>

[CmdletBinding()]
param (
    [Parameter(Mandatory)]
    [string]$RepoName,

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

#--- API version ------------------------------------------------------------
$ApiVersion = '7.2'

#--- Auth (shared helper) ---------------------------------------------------
. "$PSScriptRoot/../../_shared/AdoAuth.ps1"
$headers = New-AdoAuthHeader -Pat $Pat
Write-Verbose "Creating repository '$RepoName' in project '$ProjectId'"

#--- Build request body -----------------------------------------------------
$body = @{
    name    = $RepoName
    project = @{
        id = $ProjectId
    }
} | ConvertTo-Json -Depth 3

#--- Call the API -----------------------------------------------------------
$uri = "https://dev.azure.com/$Organization/$ProjectId/_apis/git/repositories?api-version=$ApiVersion"

Write-Verbose "POST $uri"

$response = Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $body -ContentType 'application/json'

#--- Version guard ----------------------------------------------------------
if (-not $response.id) {
    Write-Warning "Unexpected response — the server may not support api-version $ApiVersion."
}

#--- Output -----------------------------------------------------------------
Write-Host "Repository created: $($response.name)"
[PSCustomObject]@{
    Id            = $response.id
    Name          = $response.name
    Project       = $response.project.name
    RemoteUrl     = $response.remoteUrl
    SshUrl        = $response.sshUrl
    WebUrl        = $response.webUrl
} | Format-List
