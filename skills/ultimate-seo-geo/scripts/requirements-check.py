#!/usr/bin/env python3
"""
Verify Python packages needed by most audit scripts (requests, beautifulsoup4).

Usage:
    python scripts/requirements-check.py
    python scripts/requirements-check.py --json
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

# (PyPI distribution name, import name to probe)
REQUIRED = (
    ("requests", "requests"),
    ("beautifulsoup4", "bs4"),
)

ROOT = Path(__file__).resolve().parent.parent
REQ_FILE = ROOT / "requirements.txt"


def _has_module(import_name: str) -> bool:
    return importlib.util.find_spec(import_name) is not None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check that audit-script dependencies are installed."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit one JSON object on stdout (exit 1 if anything missing)",
    )
    args = parser.parse_args()

    missing = [pypi for pypi, imp in REQUIRED if not _has_module(imp)]

    if REQ_FILE.is_file():
        hint = (
            "pip install -r requirements.txt  "
            "(from repo root; PEP 668 e.g. Homebrew: "
            "python3 -m venv .venv && .venv/bin/pip install -r requirements.txt)"
        )
    else:
        hint = "pip install requests beautifulsoup4"

    if args.json:
        payload: dict = {
            "ok": len(missing) == 0,
            "python": sys.version.split()[0],
            "checked": [{"pypi": p, "import": i} for p, i in REQUIRED],
        }
        if missing:
            payload["missing"] = missing
            payload["hint"] = hint
        print(json.dumps(payload))
        return 0 if not missing else 1

    if not missing:
        print("OK: requests and beautifulsoup4 (bs4) are importable.")
        return 0

    print("Missing:", ", ".join(missing), file=sys.stderr)
    print(hint, file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
