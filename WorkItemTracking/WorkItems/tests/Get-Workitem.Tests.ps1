<#
.SYNOPSIS
    Pester offline unit tests for Get-WorkItem.ps1

.DESCRIPTION
    Mocks Invoke-RestMethod to validate URL construction with project and work item ID,
    auth headers, response parsing, and error handling.
#>

BeforeAll {
    $ScriptPath = Join-Path $PSScriptRoot '..' 'Get-WorkItem.ps1'
    $FixturePath = Join-Path $PSScriptRoot 'fixtures'
    $WorkItemId = '42'
    $ProjectId = 'ProjectAlpha'
}

Describe 'Get-WorkItem.ps1' -Tag 'Offline', 'WIT' {

    Context 'Input validation' {

        It 'Throws when Organisation is empty' {
            {
                & $ScriptPath -Organization '' -ProjectId $ProjectId -WorkItemId $WorkItemId -Pat 'fakepat'
            } | Should -Throw '*Organisation*'
        }

        It 'Throws when ProjectId is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId '' -WorkItemId $WorkItemId -Pat 'fakepat'
            } | Should -Throw '*ProjectId*'
        }

        It 'Throws when WorkItemId is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -WorkItemId '' -Pat 'fakepat'
            } | Should -Throw '*WorkItemId*'
        }

        It 'Throws when Pat is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -WorkItemId $WorkItemId -Pat ''
            } | Should -Throw '*PAT*'
        }
    }

    Context 'Successful API call (mocked)' {

        BeforeAll {
            $fixture = Get-Content (Join-Path $FixturePath 'get_work_item_200.json') -Raw | ConvertFrom-Json
        }

        It 'Calls the correct URL including project and work item ID' {
            Mock Invoke-RestMethod { return $fixture } -Verifiable

            & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -WorkItemId $WorkItemId -Pat 'fakepat1234567890' | Out-Null

            Should -InvokeVerifiable
            Should -Invoke Invoke-RestMethod -Times 1 -Exactly -ParameterFilter {
                $Uri -eq "https://dev.azure.com/testorg/ProjectAlpha/_apis/wit/workitems/${WorkItemId}?api-version=7.2" -and
                $Method -eq 'Get'
            }
        }

        It 'Sends correct Authorization header' {
            $expectedAuth = [Convert]::ToBase64String(
                [Text.Encoding]::ASCII.GetBytes(':fakepat1234567890')
            )

            Mock Invoke-RestMethod { return $fixture }

            & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -WorkItemId $WorkItemId -Pat 'fakepat1234567890' | Out-Null

            Should -Invoke Invoke-RestMethod -Times 1 -ParameterFilter {
                $Headers['Authorization'] -eq "Basic $expectedAuth"
            }
        }

        It 'Outputs work item details with title' {
            Mock Invoke-RestMethod { return $fixture }

            $output = & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -WorkItemId $WorkItemId -Pat 'fakepat1234567890'
            $text = $output | Out-String

            $text | Should -Match 'Implement user authentication flow'
        }
    }

    Context 'HTTP error handling' {

        It 'Throws on 404 (work item not found)' {
            Mock Invoke-RestMethod {
                $ex = [System.Net.WebException]::new('The remote server returned an error: (404) Not Found.')
                throw $ex
            }

            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -WorkItemId '99999' -Pat 'fakepat'
            } | Should -Throw
        }
    }
}
