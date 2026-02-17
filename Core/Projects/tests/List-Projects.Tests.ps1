<#
.SYNOPSIS
    Pester offline unit tests for List-Projects.ps1

.DESCRIPTION
    Mocks Invoke-RestMethod to validate URL construction, auth headers,
    response parsing, and version-guard behaviour without making real API calls.
#>

BeforeAll {
    $ScriptPath = Join-Path $PSScriptRoot '..' 'List-Projects.ps1'
    $FixturePath = Join-Path $PSScriptRoot 'fixtures'
}

Describe 'List-Projects.ps1' -Tag 'Offline', 'Core' {

    Context 'Input validation' {

        It 'Throws when Organisation is empty' {
            {
                & $ScriptPath -Organization '' -Pat 'fakepat'
            } | Should -Throw '*Organisation*'
        }

        It 'Throws when Pat is empty' {
            {
                & $ScriptPath -Organization 'testorg' -Pat ''
            } | Should -Throw '*PAT*'
        }
    }

    Context 'Successful API call (mocked)' {

        BeforeAll {
            $fixture = Get-Content (Join-Path $FixturePath 'list_projects_200.json') -Raw | ConvertFrom-Json
        }

        It 'Calls the correct URL with api-version 7.2-preview.4' {
            Mock Invoke-RestMethod {
                return $fixture
            } -Verifiable

            & $ScriptPath -Organization 'testorg' -Pat 'fakepat1234567890' | Out-Null

            Should -InvokeVerifiable
            Should -Invoke Invoke-RestMethod -Times 1 -Exactly -ParameterFilter {
                $Uri -eq 'https://dev.azure.com/testorg/_apis/projects?api-version=7.2-preview.4' -and
                $Method -eq 'Get'
            }
        }

        It 'Sends correct Authorization header' {
            $expectedAuth = [Convert]::ToBase64String(
                [Text.Encoding]::ASCII.GetBytes(':fakepat1234567890')
            )

            Mock Invoke-RestMethod {
                return $fixture
            }

            & $ScriptPath -Organization 'testorg' -Pat 'fakepat1234567890' | Out-Null

            Should -Invoke Invoke-RestMethod -Times 1 -ParameterFilter {
                $Headers['Authorization'] -eq "Basic $expectedAuth"
            }
        }

        It 'Parses project count from response' {
            Mock Invoke-RestMethod { return $fixture }

            $output = & $ScriptPath -Organization 'testorg' -Pat 'fakepat1234567890'

            # The script writes "Total projects: 3" as the first output
            ($output | Out-String) | Should -Match 'Total projects: 3'
        }
    }

    Context 'Version guard' {

        It 'Writes a warning when response lacks count property' {
            $badResponse = [PSCustomObject]@{ value = @() }

            Mock Invoke-RestMethod { return $badResponse }

            $warnings = & $ScriptPath -Organization 'testorg' -Pat 'fakepat' 3>&1 |
                Where-Object { $_ -is [System.Management.Automation.WarningRecord] }

            $warnings | Should -Not -BeNullOrEmpty
            ($warnings | Out-String) | Should -Match 'Unexpected response'
        }
    }
}
