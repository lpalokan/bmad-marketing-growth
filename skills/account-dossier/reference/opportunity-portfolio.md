# The opportunity portfolio

A dossier answers what to do first. A portfolio answers what the account is
worth working for. Where both are wanted, they are **one document with the
portfolio inside it**, never a dossier with a portfolio bolted on the end.

This file owns the portfolio contract. It was written from the merged
Ålandsbanken dossier of 19 August 2026, which established the shape.

## When to build one

Only when asked. A dossier without a portfolio is complete and is the default.

Build one when the user asks for a portfolio, an account plan, a
land-and-expand view, or "everything we could sell here". Two account facts
also make one worth offering unprompted:

- the account has more than one business where an offering has a home;
- the account has a structure, such as a group of supervised entities or a
  technology subsidiary, that changes what the same offering is worth.

## Where it goes

**Section 5, between the storyline and the first-touch messages.** The document
becomes nine sections and everything below section 4 shifts down by one.

| | Dossier alone | Dossier with a portfolio |
|---|---|---|
| 5 | First-touch messages | **Opportunity portfolio** |
| 6 | Questions for discovery | First-touch messages |
| 7 | Before you send | Questions for discovery |
| 8 | Sources | Before you send |
| 9 | | Sources |

The placement is the point and it is not a matter of taste. The storyline ends
by naming one ask. A reader who has just been told what to sell first is in
exactly the right position to be shown what sits behind it. Put the portfolio
after the messages and it reads as reference material nobody opens. Put it in
an appendix and it has been written for the author rather than the seller.

**Never append it.** A "Part Two", an annex, or anything after the sources
fails this standard even when the content is good.

## Frontmatter

Three fields change.

```yaml
title: "<Account>: account dossier and opportunity portfolio"
commercial_model: <the shape the first engagement takes>
structure_version: merged dossier, nine sections with the opportunity portfolio at section 5
```

The "How to read this" note says the document is both things, gives the section
count, and points a hurried seller at section 1 followed by section 5.1.

## The three tiers

Nine opportunities, three per tier. The tiers are the spine of the section and
they are defined by **who has to say yes**, not by size of prize.

| Axis | Small | Large | Transformative |
|---|---|---|---|
| The question it answers | Does this work here | Does this scale across our footprint | Does this change how we assure the business |
| Sponsor level | Department head | Management group | Board or its committee |
| Scope | One population, one entity | One domain, several entities | The group, including subsidiaries |
| Our shape | One orchestration agent, one capability | One agent at scale | Custom orchestration, or a partnership |
| Time to first value | Weeks | Quarters | Years |
| Risk to the customer | A pilot they can walk away from | Change to a live control process | Change to the assurance model itself |
| What it buys us | A coverage number nobody can argue with | A budget line | A position inside the operating model |

Reproduce that table as subsection 5.2, adapted to the account. It is what
stops a reader treating the tiers as small, medium and large versions of the
same deal.

Nine is a target rather than a quota. An account that honestly carries seven
gets seven, and the section says which tier came up short and why. Padding a
tier to reach nine is the failure this standard exists to prevent.

## Section shape

### 5.1 The portfolio at a glance

One table, and it is the only part most readers will read.

| Column | Holds |
|---|---|
| ID | S1 to S3, L1 to L3, T1 to T3 |
| Tier | Small, Large, Transformative |
| Opportunity | A complete sentence naming the work, not a product |
| Sponsor | A named person from section 3 wherever one exists |
| Our shape | The offering and the capability, in our own vocabulary |
| Time to first value | Weeks, quarters, years |
| Label | KNOW, ASSUME or SPECULATIVE |
| Qualifier | The single question that would confirm or kill it |

Follow the table with one short paragraph reading the shape of the whole set.
Not a summary of the rows. What the pattern across them tells a seller, such as
every small item sitting inside one function, or every transformative item
waiting on somebody who is not in the room.

### 5.2 How the three tiers differ

The axis table above, adapted.

### 5.3, 5.4, 5.5 One subsection per tier

Each carries a heading that states a conclusion about the tier, in the house
style. "Small, and every one of them is reachable this year" is a heading.
"Small opportunities" is a label and fails.

Then three opportunities, each with five blocks in this order and no others.

- **What it is.** The work, described so the customer would recognise it.
  Our capability in one sentence, never a feature list.
- **Why this account.** The account's own facts, sourced, that make this
  opportunity exist here rather than anywhere. If this block could appear in
  another account's dossier, the opportunity is not real yet.
- **What it needs from them.** Access, a decision, a named owner, a timebox.
  Concrete enough that a seller could ask for it out loud.
- **What would kill it.** The honest failure mode, named. Every opportunity
  has one. An opportunity with no kill condition has not been thought about.
- **The label and the qualifier.** `ASSUME` or `SPECULATIVE`, then one
  sentence beginning "The qualifier is". This is the single question that
  moves it forward or closes it.

### 5.6 What we ran and excluded, with the reasons

Every offering and capability considered and rejected, each with the reason,
in prose rather than a table.

This subsection carries more weight than it looks. It is what proves the
portfolio is a selection rather than a catalogue, and it stops the next person
re-running the same dead end. Where an offering has no home at the account at
all, say so plainly. Where one is real but premature, mark it **held back
rather than excluded** and say what would unlock it.

## The third label

The portfolio adds `SPECULATIVE` to the KNOW, ASSUME and GAP set in
`source-fidelity.md`. It is used only here, and only on an opportunity.

- **ASSUME** is our reasoning applied to facts we have. The opportunity
  follows from what the account has published.
- **SPECULATIVE** means a load-bearing part of the opportunity is unknown, and
  we are naming it anyway because it would be material if true.

A `SPECULATIVE` opportunity is honest. A `SPECULATIVE` opportunity presented
without its label is an invention. Nothing in the portfolio is ever `KNOW`
unless the account has already told us it wants the thing.

## What never appears in a portfolio

- **Any value, price, deal size or revenue estimate.** We have no basis for
  one and a plausible figure is a fabrication wearing a forecast's clothes.
  The portfolio ranks and sequences. It does not price.
- **A probability or a confidence percentage** on an opportunity.
- **A close date.** Time to first value is a shape, not a forecast.
- **An opportunity built on a capability our own material marks unconfirmed.**
  Check `offerings/` before writing one. Where the capability is unconfirmed,
  that belongs in 5.6 as an exclusion with the open item cited.

## Length

**2,500 to 3,500 words**, inside a total document of 7,000 to 10,000. The
dossier's own sections keep their existing budget in `length-budget.md`
unchanged, because the portfolio does not license a longer dossier.

Roughly: 5.1 and 5.2 are tables plus two short paragraphs, each opportunity
runs 200 to 300 words across its five blocks, and 5.6 takes 300 to 500.

If the section overruns, cut a whole opportunity and say in 5.6 why it went.
Never meet the budget by shortening the five blocks, because the blocks are
what make an opportunity assessable.
