"""Render a buying-committee hierarchy as an inline SVG org chart.

The chart maps the *buying committee*, not the customer's real organisation.
Vertical position encodes decision altitude. Hue encodes the role a seat plays
for us. Every card is the same size, so nothing about a seat's importance is
smuggled in through area (see the dossier standard's diagram rule: length and
2-D position read quantitatively, so peers get equal extent and differ by hue).

Border style encodes provenance, which is the part an Account Executive needs
before picking up the phone:

    solid   verified on the company's own published page
    dashed  enrichment-derived, uncorroborated, re-verify before contact
    dotted  announced and not yet in seat

Palette is the dossier stylesheet's own, read from the same brand pack. With
DOSSIER_BRAND unset both fall back to the brand-neutral placeholder, so a chart
is never accidentally drawn in some other company's colours. The third accent
appears only inside the gradient rule,
never as a fill, per the brand spec.

Usage
    python build_committee_chart.py <committee.json> [out.svg]

Writes committee-chart.svg next to the spec unless an output path is given.
Standard library only.

The spec is JSON:

    {
      "account": "Legal entity name",
      "subtitle": "One line. The dated fact that makes this committee shape.",
      "root": {
        "name": "...", "title": "...", "role": "air", "prov": "page",
        "reports": [
          {"name": "...", "title": "...", "role": "buyer", "prov": "page",
           "reports": [{"name": "...", "title": "...", "role": "owner", "prov": "clay"}]}
        ]
      }
    }

    role: air | buyer | owner | mandate | gate | finance | ops
    prov: page | clay | announced

Only the root and one level of reports are laid out. A committee needing three
levels is a committee that has not been reduced to the people who decide.
"""

import json
import os
import re
import sys
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

CARD_W, CARD_H = 196, 66
GAP_X, GAP_Y = 14, 46
PAD_TOP = 96
PAD_SIDE = 28

# Seats below the executive line stack vertically under their own executive
# instead of spreading sideways. A committee map that runs 2,000 pixels wide
# has to be shrunk to fit a document column, and shrinking is what makes a
# diagram unreadable. Stacking keeps every label at its designed size.
INDENT = 20
SUB_W, SUB_H = CARD_W - INDENT, 58
SUB_GAP = 9

# Brand tokens, matching assets/dossier.css. The values here are the same
# brand-neutral placeholder that stylesheet ships, and DOSSIER_BRAND overrides
# them from the same pack file, so the diagram and the page it sits in stay one
# design. Structure colours (white, the greys, the panel tint) are not brand and
# are not overridable.
TOKENS = {
    "ink":      "#111111",
    "accent":   "#2450D8",
    "accent-2": "#7FB0FF",
    "deep":     "#16307F",
    "font":     "Inter, Arial, Calibri, system-ui, sans-serif",
}

# The top rule is the stylesheet's --grad-full, read stop by stop rather than
# rebuilt from the tokens above. A brand's gradient can legitimately contain a
# hue that appears nowhere else -- Digital Workforce's magenta does -- and
# deriving the rule from accent and deep would quietly drop it.
GRAD = ["#7FB0FF", "#2450D8", "#16307F"]
WHITE, GREY, RULE, PANEL = "#FFFFFF", "#777777", "#B3B3B3", "#F5F7FF"


def load_brand() -> None:
    """Overlay the brand tokens from the pack DOSSIER_BRAND names, if any."""
    name = os.environ.get("DOSSIER_BRAND", "").strip()
    if not name:
        return
    path = Path(name)
    if not path.suffix:
        path = Path(__file__).resolve().parent / "assets" / "brands" / f"{name}.css"
    elif not path.is_absolute() and not path.exists():
        path = Path(__file__).resolve().parent / "assets" / "brands" / path
    if not path.exists():
        raise SystemExit(
            f"DOSSIER_BRAND={name!r} not found. Looked at {path}. Give a path to "
            f"the company's pack, or unset DOSSIER_BRAND to draw in the neutral "
            f"placeholder palette."
        )
    css = path.read_text(encoding="utf-8")
    for token, key in (("ink", "ink"), ("accent", "accent"),
                       ("accent-2", "accent-2"), ("deep", "deep")):
        m = re.search(r"--" + re.escape(token) + r"\s*:\s*([^;}]+)", css)
        if m:
            TOKENS[key] = m.group(1).strip()
    m = re.search(r"--brand-font\s*:\s*([^;}]+)", css)
    if m:
        # An SVG attribute reads better spaced, and the quotes a stylesheet puts
        # round a family name are not needed once it is in font-family=.
        TOKENS["font"] = ", ".join(
            part.strip().strip("'\"") for part in m.group(1).strip().split(",")
        )
    m = re.search(r"--grad-full\s*:\s*([^;}]+)", css)
    if m:
        stops = re.findall(r"#[0-9A-Fa-f]{3,8}", m.group(1))
        if len(stops) == 3:
            GRAD[:] = stops


load_brand()

