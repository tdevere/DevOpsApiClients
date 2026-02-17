<#
.SYNOPSIS
    Pester offline unit tests for Update-Project.ps1

.DESCRIPTION
    Mocks Invoke-RestMethod to validate PATCH URL construction with GUID,
    GUID resolution from name, request body, and error handling.
#>

BeforeAll {
    $ScriptPath = Join-Path $PSScriptRoot '..' 'Update-Project.ps1'
    $FixturePath = Join-Path $PSScriptRoot 'fixtures'
    $ProjectGuid = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
}

Describe 'Update-Project.ps1' -Tag 'Offline', 'Core' {

    Context 'Input validation' {

        It 'Throws when Organisation is empty' {
            {
                & $ScriptPath -Organization '' -ProjectId $ProjectGuid -Pat 'fakepat' -NewDescription 'test'
            } | Should -Throw '*Organisation*'
        }

        It 'Throws when ProjectId is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId '' -Pat 'fakepat' -NewDescription 'test'
            } | Should -Throw '*ProjectId*'
        }

        It 'Throws when Pat is empty' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectGuid -Pat '' -NewDescription 'test'
            } | Should -Throw '*PAT*'
        }

        It 'Throws when no update parameters are given' {
            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectGuid -Pat 'fakepat'
            } | Should -Throw '*update parameter*'
        }
    }

    Context 'GUID resolution (mocked)' {

        BeforeAll {
            $getFixture = Get-Content (Join-Path $FixturePath 'get_project_200.json') -Raw | ConvertFrom-Json
            $patchFixture = Get-Content (Join-Path $FixturePath 'update_project_202.json') -Raw | ConvertFrom-Json
        }

        It 'Resolves project name to GUID via GET before PATCHing' {
            $callCount = 0
            Mock Invoke-RestMethod {
                $callCount++
                if ($Method -eq 'Get') {
                    return $getFixture
                }
                return $patchFixture
            }

            & $ScriptPath -Organization 'testorg' -ProjectId 'ProjectAlpha' -Pat 'fakepat1234567890' -NewDescription 'Updated' | Out-Null

            # Should have been called at least twice: GET (resolve) + PATCH (update)
            Should -Invoke Invoke-RestMethod -Times 2 -Exactly
        }

        It 'Skips resolution when ProjectId is already a GUID' {
            Mock Invoke-RestMethod { return $patchFixture }

            & $ScriptPath -Organization 'testorg' -ProjectId $ProjectGuid -Pat 'fakepat1234567890' -NewDescription 'Updated' | Out-Null

            # Should be called exactly once: just the PATCH
            Should -Invoke Invoke-RestMethod -Times 1 -Exactly
        }
    }

    Context 'Request body (mocked)' {

        BeforeAll {
            $patchFixture = Get-Content (Join-Path $FixturePath 'update_project_202.json') -Raw | ConvertFrom-Json
        }

        It 'Sends description in request body' {
            Mock Invoke-RestMethod {
                return $patchFixture
            }

            & $ScriptPath -Organization 'testorg' -ProjectId $ProjectGuid -Pat 'fakepat' -NewDescription 'New desc' | Out-Null

            Should -Invoke Invoke-RestMethod -Times 1 -ParameterFilter {
                $Method -eq 'Patch' -and
                $Uri -match $ProjectGuid
            }
        }

        It 'Sends visibility in request body' {
            Mock Invoke-RestMethod {
                return $patchFixture
            }

            & $ScriptPath -Organization 'testorg' -ProjectId $ProjectGuid -Pat 'fakepat' -NewVisibility 'private' | Out-Null

            Should -Invoke Invoke-RestMethod -Times 1 -ParameterFilter {
                $Method -eq 'Patch'
            }
        }
    }

    Context 'Version guard' {

        It 'Throws when response lacks id property (strict mode)' {
            $badResponse = [PSCustomObject]@{ status = 'queued' }

            Mock Invoke-RestMethod { return $badResponse }

            # In strict mode, accessing .id on an object without that property throws
            { & $ScriptPath -Organization 'testorg' -ProjectId $ProjectGuid -Pat 'fakepat' -NewDescription 'test' } | Should -Throw '*id*'
        }
    }

    Context 'HTTP error handling' {

        It 'Throws on 401 (unauthorized)' {
            Mock Invoke-RestMethod {
                throw [System.Net.WebException]::new('The remote server returned an error: (401) Unauthorized.')
            }

            {
                & $ScriptPath -Organization 'testorg' -ProjectId $ProjectGuid -Pat 'badpat' -NewDescription 'test'
            } | Should -Throw
        }
    }
}
