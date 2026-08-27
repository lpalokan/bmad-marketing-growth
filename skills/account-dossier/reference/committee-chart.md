# The buying-committee chart

Section 3 opens with a diagram of the committee. It is drawn, not described in
characters, and it answers a question the table underneath it cannot: who is
above whom, and how much of that do we actually know.

## What it is, and what it is not

**It maps the buying committee, not the customer's organisation.** Nobody
should read it as an org chart, and the eyebrow on every chart says so. The
seats are arranged by how a decision travels toward us, which is often not how
the company is structured.

That distinction has to survive contact with a reader who glances at it, which
is why the eyebrow is not optional.

## The three encodings

Every chart carries exactly three, and adding a fourth makes it unreadable.

**Vertical position is decision altitude.** The root is air cover. The row
beneath it is the executive line where the money and the mandate sit. Anything
below that is a working owner or a specialist who does the job rather than
approves it.

**Hue is the role the seat plays for us.** Not seniority, which position
already carries.

| Role | Fill | Means |
|---|---|---|
| `air` | Ink | Air cover, usually the chief executive |
| `buyer` | Blue | Economic buyer and champion |
| `owner` | Navy | Working owner, the entry point |
| `mandate` | White, blue border | Co-owner of the mandate |
| `gate` | White, blue border | Technical, security, legal or model-risk gate |
| `finance` | White, grey border | Finance |
| `ops` | Panel tint | Operational sponsor, coach or watch |

**Border style is provenance**, and it is the encoding an Account Executive
needs most, because it says which names are safe to use.

| Style | Means |
|---|---|
| Solid | Verified on the company's own published page |
| Dashed | Enrichment-derived and uncorroborated. Re-verify before contact |
| Dotted | Announced and not yet in seat |

On a dark card a dashed border in the fill's own colour is invisible, so the
provenance stroke switches to cyan there. The legend says so. An encoding a
reader cannot see is worse than no encoding, because it looks like a decision
was made.

**Every card is the same size.** Length and two-dimensional position read
quantitatively whether or not that was intended, so a bigger card would claim a
bigger seat. Peers get equal extent and differ by hue.

## Layout

Root centred, the executive line across, and everything below stacked
vertically under its own executive with a small indent.

Sub-reports stack rather than spreading sideways for one reason. A committee
map that runs 2,000 pixels wide has to be shrunk to fit a page, and shrinking
is what makes a diagram unreadable. Stacking keeps every label at its designed
size.

**Two levels below the root is the limit.** A committee needing three has not
been reduced to the people who decide, and the fix is editorial rather than
typographic.

## How it sits in the page

The chart is wider than the prose column by design, so it **breaks out of the
column** and runs to its own natural width, centred, capped at the window. It
never shrinks into the column and it never scrolls sideways.

```css
.orgfig{position:relative;left:50%;transform:translateX(-50%);
        width:calc(100vw - 48px);max-width:var(--natural)}
.orgfig svg{display:block;width:100%;height:auto}
```

A wide scan table gets the same treatment, capped at 1300 pixels. Squeezing an
eight-column table into the prose column wraps every cell and turns a
one-glance table into three screens.

Caption the figure underneath, saying what the encodings mean and why it runs
wide. The caption is for the reader who arrives at the diagram first.

## Building one

`tools/build_committee_chart.py` takes a JSON spec and writes the SVG. Standard
library only.

```
python tools/build_committee_chart.py committee.json [out.svg]
```

Put the spec beside the account record so the chart can be rebuilt when a seat
moves. The renderer embeds the SVG inline, so the page stays self-contained and
a shared folder needs no image files.

## The rules that are not about drawing

- **A name reaches the chart on the same terms it reaches the table.** The
  chart is not a place to show an uncorroborated seat without its flag.
- **The subtitle carries the dated fact that makes this committee shape.** A
  merger completing, a statutory duty, an executive small enough to fit in one
  room. Not the account's boilerplate.
- **Nothing on the chart is a person's contact detail.** The dossier gets
  forwarded.
- **Look at the rendered chart before it ships.** Every defect found in the
  first build of this standard, a truncated title, an invisible border, a
  figure too wide to read, was invisible in the source and obvious in the
  render.
