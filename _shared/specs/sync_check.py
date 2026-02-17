#!/usr/bin/env python3
"""
API Spec Sync — Detection Script

Compares upstream Azure DevOps REST API specifications against locally stored
hashes. Outputs a structured JSON report of detected changes per domain.

Usage:
    python sync_check.py                  # Check all domains
    python sync_check.py --domain core    # Check a single domain
    python sync_check.py --update-hashes  # Write new hashes after sync

Exit codes:
    0  — No changes detected (or hashes updated successfully)
    1  — Error (network, parse, file I/O)
    2  — Changes detected (delta report written to stdout)
"""

import argparse
import hashlib
import json
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
HASHES_FILE = SCRIPT_DIR / "last_sync_hashes.json"
URLS_FILE = SCRIPT_DIR / "upstream_urls.json"

# ---------------------------------------------------------------------------
# Domain → local directory mapping
# ---------------------------------------------------------------------------
DOMAIN_DIR_MAP = {
    "core":  "Core",
    "git":   "Git",
    "build": "Build",
    "wit":   "WorkItemTracking",
}


def load_json(path: Path) -> dict:
    """Load a JSON file and return the parsed dict."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict) -> None:
    """Write a dict to a JSON file with pretty formatting."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def fetch_spec(url: str, timeout: int = 30) -> bytes | None:
    """Fetch the upstream spec, returning raw bytes or None on failure."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "DevOpsApiClients-SyncCheck/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except (urllib.error.URLError, urllib.error.HTTPError, OSError) as exc:
        print(f"WARN: Failed to fetch {url}: {exc}", file=sys.stderr)
        return None


def sha256_hex(data: bytes) -> str:
    """Return the SHA-256 hex digest of the given bytes."""
    return hashlib.sha256(data).hexdigest()


def classify_changes(old_spec: dict | None, new_spec: dict) -> dict:
    """
    Compare two parsed spec dicts and classify changes.

    Returns:
        {
            "change_type": "non-breaking" | "breaking" | "in-sync",
            "added_paths": [...],
            "removed_paths": [...],
            "added_definitions": [...],
            "removed_definitions": [...],
            "summary": "human-readable description"
        }
    """
    if old_spec is None:
        # First sync — treat everything as new (non-breaking)
        paths = list(new_spec.get("paths", {}).keys())
        defs = list(new_spec.get("definitions", {}).keys())
        return {
            "change_type": "non-breaking",
            "added_paths": paths,
            "removed_paths": [],
            "added_definitions": defs,
            "removed_definitions": [],
            "summary": f"Initial sync. {len(paths)} paths, {len(defs)} definitions catalogued.",
        }

    old_paths = set(old_spec.get("paths", {}).keys())
    new_paths = set(new_spec.get("paths", {}).keys())
    old_defs = set(old_spec.get("definitions", {}).keys())
    new_defs = set(new_spec.get("definitions", {}).keys())

    added_paths = sorted(new_paths - old_paths)
    removed_paths = sorted(old_paths - new_paths)
    added_defs = sorted(new_defs - old_defs)
    removed_defs = sorted(old_defs - new_defs)

    # Check for type changes in shared definitions
    type_changes = []
    for defn in old_defs & new_defs:
        old_props = old_spec.get("definitions", {}).get(defn, {}).get("properties", {})
        new_props = new_spec.get("definitions", {}).get(defn, {}).get("properties", {})
        for prop in set(old_props.keys()) & set(new_props.keys()):
            old_type = old_props[prop].get("type")
            new_type = new_props[prop].get("type")
            if old_type and new_type and old_type != new_type:
                type_changes.append(f"{defn}.{prop}: {old_type} → {new_type}")

    is_breaking = bool(removed_paths or removed_defs or type_changes)

    if not added_paths and not removed_paths and not added_defs and not removed_defs and not type_changes:
        # Content changed but paths/defs are the same — likely description edits
        return {
            "change_type": "non-breaking",
            "added_paths": [],
            "removed_paths": [],
            "added_definitions": [],
            "removed_definitions": [],
            "type_changes": [],
            "summary": "Spec content changed (descriptions, examples, or metadata). No structural impact.",
        }

    parts = []
    if added_paths:
        parts.append(f"+{len(added_paths)} endpoints")
    if removed_paths:
        parts.append(f"-{len(removed_paths)} endpoints")
    if added_defs:
        parts.append(f"+{len(added_defs)} definitions")
    if removed_defs:
        parts.append(f"-{len(removed_defs)} definitions")
    if type_changes:
        parts.append(f"{len(type_changes)} type changes")

    return {
        "change_type": "breaking" if is_breaking else "non-breaking",
        "added_paths": added_paths,
        "removed_paths": removed_paths,
        "added_definitions": added_defs,
        "removed_definitions": removed_defs,
        "type_changes": type_changes,
        "summary": "; ".join(parts),
    }


def check_domain(domain: str, url: str, stored_hash: str | None) -> dict | None:
    """
    Check a single domain for upstream changes.

    Returns a delta report dict, or None if no changes / fetch failed.
    """
    raw = fetch_spec(url)
    if raw is None:
        return None

    current_hash = sha256_hex(raw)

    if current_hash == stored_hash:
        return None  # In sync

    # Parse spec for classification
    try:
        new_spec = json.loads(raw)
    except json.JSONDecodeError:
        print(f"WARN: Upstream spec for '{domain}' is not valid JSON. Treating as opaque change.", file=sys.stderr)
        return {
            "domain": domain,
            "previous_hash": stored_hash,
            "new_hash": current_hash,
            "change_type": "non-breaking",
            "classification": {
                "change_type": "non-breaking",
                "summary": "Spec content changed but is not valid JSON for diff analysis.",
            },
            "detected_at": datetime.now(timezone.utc).isoformat(),
            "spec_url": url,
        }

    # Try to load the old spec for diff (if we have a cached copy)
    old_spec = None
    cache_path = SCRIPT_DIR / f".cache_{domain}.json"
    if cache_path.exists():
        try:
            old_spec = json.loads(cache_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass

    classification = classify_changes(old_spec, new_spec)

    # Cache the new spec for future diffs
    try:
        cache_path.write_text(json.dumps(new_spec, indent=2, ensure_ascii=False), encoding="utf-8")
    except OSError as exc:
        print(f"WARN: Could not cache spec for '{domain}': {exc}", file=sys.stderr)

    return {
        "domain": domain,
        "local_dir": DOMAIN_DIR_MAP.get(domain, domain),
        "previous_hash": stored_hash,
        "new_hash": current_hash,
        "change_type": classification["change_type"],
        "classification": classification,
        "detected_at": datetime.now(timezone.utc).isoformat(),
        "spec_url": url,
    }


def update_hashes(deltas: list[dict]) -> None:
    """Persist new hashes for domains that were successfully synced."""
    hashes = load_json(HASHES_FILE)
    now = datetime.now(timezone.utc).isoformat()

    for delta in deltas:
        domain = delta["domain"]
        if domain in hashes:
            hashes[domain]["hash"] = delta["new_hash"]
            hashes[domain]["synced_at"] = now
        else:
            hashes[domain] = {
                "hash": delta["new_hash"],
                "synced_at": now,
                "spec_url": delta["spec_url"],
            }

    save_json(HASHES_FILE, hashes)
    print(f"Updated hashes for: {', '.join(d['domain'] for d in deltas)}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check upstream API spec changes.")
    parser.add_argument(
        "--domain",
        choices=["all", "core", "git", "build", "wit"],
        default="all",
        help="Domain to check (default: all)",
    )
    parser.add_argument(
        "--update-hashes",
        action="store_true",
        help="Write new hashes to last_sync_hashes.json (run after successful sync)",
    )
    args = parser.parse_args()

    urls = load_json(URLS_FILE)
    hashes = load_json(HASHES_FILE)

    domains = list(urls.keys()) if args.domain == "all" else [args.domain]

    deltas = []
    for domain in domains:
        url = urls.get(domain)
        if not url:
            print(f"WARN: No upstream URL configured for domain '{domain}'", file=sys.stderr)
            continue

        stored = hashes.get(domain, {}).get("hash")
        delta = check_domain(domain, url, stored)

        if delta:
            deltas.append(delta)
            print(
                f"  CHANGED  {domain:8s}  {delta['change_type']:13s}  {delta['classification']['summary']}",
                file=sys.stderr,
            )
        else:
            print(f"  IN-SYNC  {domain}", file=sys.stderr)

    if not deltas:
        report = {"status": "in-sync", "domains_checked": domains, "deltas": []}
        print(json.dumps(report, indent=2))
        return 0

    if args.update_hashes:
        update_hashes(deltas)

    report = {
        "status": "changes-detected",
        "domains_checked": domains,
        "deltas": deltas,
    }
    print(json.dumps(report, indent=2))
    return 2  # Signal to CI: changes detected


if __name__ == "__main__":
    sys.exit(main())
