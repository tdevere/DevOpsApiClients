#!/usr/bin/env python3
"""Parse all Azure DevOps REST API 7.2 specs from the locally cloned repo.
Produces a comprehensive listing of all domains and their endpoints."""

import json
import os
import sys
from pathlib import Path

SPEC_ROOT = Path("/tmp/vsts-rest-api-specs/specification")
OUTPUT = Path("/workspaces/DevOpsApiClients/_research/api_specs_full.json")

DOMAINS = [
    "account", "advancedSecurity", "approvalsAndChecks", "artifacts",
    "artifactsPackageTypes", "audit", "build", "core", "dashboard",
    "delegatedAuth", "distributedTask", "environments", "extensionManagement",
    "favorite", "git", "governance", "graph", "hooks", "ims",
    "memberEntitlementManagement", "notification", "operations",
    "permissionsReport", "pipelines", "policy", "processDefinitions",
    "processadmin", "processes", "profile", "release", "resourceUsage",
    "search", "security", "securityRoles", "serviceEndpoint", "status",
    "symbol", "test", "testPlan", "testResults", "tfvc", "tokenAdmin",
    "tokenAdministration", "tokens", "wiki", "wit", "work"
]


def load_spec(path):
    """Load a JSON spec file, handling BOM."""
    raw = path.read_bytes()
    if raw.startswith(b'\xef\xbb\xbf'):
        raw = raw[3:]
    return json.loads(raw.decode('utf-8'))


def extract_endpoints(spec):
    """Extract all endpoint paths + methods from a Swagger spec."""
    endpoints = []
    for path, methods in spec.get("paths", {}).items():
        for method, details in methods.items():
            if method.lower() in ("get", "post", "put", "patch", "delete", "head", "options"):
                endpoints.append({
                    "path": path,
                    "method": method.upper(),
                    "operationId": details.get("operationId", ""),
                    "description": (details.get("description", "") or "")[:200].replace("\n", " ").strip(),
                    "tags": details.get("tags", [])
                })
    return endpoints


results = {}

for domain in DOMAINS:
    domain_dir = SPEC_ROOT / domain
    if not domain_dir.exists():
        results[domain] = {"error": "Directory not found", "versions": [], "endpoints": []}
        continue
    
    # Get all version directories
    versions = sorted([d.name for d in domain_dir.iterdir() if d.is_dir()])
    
    # Pick target version: prefer 7.2
    target = "7.2" if "7.2" in versions else None
    if not target:
        numeric = [v for v in versions if v and v[0].isdigit()]
        target = numeric[-1] if numeric else None
    
    if not target:
        results[domain] = {"versions": versions, "target": None, "endpoints": [], "spec_files": []}
        continue
    
    target_dir = domain_dir / target
    spec_files = sorted([f.name for f in target_dir.glob("*.json")])
    
    # Parse all spec files in this version
    all_endpoints = []
    for sf in spec_files:
        try:
            spec = load_spec(target_dir / sf)
            eps = extract_endpoints(spec)
            for ep in eps:
                ep["spec_file"] = sf
            all_endpoints.extend(eps)
        except Exception as e:
            print(f"  Error parsing {domain}/{target}/{sf}: {e}", file=sys.stderr)
    
    results[domain] = {
        "versions": versions,
        "target": target,
        "spec_files": spec_files,
        "endpoint_count": len(all_endpoints),
        "endpoints": all_endpoints
    }

# Save full JSON
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT, "w") as f:
    json.dump(results, f, indent=2)

# ── Print Summary Table ──
print("=" * 110)
print(f"{'DOMAIN':<40} {'TARGET':>6} {'SPEC_FILES':>11} {'ENDPOINTS':>10}  SPEC FILE NAMES")
print("=" * 110)

total_endpoints = 0
total_spec_files = 0
for domain in DOMAINS:
    r = results[domain]
    t = r.get("target", "-") or "-"
    sfs = r.get("spec_files", [])
    ec = r.get("endpoint_count", 0)
    total_endpoints += ec
    total_spec_files += len(sfs)
    sf_names = ", ".join(sfs) if sfs else "(none)"
    print(f"{domain:<40} {t:>6} {len(sfs):>11} {ec:>10}  {sf_names}")

print("=" * 110)
print(f"{'TOTAL':<40} {'':>6} {total_spec_files:>11} {total_endpoints:>10}")

# ── Detailed Endpoint Listing ──
print("\n\n")
print("=" * 120)
print("FULL ENDPOINT LISTING BY DOMAIN")
print("=" * 120)

for domain in DOMAINS:
    r = results[domain]
    eps = r.get("endpoints", [])
    if not eps:
        print(f"\n{'─'*80}")
        print(f"  {domain} — NO ENDPOINTS (versions: {r.get('versions', [])})")
        continue
    
    print(f"\n{'─'*80}")
    print(f"  {domain} (v{r['target']}) — {len(eps)} endpoints across {len(r['spec_files'])} spec file(s)")
    print(f"{'─'*80}")
    
    # Group by spec file
    by_file = {}
    for ep in eps:
        sf = ep.get("spec_file", "unknown")
        by_file.setdefault(sf, []).append(ep)
    
    for sf in sorted(by_file.keys()):
        if len(r["spec_files"]) > 1:
            print(f"\n  [{sf}]")
        for ep in sorted(by_file[sf], key=lambda x: (x["path"], x["method"])):
            print(f"    {ep['method']:8s} {ep['path']}")
            if ep.get("operationId"):
                print(f"             operationId: {ep['operationId']}")

print(f"\n\nTotal: {total_endpoints} endpoints across {len(DOMAINS)} domains")
print(f"Full JSON saved to: {OUTPUT}")
