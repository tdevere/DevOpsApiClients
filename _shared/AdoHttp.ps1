<#
.SYNOPSIS
    Shared HTTP client helpers for Azure DevOps API clients.

.DESCRIPTION
    Provides standardised request execution, URL construction,
    error handling, and version guards.
    Source this module: . $PSScriptRoot/../../_shared/AdoHttp.ps1
#>

function New-AdoUrl {
    <#
    .SYNOPSIS
        Build a full Azure DevOps REST API URL.
    .PARAMETER Organization
        The ADO org name.
    .PARAMETER Path
        The API path segment (e.g., '_apis/projects').
    .PARAMETER ApiVersion
        The api-version query parameter value.
    .PARAMETER Project
        Optional project scope in the URL.
    .PARAMETER BaseHost
        Hostname (default 'dev.azure.com'; override for vssps.dev.azure.com etc.).
    #>
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [string]$Organization,
        [Parameter(Mandatory)]
        [string]$Path,
        [Parameter(Mandatory)]
        [string]$ApiVersion,
        [Parameter()]
        [string]$Project,
        [Parameter()]
        [string]$BaseHost = 'dev.azure.com'
    )

    $base = "https://${BaseHost}/$Organization"
    if (-not [string]::IsNullOrWhiteSpace($Project)) {
        $base = "$base/$Project"
    }
    $separator = if ($Path -match '\?') { '&' } else { '?' }
    return "${base}/${Path}${separator}api-version=${ApiVersion}"
}

function Invoke-AdoRestMethod {
    <#
    .SYNOPSIS
        Execute an HTTP request against Azure DevOps with standard error handling.
    .PARAMETER Uri
        The full request URL.
    .PARAMETER Method
        The HTTP method.
    .PARAMETER Headers
        The request headers hashtable.
    .PARAMETER Body
        Optional JSON body string for POST/PATCH/PUT.
    .PARAMETER ExpectedStatusCode
        If set, use Invoke-WebRequest and accept this specific status code.
    #>
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [string]$Uri,
        [Parameter(Mandatory)]
        [string]$Method,
        [Parameter(Mandatory)]
        [hashtable]$Headers,
        [Parameter()]
        [string]$Body,
        [Parameter()]
        [int]$ExpectedStatusCode
    )

    try {
        if ($ExpectedStatusCode) {
            $params = @{
                Uri         = $Uri
                Method      = $Method
                Headers     = $Headers
                ContentType = 'application/json'
                UseBasicParsing = $true
            }
            if (-not [string]::IsNullOrWhiteSpace($Body)) {
                $params['Body'] = $Body
            }
            $response = Invoke-WebRequest @params
            if ($response.StatusCode -ne $ExpectedStatusCode) {
                Write-Warning "Expected HTTP $ExpectedStatusCode but got $($response.StatusCode)."
            }
            return $response
        }
        else {
            $params = @{
                Uri         = $Uri
                Method      = $Method
                Headers     = $Headers
                ContentType = 'application/json'
            }
            if (-not [string]::IsNullOrWhiteSpace($Body)) {
                $params['Body'] = $Body
            }
            return Invoke-RestMethod @params
        }
    }
    catch {
        $ex = $_
        $statusCode = 0
        if ($ex.Exception -is [System.Net.WebException]) {
            $webResponse = $ex.Exception.Response
            if ($webResponse) {
                $statusCode = [int]$webResponse.StatusCode
            }
        }

        switch ($statusCode) {
            401 { Write-Error "Authentication failed (HTTP 401). Verify AZURE_DEVOPS_PAT is valid and not expired. URL: $Uri" }
            403 { Write-Error "Insufficient permissions (HTTP 403). Check PAT scopes. URL: $Uri" }
            404 { Write-Error "Resource not found (HTTP 404). Verify organisation and resource identifiers. URL: $Uri" }
            429 { Write-Warning "Rate limited (HTTP 429). Retry after a delay. URL: $Uri" }
            default {
                if ($statusCode -ge 500) {
                    Write-Error "Server error (HTTP $statusCode). Check https://status.dev.azure.com. URL: $Uri"
                }
                else {
                    throw $ex
                }
            }
        }
    }
}

function Assert-AdoVersionGuard {
    <#
    .SYNOPSIS
        Validate the response shape matches expectations for the API version.
    .PARAMETER Response
        The parsed response object.
    .PARAMETER RequiredProperties
        Array of property names that must exist.
    .PARAMETER ApiVersion
        The API version string for the warning message.
    #>
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        $Response,
        [Parameter(Mandatory)]
        [string[]]$RequiredProperties,
        [Parameter(Mandatory)]
        [string]$ApiVersion
    )

    foreach ($prop in $RequiredProperties) {
        if ($Response.PSObject.Properties.Name -notcontains $prop) {
            Write-Warning "Unexpected response shape — missing '$prop'. The server may not support api-version $ApiVersion."
            return
        }
    }
}
