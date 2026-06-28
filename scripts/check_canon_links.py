#!/usr/bin/env python3
"""Check local Markdown links in the CRT Canon."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

REPO_ROOT = Path(__file__).resolve().parents[1]
CANON_ROOT = REPO_ROOT / "canon"
LINK_RE = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")


def is_local_link(target: str) -> bool:
    parsed = urlparse(target)
    return parsed.scheme == "" and parsed.netloc == "" and not target.startswith("#")


def normalize_target(raw_target: str) -> str:
    target = raw_target.strip()
    if not target:
        return target
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        # Drop optional Markdown title after whitespace.
        target = target.split()[0]
    return unquote(target.split("#", 1)[0])


def main() -> int:
    failures: list[str] = []
    checked = 0

    for markdown_file in sorted(CANON_ROOT.rglob("*.md")):
        text = markdown_file.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = normalize_target(match.group(1))
            if not target or not is_local_link(target):
                continue
            checked += 1
            resolved = (markdown_file.parent / target).resolve()
            try:
                resolved.relative_to(REPO_ROOT)
            except ValueError:
                failures.append(f"{markdown_file.relative_to(REPO_ROOT)} -> {target} escapes repository")
                continue
            if not resolved.exists():
                failures.append(f"{markdown_file.relative_to(REPO_ROOT)} -> {target}")

    if failures:
        print("FAIL canon link check: broken local Markdown links found")
        for failure in failures:
            print(f" - {failure}")
        return 1

    print(f"PASS canon link check: {checked} local Markdown links verified")
    return 0


if __name__ == "__main__":
    sys.exit(main())
