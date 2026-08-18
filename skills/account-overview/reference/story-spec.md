# The story spec

The story band is the hard part of the card and the reason the card exists. Everything else on the page is
evidence for it. Build it before anything else, and if it will not come, say so
rather than shipping a card without one.

## What a story is not

A category description is not a story. "They test controls on a sample once a
year" describes an entire industry. A seller who says it out loud has told the
buyer nothing the buyer did not already know about themselves, and has spent the
opening of the call proving we do not know them.

Neither is a list of recent news. News is undated context. A story has a
beginning, a change and a consequence, and the change has to bear on the
consequence.

## The five steps, in order

Write them as one paragraph of five or six sentences. Each step is one or two
sentences.

**1. What is the account trying to achieve.** Their stated strategy or
objectives, in their own words, from their own material. An investor day, an
annual report chair or chief executive letter, a press release. Not our
characterisation of their strategy.

**2. What changed recently that makes achieving it harder or more urgent.** This
is the compelling event and it has its own rule below.

**3. What has not changed, that should have.** The process, control or operating
model that is now under more strain than it was designed for. State it as strain
rather than as failure. Their environment is changing faster than their evidence
model. Their controls are not bad.

**4. Why the gap is already visible in their own numbers.** One or two real key
performance indicators tied to the strain. This is evidence that the gap exists
already, and it is not a scare tactic. Give the comparative, because a number
without a prior period is not an argument
(`../account-dossier/reference/house-style.md`).

**5. One sentence connecting all of it to what we do.** It reads as an insight.
It does not read as an advertisement. It names what changes for them, not what
our product contains.

## The compelling-event rule

This is the highest-leverage rule in this skill. A card built on a manufactured
trigger fails the first time the seller says it out loud to someone who knows the
account.

A compelling event qualifies only when all four hold.

- **Dated.** A specific date or month, not "recently".
- **Sourced.** A `KNOW` entry in `account.md` with a working link.
- **Structural.** It adds ground that has to be controlled, evidenced, staffed or
  reported. A logo refresh is news. A new regulated entity is an event.
- **Connected.** It bears on step 3. If the thing that changed has nothing to do
  with the thing that did not change, there is no story yet.

Where to look: acquisitions and disposals, reorganisations, leadership changes,
new regulated entities, systems renewals and their milestones, reporting-line
changes, integration deadlines, regulatory shifts with a named date.

### When there is no compelling event

Say so, in these words or close to them, to the user and in the record:

> No qualifying compelling event found for this account as of {date}. The card
> renders without the event tag.

Then set `compelling_event: none` in the frontmatter. The renderer suppresses the
badge. The band still carries the other four steps, and the card is still worth
having. What it is not is a card that claims urgency it cannot source.

Never promote a `GAP` or an `ASSUME` into an event to fill the slot. Never
convert "we think they are probably doing X" into "they are doing X".

## Framing rules

These sit on top of `house-style.md` and apply to the story band above all.

- **Never argue their controls are bad.** Argue their environment is changing
  faster than their evidence model. The first is an accusation the buyer will
  defend against. The second is an observation the buyer already agrees with.
- **Never frame the value as headcount reduction or efficiency for its own
  sake**, unless the account's own stated strategy uses that language. Check the
  research for that warning sign before choosing the frame.
- **Fear-based framing is grounded or it is absent.** Real, sourced regulatory or
  financial context only.
- **Never name a live or active enforcement action.** Convert it into general
  industry framing. Positive triggers such as growth, acquisitions and expansion
  may be named directly.
- **No product pitch.** No feature list. No "why AI". The seller knows what we
  sell. The card tells them about the account.

## The three plain-terms paragraphs

The right column elaborates the same value proposition from three angles. Three,
never two and never four. Each has a short headline and one short paragraph, and
each carries exactly one concrete detail: a number, a mechanism or a timeframe.

Suggested angles, adapted to the offering:

1. **It scales with their objective rather than against it.** What their own
   growth or change adds, and how coverage keeps pace with it.
2. **What leadership can prove instead of merely trust.** Tie it to a bar the
   account has already set for itself, such as a board risk appetite statement.
3. **It fits their current reality.** Existing systems, ongoing projects,
   operational constraints. It runs alongside what they are already doing rather
   than competing with it for capacity.

Each reads as insight. If a paragraph would survive being pasted into a card for
a different account, it is not yet about this account.

## The out-of-scope box

Two or three adjacent use cases that look obviously relevant and that we are
deliberately not leading with, each with the real sourced reason. Competing
investment already committed, an unconfirmed integration path, insufficient trust
built at this stage.

This box exists to keep the seller honest and focused. It does not undersell the
account, and the last item may be the positive one that says why the chosen entry
point fits instead.

Any unverified technical assumption carries an `Unconfirmed, gap` flag rather
than an assertion.
