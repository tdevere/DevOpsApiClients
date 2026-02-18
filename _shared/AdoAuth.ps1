<#
.SYNOPSIS
    Shared authentication helpers for Azure DevOps API clients.

.DESCRIPTION
    Provides PAT-based Basic Auth header construction and credential validation.
    Source this module: . $PSScriptRoot/../../_shared/AdoAuth.ps1
#>

function New-AdoAuthHeader {
    <#
    .SYNOPSIS
        Build HTTP headers for Azure DevOps Basic Auth.
    .PARAMETER Pat
        The Personal Access Token.
    .OUTPUTS
        Hashtable with Authorization and Content-Type headers.
    #>
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [string]$Pat
    )

    $base64Auth = [Convert]::ToBase64String(
        [Text.Encoding]::ASCII.GetBytes(":$Pat")
    )
    return @{
        Authorization = "Basic $base64Auth"
    }
}

function Assert-AdoEnv {
    <#
    .SYNOPSIS
        Validate that required environment variables / parameters are non-empty.
    .PARAMETER Name
        The human-readable parameter name.
    .PARAMETER Value
        The value to check.
    #>
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [string]$Name,
        [Parameter(Mandatory)]
        [AllowEmptyString()]
        [string]$Value
    )

    if ([string]::IsNullOrWhiteSpace($Value)) {
        throw "$Name is required. Set the corresponding environment variable or pass the parameter."
    }
}

function Get-AdoRedactedPat {
    <#
    .SYNOPSIS
        Redact a PAT for safe logging — show only the first 4 characters.
    #>
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [string]$Pat
    )

    if ($Pat.Length -le 4) { return "****" }
    return $Pat.Substring(0, 4) + "****..."
}
