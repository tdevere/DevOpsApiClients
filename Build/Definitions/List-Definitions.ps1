<#
.SYNOPSIS
    List build definitions in an Azure DevOps project.

.DESCRIPTION
    Calls GET {org}/{project}/_apis/build/definitions?api-version=7.2

.PARAMETER Organization
    Azure DevOps organization name. Falls back to $env:AZURE_DEVOPS_ORG.

.PARAMETER ProjectId
    Project name or GUID. Falls back to $env:PROJECT_ID.

.PARAMETER Pat
    Personal Access Token. Falls back to $env:AZURE_DEVOPS_PAT.
#>

[CmdletBinding()]
param(
    [string]$Organization = $env:AZURE_DEVOPS_ORG,
    [string]$ProjectId    = $env:PROJECT_ID,
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
if ([string]::IsNullOrWhiteSpace($Pat)) {
    throw "PAT is required. Supply -Pat or set `$env:AZURE_DEVOPS_PAT."
}

# ---------------------------------------------------------------------------
# Auth (shared helper)
# ---------------------------------------------------------------------------
. "$PSScriptRoot/../../_shared/AdoAuth.ps1"
$headers = New-AdoAuthHeader -Pat $Pat
Write-Verbose "Listing build definitions for project '$ProjectId' in org '$Organization'"

# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------
$apiVersion = '7.2'
$uri = "https://dev.azure.com/$Organization/$ProjectId/_apis/build/definitions?api-version=$apiVersion"

try {
    $result = Invoke-RestMethod -Uri $uri -Method Get -Headers $headers -TimeoutSec 30
}
catch {
    $statusCode = $_.Exception.Response.StatusCode.value__
    switch ($statusCode) {
        401 { throw "ERROR: Authentication failed (401). Verify AZURE_DEVOPS_PAT is valid." }
        403 { throw "ERROR: Insufficient permissions (403). Required scope: Build (Read)." }
        404 { throw "ERROR: Resource not found (404). Verify org='$Organization' and project='$ProjectId'." }
        default { throw $_ }
    }
}

# ---------------------------------------------------------------------------
# Version guard
# ---------------------------------------------------------------------------
if (-not $result.value) {
    Write-Warning "Unexpected response shape — the server may not support api-version $apiVersion."
}

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
$definitions = $result.value
Write-Output "Found $($result.count) build definition(s):"
Write-Output ""
foreach ($defn in $definitions) {
    Write-Output ("  [{0}] {1}" -f $defn.id, $defn.name)
    Write-Output ("       Path: {0}  |  Status: {1}" -f $defn.path, $defn.queueStatus)
    Write-Output ("       Author: {0}" -f $defn.authoredBy.displayName)
    Write-Output ""
}

$result | ConvertTo-Json -Depth 10
