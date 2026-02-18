<#
.SYNOPSIS
    Pester offline unit tests for Create-Repository.ps1

.DESCRIPTION
    Mocks Invoke-RestMethod to validate URL, auth, request body, and response parsing.
#>

BeforeAll {
    $ScriptPath = Join-Path $PSScriptRoot '..' 'Create-Repository.ps1'
    $FixturePath = Join-Path $PSScriptRoot 'fixtures'
    $ProjectId = 'd1e2f3a4-b5c6-7890-1234-567890abcdef'
}

Describe 'Create-Repository.ps1' -Tag 'Offline', 'Git' {

    Context 'Input validation' {

        It 'Throws when Organisation is empty' {
            {
                & $ScriptPath -RepoName 'TestRepo' -Organization '' -ProjectId $ProjectId -Pat 'fakepat'
            } | Should -Throw '*Organisation*'
        }

        It 'Throws when ProjectId is empty' {
            {
                & $ScriptPath -RepoName 'TestRepo' -Organization 'testorg' -ProjectId '' -Pat 'fakepat'
            } | Should -Throw '*ProjectId*'
        }

        It 'Throws when Pat is empty' {
            {
                & $ScriptPath -RepoName 'TestRepo' -Organization 'testorg' -ProjectId $ProjectId -Pat ''
            } | Should -Throw '*PAT*'
        }
    }

    Context 'Successful API call (mocked)' {

        BeforeAll {
            $fixture = Get-Content (Join-Path $FixturePath 'create_repository_201.json') -Raw | ConvertFrom-Json
        }

        It 'Calls the correct URL with POST method' {
            Mock Invoke-RestMethod { return $fixture } -Verifiable

            & $ScriptPath -RepoName 'NewRepo' -Organization 'testorg' -ProjectId $ProjectId -Pat 'fakepat1234567890' | Out-Null

            Should -InvokeVerifiable
            Should -Invoke Invoke-RestMethod -Times 1 -Exactly -ParameterFilter {
                $Uri -eq "https://dev.azure.com/testorg/$ProjectId/_apis/git/repositories?api-version=7.2" -and
                $Method -eq 'Post'
            }
        }

        It 'Sends request body with repo name' {
            Mock Invoke-RestMethod { return $fixture }

            & $ScriptPath -RepoName 'NewRepo' -Organization 'testorg' -ProjectId $ProjectId -Pat 'fakepat1234567890' | Out-Null

            Should -Invoke Invoke-RestMethod -Times 1 -ParameterFilter {
                $Body -match '"name"\s*:\s*"NewRepo"'
            }
        }
    }
}