# role key -> (fill, text colour, border colour, label)
ROLES = {
    "air":     (TOKENS["ink"],  WHITE,          TOKENS["ink"],    "Air cover"),
    "buyer":   (TOKENS["accent"], WHITE,        TOKENS["accent"], "Economic buyer and champion"),
    "owner":   (TOKENS["deep"], WHITE,          TOKENS["deep"],   "Working owner, the entry point"),
    "mandate": (WHITE,          TOKENS["ink"],  TOKENS["accent"], "Co-owner of the mandate"),
    "gate":    (WHITE,          TOKENS["ink"],  TOKENS["accent"], "Gate"),
    "finance": (WHITE,          TOKENS["ink"],  GREY,             "Finance"),
    "ops":     (PANEL,          TOKENS["ink"],  RULE,             "Operational, coach or watch"),
}

PROV = {"page": "none", "clay": "5 3", "announced": "1.5 3"}


class Node:
    def __init__(self, name, title, role, prov, children=None):
        self.name, self.title = name, title
        self.role, self.prov = role, prov
        self.children = children or []
        self.x = self.y = 0
        self.w = self.h = 0

    def leaves(self):
        return sum(c.leaves() for c in self.children) if self.children else 1


def layout(root):
    """Root centred, executive line across, everything below stacked."""
    row1_y = PAD_TOP + CARD_H + GAP_Y
    cursor = PAD_SIDE
    for child in root.children:
        child.x, child.y = cursor, row1_y
        child.w, child.h = CARD_W, CARD_H
        sy = row1_y + CARD_H + GAP_Y
        for sub in child.children:
            sub.x, sub.y = cursor + INDENT, sy
            sub.w, sub.h = SUB_W, SUB_H
            sy += SUB_H + SUB_GAP
        cursor += CARD_W + GAP_X
    first, last = root.children[0], root.children[-1]
    root.x = (first.x + last.x) / 2
    root.y = PAD_TOP
    root.w, root.h = CARD_W, CARD_H


def walk(node):
    yield node
    for child in node.children:
        yield from walk(child)


def wrap_title(title, width=30, limit=2):
    lines = textwrap.wrap(title, width=width)
    if len(lines) > limit:
        lines = lines[:limit]
        lines[-1] = lines[-1].rstrip(" ,") + "…"
    return lines


DARK_FILL = {"air", "buyer", "owner"}


def card(node, sub=False):
    fill, ink, border, _ = ROLES[node.role]
    dash = PROV[node.prov]
    dash_attr = "" if dash == "none" else f' stroke-dasharray="{dash}"'
    # A dashed border in the fill's own colour is invisible. On the dark cards
    # the provenance encoding has to switch to cyan or it silently disappears,
    # which would hide exactly the flag an AE needs before dialling.
    if dash != "none" and node.role in DARK_FILL:
        border = TOKENS["accent-2"]
    name_size, title_size = (11.6, 9.5) if sub else (12.6, 10.1)
    wrap_at = 28 if sub else 30
    out = [
        f'<g><rect x="{node.x:.1f}" y="{node.y:.1f}" width="{node.w}" height="{node.h}" '
        f'rx="8" fill="{fill}" stroke="{border}" stroke-width="1.6"{dash_attr}/>'
    ]
    cx = node.x + 12
    out.append(
        f'<text x="{cx:.1f}" y="{node.y + (20 if sub else 23):.1f}" font-size="{name_size}" '
        f'font-weight="700" fill="{ink}" letter-spacing="-0.01em">{escape(node.name)}</text>'
    )
    for i, line in enumerate(wrap_title(node.title, width=wrap_at)):
        out.append(
            f'<text x="{cx:.1f}" y="{node.y + (35 if sub else 39) + i * 12.4:.1f}" '
            f'font-size="{title_size}" fill="{ink}" opacity="0.82">{escape(line)}</text>'
        )
    out.append("</g>")
    return "".join(out)


def connectors(root):
    """A spine from the root across the executive line, then indented drops."""
    parts = []
    px = root.x + root.w / 2
    py = root.y + root.h
    mid = py + GAP_Y / 2
    parts.append(f'<path d="M {px:.1f} {py:.1f} V {mid:.1f}" fill="none" stroke="#B3B3B3" stroke-width="1.3"/>')
    xs = [c.x + c.w / 2 for c in root.children]
    parts.append(
        f'<path d="M {min(xs):.1f} {mid:.1f} H {max(xs):.1f}" fill="none" '
        f'stroke="#B3B3B3" stroke-width="1.3"/>'
    )
    for c in root.children:
        cx = c.x + c.w / 2
        parts.append(f'<path d="M {cx:.1f} {mid:.1f} V {c.y:.1f}" fill="none" stroke="#B3B3B3" stroke-width="1.3"/>')
        if not c.children:
            continue
        rail = c.x + INDENT / 2
        last = c.children[-1]
        parts.append(
            f'<path d="M {rail:.1f} {c.y + c.h:.1f} V {last.y + last.h / 2:.1f}" '
            f'fill="none" stroke="#B3B3B3" stroke-width="1.3"/>'
        )
        for s in c.children:
            parts.append(
                f'<path d="M {rail:.1f} {s.y + s.h / 2:.1f} H {s.x:.1f}" fill="none" '
                f'stroke="#B3B3B3" stroke-width="1.3"/>'
            )
    return "".join(parts)


