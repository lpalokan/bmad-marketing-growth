---
brief_id: <yyyy-qN-brand-narrative>
issued_by: brand-orchestrator
issued_to: brand-narrative-strategist
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<Why now; what changed in positioning, market, or strategy that
triggers this refresh.>

## Context (links)

- `{output_folder}/company-context/brand-voice.md`
- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/icp.md`
- <recent customer interviews, latest brand audit, prior narrative
  doc, analyst reports>

## Deliverable

`work/{brief_id}/v1.md`: through-line statement, narrative chapters
mapped to funnel stages, sample asset per chapter, voice compliance
notes, localization-readiness notes.

## Acceptance Criteria

- [ ] Through-line is one sentence and ties to `positioning.md`.
- [ ] Each chapter maps to one funnel stage (awareness, consideration,
      decision, expansion).
- [ ] Each chapter has a sample asset (subject line, headline, hero,
      one-pager opener) in brand voice.
- [ ] Voice compliance: every sample passes the `brand-voice.md`
      don't list.
- [ ] Localization-readiness notes flag idioms / cultural references
      that will need adaptation.
- [ ] No invented customer outcomes or quotes.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <Voice attributes that may not move (e.g. "stays expert; does not
  become irreverent")>.

## Instructions

1. Read every linked file first.
2. Use capability `NA` (narrative architecture) from your SKILL.md.
3. Write `v1.md`; update `state.yaml`.
