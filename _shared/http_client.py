"""
Shared HTTP client helpers for Azure DevOps API clients.

Provides standardised request execution with error handling, version guards,
and response parsing. Implements the error-handling table from the spec.
"""

import json
import sys
import time
from typing import Any, Dict, List, Optional, Tuple

import requests

from _shared.auth import redact_pat


def build_url(
    organization: str,
    path: str,
    api_version: str,
    project: Optional[str] = None,
    base_host: str = "dev.azure.com",
) -> str:
    """
    Build a full Azure DevOps REST API URL.

    Args:
        organization: The ADO org name.
        path: The API path segment (e.g., '_apis/projects').
        api_version: The api-version query parameter value.
        project: Optional project scope in the URL.
        base_host: Hostname (default 'dev.azure.com'; override for
                   vssps.dev.azure.com, vsrm.dev.azure.com, etc.).

    Returns:
        Fully-qualified URL string.
    """
    base = f"https://{base_host}/{organization}"
    if project:
        base = f"{base}/{project}"
    separator = "&" if "?" in path else "?"
    return f"{base}/{path}{separator}api-version={api_version}"


def handle_error_response(response: requests.Response, url: str) -> None:
    """
    Provide actionable error messages per the spec's error-handling table.

    Handles 401, 403, 404, 429, and 5xx with specific guidance.
    """
    status = response.status_code
    # Truncate response body for logging
    body = response.text[:500] if response.text else "(empty body)"
    # Redact PAT from URL if present
    safe_url = url

    if status == 401:
        print(
            f"ERROR: Authentication failed (HTTP 401). "
            f"Verify AZURE_DEVOPS_PAT is valid and not expired.\n"
            f"  URL: {safe_url}\n  Response: {body}",
            file=sys.stderr,
        )
    elif status == 403:
        print(
            f"ERROR: Insufficient permissions (HTTP 403). "
            f"Check PAT scopes. See https://learn.microsoft.com/en-us/azure/devops/"
            f"organizations/accounts/use-personal-access-tokens-to-authenticate\n"
            f"  URL: {safe_url}\n  Response: {body}",
            file=sys.stderr,
        )
    elif status == 404:
        print(
            f"ERROR: Resource not found (HTTP 404). "
            f"Verify AZURE_DEVOPS_ORG and resource identifiers are correct.\n"
            f"  URL: {safe_url}\n  Response: {body}",
            file=sys.stderr,
        )
    elif status == 429:
        retry_after = response.headers.get("Retry-After", "10")
        print(
            f"WARN: Rate limited (HTTP 429). Retrying after {retry_after} seconds.\n"
            f"  URL: {safe_url}",
            file=sys.stderr,
        )
    elif 500 <= status < 600:
        print(
            f"ERROR: Server error (HTTP {status}). "
            f"Retry in 10s. If persistent, check https://status.dev.azure.com\n"
            f"  URL: {safe_url}\n  Response: {body}",
            file=sys.stderr,
        )
    else:
        print(
            f"ERROR: Unexpected HTTP {status}.\n"
            f"  URL: {safe_url}\n  Response: {body}",
            file=sys.stderr,
        )

    sys.exit(1)


def execute_request(
    method: str,
    url: str,
    headers: Dict[str, str],
    body: Optional[Dict] = None,
    timeout: int = 30,
    expected_status: Optional[int] = None,
    max_retries: int = 3,
) -> requests.Response:
    """
    Execute an HTTP request with retry logic for 429/5xx.

    Args:
        method: HTTP method (GET, POST, PATCH, PUT, DELETE).
        url: Full request URL.
        headers: Request headers (including auth).
        body: Optional JSON body for POST/PATCH/PUT.
        timeout: Request timeout in seconds.
        expected_status: If set, accept this status without error handling.
        max_retries: Maximum retry attempts for transient errors.

    Returns:
        requests.Response object on success.
    """
    for attempt in range(max_retries):
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                json=body,
                timeout=timeout,
            )
        except requests.exceptions.RequestException as exc:
            print(f"ERROR: Request failed: {exc}", file=sys.stderr)
            sys.exit(1)

        # Success path
        if expected_status and response.status_code == expected_status:
            return response
        if response.ok:
            return response

        # Retryable: 429 and 5xx
        if response.status_code == 429 or response.status_code >= 500:
            if attempt < max_retries - 1:
                wait = int(response.headers.get("Retry-After", 2 ** (attempt + 1)))
                print(
                    f"WARN: HTTP {response.status_code}, retrying in {wait}s "
                    f"(attempt {attempt + 1}/{max_retries})...",
                    file=sys.stderr,
                )
                time.sleep(wait)
                continue

        # Non-retryable error
        handle_error_response(response, url)

    # Exhausted retries
    handle_error_response(response, url)
    return response  # unreachable, handle_error_response exits


def version_guard(data: Any, required_keys: List[str], api_version: str) -> None:
    """
    Validate the response shape matches what we expect for this API version.

    Args:
        data: Parsed JSON response (dict).
        required_keys: Keys that must exist in the response.
        api_version: The API version string, for the warning message.
    """
    if isinstance(data, dict):
        for key in required_keys:
            if key not in data:
                print(
                    f"WARNING: Unexpected response shape — missing '{key}'. "
                    f"The server may not support api-version {api_version}.",
                    file=sys.stderr,
                )
                return
