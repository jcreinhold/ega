#!/usr/bin/env python3
"""Generate SUMMARY.md for mdBook from the volume directories.

Walks ``i/`` … ``v/`` in order, derives a short human title for each
chapter file from its filename (with a small special-case map for
front-matter / bibliography / index pages), and writes ``SUMMARY.md``
at the repo root. With ``--check`` the script exits non-zero if the
committed file is stale; this is the drift gate run in CI.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUMMARY = ROOT / "SUMMARY.md"

VOLUMES: list[tuple[str, str]] = [
    ("i", "Volume I — The Language of Schemes"),
    ("ii", "Volume II — Some Classes of Morphisms"),
    ("iii", "Volume III — Cohomology of Coherent Sheaves"),
    ("iv", "Volume IV — Local Study of Schemes and Morphisms"),
    ("v", "Volume V — Construction of Schemes (unpublished)"),
]

SPECIAL_TITLES: dict[str, str] = {
    "00-front-matter": "Front matter",
    "00-front-matter-part-1": "Front matter (part 1)",
    "13-front-matter-part-2": "Front matter (part 2)",
    "20-front-matter-part-3": "Front matter (part 3)",
    "28-front-matter-part-4": "Front matter (part 4)",
    "bibliography": "Bibliography",
    "glossary": "Translation glossary",
    "conventions": "Translation conventions",
    "translation-ledger": "Translation ledger",
    "index-notation": "Index of notation",
    "index-of-notations": "Index of notations",
    "index-terminology": "Index of terminology",
    "index-of-terminology": "Index of terminology",
}

PREFIX_RE = re.compile(r"^\d+[a-z]?-")


def derive_title(stem: str) -> str:
    if stem in SPECIAL_TITLES:
        return SPECIAL_TITLES[stem]
    body = stem
    while PREFIX_RE.match(body):
        body = PREFIX_RE.sub("", body, count=1)
    # ``ch0-08-representable-functors`` → ``Ch.0 §8. Representable functors``
    m = re.match(r"ch(\d+)-(\d+)-(.+)$", body)
    if m:
        chap, sec, rest = m.groups()
        prefix = f"Ch.{chap} §{int(sec)}."
        return f"{prefix} {rest.replace('-', ' ').capitalize()}"
    return body.replace("-", " ").capitalize()


BACK_MATTER_STEMS = {
    "bibliography",
    "glossary",
    "conventions",
    "translation-ledger",
    "index-notation",
    "index-of-notations",
    "index-terminology",
    "index-of-terminology",
}


def sort_key(path: Path) -> tuple[int, str]:
    stem = path.stem
    if "front-matter" in stem:
        bucket = 0
    elif stem in BACK_MATTER_STEMS:
        bucket = 2
    else:
        bucket = 1
    return bucket, stem


def volume_entries(vol: str) -> list[tuple[str, Path]]:
    vol_dir = ROOT / vol
    skip = {"README.md"}
    paths = sorted(
        (p for p in vol_dir.glob("*.md") if p.name not in skip),
        key=sort_key,
    )
    return [(derive_title(p.stem), p.relative_to(ROOT)) for p in paths]


def render() -> str:
    lines: list[str] = ["# Summary", "", "[Introduction](index.md)", ""]
    for vol, label in VOLUMES:
        lines.append(f"# {label}")
        lines.append("")
        for title, rel in volume_entries(vol):
            lines.append(f"- [{title}]({rel.as_posix()})")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if SUMMARY.md does not match the generated output.",
    )
    args = parser.parse_args()

    new = render()
    if args.check:
        current = SUMMARY.read_text() if SUMMARY.exists() else ""
        if current != new:
            print(
                "SUMMARY.md is out of date. Run scripts/generate-summary.py.",
                file=sys.stderr,
            )
            return 1
        return 0
    SUMMARY.write_text(new)
    return 0


if __name__ == "__main__":
    sys.exit(main())
