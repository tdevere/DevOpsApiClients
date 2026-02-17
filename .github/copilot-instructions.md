# Agent Spec: Azure DevOps 7.2 API Rosetta Stone

**Project:** tdevere/DevOpsApiClients  
**Role:** Principal DevOps Engineer & API Architect

---

## 1. Core Objective

Build a definitive, cross-platform library of **tested** examples for the Azure DevOps 7.2 REST API. Every endpoint must have equivalent implementations in **Python**, **PowerShell**, and **cURL**, accompanied by offline unit tests and optional live integration tests.

---

## 2. Directory & File Standards

### 2.1 Per-Domain Layout

For every API Domain (e.g., `Core/Projects`, `Git/Repos`, `WorkItemTracking/WorkItems`):

```
<Domain>/<Resource>/
├── <operation>.py           # Python implementation (requests only)
├── <operation>.sh           # cURL / Bash implementation
├── <Verb>-<Resource>.ps1    # PowerShell standalone script
└── tests/                   # Tests live next to the code they test
    ├── test_<operation>.py          # pytest unit tests (mocked HTTP)
    ├── test_<operation>_live.py     # pytest live integration tests
    ├── <Verb>-<Resource>.Tests.ps1  # Pester unit tests (mocked HTTP)
    └── test_<operation>.bats        # bats-core unit tests (mocked HTTP)
```

Naming conventions:
- **Python**: `snake_case.py` — e.g., `list_projects.py`
- **PowerShell**: `Verb-Resource.ps1` — e.g., `List-Projects.ps1`
- **Bash/cURL**: `snake_case.sh` — e.g., `list_projects.sh`
- **Test files**: Prefixed with `test_` (Python/Bash) or suffixed with `.Tests.ps1` (Pester).

### 2.2  Shared Helpers (future)

When the project grows beyond standalone scripts, extract shared logic into:
- **Python**: A `_shared/` package with `auth.py`, `logging_utils.py`, `http_client.py`.
- **PowerShell**: A `_shared/` module with `New-AdoAuthHeader`, `Write-AdoLog`, `Invoke-AdoRestMethod`.
- **Bash**: A `_shared/common.sh` sourced by all scripts.

> **Current state:** Scripts are self-contained. Extract helpers when ≥3 scripts duplicate the same logic.

---

## 3. Technical Requirements

### 3.1 Authentication
- **Method**: Basic Auth via PAT.
- **Header**: `Authorization: Basic [Base64(":PAT")]`.
- **Environment variables**: `AZURE_DEVOPS_PAT`, `AZURE_DEVOPS_ORG`, `PROJECT_ID`.
- Never hard-code credentials. Always read from environment.

### 3.2 API Versioning
- Hardcode `api-version=7.2` unless a preview sub-version is strictly required.
- Include a **version guard** in every script that validates expected response keys.

### 3.3 PowerShell Compatibility
- Support **Windows PowerShell 5.1** AND **PowerShell 7+ (Linux/macOS)**.
- Avoid Windows-only .NET types (e.g., `System.Web.HttpUtility`).
- Use `[Convert]::ToBase64String` and `Invoke-RestMethod` for maximum compatibility.

### 3.4 Logging (Mandatory)

All implementations must log their activity:
- **Output directory**: `logs/` (created automatically; git-ignored).
- **Dual format**: `.log` (human-readable) and `.json` (structured/machine-readable).
- **PAT redaction**: Mask tokens before writing to any log. Show only the first 4 characters: `abcd****...`.
- **Log levels**: `INFO`, `WARN`, `ERROR`. Include timestamps (UTC ISO-8601).
- **CI mode**: When `CI=true` environment variable is set, also emit `::error::` / `::warning::` GitHub Actions annotations.

---

## 4. Testing Strategy

### 4.1 Two-Tier Test Model

| Tier | Name | Runs When | Requires Secrets | Frameworks |
|------|------|-----------|------------------|------------|
| **T1** | **Offline Unit Tests** | Every push, every PR | No | pytest + responses, Pester (Mock), bats-core |
| **T2** | **Live Integration Tests** | Merge to `main`, `workflow_dispatch`, or label `run-live-tests` | Yes (`AZURE_DEVOPS_PAT`, etc.) | pytest (live), PowerShell (live), bash (live) |

### 4.2 Offline Unit Tests (T1) — Always Run

