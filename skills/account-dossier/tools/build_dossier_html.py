"""Render an account dossier .md into branded HTML.

Usage
    python build_dossier_html.py <account-slug> [source-md] [output-stem]

    <account-slug>  folder under the dossiers root, and the default output stem
    [source-md]     alternate markdown inside that folder, e.g. dossier-2026-08-04.md
    [output-stem]   alternate output name, so a dated build never overwrites a
                    standing one

Paths
    dossiers root   {output_folder}/work/dossiers/            (override: DOSSIER_ROOT)
    html output     {output_folder}/work/dossiers-html/       (override: DOSSIER_HTML)

Branding
    The render is unbranded by default. Set DOSSIER_LOGO to a filename or URL
    to place a logo in the header and footer, e.g. DOSSIER_LOGO=acme-logo.png.
    A relative value resolves against the html output folder, so drop the image
    in beside the generated pages. Unset means no <img> is emitted at all.

Notes
    Styling lives in assets/dossier.css next to this file. If a sibling .html
    already exists in the output folder its <style> block is reused instead, so a
    project that has diverged keeps its own look.

Requires: markdown (pip install markdown)
"""

import os
import re
import sys
from pathlib import Path

import markdown

TOOLS = Path(__file__).resolve().parent
DEFAULT_ROOT = Path.cwd() / "output" / "work" / "dossiers"
DEFAULT_HTML = Path.cwd() / "output" / "work" / "dossiers-html"

ROOT = Path(os.environ.get("DOSSIER_ROOT", DEFAULT_ROOT))
OUT_DIR = Path(os.environ.get("DOSSIER_HTML", DEFAULT_HTML))

# Unbranded by default; a consuming project opts in via DOSSIER_LOGO.
LOGO = os.environ.get("DOSSIER_LOGO", "").strip()


def read_css() -> str:
    """Prefer a sibling render's style block, so a diverged project keeps its look."""
    for sibling in sorted(OUT_DIR.glob("*.html")):
        html = sibling.read_text(encoding="utf-8", errors="replace")
        if "<style>" in html and "</style>" in html:
            return html[html.index("<style>") + len("<style>"): html.index("</style>")]
    return (TOOLS / "assets" / "dossier.css").read_text(encoding="utf-8")


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return {}, text
    end = text.index("\n---", 3)
    meta = {}
    for line in text[3:end].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, text[end + 4:].lstrip("\n")


def wrap_tables(html: str) -> str:
    """Tables scroll inside their own container instead of pushing the page wide.

    A key/value table written with an empty header row would otherwise render as a
    bare navy bar, so drop any thead that carries no text.
    """
    html = re.sub(
        r"<thead>\s*<tr>(?:\s*<th[^>]*>\s*</th>)+\s*</tr>\s*</thead>", "", html
    )
    return html.replace("<table>", '<div class="tablewrap"><table>').replace(
        "</table>", "</table></div>"
    )


RINGS = (
    '<svg class="rings" viewBox="0 0 200 200" aria-hidden="true">'
    + "".join(
        f'<circle cx="100" cy="100" r="{r}" fill="none" stroke="url(#rg)" stroke-width="1.4"/>'
        for r in (30, 46, 62, 78, 94)
    )
    + '<defs><linearGradient id="rg" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0" stop-color="#0000FF"/><stop offset="1" stop-color="#00FFFF"/>'
    "</linearGradient></defs></svg>"
)


def build(slug: str, source: str | None = None, out: str | None = None) -> Path:
    md_path = ROOT / slug / (source or "dossier.md")
    body_md = md_path.read_text(encoding="utf-8")
    meta, body_md = split_frontmatter(body_md)

    # The H1 and the "how to read this" note become the hero, so drop them from
    # the article rather than saying the same thing twice.
    body_md = re.sub(r"^# .*?\n", "", body_md, count=1, flags=re.M)
    intro = ""
    m = re.match(r"\s*\*\*How to read this\.\*\*(.*?)\n\n---\n", body_md, flags=re.S)
    if m:
        intro = markdown.markdown(" ".join(m.group(1).split()))
        intro = re.sub(r"^<p>|</p>$", "", intro.strip())
        body_md = body_md[m.end():]

    article = wrap_tables(
        markdown.markdown(body_md, extensions=["tables", "sane_lists", "attr_list"])
    )

    tier = meta.get("action_tier", "B")
    title = meta.get("account", slug)
    chips = "".join(
        f'<span class="chip"><span class="lbl">{label}</span> <b>{value}</b></span>'
        for label, value in (
            ("Fit", meta.get("fit", "")),
            ("Timing", meta.get("timing", "")),
            ("Offering", meta.get("lead_offering", "")),
            ("Prepared", meta.get("created", "")),
        )
        if value
    )

    # `not_to_be_confused_with` stays internal metadata. Naming the other company
    # in the reader's view plants the confusion it exists to prevent.
    # See reference/third-parties.md.

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    logo_header = f'<img class="logo" src="{LOGO}" alt="">' if LOGO else ""
    logo_footer = f'<img src="{LOGO}" alt="">' if LOGO else ""
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Account dossier</title>
<style>{read_css()}</style>
</head><body>
<div class="toprule"></div>
<header class="site">
  {logo_header}
  <nav><a href="index.html">&larr; All dossiers</a></nav>
</header>

<main class="wrap">
  <section class="hero">{RINGS}
    <div class="hero-inner">
      <div class="chips"><span class="pill {tier}">Tier {tier}</span></div>
      <h1 class="title">{title}</h1>
      <div class="under"></div>
      <div class="chips">{chips}</div>
      <p class="rec">{intro}</p>
    </div>
  </section>
  <article class="md">{article}</article>
</main>
<footer class="site"><div class="fwrap">
  {logo_footer}
  <div class="tag">Account dossier, prepared {meta.get('created', '')}.</div>
</div></footer>
</body></html>
"""

    out_path = OUT_DIR / f"{out or slug}.html"
    out_path.write_text(html, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    print(build(*sys.argv[1:4]))
