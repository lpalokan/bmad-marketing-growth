---
brief_id: <slug-offering-advice>
issued_by: sales-prospecting-orchestrator
issued_to: service-offering-advisor
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. Recommend the best-fit offering(s) for {account}, with the pains
and proof to lead with — e.g. "Recommend which offering best fits {account} given
its profile and why-now, name the pains to lead with and the proof to cite, so
the storyline and approach can be built on a focused, provable pitch.">

## Context (links)

- `{output_folder}/company-context/icp.md` (if present)
- `{output_folder}/company-context/offerings.md` (+ `offerings/<slug>.md`)
- `{output_folder}/company-context/positioning.md` (if present)
- `{output_folder}/work/{account-id}/account-profile.md` (the account's profile)

## Deliverable

Write `{output_folder}/work/{account-id}/offering-advice.md` (as `v1.md` in the
work folder). Include: the recommended offering(s) with a fit rationale tied to
the account's pains; a pains → outcomes → metric map per recommended offering;
the case study/proof to cite; what NOT to lead with; and a **Sources** section.

## Acceptance Criteria

- [ ] Recommends ≥1 offering with a fit rationale tied to the account's actual pains.
- [ ] Maps each recommended offering's pains → quantifiable outcomes → the metric moved.
- [ ] Cites ≥1 relevant case study / proof (matched on vertical or pain where possible).
- [ ] Names what NOT to lead with for this account.
- [ ] Every claim is sourced; gaps marked `[UNKNOWN — needs input]`, not filled with guesses.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <e.g. offerings in scope for this motion; regions; confidentiality of proof; depth vs speed>

## Instructions

1. Read the Context (links) that exist. Do not block on missing context.
2. Use capability AO (advise which offering fits), drawing on the catalog (OC) and proof library (PL).
3. Recommend the best-fit offering(s), not the biggest; lead with the pains that match the account.
4. Write `v1.md`; set `state.yaml` `status: in-review`; notify the orchestrator.