Offline tests validate script logic **without making any HTTP calls**. They:
- Mock all HTTP responses using recorded fixtures (JSON files in `tests/fixtures/`).
- Verify correct URL construction, header assembly, query-parameter formatting.
- Verify error-handling paths (401, 403, 404, 500 responses).
- Verify logging output (correct format, PAT redaction).
- Run in **< 30 seconds** with zero external dependencies.

**Frameworks:**
- **Python**: `pytest` + `responses` (or `requests-mock`) for HTTP stubbing.
- **PowerShell**: `Pester` v5+ with `Mock` for `Invoke-RestMethod`.
- **Bash**: `bats-core` with stubbed `curl` (shell function override or `$PATH` shim).

**File pattern**: `tests/test_<operation>.py`, `tests/<Verb>-<Resource>.Tests.ps1`, `tests/test_<operation>.bats`

### 4.3 Live Integration Tests (T2) — Gated

Live tests hit the real Azure DevOps API and follow the **Stateful Testing Lifecycle**:

1. **Arrange**: Dynamically fetch or create prerequisite IDs (e.g., Project ID).
2. **Pre-Check**: `GET` the resource to confirm starting state.
3. **Execute**: Perform the target operation (POST, PATCH, DELETE).
4. **Verify**: `GET` the resource to confirm the expected state change.
5. **Teardown**: Revert or delete sacrificial test artifacts immediately.

**Rules for live tests:**
- **Dedicated test project**: All mutating operations target `ADO_TEST_PROJECT` — a sacrificial project reserved for CI. Never mutate production projects.
- **Idempotent teardown**: Teardown must not fail if the resource was already cleaned up (handle 404 gracefully).
- **Timeout**: Each live test has a 60-second timeout. API operations that queue (e.g., project creation) must poll with backoff.
- **File naming**: Live tests are in separate files suffixed `_live` — e.g., `test_update_project_live.py`. This ensures they're easy to exclude.

### 4.4 Scoped Testing — Path-Based CI Filtering

To avoid running unrelated tests when only one API domain changes:

```yaml
# In CI workflow, use dorny/paths-filter or native paths: filters
- uses: dorny/paths-filter@v3
  id: changes
  with:
    filters: |
      core:
        - 'Core/**'
      git:
        - 'Git/**'
      build:
        - 'Build/**'
      wit:
        - 'WorkItemTracking/**'
      shared:
        - '_shared/**'
        - '.github/workflows/**'
```

**Scope rules:**
- If `core` files changed → run only `Core/` tests.
- If `shared` or workflow files changed → run **all** tests (full matrix).
- If only docs changed (`.md` files) → run lint only, skip all tests.
- `workflow_dispatch` always runs the full suite.

### 4.5 Test Fixtures

Store reusable mock API responses in `tests/fixtures/`:
```
tests/
└── fixtures/
    ├── core/
    │   ├── list_projects_200.json
    │   ├── get_project_200.json
    │   ├── get_project_404.json
    │   └── update_project_200.json
    └── git/
        └── ...
```

Fixture files are **real API response snapshots** captured once and committed. When the API version changes, refresh fixtures.

### 4.6 Test Markers / Tags

Use markers to allow granular test selection:

- **Python**: `@pytest.mark.offline`, `@pytest.mark.live`, `@pytest.mark.core`, `@pytest.mark.git`
- **Pester**: `Tag` parameter: `-Tag 'Offline'`, `-Tag 'Live'`, `-Tag 'Core'`
- **bats**: By convention, separate files for live vs. offline.

CI runs: `pytest -m "offline"` (always) and `pytest -m "live"` (gated).

---

## 5. Error Handling

All implementations must trap HTTP status codes and provide **actionable** feedback:

| Status | Action |
|--------|--------|
| **401** | `ERROR: Authentication failed. Verify AZURE_DEVOPS_PAT is valid and not expired.` |
| **403** | `ERROR: Insufficient permissions. Required PAT scope: <scope>. See https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate` |
| **404** | `ERROR: Resource not found. Verify AZURE_DEVOPS_ORG='<org>' and PROJECT_ID='<id>' are correct.` |
| **429** | `WARN: Rate limited. Retrying after {Retry-After} seconds.` (implement exponential backoff) |
| **5xx** | `ERROR: Server error (<code>). Retry in 10s. If persistent, check https://status.dev.azure.com` |

