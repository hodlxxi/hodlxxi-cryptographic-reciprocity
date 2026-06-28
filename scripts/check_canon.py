#!/usr/bin/env python3
"""Run all CRT Canon maintenance checks."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CHECKS = (
    ("Canon Markdown links", "scripts/check_canon_links.py"),
    ("Canon claim IDs", "scripts/check_canon_claim_ids.py"),
)


def run_check(label: str, script: str) -> int:
    print(f"\n=== {label} ===", flush=True)
    result = subprocess.run([sys.executable, script], cwd=REPO_ROOT, check=False)
    return result.returncode


def main() -> int:
    failures: list[tuple[str, int]] = []

    for label, script in CHECKS:
        returncode = run_check(label, script)
        if returncode != 0:
            failures.append((label, returncode))

    print("\n=== Canon maintenance summary ===", flush=True)
    if failures:
        print("FAIL canon maintenance checks")
        for label, returncode in failures:
            print(f" - {label}: exit {returncode}")
        return failures[0][1]

    print(f"PASS canon maintenance checks: {len(CHECKS)} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
