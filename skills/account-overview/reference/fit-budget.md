# The fit budget

**The card is one page, 1280 by 720, and nothing scrolls.** That is the design
constraint and everything here follows from it. A one-slider that overflows its
canvas is not a one-slider.

The dossier's budget is a reading time. This one is a physical dimension, which
makes it stricter. There is no band to sit inside. Either it fits or the layout
breaks.

## Where the 720 pixels go

Measured from the rendered layout at the type sizes in `design-spec.md`. These
are the design's own numbers and they are stated so they can be argued with.

| Block | Height |
|---|---|
| Canvas padding, top and bottom | 44 |
| Header | 42 |
| Story band | 130 |
| Two-column body | 310 |
| Out-of-scope box | 100 |
| Footer | 34 |
| Gaps between blocks | 45 |
| Slack | 15 |

Measured off a rendered card at the caps below, rather than calculated. Re-measure
if the type sizes in `design-spec.md` change, because these two files have to
agree or the caps stop meaning anything.

The slack absorbs a line that wraps one word further than expected. It is not
spare capacity.

## Per-slot caps

Characters, including spaces. The renderer warns on any slot over its cap and
`--strict` makes the warning fatal.

| Slot | Cap | Notes |
|---|---|---|
| Title | 70 | The account's name and four or five words |
| Meta line | 90 | Tier, offering, date prepared |
| Story band | 750 | Five or six sentences, one paragraph |
| Objectives, per item | 130 | Two rendered lines |
| Challenges, per item | 130 | Two rendered lines |
| Objectives and challenges, combined item count | 7 | Three plus four, or four plus three |
| Plain-terms headline, each | 60 | One line, no terminal period |
| Plain-terms paragraph, each | 230 | Three rendered lines |
| Plain-terms paragraph count | 3 | Exactly three, never two and never four |
| Out-of-scope heading, each | 45 | Excluding the flag |
| Out-of-scope body, each | 190 | Three rendered lines |
| Out-of-scope item count | 3 | Two is allowed, three is the cap |
| Buyer threads line | 200 | The whole line, all contacts |
| Sources line | 300 | Including any metric-discrepancy flag |

## What to cut, in this order

Meet the caps by deleting whole items. Compressing every sentence to reach a
number produces telegraphese, which is shorter and worse. The anti-metric rule in
`../account-dossier/reference/house-style.md` still governs.

1. **The fourth item in a column.** Seven items across objectives and challenges
   is the cap, and the seventh is usually the weakest of the four in whichever
   column has four.
2. **Anything the reader already met.** A fact belongs in one slot. Its
   consequence belongs in another. Restating the fact to introduce the
   consequence is the largest source of overflow on a card this size.
3. **The second number in a bullet that already has one.** One number per
   challenge bullet carries the point. Two compete.
4. **Hedging.** One clear sentence with a label beats three careful ones.
5. **Any adjective doing no work.** On a card this dense, "significant",
   "considerable" and "robust" are pure length.
6. **The third out-of-scope item**, where it is a restatement of the first two
   rather than the positive one that says why the chosen entry point fits.

If the card still overruns after all six, the story band is where the words are.
Cut there last, and cut a whole sentence rather than trimming all six.

## What must never be cut to fit

- The comparative on a number. A figure without its prior period is not an
  argument, and dropping it to save eight characters removes the point.
- The date on the compelling event.
- The `Unconfirmed, gap` flag on an unverified technical assumption. If the flag
  will not fit, the assumption comes off the card.
- The metric-discrepancy flag in the sources line, where one exists.

Cut the item entirely before cutting any of these four out of it.

## The budget is a dimension, never a score

- A card inside the caps proves it is publishable. It proves nothing about
  whether the story is any good.
- Never report a character count as evidence of quality, on the card or to the
  user.
- Never reach a cap by dropping articles or turning prose into fragments.
- Read the rendered card at full size before it is shown to anyone. The caps are
  derived estimates and a real render is the only measurement that counts.
