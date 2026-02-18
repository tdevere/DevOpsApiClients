# GitHub API Authentication Format Update

## Problem

The repository workflows were using the deprecated GitHub API authentication format:
```bash
-H "Authorization: token $ADMIN_PAT"
```

This format is deprecated and does **not work** with GitHub's fine-grained personal access tokens (PATs), which are now the recommended token type for enhanced security.

## Solution

Updated all GitHub API authentication headers to use the modern Bearer token format:
```bash
-H "Authorization: Bearer $ADMIN_PAT"
```

## Affected Workflows

### 1. `.github/workflows/auto-heal.yml`
- **Line 388**: Unassign copilot during escalation (DELETE request)
- **Line 594**: Assign copilot to new fix issue (POST request)
- **Line 602**: Verify copilot assignment (GET request)

### 2. `.github/workflows/project-completion.yml`
- **Line 248**: Assign copilot to project completion issue (POST request)
- **Line 256**: Verify copilot assignment (GET request)

## Token Type Compatibility

| Token Type | `Authorization: token` | `Authorization: Bearer` |
|------------|------------------------|-------------------------|
| Classic PAT | ✅ Works | ✅ Works |
| Fine-grained PAT | ❌ Fails | ✅ Works |

## References

- [GitHub REST API Authentication](https://docs.github.com/en/rest/overview/authenticating-to-the-rest-api)
- [About fine-grained personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#about-fine-grained-personal-access-tokens)

## Implementation Notes

- Classic PATs will continue to work with the new Bearer format
- Fine-grained PATs now work correctly with the updated authentication
- No workflow functionality changes—only the authentication header format was updated
- All YAML syntax validated successfully

## Future Development

When adding new GitHub API calls in workflows, always use the Bearer format:
```yaml
curl -X POST \
  -H "Authorization: Bearer ${{ secrets.GITHUB_TOKEN }}" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "https://api.github.com/repos/$OWNER/$REPO/..."
```

---

**Fixed by**: GitHub Copilot Agent  
**Date**: 2026-02-18  
**Related PR**: #[PR number will be added]
