---
brief_id: <slug-buying-committee>
issued_by: sales-prospecting-orchestrator
issued_to: buying-committee-mapper
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. What must exist and why now — e.g. "Map {account}'s buying
committee into a named, multi-threaded decision-making unit so the storyline and
outreach reach the economic buyer through a qualified champion, not a single
friendly contact.">

## Context (links)

- `{output_folder}/company-context/icp.md` (if present — buyer personas)
- `{output_folder}/company-context/buying-committee-model.md` (if present — the role → titles → criteria template)
- `{output_folder}/work/{account-id}/account-profile.md` (if present — org shape)
- `{output_folder}/work/{account-id}/fit-scorecard.md` (if present)
- <add: anything the user already shared about people at the account>

## Deliverable

Write `{output_folder}/work/{account-id}/buying-committee.md` (as `v1.md` in the
work folder). Include: the named DMU mapped to MEDDPICC roles (Economic Buyer,
Champion, Technical/evaluator buyer, Users, Procurement/Security/Legal); per
person a role, the metrics they own, and likely decision criteria; the reporting
lines and the **champion→EB path**; and a **Sources** section labeling each
person **confirmed** vs **inferred**.

## Acceptance Criteria

- [ ] Economic buyer, champion, technical buyer, and users identified — or each explicitly marked unknown.
- [ ] Champion qualified on **power + access-to-EB + personal motivation** (not title alone).
- [ ] Each person carries a role in the committee, the metrics they own, and likely decision criteria (technical/business/personal).
- [ ] Reporting lines / the champion→EB path are noted (or the gap is flagged).
- [ ] Every person carries a source; **inferred** vs **confirmed** is clearly labeled.
- [ ] The map is multi-threaded (not single-threaded); who else must be reached is named.
- [ ] Gaps are marked `[UNKNOWN — needs input]`, not filled with guesses.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <e.g. Clay credit budget; regions; seniority scope; confidentiality of contact sources>

## Instructions

1. Read the Context (links) that exist. Do not block on missing context.
2. Use capability MC (map committee); tune CM (the model) only if the reusable template is missing or stale.
3. Prefer Clay `find-and-enrich-contacts-at-company` / `find-and-enrich-list-of-contacts`; fall back to LinkedIn / Sales Navigator / web when unavailable.
4. Write `v1.md`; set `state.yaml` `status: in-review`; notify the orchestrator.
