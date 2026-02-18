<#
.SYNOPSIS
    Pester offline unit tests for List-Definitions.ps1

.DESCRIPTION
    Mocks Invoke-RestMethod to validate URL construction,
    auth header, response parsing, and error handling.
#>

BeforeAll {
    $ScriptPath = Join-Path $PSScriptRoot '..' 'List-Definitions.ps1'
    $FixturePath = Join-Path $PSScriptRoot 'fixtures'
    $ProjectId = 'ProjectAlpha'
}

Describe 'List-Definitions.ps1' -Tag 'Offline', 'Build' {

    Context 'Input validation' {

        It 'Throws when Organisation is empty' {
            {
                & $ScriptPath -Organization '' -ProjectId $ProjectId -Pat 'fakepat'
            } | Should -Throw '*Organisation*'
        }

        It 'Throws when ProjectId is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId '' -Pat 'fakepat'
            } | Should -Throw '*ProjectId*'
        }

        It 'Throws when Pat is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -Pat ''
            } | Should -Throw '*PAT*'
        }
    }

    Context 'Successful API call (mocked)' {

        BeforeAll {
            $fixture = Get-Content (Join-Path $FixturePath 'list_definitions_200.json') -Raw | ConvertFrom-Json
        }

        It 'Calls the correct URL' {
            Mock Invoke-RestMethod { return $fixture } -Verifiable

            & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -Pat 'fakepat1234567890' | Out-Null

            Should -InvokeVerifiable
            Should -Invoke Invoke-RestMethod -Times 1 -Exactly -ParameterFilter {
                $Uri -eq "https://dev.azure.com/testorg/ProjectAlpha/_apis/build/definitions?api-version=7.2" -and
                $Method -eq 'Get'
            }
        }

        It 'Sends correct Authorization header' {
            $expectedAuth = [Convert]::ToBase64String(
                [Text.Encoding]::ASCII.GetBytes(':fakepat1234567890')
            )

            Mock Invoke-RestMethod { return $fixture }

            & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -Pat 'fakepat1234567890' | Out-Null

            Should -Invoke Invoke-RestMethod -Times 1 -ParameterFilter {
                $Headers['Authorization'] -eq "Basic $expectedAuth"
            }
        }

        It 'Outputs definition count' {
            Mock Invoke-RestMethod { return $fixture }

            $output = & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -Pat 'fakepat1234567890'
            $text = $output | Out-String

            $text | Should -Match '2 build definition'
        }
    }

    Context 'HTTP error handling' {

        It 'Throws on 401 (auth failure)' {
            Mock Invoke-RestMethod {
                $ex = [System.Net.WebException]::new('The remote server returned an error: (401) Unauthorized.')
                throw $ex
            }

            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -Pat 'badpat'
            } | Should -Throw
        }
    }
}
