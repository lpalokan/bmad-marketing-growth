"""Render an account dossier .md into branded HTML.

Usage
    python build_dossier_html.py <account-slug> [source-md] [output-stem]
    python build_dossier_html.py --check [path ...]
    python build_dossier_html.py --repair [path ...]

    <account-slug>  folder under the dossiers root, and the default output stem
    [source-md]     alternate markdown inside that folder, e.g. dossier-2026-08-04.md
    [output-stem]   alternate output name, so a dated build never overwrites a
                    standing one

    --check         report mojibake in the dossier markdown and the rendered
                    pages, and exit non-zero if any is found. Takes explicit
                    paths, or scans both folders when given none.
    --repair        the same scan, writing the repaired text back as UTF-8.

Paths
    dossiers root   {output_folder}/work/dossiers/            (override: DOSSIER_ROOT)
    html output     {output_folder}/work/dossiers-html/       (override: DOSSIER_HTML)

Branding
    The render is unbranded by default. Set DOSSIER_LOGO to a filename or URL
    to place a logo in the header and footer, e.g. DOSSIER_LOGO=acme-logo.png.
    A relative value resolves against the html output folder, so drop the image
    in beside the generated pages. Unset means no <img> is emitted at all.

Encoding
    Every file this tool reads and writes is UTF-8. Scandinavian and Finnish
    text is the normal case, not the exception, so the build refuses to leave a
    page in which "ä" has become "Ã¤".

    That corruption never comes from this script. It comes from a later step
    that reads the finished page in the system codepage and saves it as UTF-8.
    On Windows PowerShell 5.1, `Get-Content page.html | ... > page.html` does
    exactly that, and so does any Set-Content without `-Encoding utf8`. Do not
    post-process a rendered page through the shell. Re-render it instead, or
    edit the markdown and re-render.

Notes
    Styling lives in assets/dossier.css next to this file. If a sibling .html
    already exists in the output folder its <style> block is reused instead, so a
    project that has diverged keeps its own look.

Requires: markdown (pip install markdown)
"""

import codecs
import os
import re
import sys
from pathlib import Path

import markdown

# A Nordic name in a progress line must not be able to kill the build on a
# console that cannot spell it. Report what the console can, and carry on.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(errors="replace")
    except (AttributeError, ValueError):
        pass

TOOLS = Path(__file__).resolve().parent
DEFAULT_ROOT = Path.cwd() / "output" / "work" / "dossiers"
DEFAULT_HTML = Path.cwd() / "output" / "work" / "dossiers-html"

ROOT = Path(os.environ.get("DOSSIER_ROOT", DEFAULT_ROOT))
OUT_DIR = Path(os.environ.get("DOSSIER_HTML", DEFAULT_HTML))

# Unbranded by default; a consuming project opts in via DOSSIER_LOGO.
LOGO = os.environ.get("DOSSIER_LOGO", "").strip()


# --- encoding guard -------------------------------------------------------
#
# One pass of the damage is: UTF-8 bytes read back through a single-byte
# codepage, then saved as UTF-8 again. It is reversible, because the wrong
# decode is lossless for the codepages that cause it. Encoding the text back to
# that codepage and decoding it as UTF-8 undoes the pass.
#
# The test for "is this file damaged" is the repair itself. A clean document
# either fails to encode to the single-byte codepage, or produces bytes that
# are not valid UTF-8, so it comes back unchanged. Only text that really is a
# UTF-8 stream wearing the wrong decoding survives the whole round trip.

def repair_mojibake(text: str) -> str:
    """Undo any number of wrong-codepage round trips. A clean string is returned as is."""
    for _ in range(4):
        nxt = _undo_one_pass(text)
        if nxt is None:
            return text
        text = nxt
    return text


def _windows_hole(exc):
    """cp1252 leaves five byte values undefined. Windows reads them as C1 controls."""
    chars = exc.object[exc.start:exc.end]
    if all(ord(c) in (0x81, 0x8D, 0x8F, 0x90, 0x9D) for c in chars):
        return bytes(ord(c) for c in chars), exc.end
    raise exc


codecs.register_error("dossier_cp1252_holes", _windows_hole)


def _undo_one_pass(text: str) -> str | None:
    for codepage, errors in (("cp1252", "dossier_cp1252_holes"), ("latin-1", "strict")):
        try:
            raw = text.encode(codepage, errors)
        except UnicodeEncodeError:
            continue
        try:
            fixed = raw.decode("utf-8")
        except UnicodeDecodeError:
            continue
        if fixed != text:
            return fixed
    return None


def is_mojibake(text: str) -> bool:
    return repair_mojibake(text) != text


def read_utf8(path: Path, *, label: str = "") -> str:
    """Read as UTF-8 and repair a wrong-codepage round trip rather than carrying it forward."""
    text = path.read_text(encoding="utf-8")
    fixed = repair_mojibake(text)
    if fixed != text:
        where = label or str(path)
        print(
            f"warning: {where} was saved through the wrong codepage, so its "
            f"Nordic letters are mangled. Repaired for this build. "
            f"Run --repair to fix the file itself.",
            file=sys.stderr,
        )
    return fixed


def scan(paths, repair: bool) -> int:
    """Report, and optionally fix, wrong-codepage damage. Returns the count of bad files."""
    bad = 0
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            bad += 1
            print(f"NOT UTF-8  {path}: {exc}", file=sys.stderr)
            continue
        fixed = repair_mojibake(text)
        if fixed == text:
            continue
        bad += 1
        if repair:
            path.write_text(fixed, encoding="utf-8")
            print(f"repaired   {path}")
        else:
            sample = sorted({m for m in re.findall(r"\w*[Â-ô][-¿–’“”†…€™]\w*", text)})[:3]
            print(f"mojibake   {path}  e.g. {', '.join(sample) or '(punctuation only)'}")
    return bad


def default_scan_paths():
    return sorted(ROOT.glob("*/*.md")) + sorted(OUT_DIR.glob("*.html"))


# --- render ---------------------------------------------------------------

def read_css() -> str:
    """Prefer a sibling render's style block, so a diverged project keeps its look."""
    for sibling in sorted(OUT_DIR.glob("*.html")):
        try:
            html = sibling.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue  # a page saved in the wrong encoding is not a style source
        if "<style>" in html and "</style>" in html:
            css = html[html.index("<style>") + len("<style>"): html.index("</style>")]
            return repair_mojibake(css)
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
    body_md = read_utf8(md_path)
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
<title>{title} &middot; Account dossier</title>
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

    # Read the page back the way a browser will. A build that cannot prove its
    # own output is clean UTF-8 is a failed build, not a page to go and inspect.
    written = out_path.read_text(encoding="utf-8")
    if is_mojibake(written):
        raise SystemExit(f"{out_path} was written with mangled characters. Not usable.")
    return out_path


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] in ("--check", "--repair"):
        targets = [Path(a) for a in args[1:]] or default_scan_paths()
        count = scan(targets, repair=args[0] == "--repair")
        if args[0] == "--check" and count:
            sys.exit(f"{count} file(s) hold mojibake. Run --repair, or re-render.")
        print(f"{'repaired' if args[0] == '--repair' else 'checked'} {len(targets)} file(s), {count} affected.")
        sys.exit(0)
    if not args:
        sys.exit(__doc__)
    print(build(*args[:3]))
