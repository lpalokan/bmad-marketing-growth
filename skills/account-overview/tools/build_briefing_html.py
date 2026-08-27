"""Render an account overview briefing .md into a branded 1280x720 HTML card.

Usage
    python build_briefing_html.py <account-slug> [source-md] [output-stem] [--strict]

    <account-slug>  folder under the briefings root, and the default output stem
    [source-md]     alternate markdown inside that folder, e.g. briefing-2026-08-17.md
    [output-stem]   alternate output name, so a dated build never overwrites a
                    standing one
    --strict        exit non-zero when any slot is over its cap

Paths
    briefings root  {output_folder}/work/dossiers/         (override: BRIEFING_ROOT)
    html output     the account's own folder, beside its markdown, as
                    overview.html                          (override: BRIEFING_HTML)

    One account is one folder. The card renders next to the dossier it shares an
    account with, so a seller opening the folder finds the 30-second read and the
    30-minute one together.

The card shares an account folder with the dossier, because it is the same
account. Only the rendered output goes somewhere of its own.

Branding
    assets/briefing.css ships a brand-neutral placeholder palette, so an install
    that has not chosen a brand renders in something obviously generic rather
    than in someone else's identity.

    Set BRIEFING_BRAND to a brand pack: a small CSS file redefining the six
    brand tokens, appended after the stylesheet. Give it a path. A bare name
    resolves against assets/brands/, which ships empty: this module carries no
    company's colours. A company that has a brand-compliance skill usually keeps
    its pack beside it. The pack in use is printed on build and recorded in an
    HTML comment.

    No logo by default. Set BRIEFING_LOGO to a filename or URL to place one
    bottom right. A relative value resolves against the html output folder.
    Check the brand minimum size before turning it on.

Emphasis
    Numbers are given weight by this renderer, not by the source. Currency
    amounts, percentages, ratios and bare figures with units are wrapped in a
    span that takes the accent colour and a size step. The source stays free of
    bold, per ../account-dossier/reference/house-style.md.

Requires: Python 3.10+. Standard library only, deliberately, so a card can be
rebuilt anywhere.
"""

import html
import os
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
DEFAULT_ROOT = Path.cwd() / "output" / "work" / "dossiers"

ROOT = Path(os.environ.get("BRIEFING_ROOT", DEFAULT_ROOT))

# The card is written into the account's own folder, beside the dossier. A
# project that wants every card collected in one place sets BRIEFING_HTML.
_ENV_HTML = os.environ.get("BRIEFING_HTML", "").strip()
OUT_DIR = Path(_ENV_HTML) if _ENV_HTML else None


def out_dir_for(slug: str) -> Path:
    return OUT_DIR if OUT_DIR else ROOT / slug
LOGO = os.environ.get("BRIEFING_LOGO", "").strip()

# The stylesheet ships a brand-neutral placeholder palette. A brand pack is a
# small CSS file redefining the seven brand tokens, appended after it. Usually a
# path, since assets/brands/ ships empty and a company keeps its own packs with
# its brand-compliance skill.
BRAND = os.environ.get("BRIEFING_BRAND", "").strip()


def brand_css() -> tuple[str, str]:
    """Return the brand pack's CSS and the name to report. Neutral when unset."""
    if not BRAND:
        return "", "neutral placeholder"
    path = Path(BRAND)
    if not path.suffix:
        path = TOOLS / "assets" / "brands" / f"{BRAND}.css"
    elif not path.is_absolute():
        path = (TOOLS / "assets" / "brands" / path) if not path.exists() else path
    if not path.exists():
        packaged = sorted(p.stem for p in (TOOLS / "assets" / "brands").glob("*.css"))
        raise SystemExit(
            f"BRIEFING_BRAND={BRAND!r} not found. Looked at {path}. "
            + (
                "Packaged packs: " + ", ".join(packaged)
                if packaged
                else "No packs ship with this module. Give a path to the company's "
                "pack, usually kept with its brand-compliance skill, or unset "
                "BRIEFING_BRAND to render in the neutral placeholder palette."
            )
        )
    return "\n" + path.read_text(encoding="utf-8"), path.stem

# reference/fit-budget.md holds these and the reasoning behind them. Kept here as
# a warning only: the caps are derived estimates and a real render is the only
# measurement that counts.
CAPS = {
    "title": 70,
    "meta": 90,
    "story": 750,
    "objective": 130,
    "challenge": 130,
    "means_head": 60,
    "means_body": 230,
    "scope_head": 45,
    "scope_body": 190,
    "threads": 200,
    "sources": 300,
}
COUNT_CAPS = {"left_items": 7, "means": 3, "scope": 3}

warnings: list[str] = []


def cap(slot: str, text: str, where: str = "") -> str:
    limit = CAPS.get(slot)
    if limit and len(text) > limit:
        warnings.append(
            f"{slot}{' ' + where if where else ''}: {len(text)} chars, cap {limit}"
        )
    return text


