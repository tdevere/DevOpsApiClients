#!/usr/bin/env python3
"""Generate a comprehensive markdown report of all Azure DevOps 7.2 API endpoints."""

import json

with open("/workspaces/DevOpsApiClients/_research/api_specs_full.json") as f:
    data = json.load(f)

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

lines = []
lines.append("# Azure DevOps REST API 7.2 — Complete Endpoint Inventory")
lines.append("")
lines.append("Generated from: `MicrosoftDocs/vsts-rest-api-specs` (master branch)")
lines.append("")

# Summary table
lines.append("## Summary")
lines.append("")
lines.append("| # | Domain | Version | Spec Files | Endpoints |")
lines.append("|---|--------|---------|------------|-----------|")

total = 0
for i, d in enumerate(DOMAINS, 1):
    r = data.get(d, {})
    t = r.get("target", "-") or "-"
    sc = len(r.get("spec_files", []))
    ec = r.get("endpoint_count", 0)
    total += ec
    anchor = d.lower()
    lines.append(f"| {i} | [{d}](#{anchor}) | {t} | {sc} | {ec} |")

lines.append(f"| | **TOTAL** | | | **{total}** |")
lines.append("")

# Detailed per-domain
for d in DOMAINS:
    r = data.get(d, {})
    t = r.get("target", "-") or "-"
    versions = r.get("versions", [])
    spec_files = r.get("spec_files", [])
    eps = r.get("endpoints", [])
    
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## {d}")
    lines.append(f"")
    lines.append(f"- **Target Version**: {t}")
    lines.append(f"- **All Versions**: {', '.join(versions) if versions else 'none'}")
    lines.append(f"- **Spec Files**: {', '.join(spec_files) if spec_files else 'none'}")
    lines.append(f"- **Endpoint Count**: {len(eps)}")
    lines.append(f"")
    
    if not eps:
        lines.append("*No endpoints found in spec.*")
        lines.append("")
        continue
    
    # Group by spec file
    by_file = {}
    for ep in eps:
        sf = ep.get("spec_file", "unknown")
        by_file.setdefault(sf, []).append(ep)
    
    for sf in sorted(by_file.keys()):
        if len(spec_files) > 1:
            lines.append(f"### {sf}")
            lines.append("")
        
        lines.append("| Method | Path | Operation ID |")
        lines.append("|--------|------|-------------|")
        
        for ep in sorted(by_file[sf], key=lambda x: (x["path"], x["method"])):
            m = ep["method"]
            p = ep["path"]
            oid = ep.get("operationId", "")
            lines.append(f"| {m} | `{p}` | {oid} |")
        
        lines.append("")

report = "\n".join(lines)

with open("/workspaces/DevOpsApiClients/_research/api_endpoint_inventory.md", "w") as f:
    f.write(report)

print(f"Report written: {len(lines)} lines, {total} endpoints across {len(DOMAINS)} domains")