Error messages must include the **request URL** (with PAT redacted) and the **response body** (truncated to 500 chars).

---

## 6. CI/CD Pipeline Design

### 6.1 Workflow Structure

```
ci-test-and-release.yml
├── Job: lint              (always — no secrets needed)
│   ├── py_compile *.py
│   ├── bash -n *.sh
│   └── PowerShell Parser *.ps1
│
├── Job: detect-changes    (path-based filtering)
│
├── Job: test-offline      (always — no secrets needed)
│   ├── pytest -m offline  (scoped by detected changes)
│   ├── Invoke-Pester -Tag Offline
│   └── bats tests/
│
├── Job: test-live         (gated: main push OR label OR dispatch)
│   ├── Requires: AZURE_DEVOPS_PAT, AZURE_DEVOPS_ORG, ADO_TEST_PROJECT
│   ├── pytest -m live     (scoped by detected changes)
│   ├── Invoke-Pester -Tag Live
│   └── bash live tests
│
└── Job: release           (main push only, after all jobs pass)
```

### 6.2 Required Secrets & Variables

| Secret / Variable | Required By | Description |
|---|---|---|
| `AZURE_DEVOPS_PAT` | T2 (live) | PAT with scopes matching the API domain under test |
| `AZURE_DEVOPS_ORG` | T2 (live) | Organization name |
| `ADO_TEST_PROJECT` | T2 (live) | **Dedicated sacrificial project** for mutating tests |
| `PROJECT_ID` | T2 (live) | Specific project ID/name (can equal `ADO_TEST_PROJECT`) |

### 6.3 PR vs. Main Push Behavior

| Event | Lint | Offline Tests | Live Tests | Release |
|-------|------|--------------|------------|---------|
| PR to `main` | Yes (all) | Yes (scoped) | No* | No |
| Push to `main` | Yes (all) | Yes (all) | Yes (all) | Yes |
| `workflow_dispatch` | Yes (all) | Yes (all) | Yes (all) | No |

\* PRs can opt in to live tests by adding the `run-live-tests` label.

---

## 7. Code Generation Rules for Agents

When generating new API client implementations:

1. **Always create all three languages** (Python, PowerShell, Bash) for every operation.
2. **Always create offline unit tests** for every new script (at minimum: success path + one error path).
3. **Include a `tests/fixtures/` JSON file** with a sample API response for the operation.
4. **Follow the Stateful Testing Lifecycle** for any live test that mutates state.
5. **Never commit code without passing `lint`** — run syntax checks before declaring done.
6. **Update the domain README.md** with the new operation in the operations table.
7. **Use `ADO_TEST_PROJECT`** (not `PROJECT_ID`) as the target for any mutating live test.

---

## 8. Upstream API Specification Monitoring & Sync

### 8.1 Purpose

Maintain continuous alignment with the official Microsoft Azure DevOps REST API v7.2 specifications. When upstream schemas change (new fields, endpoints, or breaking modifications), automatically detect the delta and propagate updates through clients, fixtures, and tests.

### 8.2 Spec Tracking Infrastructure

```
_shared/
└── specs/
    ├── last_sync_hashes.json    # Per-domain SHA-256 of last-synced upstream spec
    ├── upstream_urls.json       # Canonical URLs for each domain's spec source
    └── sync_check.py            # Detection script (runs on schedule)
```

**`last_sync_hashes.json`** format:
```json
{
  "core": { "hash": "abc123...", "synced_at": "2026-02-17T00:00:00Z", "spec_url": "..." },
  "git":  { "hash": "def456...", "synced_at": "2026-02-17T00:00:00Z", "spec_url": "..." },
  "build": { "hash": null, "synced_at": null, "spec_url": "..." },
  "wit":   { "hash": null, "synced_at": null, "spec_url": "..." }
}
```

**`upstream_urls.json`** maps domains to their upstream spec sources:
```json
{
  "core":  "https://raw.githubusercontent.com/MicrosoftDocs/vsts-rest-api-specs/master/specification/core/7.2/core.json",
  "git":   "https://raw.githubusercontent.com/MicrosoftDocs/vsts-rest-api-specs/master/specification/git/7.2/git.json",
  "build": "https://raw.githubusercontent.com/MicrosoftDocs/vsts-rest-api-specs/master/specification/build/7.2/build.json",
  "wit":   "https://raw.githubusercontent.com/MicrosoftDocs/vsts-rest-api-specs/master/specification/workItemTracking/7.2/workItemTracking.json"
}
```