def legend(y, width):
    """Two encodings, stated on the chart so it needs no caption to be read."""
    items = [
        (TOKENS["accent"], "Economic buyer and champion"),
        (TOKENS["deep"], "Working owner, the entry point"),
        (TOKENS["ink"], "Air cover"),
        ("#FFFFFF", "Gate, finance or mandate co-owner"),
        ("#F5F7FF", "Operational, coach or watch"),
    ]
    out = [
        f'<text x="{PAD_SIDE}" y="{y}" font-size="9.2" font-weight="700" fill="{TOKENS["accent"]}" '
        f'letter-spacing="0.14em">ROLE FOR US</text>'
    ]
    x = PAD_SIDE
    yy = y + 18
    for fill, label in items:
        stroke = TOKENS["accent"] if fill == WHITE else (RULE if fill == PANEL else fill)
        out.append(
            f'<rect x="{x}" y="{yy - 9}" width="12" height="12" rx="3" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="1.4"/>'
        )
        out.append(f'<text x="{x + 18}" y="{yy}" font-size="10.2" fill="#333">{escape(label)}</text>')
        x += 22 + len(label) * 5.6 + 22
    out.append(
        f'<text x="{PAD_SIDE}" y="{y + 48}" font-size="9.2" font-weight="700" fill="{TOKENS["accent"]}" '
        f'letter-spacing="0.14em">HOW THE SEAT WAS VERIFIED</text>'
    )
    x = PAD_SIDE
    yy = y + 66
    for dash, label in [
        ("none", "Verified on the company's own page"),
        ("5 3", "From Clay, uncorroborated, re-verify before contact. Cyan on dark cards."),
        ("1.5 3", "Announced, not yet in seat"),
    ]:
        d = "" if dash == "none" else f' stroke-dasharray="{dash}"'
        out.append(
            f'<rect x="{x}" y="{yy - 9}" width="12" height="12" rx="3" fill="#FFFFFF" '
            f'stroke="{TOKENS["ink"]}" stroke-width="1.5"{d}/>'
        )
        out.append(f'<text x="{x + 18}" y="{yy}" font-size="10.2" fill="#333">{escape(label)}</text>')
        x += 22 + len(label) * 5.6 + 22
    return "".join(out)


def render(root, account, subtitle):
    layout(root)
    nodes = list(walk(root))
    right = max(n.x + n.w for n in nodes)
    bottom = max(n.y + n.h for n in nodes)
    legend_y = bottom + 46
    W = int(max(right + PAD_SIDE, 980))
    H = int(legend_y + 88)

    head = (
        f'<text x="{PAD_SIDE}" y="34" font-size="9.6" font-weight="700" fill="{TOKENS["accent"]}" '
        f'letter-spacing="0.14em">BUYING COMMITTEE, NOT THE ORGANISATION CHART</text>'
        f'<text x="{PAD_SIDE}" y="60" font-size="19" font-weight="800" fill="{TOKENS["ink"]}" '
        f'letter-spacing="-0.02em">{escape(account)}</text>'
        f'<text x="{PAD_SIDE}" y="79" font-size="11" fill="#777">{escape(subtitle)}</text>'
    )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'role="img" aria-label="Buying committee map for {escape(account)}" '
        f'font-family="{TOKENS["font"]}">'
        f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="{GRAD[0]}"/><stop offset="0.48" stop-color="{GRAD[1]}"/>'
        f'<stop offset="1" stop-color="{GRAD[2]}"/></linearGradient></defs>'
        f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>'
        f'<rect x="0" y="0" width="{W}" height="4" fill="url(#g)"/>'
        f'{head}{connectors(root)}'
        + card(root)
        + "".join(card(c) for c in root.children)
        + "".join(card(s, sub=True) for c in root.children for s in c.children)
        + f'<line x1="{PAD_SIDE}" y1="{bottom + 22}" x2="{W - PAD_SIDE}" y2="{bottom + 22}" '
          f'stroke="#E6E6E6" stroke-width="1"/>'
        + legend(legend_y, W)
        + "</svg>"
    )


def load(spec_path: Path):
    """Read a committee spec. See the docstring for the shape."""
    raw = json.loads(spec_path.read_text(encoding="utf-8"))

    def node(d):
        return Node(d["name"], d["title"], d["role"], d["prov"],
                    [node(c) for c in d.get("reports", [])])

    return dict(account=raw["account"], subtitle=raw["subtitle"], root=node(raw["root"]))


USAGE = """usage: build_committee_chart.py committee.json [out.svg]

Writes the buying-committee chart as SVG. With no output path it writes
committee-chart.svg beside the spec. reference/committee-chart.md owns the
encodings and the layout rules the spec has to satisfy."""


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(USAGE)
        raise SystemExit(0 if len(sys.argv) > 1 else 2)
    spec_path = Path(sys.argv[1])
    spec = load(spec_path)
    svg = render(spec["root"], spec["account"], spec["subtitle"])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else spec_path.with_name("committee-chart.svg")
    out.write_text(svg, encoding="utf-8")
    print(out)