# Currency amounts, percentages, ratios, and bare figures with a unit or a
# comparative. Deliberately conservative: a number that is part of a word, an
# ordinal like "1." opening a headline, and anything inside a tag are left alone.
NUM = re.compile(
    r"(?<![\w>])("
    r"(?:EUR|USD|GBP|SEK|NOK|DKK|CHF|€|\$|£)\s?\d[\d\s.,]*"
    r"(?:\s?(?:million|billion|thousand|m|bn|k))?"
    r"|[+-]?\d[\d.,]*\s?%"
    r"|[+-]?\d[\d.,]*\s?(?:million|billion|thousand|percentage points|pp|bps|"
    r"days?|weeks?|months?|years?|hours?|FTEs?|entities|people)"
    r"|\d{4}-\d{2}-\d{2}"
    r"|\d[\d.,]*"
    r")(?![\w%])"
)

# Bare four-digit years read as noise when every one of them is coloured, so a
# year only takes the treatment when it sits next to a month.
MONTHS = (
    "January|February|March|April|May|June|July|August|September|October|"
    "November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec"
)
DATE = re.compile(rf"\b(?:{MONTHS})\s+\d{{4}}\b|\b\d{{1,2}}\s+(?:{MONTHS})\s+\d{{4}}\b")


def wrap(match: re.Match) -> str:
    """Sentence punctuation stays outside the span, so "SFCR 2025." does not
    colour its own full stop."""
    figure = match.group(1) if match.re.groups else match.group(0)
    tail = ""
    while figure and figure[-1] in ".,":
        tail = figure[-1] + tail
        figure = figure[:-1]
    return f'<span class="n">{figure}</span>{tail}' if figure else tail


def numbers(text: str) -> str:
    """Give figures visual weight through colour and size instead of bold."""
    text = DATE.sub(wrap, text)
    parts = re.split(r'(<span class="n">.*?</span>)', text)
    for i, part in enumerate(parts):
        if not part.startswith('<span'):
            parts[i] = NUM.sub(wrap, part)
    return "".join(parts)


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def body(text: str) -> str:
    return numbers(esc(" ".join(text.split())))


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


def sections(md: str) -> dict[str, str]:
    """Split on level-two headings. Unknown sections are ignored, not an error."""
    out, current, buf = {}, None, []
    for line in md.splitlines():
        if line.startswith("## "):
            if current:
                out[current] = "\n".join(buf).strip()
            current, buf = line[3:].strip().lower(), []
        else:
            buf.append(line)
    if current:
        out[current] = "\n".join(buf).strip()
    return out


def bullets(block: str) -> list[str]:
    return [
        line.lstrip("-* ").strip()
        for line in block.splitlines()
        if line.strip().startswith(("-", "*"))
    ]


FLAG = re.compile(r"\s*\[flag:\s*([^\]]+)\]\s*$")


def subsections(block: str) -> list[tuple[str, str, str]]:
    """Level-three headings into (heading, flag, body) triples."""
    out, head, flag, buf = [], None, "", []
    for line in block.splitlines():
        if line.startswith("### "):
            if head is not None:
                out.append((head, flag, " ".join(" ".join(buf).split())))
            raw = line[4:].strip()
            m = FLAG.search(raw)
            flag = m.group(1).strip() if m else ""
            head = FLAG.sub("", raw).strip()
            buf = []
        elif head is not None:
            buf.append(line)
    if head is not None:
        out.append((head, flag, " ".join(" ".join(buf).split())))
    return out


def plain(block: str) -> str:
    """A section that is one paragraph of prose, with any template note dropped."""
    text = "\n".join(
        line for line in block.splitlines() if not line.strip().startswith("<")
    )
    return " ".join(text.split())


EVENT = '<span class="event">Compelling event</span>'

RINGS = (
    '<svg class="rings" viewBox="0 0 200 200" aria-hidden="true">'
    + "".join(
        f'<circle cx="100" cy="100" r="{r}" fill="none" stroke="url(#rg)" stroke-width="1.4"/>'
        for r in (30, 46, 62, 78, 94)
    )
    + '<defs><linearGradient id="rg" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0" stop-color="var(--ring-a)"/>'
    '<stop offset="1" stop-color="var(--ring-b)"/>'
    "</linearGradient></defs></svg>"
)