### 8.3 Detection Logic

The `sync_check.py` script runs on a **scheduled CI trigger** (weekly cron or `workflow_dispatch`):

1. **Fetch** the current upstream spec for each domain listed in `upstream_urls.json`.
2. **Hash** the response body (SHA-256).
3. **Compare** against the stored hash in `last_sync_hashes.json`.
4. **Classify** the delta:
   - **Non-Breaking**: New optional properties, new endpoints, added enum values.
   - **Breaking**: Removed required fields, changed property types, removed endpoints.
5. **Output** a structured JSON diff report to stdout for the workflow to consume.

Classification heuristic:
- If upstream adds keys not present locally → `non-breaking`.
- If upstream removes keys present locally OR changes a value type → `breaking`.
- If no delta → `in-sync` (no action).

### 8.4 Autonomous Synthesis (Agent Actions on Delta)

When a delta is detected, the agent (or CI automation) must:

#### 8.4.1 Update Fixtures
- Regenerate `tests/fixtures/*.json` files to match the new schema.
- Add new fields with realistic sample values.
- For breaking changes, keep the old fixture as `<name>_v1.json` alongside the new one.

#### 8.4.2 Refactor Clients
- **Non-Breaking**: Add new optional parameters to Python (`argparse`), PowerShell (`param`), and Bash (positional/env) scripts. Existing behavior must not change.
- **Breaking**: Do **not** overwrite existing scripts. Instead, create a versioned copy (e.g., `get_project_v2.py`) and mark the original with a deprecation comment header.

#### 8.4.3 Version Management (Breaking Changes Only)
- Create a versioned directory if the change affects the operation signature:
  ```
  Core/Projects/
  ├── get_project.py          # Original (deprecated header added)
  ├── get_project_v2.py       # New version
  └── tests/
      ├── test_get_project.py     # Still tests original
      └── test_get_project_v2.py  # Tests new version
  ```
- Add a `@deprecated` marker/comment to the original with a pointer to the replacement.
- Update the domain `README.md` to reflect both versions.

### 8.5 Validation Gate

Every automated sync update **must** pass through this gate before a PR is opened:

```
Sync Detected
    │
    ▼
Update fixtures + clients
    │
    ▼
Run T1 Offline Tests ──── FAIL ──→ Abort, open issue instead of PR
    │
   PASS
    │
    ▼
Secrets available? ──── NO ──→ Open PR with T1-only badge
    │
   YES
    │
    ▼
Run T2 Live Tests ──── FAIL ──→ Open PR tagged "upstream-live-mismatch"
    │                            (spec changed but API not yet updated)
   PASS
    │
    ▼
Open PR with full-pass badge
```

- **T1 must pass** for a PR to be created. If T1 fails, the workflow opens a GitHub Issue instead, tagged `api-sync-failure`.
- **T2 failure is non-blocking** for PR creation but is flagged — upstream docs sometimes lead the actual service deployment.

### 8.6 Automated PR Format

PRs generated by the sync workflow must follow this template:

- **Title**: `[API-SYNC] <Domain>: <Change Description>`
- **Labels**: `api-sync`, and one of `non-breaking` or `breaking`
- **Body**:
  ```markdown
  ## Upstream API Spec Change Detected

  | Field | Value |
  |-------|-------|
  | **Domain** | Core/Projects |
  | **Change Type** | Non-Breaking / Breaking |
  | **Upstream Spec** | [link to spec file] |
  | **Previous Hash** | `abc123...` |
  | **New Hash** | `def456...` |
  | **Detected At** | 2026-02-17T12:00:00Z |

  ### Changes
  - Added optional field `lastAccessedDate` to Project response
  - Added new endpoint `GET /projects/{id}/properties`

  ### Files Modified
  - `Core/Projects/tests/fixtures/get_project_200.json`
  - `Core/Projects/get_project.py` (new param)
  - ...

  ### Test Results
  | Tier | Result |
  |------|--------|
  | T1 Offline | ✅ Passed |
  | T2 Live | ✅ Passed / ⚠️ Skipped (no secrets) / ❌ Failed (upstream not yet live) |
  ```

### 8.7 CI Workflow Integration

Add a dedicated workflow `api-spec-sync.yml`:

