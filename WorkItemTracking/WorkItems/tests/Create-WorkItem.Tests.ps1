<#
.SYNOPSIS
    Pester offline unit tests for Create-WorkItem.ps1

.DESCRIPTION
    Mocks Invoke-RestMethod to validate URL construction with $type,
    JSON Patch content type, body structure, and error handling.
#>

BeforeAll {
    $ScriptPath = Join-Path $PSScriptRoot '..' 'Create-WorkItem.ps1'
    $FixturePath = Join-Path $PSScriptRoot 'fixtures'
    $ProjectId = 'ProjectAlpha'
    $WorkItemType = 'Task'
    $Title = 'Add unit tests for auth module'
}

Describe 'Create-WorkItem.ps1' -Tag 'Offline', 'WIT' {

    Context 'Input validation' {

        It 'Throws when Organisation is empty' {
            {
                & $ScriptPath -Organization '' -ProjectId $ProjectId -WorkItemType $WorkItemType -Title $Title -Pat 'fakepat'
            } | Should -Throw '*Organisation*'
        }

        It 'Throws when ProjectId is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId '' -WorkItemType $WorkItemType -Title $Title -Pat 'fakepat'
            } | Should -Throw '*ProjectId*'
        }

        It 'Throws when WorkItemType is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -WorkItemType '' -Title $Title -Pat 'fakepat'
            } | Should -Throw '*WorkItemType*'
        }

        It 'Throws when Title is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -WorkItemType $WorkItemType -Title '' -Pat 'fakepat'
            } | Should -Throw '*Title*'
        }

        It 'Throws when Pat is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -WorkItemType $WorkItemType -Title $Title -Pat ''
            } | Should -Throw '*PAT*'
        }
    }

    Context 'Successful API call (mocked)' {

        BeforeAll {
            $fixture = Get-Content (Join-Path $FixturePath 'create_work_item_200.json') -Raw | ConvertFrom-Json
        }

        It 'Calls the correct URL with $type in the path' {
            Mock Invoke-RestMethod { return $fixture } -Verifiable

            & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -WorkItemType $WorkItemType -Title $Title -Pat 'fakepat1234567890' | Out-Null

            Should -InvokeVerifiable
            Should -Invoke Invoke-RestMethod -Times 1 -Exactly -ParameterFilter {
                $Uri -eq "https://dev.azure.com/testorg/ProjectAlpha/_apis/wit/workitems/`$Task?api-version=7.2" -and
                $Method -eq 'Post'
            }
        }

        It 'Sends JSON Patch content type' {
            Mock Invoke-RestMethod { return $fixture }

            & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -WorkItemType $WorkItemType -Title $Title -Pat 'fakepat1234567890' | Out-Null

            Should -Invoke Invoke-RestMethod -Times 1 -ParameterFilter {
                $Headers['Content-Type'] -eq 'application/json-patch+json'
            }
        }

        It 'Includes Title in the request body' {
            Mock Invoke-RestMethod { return $fixture }

            & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -WorkItemType $WorkItemType -Title $Title -Pat 'fakepat1234567890' | Out-Null

            Should -Invoke Invoke-RestMethod -Times 1 -ParameterFilter {
                $Body -match 'System.Title'
            }
        }

        It 'Outputs created work item ID' {
            Mock Invoke-RestMethod { return $fixture }

            $output = & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -WorkItemType $WorkItemType -Title $Title -Pat 'fakepat1234567890'
            $text = $output | Out-String

            $text | Should -Match '#101'
        }
    }

    Context 'HTTP error handling' {

        It 'Throws on 401 (auth failure)' {
            Mock Invoke-RestMethod {
                $ex = [System.Net.WebException]::new('The remote server returned an error: (401) Unauthorized.')
                throw $ex
            }

            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectId -WorkItemType $WorkItemType -Title $Title -Pat 'badpat'
            } | Should -Throw
        }
    }
}
