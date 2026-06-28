#!/usr/bin/env python3
"""Check CRT Canon claim IDs against the central claim registry."""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CANON_ROOT = REPO_ROOT / "canon"
CHAPTERS_ROOT = CANON_ROOT / "chapters"
CLAIMS_FILE = CANON_ROOT / "CLAIMS.md"
CLAIM_ID_RE = re.compile(r"CRT-[A-Z0-9-]+-[0-9]{3}")


def rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def scan_chapter_claim_ids() -> dict[str, list[str]]:
    locations: dict[str, list[str]] = defaultdict(list)
    for chapter_file in sorted(CHAPTERS_ROOT.glob("**/*.md")):
        text = chapter_file.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in CLAIM_ID_RE.finditer(line):
                locations[match.group(0)].append(f"{rel(chapter_file)}:{line_number}")
    return dict(locations)


def scan_registry_claim_ids() -> tuple[list[str], dict[str, list[int]]]:
    ids: list[str] = []
    locations: dict[str, list[int]] = defaultdict(list)
    for line_number, line in enumerate(CLAIMS_FILE.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells or cells[0] in {"Claim ID", "---"}:
            continue
        matches = CLAIM_ID_RE.findall(cells[0])
        for claim_id in matches:
            ids.append(claim_id)
            locations[claim_id].append(line_number)
    return ids, dict(locations)


def main() -> int:
    if not CLAIMS_FILE.exists():
        print(f"FAIL canon claim ID check: missing {rel(CLAIMS_FILE)}")
        return 1

    chapter_locations = scan_chapter_claim_ids()
    registry_ids, registry_locations = scan_registry_claim_ids()
    registry_counts = Counter(registry_ids)

    failures: list[str] = []

    for claim_id in sorted(chapter_locations):
        count = registry_counts[claim_id]
        if count == 0:
            failures.append(
                f"chapter claim ID missing from registry: {claim_id} "
                f"({', '.join(chapter_locations[claim_id])})"
            )
        elif count > 1:
            failures.append(
                f"chapter claim ID appears {count} times in registry: {claim_id} "
                f"({', '.join(f'{rel(CLAIMS_FILE)}:{line}' for line in registry_locations[claim_id])})"
            )

    for claim_id, count in sorted(registry_counts.items()):
        if count > 1:
            failures.append(
                f"duplicate registry claim ID: {claim_id} "
                f"({', '.join(f'{rel(CLAIMS_FILE)}:{line}' for line in registry_locations[claim_id])})"
            )
        if claim_id not in chapter_locations:
            failures.append(
                f"registry claim ID absent from chapters: {claim_id} "
                f"({', '.join(f'{rel(CLAIMS_FILE)}:{line}' for line in registry_locations[claim_id])})"
            )

    if failures:
        print("FAIL canon claim ID check: registry and chapter claim IDs drifted")
        for failure in failures:
            print(f" - {failure}")
        return 1

    print(
        "PASS canon claim ID check: "
        f"{len(chapter_locations)} chapter claim IDs match "
        f"{len(registry_ids)} registry entries"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