def build(slug: str, source: str | None = None, out: str | None = None) -> Path:
    md_path = ROOT / slug / (source or "briefing.md")
    meta, md = split_frontmatter(md_path.read_text(encoding="utf-8"))
    sec = sections(md)

    account = meta.get("account", slug)
    title = cap("title", plain(sec.get("title", "")) or f"{account}, account read before the call")

    meta_bits = [
        ("Tier", meta.get("action_tier", "")),
        ("Offering", meta.get("offering", "")),
        ("Prepared", meta.get("created", "")),
    ]
    meta_line = " ".join(f"{label} {value}" for label, value in meta_bits if value)
    cap("meta", meta_line)
    meta_html = " &middot; ".join(
        f"{esc(label)} <b>{esc(value)}</b>" for label, value in meta_bits if value
    )

    # The event badge is placed by the author with an [event] marker so it lands
    # on the clause that carries the trigger. No marker and no event is fine.
    story_raw = plain(sec.get("story", ""))
    cap("story", story_raw.replace("[event]", ""))
    story = body(story_raw.replace("[event]", "\x00"))
    if meta.get("compelling_event", "").lower().startswith("y"):
        story = story.replace("\x00", EVENT)
    else:
        story = story.replace("\x00", "")
        if "[event]" in story_raw:
            warnings.append("story: [event] marker present but compelling_event is not yes")

    objectives = bullets(sec.get("objectives", ""))
    challenges = bullets(sec.get("challenges", ""))
    for i, item in enumerate(objectives, 1):
        cap("objective", item, f"#{i}")
    for i, item in enumerate(challenges, 1):
        cap("challenge", item, f"#{i}")
    if len(objectives) + len(challenges) > COUNT_CAPS["left_items"]:
        warnings.append(
            f"left column: {len(objectives) + len(challenges)} items, "
            f"cap {COUNT_CAPS['left_items']}"
        )

    means = subsections(sec.get("what this means", ""))
    if len(means) != COUNT_CAPS["means"]:
        warnings.append(f"what this means: {len(means)} paragraphs, must be exactly 3")
    for i, (head, _flag, text) in enumerate(means, 1):
        cap("means_head", head, f"#{i}")
        cap("means_body", text, f"#{i}")

    scope = subsections(sec.get("out of scope", ""))
    if len(scope) > COUNT_CAPS["scope"]:
        warnings.append(f"out of scope: {len(scope)} items, cap {COUNT_CAPS['scope']}")
    for i, (head, _flag, text) in enumerate(scope, 1):
        cap("scope_head", head, f"#{i}")
        cap("scope_body", text, f"#{i}")

    threads = cap("threads", plain(sec.get("buyer threads", "")))
    sources = cap("sources", plain(sec.get("sources", "")))

    items_html = "".join(
        f'<div class="item"><div class="dot"></div><div class="txt">{body(item)}</div></div>'
        for item in objectives
    )
    ch_html = "".join(
        f'<div class="item ch"><div class="dot"></div><div class="txt">{body(item)}</div></div>'
        for item in challenges
    )
    means_html = "".join(
        f'<div class="para"><div class="t"><span class="idx">{i}</span>{esc(head)}</div>'
        f'<div class="d">{body(text)}</div></div>'
        for i, (head, _flag, text) in enumerate(means, 1)
    )
    scope_html = "".join(
        f'<div class="scope-item"><b>{esc(head)}'
        + (f'<span class="flag">{esc(flag)}</span>' if flag else "")
        + f"</b>{body(text)}</div>"
        for head, flag, text in scope
    )

    out_dir = out_dir_for(slug)
    out_dir.mkdir(parents=True, exist_ok=True)
    pack, pack_name = brand_css()
    css = (TOOLS / "assets" / "briefing.css").read_text(encoding="utf-8") + pack
    logo_html = f'<img class="logo" src="{esc(LOGO)}" alt="">' if LOGO else ""

    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>{esc(account)} &middot; Account overview</title>
<!-- brand pack: {pack_name} -->
<style>{css}</style>
</head><body>
<div class="slide">
  <div class="toprule"></div>

  <div class="headrow">
    <div>
      <div class="eyebrow">Seller briefing &middot; Internal &middot; Not for customer</div>
      <h1>{esc(title)}</h1>
    </div>
    <div class="meta">{meta_html}</div>
  </div>

  <div class="valueprop">{RINGS}
    <div class="vp-inner">
      <div class="tag">Focus value proposition for this account, the story</div>
      <p>{story}</p>
    </div>
  </div>

  <div class="body">
    <div class="col left">
      <div class="subhead">Organisation's objectives</div>
      {items_html}
      <div class="subhead ch">Challenges this creates</div>
      {ch_html}
    </div>
    <div class="col right">
      <div class="subhead">What this means for {esc(account)}, in plain terms</div>
      {means_html}
    </div>
  </div>

  <div class="scope">
    <div class="tag">Where we are <u>not</u> focused, this account, this stage</div>
    <div class="scope-body">{scope_html}</div>
  </div>

  <footer>
    <div class="buyers">{body(threads)}</div>
    <div class="right">{logo_html}<div class="src">{body(sources)}</div></div>
  </footer>
</div>
</body></html>
"""

    out_path = out_dir / f"{out or 'overview'}.html"
    out_path.write_text(page, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--strict"]
    strict = "--strict" in sys.argv
    if not args:
        sys.exit(__doc__)
    print(build(*args[:3]))
    print(f"brand pack: {brand_css()[1]}")
    if warnings:
        print("\nOver budget, see reference/fit-budget.md:", file=sys.stderr)
        for w in warnings:
            print(f"  {w}", file=sys.stderr)
        print("\nCut whole items in the order that file sets. Do not chop "
              "sentences into fragments.", file=sys.stderr)
        if strict:
            sys.exit(1)
