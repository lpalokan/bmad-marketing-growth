# The research brief

This runs only where no `account.md` exists for the account, or where the record
predates the event the card is about. Where a dossier already exists, the card is
a selection pass and this file is skipped.

Fetch order and live-verification rules come from
`../account-dossier/reference/research-method.md`. This file says only what a
one-slider needs, which is less than a dossier needs and differently weighted.

Every finding goes into `account.md`, in the section that record owns, with a
`KNOW`, `ASSUME` or `GAP` label and a link at the point of capture. The card is a
selection from the record. It is never a separate set of facts held only in the
rendered file.

## The six things to dig for

**1. Their own stated strategy, goals and ambitions.** In their words, not ours.
Investor days, annual report chair and chief executive letters, press releases,
internal-facing strategy launches that were published. Three to five of these
become the objectives column.

**2. Key performance indicators relevant to this offering.** Swap the set for the
industry and the offering. Risk and compliance work uses combined ratio, expense
ratio, risk ratio, operational risk capital and solvency ratio. A captive-finance
account would use approval-to-funding time, delinquency rate and portfolio at
risk. A hospital group would use something else again. Pick the two or three that
bear on the strain in step 3 of the story, and always capture the comparative.

**3. Anything that changed recently and created new complexity or new risk.**
This is where the compelling event lives, and `story-spec.md` holds the rule it
has to pass. Acquisitions, reorganisations, leadership changes, new regulated
entities, systems renewals and their milestones, reporting-line changes,
integration deadlines.

**4. Their control and governance model, as they describe it themselves.** Lines
of defence, board risk appetite statements, supervision and testing cadence,
named control owners, the window in the year when the work is done. Their own
description is what makes step 3 of the story land, because it is unarguable.

**5. Their technology estate, split into confirmed and assumed.** Flag anything
not publicly confirmed. Do not assert vendor names, core platforms or integration
paths that are not sourced. An unconfirmed one belongs in the out-of-scope box
behind a flag, or off the card.

**6. Known buyer contacts and the thread each one owns.** Cost, coverage, risk,
compliance, technology. Verify people live this session. Enrichment-derived
people are corroborated before they reach the card, per
`../account-dossier/reference/enrichment-and-provenance.md`.

## What may never happen

- Never invent a number, a quote or a technology detail.
- Never assert an unconfirmed vendor, platform or integration path.
- Never name a live or active enforcement action. Convert it to general industry
  framing.
- Never upgrade an `ASSUME` to a `KNOW` without doing the verification yourself.

Where something is unconfirmed, mark it as a gap. A named gap is useful to a
seller. A plausible default is a liability.

## Conflicting sources

Where two sources define the same metric differently, keep both and flag the
discrepancy in the sources line on the card. Group and non-life combined ratios
computed on different bases are the classic case. Picking one silently is how a
seller gets caught quoting the wrong one live.

The flag is short and goes in the sources line, not in the story band. For
example: `Combined ratio: group 121.5% against non-life ex-interest 119.4%.
Definitions differ, verify before quoting externally.`

## How much is enough

Stop when the story's five steps each have a source and the card's slots are
filled inside the fit budget. A one-slider does not need the full dossier
research pass, and running one produces a card built from ten percent of the
material and a record nobody asked for.

If the user wants the rest of the material, that is the `account-dossier` skill
and it is a separate ask.