```yaml
name: API Spec Sync
on:
  schedule:
    - cron: '0 6 * * 1'     # Weekly on Monday 06:00 UTC
  workflow_dispatch:
    inputs:
      domain:
        description: 'Domain to check (or "all")'
        default: 'all'
        type: choice
        options: [all, core, git, build, wit]
```

This workflow:
1. Runs `sync_check.py` to detect deltas.
2. If delta found, creates a feature branch `api-sync/<domain>-<date>`.
3. Applies autonomous synthesis (fixtures + clients).
4. Runs T1 offline tests on the branch.
5. If T1 passes, opens a PR. If T1 fails, opens an Issue.
6. Optionally runs T2 if secrets are available.

---

## 9. Access Control & Requester Validation

### 9.1 Purpose

Prevent unauthorized users from triggering agent-driven API generation, burning LLM token credits, or running live tests against the Azure DevOps environment. All automated work is gated behind identity verification.

### 9.2 Security Model — "Trusted Contributor Gate"

The authorization gate uses a two-part model:

1. **GitHub Issue Form**: Standardizes the API coverage request (domain, operation, endpoint).
2. **Permission Check**: The workflow validates `github.actor` against an approved list **and** the `author_association` field before any agent work begins.

### 9.3 Authorization Rules

| Check | Allowed Values | Purpose |
|-------|---------------|---------|
| **Hardcoded allowlist** | `tdevere` (extend as needed) | Explicit approval for specific users |
| **Author association** | `COLLABORATOR`, `MEMBER`, `OWNER` | Automatic approval for repo/org members |
| **Label gate** | `needs-api-coverage` | Final-click approval — an owner/member must add the label |

**Rejected associations** (agent must **not** process requests from):
- `NONE` — no relationship to the repository
- `FIRST_TIME_CONTRIBUTOR` — first-time contributor with no prior merged PR
- `FIRST_TIMER` — first-time GitHub contributor ever
- `CONTRIBUTOR` — has merged PRs but is not a collaborator/member (use allowlist to override if needed)

### 9.4 Agent Behavior on Rejection

When an unauthorized user triggers the workflow, the agent must:

1. **Not** create a pull request or branch.
2. **Not** run any LLM-powered code generation.
3. Post a polite issue comment:
   > *"I'm sorry, @user, but automated API generation is currently restricted to approved project members."*
4. Exit cleanly with a success status (do not fail the workflow — the rejection is intentional).

### 9.5 Issue Form Contract

API coverage requests are submitted via a structured GitHub Issue Form (`.github/ISSUE_TEMPLATE/api-coverage-request.yml`) with these required fields:

| Field | Type | Description |
|-------|------|-------------|
| **API Domain** | dropdown | `Core`, `Git`, `Build`, `WorkItemTracking` |
| **Operation** | text | Human-readable name (e.g., "List Repositories") |
| **REST Endpoint** | text | Full path (e.g., `GET /{org}/_apis/git/repositories`) |
| **HTTP Method** | dropdown | `GET`, `POST`, `PUT`, `PATCH`, `DELETE` |
| **Priority** | dropdown | `High`, `Medium`, `Low` |
| **Additional Context** | textarea | Optional notes, links to docs, edge cases |

### 9.6 Workflow File

The authorization workflow lives at `.github/workflows/agent-api-request.yml` and contains three jobs:

1. **`authorize`** — Validates `github.actor` and `author_association`. Outputs `is_authorized`.
2. **`reject`** — Runs only when unauthorized. Posts a polite rejection comment on the issue.
3. **`generate-api`** — Runs only when authorized AND the `needs-api-coverage` label is present. Parses the issue body, generates code, runs T1 tests, and reports results.

### 9.7 Extending the Allowlist

To grant access to a new contributor:
- **Preferred**: Invite them as a repository collaborator — they are automatically authorized via `author_association`.
- **Alternative**: Add their GitHub username to the `APPROVED_USERS` variable in the `authorize` job.

### 9.8 Audit Trail

Every agent invocation is fully auditable:
- **Who**: `github.actor` + `author_association` logged in the authorize step.
- **What**: Issue number, domain, operation, endpoint parsed and logged.
- **When**: GitHub Actions run timestamp and duration.
- **Outcome**: Acknowledgment comment, result comment, and (if generated) PR link — all on the issue thread.