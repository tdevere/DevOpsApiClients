<#
.SYNOPSIS
    Pester offline unit tests for List-Repositories.ps1

.DESCRIPTION
    Mocks Invoke-RestMethod to validate URL construction, auth headers,
    response parsing, and version-guard behaviour without making real API calls.
#>

BeforeAll {
    $ScriptPath = Join-Path $PSScriptRoot '..' 'List-Repositories.ps1'
    $FixturePath = Join-Path $PSScriptRoot 'fixtures'
}

Describe 'List-Repositories.ps1' -Tag 'Offline', 'Git' {

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
            $fixture = Get-Content (Join-Path $FixturePath 'list_repositories_200.json') -Raw | ConvertFrom-Json
        }

        It 'Calls the correct URL with api-version 7.2' {
            Mock Invoke-RestMethod {
                return $fixture
            } -Verifiable

            & $ScriptPath -Organization 'testorg' -Pat 'fakepat1234567890' | Out-Null

            Should -InvokeVerifiable
            Should -Invoke Invoke-RestMethod -Times 1 -Exactly -ParameterFilter {
                $Uri -eq 'https://dev.azure.com/testorg/_apis/git/repositories?api-version=7.2' -and
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

        It 'Parses repository count from response' {
            Mock Invoke-RestMethod { return $fixture }

            $output = & $ScriptPath -Organization 'testorg' -Pat 'fakepat1234567890'

            ($output | Out-String) | Should -Match 'Total repositories: 3'
        }

        It 'Outputs repository names' {
            Mock Invoke-RestMethod { return $fixture }

            $output = & $ScriptPath -Organization 'testorg' -Pat 'fakepat1234567890'
            $text = $output | Out-String

            $text | Should -Match 'ContosoRepo'
            $text | Should -Match 'WidgetService'
            $text | Should -Match 'InfraAsCode'
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
