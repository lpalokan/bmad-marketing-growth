---
brief_id: <yyyy-mm-{topic}-tech-content>
issued_by: content-architect
issued_to: technical-content-writer
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<Deliverable type, target audience, distribution, business outcome.>

## Context (links)

- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/brand-voice.md`
- <link to source material: PRD, architecture docs, customer
  interviews, competing whitepapers>

## Deliverable

`work/{brief_id}/v1.md` (or sub-files per Constraints): full piece
ready for technical-accuracy review, with sources cited for every
benchmark and a reviewer plan.

## Acceptance Criteria

- [ ] Each numeric / benchmark claim has an inline source.
- [ ] All code / config samples are syntactically valid and runnable
      in the language / platform claimed.
- [ ] Architecture diagrams have alt text describing the diagram.
- [ ] Technical accuracy reviewer is named and scheduled.
- [ ] Brand voice: passes `brand-voice.md` don't list.
- [ ] No invented customer quotes.
- [ ] Reading-grade target met (specify in Constraints).

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Length target: <e.g. 8-12 pages>.
- Reading grade: <e.g. ≤ Grade 12 Flesch-Kincaid>.
- <Embargo, NDA, or competitive-mention rules.>

## Instructions

1. Read linked source material first.
2. Use capability `WP` (whitepaper) / `SB` (solution brief) / `TG`
   (technical guide) from your SKILL.md.
3. Write `v1.md`; update `state.yaml`.
