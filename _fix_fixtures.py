#!/usr/bin/env python3
"""
Bulk-fix fixture JSON files that are plain arrays.

ADO list endpoints return { "count": N, "value": [...] }.
Scripts use Set-StrictMode -Version Latest and access $response.value,
which throws PropertyNotFoundException on a plain array.

This script wraps plain-array fixtures in the correct ADO paged format.
"""

import json
import sys
from pathlib import Path

# Handwritten tests that check for specific names/counts — must use exact values.
SPECIFIC_FIXTURES: dict[str, dict] = {
    "Core/Projects/tests/fixtures/list_projects_200.json": {
        "count": 3,
        "value": [
            {
                "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                "name": "AlphaProject",
                "description": "First test project",
                "state": "wellFormed",
                "revision": 1,
                "url": "https://dev.azure.com/testorg/_apis/projects/a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                "lastUpdateTime": "2026-01-15T10:30:00Z",
            },
            {
                "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
                "name": "BetaProject",
                "description": "Second test project",
                "state": "wellFormed",
                "revision": 2,
                "url": "https://dev.azure.com/testorg/_apis/projects/b2c3d4e5-f6a7-8901-bcde-f12345678901",
                "lastUpdateTime": "2026-01-16T10:30:00Z",
            },
            {
                "id": "c3d4e5f6-a7b8-9012-cdef-123456789012",
                "name": "GammaProject",
                "description": "Third test project",
                "state": "wellFormed",
                "revision": 3,
                "url": "https://dev.azure.com/testorg/_apis/projects/c3d4e5f6-a7b8-9012-cdef-123456789012",
                "lastUpdateTime": "2026-01-17T10:30:00Z",
            },
        ],
    },
    "Git/Repositories/tests/fixtures/list_repositories_200.json": {
        "count": 3,
        "value": [
            {
                "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                "name": "ContosoRepo",
                "defaultBranch": "refs/heads/main",
                "isDisabled": False,
                "isFork": False,
                "isInMaintenance": False,
                "size": 1024,
                "project": {"id": "p1b2c3d4-e5f6-7890-abcd-ef1234567890", "name": "AlphaProject"},
                "creationDate": "2026-01-15T10:30:00Z",
            },
            {
                "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
                "name": "WidgetService",
                "defaultBranch": "refs/heads/main",
                "isDisabled": False,
                "isFork": False,
                "isInMaintenance": False,
                "size": 2048,
                "project": {"id": "p1b2c3d4-e5f6-7890-abcd-ef1234567890", "name": "AlphaProject"},
                "creationDate": "2026-01-16T10:30:00Z",
            },
            {
                "id": "c3d4e5f6-a7b8-9012-cdef-123456789012",
                "name": "InfraAsCode",
                "defaultBranch": "refs/heads/main",
                "isDisabled": False,
                "isFork": False,
                "isInMaintenance": False,
                "size": 512,
                "project": {"id": "p1b2c3d4-e5f6-7890-abcd-ef1234567890", "name": "AlphaProject"},
                "creationDate": "2026-01-17T10:30:00Z",
            },
        ],
    },
}


def fix_fixtures(root: Path, dry_run: bool = False) -> tuple[int, int]:
    """
    Wrap all plain-array fixture files with ADO paged format.
    Returns (fixed_count, skipped_count).
    """
    fixed = 0
    skipped = 0

    fixture_files = list(root.rglob("*.json"))
    fixture_files = [
        f for f in fixture_files
        if "fixtures" in f.parts and not f.name.endswith("_404.json")
    ]

    for path in sorted(fixture_files):
        rel = path.relative_to(root).as_posix()

        # Check for specific override
        if rel in SPECIFIC_FIXTURES:
            new_data = SPECIFIC_FIXTURES[rel]
            if dry_run:
                print(f"  [DRY] SPECIFIC {rel}")
            else:
                path.write_text(json.dumps(new_data, indent=2) + "\n", encoding="utf-8")
                print(f"  [OK] SPECIFIC {rel}")
            fixed += 1
            continue

        try:
            raw = path.read_text(encoding="utf-8").strip()
        except Exception as e:
            print(f"  ✗ read error {rel}: {e}")
            skipped += 1
            continue

        if not raw.startswith("["):
            skipped += 1
            continue  # Already wrapped or not an array

        try:
            data = json.loads(raw)
        except json.JSONDecodeError as e:
            print(f"  ✗ JSON error {rel}: {e}")
            skipped += 1
            continue

        if not isinstance(data, list):
            skipped += 1
            continue

        wrapped = {"count": len(data), "value": data}
        if dry_run:
            print(f"  [DRY] WRAP ({len(data)} items) {rel}")
        else:
            path.write_text(json.dumps(wrapped, indent=2) + "\n", encoding="utf-8")
            print(f"  [OK] WRAP ({len(data)} items) {rel}")
        fixed += 1

    return fixed, skipped


def main():
    dry_run = "--dry-run" in sys.argv
    root = Path(__file__).parent

    print(f"{'[DRY RUN] ' if dry_run else ''}Fixing plain-array fixture files...\n")
    fixed, skipped = fix_fixtures(root, dry_run=dry_run)
    print(f"\nDone. Fixed: {fixed}, Skipped (already object/error): {skipped}")


if __name__ == "__main__":
    main()
