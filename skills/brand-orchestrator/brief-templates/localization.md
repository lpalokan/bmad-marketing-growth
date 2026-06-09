---
brief_id: <yyyy-mm-{locale}-rollout>
issued_by: brand-orchestrator
issued_to: localization-international-lead
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<Target locale(s), assets in scope, launch date, budget, owner per
locale.>

## Context (links)

- `{output_folder}/company-context/brand-voice.md`
- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/icp.md`
- <link to current English source-of-truth assets, prior locale rollout
  retros, translation memory, glossary if any>

## Deliverable

`work/{brief_id}/v1.md`: per-locale voice adaptation guide, glossary
delta, translation-memory setup, QA plan, in-market reviewer plan.

## Acceptance Criteria

- [ ] Voice adaptation guide names what stays and what bends in this
      locale (with examples).
- [ ] Glossary covers product names, core noun phrases, and any
      regulated terms (e.g. financial / health).
- [ ] Translation memory setup specified: tool, leverage strategy,
      reuse plan.
- [ ] QA plan covers: linguistic review, in-market review,
      typographic / encoding sanity, hreflang verification.
- [ ] At least one in-market reviewer named per locale.
- [ ] No locale shipped without an in-market reviewer.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Locales: <list>.
- Vendor / freelancer pool: <user-supplied>.
- <Compliance constraints per locale.>

## Instructions

1. Read linked context first.
2. Use capability `LR` (locale rollout) from your SKILL.md.
3. Write `v1.md`; update `state.yaml`.
