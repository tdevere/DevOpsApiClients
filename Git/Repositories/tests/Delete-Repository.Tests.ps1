<#
.SYNOPSIS
    Pester offline unit tests for Delete-Repository.ps1

.DESCRIPTION
    Mocks Invoke-WebRequest to validate URL, auth, and 204 handling.
#>

BeforeAll {
    $ScriptPath = Join-Path $PSScriptRoot '..' 'Delete-Repository.ps1'
    $FixturePath = Join-Path $PSScriptRoot 'fixtures'
    $RepoGuid = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
    $ProjectId = 'ProjectAlpha'
}

Describe 'Delete-Repository.ps1' -Tag 'Offline', 'Git' {

    Context 'Input validation' {

        It 'Throws when Organisation is empty' {
            {
                & $ScriptPath -Organization '' -ProjectId $ProjectId -RepositoryId $RepoGuid -Pat 'fakepat'
            } | Should -Throw '*Organisation*'
        }

        It 'Throws when ProjectId is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId '' -RepositoryId $RepoGuid -Pat 'fakepat'
            } | Should -Throw '*ProjectId*'
        }

        It 'Throws when RepositoryId is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -RepositoryId '' -Pat 'fakepat'
            } | Should -Throw '*RepositoryId*'
        }

        It 'Throws when Pat is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -RepositoryId $RepoGuid -Pat ''
            } | Should -Throw '*PAT*'
        }
    }

    Context 'Successful API call (mocked)' {

        It 'Calls the correct URL with DELETE method and returns 204' {
            $mockResponse = [PSCustomObject]@{ StatusCode = 204; Content = '' }
            Mock Invoke-WebRequest { return $mockResponse } -Verifiable

            & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -RepositoryId $RepoGuid -Pat 'fakepat1234567890' | Out-Null

            Should -InvokeVerifiable
            Should -Invoke Invoke-WebRequest -Times 1 -Exactly -ParameterFilter {
                $Uri -eq "https://dev.azure.com/testorg/ProjectAlpha/_apis/git/repositories/${RepoGuid}?api-version=7.2" -and
                $Method -eq 'Delete'
            }
        }
    }

    Context 'HTTP error handling' {

        It 'Throws on 404 (repository not found)' {
            Mock Invoke-WebRequest {
                $ex = [System.Net.WebException]::new('The remote server returned an error: (404) Not Found.')
                throw $ex
            }

            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -RepositoryId 'NonExistent' -Pat 'fakepat'
            } | Should -Throw
        }
    }
}
