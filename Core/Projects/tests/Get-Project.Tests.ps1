<#
.SYNOPSIS
    Pester offline unit tests for Get-Project.ps1

.DESCRIPTION
    Mocks Invoke-RestMethod to validate URL construction with project ID,
    auth headers, response parsing, and error handling.
#>

BeforeAll {
    $ScriptPath = Join-Path $PSScriptRoot '..' 'Get-Project.ps1'
    $FixturePath = Join-Path $PSScriptRoot 'fixtures'
    $ProjectGuid = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
}

Describe 'Get-Project.ps1' -Tag 'Offline', 'Core' {

    Context 'Input validation' {

        It 'Throws when Organisation is empty' {
            {
                & $ScriptPath -Organization '' -ProjectId $ProjectGuid -Pat 'fakepat'
            } | Should -Throw '*Organisation*'
        }

        It 'Throws when ProjectId is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId '' -Pat 'fakepat'
            } | Should -Throw '*ProjectId*'
        }

        It 'Throws when Pat is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectGuid -Pat ''
            } | Should -Throw '*PAT*'
        }
    }

    Context 'Successful API call (mocked)' {

        BeforeAll {
            $fixture = Get-Content (Join-Path $FixturePath 'get_project_200.json') -Raw | ConvertFrom-Json
        }

        It 'Calls the correct URL including project ID' {
            Mock Invoke-RestMethod { return $fixture } -Verifiable

            & $ScriptPath -Organization 'testorg' -ProjectId $ProjectGuid -Pat 'fakepat1234567890' | Out-Null

            Should -InvokeVerifiable
            Should -Invoke Invoke-RestMethod -Times 1 -Exactly -ParameterFilter {
                $Uri -eq "https://dev.azure.com/testorg/_apis/projects/${ProjectGuid}?api-version=7.2-preview.4" -and
                $Method -eq 'Get'
            }
        }

        It 'Sends correct Authorization header' {
            $expectedAuth = [Convert]::ToBase64String(
                [Text.Encoding]::ASCII.GetBytes(':fakepat1234567890')
            )

            Mock Invoke-RestMethod { return $fixture }

            & $ScriptPath -Organization 'testorg' -ProjectId $ProjectGuid -Pat 'fakepat1234567890' | Out-Null

            Should -Invoke Invoke-RestMethod -Times 1 -ParameterFilter {
                $Headers['Authorization'] -eq "Basic $expectedAuth"
            }
        }

        It 'Outputs project details with expected fields' {
            Mock Invoke-RestMethod { return $fixture }

            $output = & $ScriptPath -Organization 'testorg' -ProjectId $ProjectGuid -Pat 'fakepat1234567890'
            $text = $output | Out-String

            $text | Should -Match 'ProjectAlpha'
            $text | Should -Match 'wellFormed'
        }
    }

    Context 'Version guard' {

        It 'Throws when response lacks id property (strict mode)' {
            $badResponse = [PSCustomObject]@{ name = 'Broken' }

            Mock Invoke-RestMethod { return $badResponse }

            # In strict mode, accessing .id on an object without that property throws
            { & $ScriptPath -Organization 'testorg' -ProjectId $ProjectGuid -Pat 'fakepat' } | Should -Throw '*id*'
        }
    }

    Context 'HTTP error handling' {

        It 'Throws on 404 (project not found)' {
            Mock Invoke-RestMethod {
                $ex = [System.Net.WebException]::new('The remote server returned an error: (404) Not Found.')
                throw $ex
            }

            {
                & $ScriptPath -Organization 'testorg' -ProjectId 'NonExistent' -Pat 'fakepat'
            } | Should -Throw
        }
    }
}
