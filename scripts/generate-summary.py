#!/usr/bin/env python3
"""Generate SUMMARY.md for the EGA mdBook from the installment directories.

The top level is the published installment (EGA I … EGA V). Within each
installment, section files are grouped under their chapter as a nested,
collapsible list so the two-level structure of the work is visible in the
sidebar. Chapter numbers are arabic (0–5); the installment numerals stay roman
because that is how the work is cited.

A chapter that has an intro / landing page links its heading to that page; a
chapter without one — the Chapter 0 continuations carried by EGA III and IV, and
the single-chapter installments — renders as a non-clickable heading (an mdBook
"draft" item) that still groups its sections.

Two filename schemes coexist and both are parsed here:

  * EGA I, II      ``CC-SS-slug.md``      CC = chapter, SS = section (00 = landing)
  * EGA III, IV, V ``NN-chC-SS-slug.md``  NN = reading order, chC = chapter,
                                          SS = section (00 = intro)

Section labels are read from each file's own ``§N.`` heading so the sidebar entry
matches the page heading exactly, whatever level that heading sits at. With
``--check`` the script exits non-zero if the committed SUMMARY.md is stale; this
is the drift gate run in CI.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUMMARY = ROOT / "SUMMARY.md"

# Installment directory → top-level (part) header. The title is the official
# title of the installment, which coincides with its principal chapter's title.
INSTALLMENTS: list[tuple[str, str]] = [
    ("i", "EGA I — The Language of Schemes"),
    ("ii", "EGA II — Elementary Global Study of Some Classes of Morphisms"),
    ("iii", "EGA III — Cohomological Study of Coherent Sheaves"),
    ("iv", "EGA IV — Local Study of Schemes and Morphisms of Schemes"),
    ("v", "EGA V — Construction of Schemes (unpublished)"),
]

# Chapter number → chapter title (used for the grouping heading in the sidebar).
CHAPTER_TITLES: dict[int, str] = {
    0: "Preliminaries",
    1: "The Language of Schemes",
    2: "Elementary Global Study of Some Classes of Morphisms",
    3: "Cohomological Study of Coherent Sheaves",
    4: "Local Study of Schemes and Morphisms of Schemes",
    5: "Construction of Schemes",
}

# Chapter 0 is carried across several installments; mark the later slices.
CONTINUATION = {("iii", 0), ("iv", 0)}

SPECIAL_TITLES: dict[str, str] = {
    "bibliography": "Bibliography",
    "glossary": "Translation glossary",
    "conventions": "Translation conventions",
    "translation-ledger": "Translation ledger",
    "index-notation": "Index of notation",
    "index-of-notations": "Index of notations",
    "index-terminology": "Index of terminology",
    "index-of-terminology": "Index of terminology",
}

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

SCHEME_B = re.compile(r"^\d+[a-z]?-ch(\d+)-(\d+)-")  # NN-chC-SS-slug (EGA III/IV/V)
SCHEME_A = re.compile(r"^(\d+)-(\d+)-")  # CC-SS-slug (EGA I/II)
SECTION_HEADING = re.compile(r"^#{1,6}\s*(§.*\S)\s*$")


def chapter_section(stem: str) -> tuple[int | None, int | None]:
    """(chapter, section) from a filename stem, or (None, None) if not a chapter file."""
    m = SCHEME_B.match(stem) or SCHEME_A.match(stem)
    if m:
        return int(m.group(1)), int(m.group(2))
    return None, None


def section_label(path: Path) -> str | None:
    """The first ``§…`` heading's text, ignoring fenced code. Matches the page."""
    in_fence = False
    for line in path.read_text().splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = SECTION_HEADING.match(line)
        if m:
            return m.group(1).strip()
    return None


def slug_label(stem: str) -> str:
    """Fallback title for a file with no ``§`` heading (e.g. a split part 2)."""
    body = re.sub(r"^\d+[a-z]?-", "", stem)  # leading NN- / CC-
    body = re.sub(r"^ch\d+-", "", body)  # chC-
    body = re.sub(r"^\d+-", "", body)  # SS-
    return body.replace("-", " ").strip().capitalize()


def loose_title(path: Path) -> str:
    """Title for a front/back-matter page (special-cased, else slug-derived)."""
    return SPECIAL_TITLES.get(path.stem, slug_label(path.stem))


def installment(vol: str) -> tuple[list[Path], OrderedDict[int, dict], list[Path]]:
    """Partition an installment's files into front matter, chapters, back matter."""
    vol_dir = ROOT / vol
    front: list[Path] = []
    back: list[Path] = []
    chapters: OrderedDict[int, dict] = OrderedDict()
    for path in sorted(vol_dir.glob("*.md"), key=lambda p: p.stem):
        stem = path.stem
        if stem == "README":
            continue
        if "front-matter" in stem:
            front.append(path)
            continue
        if stem in BACK_MATTER_STEMS:
            back.append(path)
            continue
        chap, sec = chapter_section(stem)
        if chap is None:
            # Not a recognised chapter file; keep it visible as a loose entry.
            chapters.setdefault(-1, {"landing": None, "sections": []})[
                "sections"
            ].append((10**6, loose_title(path), path))
            continue
        entry = chapters.setdefault(chap, {"landing": None, "sections": []})
        if sec == 0:
            entry["landing"] = path
        else:
            label = section_label(path) or slug_label(stem)
            entry["sections"].append((sec, label, path))
    return front, chapters, back


def render() -> str:
    lines: list[str] = ["# Summary", "", "[Introduction](index.md)", ""]
    for vol, header in INSTALLMENTS:
        lines.append(f"# {header}")
        lines.append("")
        front, chapters, back = installment(vol)
        # Front-matter pages are the volume's landing pages, so they get the
        # installment's full title (with a part suffix when the front matter
        # is split) instead of a generic "Front matter" label.
        multi_front = len(front) > 1
        for i, path in enumerate(front):
            rel = path.relative_to(ROOT).as_posix()
            label = f"{header} (part {i + 1})" if multi_front else header
            lines.append(f"- [{label}]({rel})")
        for chap, data in chapters.items():
            cont = " (cont.)" if (vol, chap) in CONTINUATION else ""
            title = f"Chapter {chap} — {CHAPTER_TITLES.get(chap, '')}{cont}"
            if data["landing"] is not None:
                rel = data["landing"].relative_to(ROOT).as_posix()
                lines.append(f"- [{title}]({rel})")
            else:
                lines.append(f"- [{title}]()")  # mdBook draft: groups, not clickable
            for _sec, label, path in sorted(
                data["sections"], key=lambda t: (t[0], t[2].stem)
            ):
                rel = path.relative_to(ROOT).as_posix()
                lines.append(f"  - [{label}]({rel})")
        for path in back:
            rel = path.relative_to(ROOT).as_posix()
            lines.append(f"- [{loose_title(path)}]({rel})")
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
