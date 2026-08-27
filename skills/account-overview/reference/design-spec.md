# The design spec

The card is restrained, Nordic and executive. It is a working tool for a seller
rather than a leave-behind, so it earns its density. Type does the work and
decoration does none.

## Canvas

**1280 by 720, fixed.** True sixteen by nine, so the card drops into a deck or a
screenshot with no letterboxing. Nothing scrolls and nothing overflows. Padding
is 26 top, 46 left and right, 18 bottom.

The reference card this standard came from was 1280 by 860. That is not sixteen
by nine and it letterboxes on a slide. The 140 pixels it had spare are the reason
`fit-budget.md` is strict.

## Colour

**Two colours, plus the neutral ramp.** The neutrals are structure rather than a
third hue. No fourth hue enters the card for any reason. That rule holds whatever
brand the card is rendered in.

The card is built from seven brand tokens and a fixed set of structural ones. Only
the six are a brand's to change.

| Role | Token | Neutral default |
|---|---|---|
| Ink, all body text and the story band background | `--ink` | `#111111` |
| Accent on light, section labels, numbers | `--accent` | `#2450D8` |
| Accent on dark, inside the story band only | `--accent-dark` | `#7FB0FF` |
| The five-pixel rule across the top | `--rule` | solid `--accent` |
| Rings behind the story band, gradient start and end | `--ring-a`, `--ring-b` | `--accent` |

Structural tokens, which a brand pack leaves alone: `--white` `#FFFFFF`, `--g1`
`#333333`, `--g2` `#777777`, `--g4` `#E6E6E6`, `--panel2` `#F4F4F6`.

One accent is used in two contexts rather than two accents being introduced. A
saturated accent reads well on white and badly on near-black, so it lightens
inside the story band and stays the same colour otherwise.

### The default palette is a placeholder

The values above are deliberately not any real company's colours. An install that
has not chosen a brand renders in something obviously generic, rather than
shipping someone else's identity to a stranger who installed the module. Swap
them for your own.

### Brand packs

A brand pack is a small CSS file redefining the seven tokens and nothing else. It
is appended after the stylesheet, so it wins on the cascade without the base
stylesheet having to know it exists.

```
BRIEFING_BRAND=<path to the pack> python tools/build_briefing_html.py <account-id>
```

A bare name resolves against `tools/assets/brands/`. A path is taken as given.
The renderer prints the pack in use on every build and records it in an HTML
comment, so a card is never ambiguous about which brand it was rendered in.

### This module ships no company's pack

`tools/assets/brands/` is empty in a fresh install, on purpose. Shipping one
company's colours inside a suite other companies install would render their work
in someone else's identity, which is worse than rendering it in an obvious
placeholder.

A company that has written its visual identity down usually keeps its packs
beside its brand-compliance skill. Digital Workforce, for example, ships
`briefing.css` and a matching `dossier.css` at
`dwf-brand-compliance/reference/brand/css/`; pointing `BRIEFING_BRAND` and
`DOSSIER_BRAND` at that pair makes a card and a dossier for the same account read
as one family.

Wherever a pack comes from, the brand-compliance skill that owns it is the source
of truth. If the pack and that skill disagree, the skill wins and the pack is
stale.

### Writing a pack

Redefine the seven brand tokens and nothing else. Leave the structure tokens alone.
Then read **What is forbidden, in any brand** below — those rules hold whoever
the brand belongs to.

### What is forbidden, in any brand

- No third hue. The beige and teal in the reference card this standard came from
  are off-palette and fail a brand review as Critical findings.
- No stock photography.
- No icons requiring an external asset.
- No gradient behind text, and none as a large fill.
- No humanoid or robot imagery.

## Typography

**One family throughout, set by the pack's `--brand-font`.** The neutral
placeholder is `'Inter', Arial, Calibri, system-ui, sans-serif`; a brand pack
replaces it with the company's own. Weight creates hierarchy. There is no second
typeface and no serif anywhere, whatever the family is.

| Element | Size | Weight | Colour |
|---|---|---|---|
| Eyebrow | 10 | 700 | `--accent`, uppercase, 0.14em tracking |
| Title | 22 | 800 | `--ink` |
| Meta | 9.5 | 400 | `--g2`, with 700 on its values |
| Story band label | 9.5 | 800 | `--accent-dark`, uppercase |
| Story band body | 13.2 | 400 | `--white` at 1.52 line height |
| Column subhead | 11.2 | 800 | `--ink` on the left, `--accent` on the right |
| Bullet text | 11.5 | 400 | `--g1` |
| Plain-terms headline | 12.2 | 800 | `--ink` |
| Plain-terms body | 11.5 | 400 | `--g1` |
| Out-of-scope heading | 10.9 | 800 | `--ink` |
| Out-of-scope body | 10.4 | 400 | `--g1` |
| Footer | 8.5 | 400 | `--g2` |

These sizes and the height table in `fit-budget.md` are one decision. Changing a
size here without re-measuring there leaves the caps describing a card that no
longer exists.

## Emphasis

**Bold does not appear in body text.** The card inherits that rule from
`../account-dossier/reference/house-style.md` without an exception.

The rule exists because bold competes with the other devices that carry
hierarchy, and a bolded lead-in reads as a heading. That is as true on a card as
it is in a document. A card whose every third phrase is bold has no emphasis at
all, only noise.

Bold is permitted in three places and nowhere else, all of them structural:

- the column subheads, which are headings;
- the plain-terms headlines, which are headings;
- the out-of-scope headings, which are headings.

### How numbers get their weight instead

Every number still has to be scannable, because a seller scans the card rather
than reading it. Numbers get their weight from colour and a size step, which are
typographic devices rather than emphasis:

- accent colour, `--accent` on light and `--accent-dark` on dark;
- one size step up, roughly 1.08 of the surrounding text;
- letter spacing of `-0.01em`, which is what keeps a coloured figure from looking
  like a link.

The renderer applies this automatically to currency amounts, percentages, ratios
and bare figures with units. Nothing in the source markdown is marked up for it,
which is what keeps the source bold-free and the treatment consistent across
every card.

Dates in the story band take the same treatment, because the date on a compelling
event is the part a seller most needs to have in mind.

### Italics

Not used. There is nothing on a card that italics would carry which a heading or
a flag does not carry better.

## Structural vocabulary

The card borrows its shapes from the presentation template, so a seller who has
seen a deck recognises the card.

| Card block | Template equivalent |
|---|---|
| Story band, dark, full width | The dark statement slide |
| Two-column body | The two-text-box layout |
| Three plain-terms paragraphs | The three-glass-card layout |
| Out-of-scope box, light panel | A footnote panel |
| Gradient rule and rings | The template's standing brand elements |

Corners are 8 pixels. Hairlines are one pixel of `--g4`. There are no drop
shadows anywhere, because the brand forbids effects on the logo and the card
carries none for consistency.

## The header and the internal marker

The eyebrow reads `Seller briefing · Internal · Not for customer` and it is not
optional. It is the only thing standing between an internal card and an
accidental forward. It stays at the top left, in accent colour, above the title.

The title is the account's legal entity name and a short phrase saying what the
card is. The meta block sits right-aligned and carries the tier, the offering and
the date prepared.

## Logo

The card carries no logo by default. The gradient rule and the rings identify it
as ours, and 1280 by 720 has no room to spend on a mark the internal audience
does not need. Where one is wanted, set `BRIEFING_LOGO` and it renders bottom
right at 22 pixels high, which clears the brand's 100-pixel-wide digital minimum
only for the full wordmark. Check the minimum before turning it on.
