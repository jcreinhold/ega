#!/usr/bin/env python3
"""Post-process the built EGA mdBook site for search engines.

Run after `mdbook build`. Does two things:

  1. Rewrites canonical / og:url URLs. mdBook's `{{path}}` template variable
     is the *source* (.md) path, so the `<link rel="canonical">` emitted by
     theme/head.hbs points at `….md`; rewrite it to the served `.html` URL.
  2. Writes sitemap.xml (canonical URLs of all public HTML pages) and
     robots.txt (allow crawling, advertise the sitemap).

Excluded from the sitemap:
  * 404.html — GitHub Pages error page, not indexable content.
  * print.html — mdBook's whole-book print view: duplicate content of every
    chapter on one URL.
  * toc.html — mdBook's noscript table-of-contents fallback: thin duplicate
    of the sidebar, and mdBook itself marks it noindex.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_ROOT = "https://jcreinhold.github.io/ega/"
EXCLUDE = {"404.html", "print.html", "toc.html"}

# Canonical / og:url URLs emitted from `{{path}}` end in the source `.md`
# suffix; the served page is the same path with `.html`.
MD_URL = re.compile(rf'({re.escape(SITE_ROOT)}[^"]+)\.md(")', flags=re.ASCII)

ROBOTS = f"""\
User-agent: *
Allow: /

Sitemap: {SITE_ROOT}sitemap.xml
"""


def html_pages(build_dir: Path) -> list[str]:
    """Site-root-relative URLs of all public HTML pages, sorted."""
    urls = []
    for path in sorted(build_dir.rglob("*.html")):
        rel = path.relative_to(build_dir).as_posix()
        if rel in EXCLUDE:
            continue
        urls.append(rel)
    return urls


def fix_canonical_urls(build_dir: Path) -> int:
    """Rewrite `.md` canonical/og:url URLs to `.html` in every built page."""
    fixed = 0
    for path in build_dir.rglob("*.html"):
        text = path.read_text()
        new = MD_URL.sub(r"\1.html\2", text)
        if new != text:
            path.write_text(new)
            fixed += 1
    return fixed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--build-dir",
        default="book",
        help="mdBook build directory (default: book).",
    )
    args = parser.parse_args()
    build_dir = (ROOT / args.build_dir).resolve()
    if not build_dir.is_dir():
        raise SystemExit(
            f"build directory not found: {build_dir} (run `mdbook build` first)"
        )

    fixed = fix_canonical_urls(build_dir)
    urls = html_pages(build_dir)
    sitemap = "\n".join(
        [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
            *(f"  <url><loc>{SITE_ROOT}{u}</loc></url>" for u in urls),
            "</urlset>",
            "",
        ]
    )
    (build_dir / "sitemap.xml").write_text(sitemap)
    (build_dir / "robots.txt").write_text(ROBOTS)
    print(
        f"rewrote canonical URLs in {fixed} pages; "
        f"wrote {build_dir / 'sitemap.xml'} ({len(urls)} URLs) and {build_dir / 'robots.txt'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
