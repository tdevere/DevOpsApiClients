"""
Shared logging utilities for Azure DevOps API clients.

Provides dual-format logging (.log human-readable + .json structured),
PAT redaction, and GitHub Actions annotation support.
"""

import datetime
import json
import os
import sys
from pathlib import Path
from typing import Optional

from _shared.auth import redact_pat

# Log output directory — created automatically, should be .gitignored
LOG_DIR = Path(__file__).resolve().parents[1] / "logs"


def _ensure_log_dir() -> Path:
    """Create the logs/ directory if it doesn't exist."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    return LOG_DIR


def _timestamp() -> str:
    """Return the current UTC time in ISO-8601 format."""
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def _redact_message(message: str, pat: Optional[str] = None) -> str:
    """Redact any PAT occurrences in the message."""
    if pat and len(pat) > 4:
        message = message.replace(pat, redact_pat(pat))
    # Also try to catch PATs from environment
    env_pat = os.environ.get("AZURE_DEVOPS_PAT", "")
    if env_pat and len(env_pat) > 4 and env_pat in message:
        message = message.replace(env_pat, redact_pat(env_pat))
    return message


class AdoLogger:
    """
    Dual-format logger for Azure DevOps API client scripts.

    Writes to:
      - logs/<operation>.log  (human-readable)
      - logs/<operation>.json (structured, one JSON object per line)
      - stderr (always)
      - GitHub Actions annotations when CI=true
    """

    def __init__(self, operation: str, pat: Optional[str] = None):
        self.operation = operation
        self.pat = pat or os.environ.get("AZURE_DEVOPS_PAT", "")
        self._ci_mode = os.environ.get("CI", "").lower() == "true"
        self._log_dir = _ensure_log_dir()
        self._log_file = self._log_dir / f"{operation}.log"
        self._json_file = self._log_dir / f"{operation}.json"

    def _write(self, level: str, message: str) -> None:
        """Write a log entry to all outputs."""
        safe_msg = _redact_message(message, self.pat)
        ts = _timestamp()

        # Human-readable log
        log_line = f"[{ts}] [{level}] {safe_msg}\n"
        with open(self._log_file, "a", encoding="utf-8") as f:
            f.write(log_line)

        # Structured JSON log
        entry = {
            "timestamp": ts,
            "level": level,
            "operation": self.operation,
            "message": safe_msg,
        }
        with open(self._json_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")

        # Console output
        print(f"[{level}] {safe_msg}", file=sys.stderr)

        # GitHub Actions annotations
        if self._ci_mode:
            if level == "ERROR":
                print(f"::error::{safe_msg}")
            elif level == "WARN":
                print(f"::warning::{safe_msg}")

    def info(self, message: str) -> None:
        """Log at INFO level."""
        self._write("INFO", message)

    def warn(self, message: str) -> None:
        """Log at WARN level."""
        self._write("WARN", message)

    def error(self, message: str) -> None:
        """Log at ERROR level."""
        self._write("ERROR", message)
