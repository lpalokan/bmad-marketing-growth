---
brief_id: <yyyy-mm-competitor-{name}-teardown>
issued_by: product-marketing-orchestrator
issued_to: competitive-intelligence-pmm
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. Name the competitor, why now, and what the deliverable
will be used for — e.g. "Build a teardown of {Competitor X} after we
lost the {ACME} deal to them in Q2. Deliverable will feed (a) sales
battle card, (b) PMM section in `positioning.md` Primary Alternatives,
(c) AR briefing pack.">

## Context (links)

- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/positioning.md`
- <competitor URL>, <competitor pricing page>, <latest analyst report
  if available>, <user-supplied win/loss notes>

## Deliverable

Write under `{output_folder}/work/{brief_id}/v1.md`:

- Competitor overview (1 paragraph).
- Positioning frame: their stated category, their stated buyer, their
  stated key benefit, their reason-to-believe.
- ICP overlap with us (which segments / personas).
- Pricing model (tiers, anchor, packaging).
- Top 3 strengths (with public sources).
- Top 3 weaknesses (with public sources or our own product evidence).
- "How we sell against them" — 5 bullets, actionable for AEs.
- Red-team: 3 scenarios where the competitor wins and why.
- Battle card (1 page, copy-pasteable into sales tools).

## Acceptance Criteria

- [ ] Every public claim has an inline source link or footnote.
- [ ] No competitive claim is asserted without a source.
- [ ] ICP overlap names specific segments from our `icp.md`.
- [ ] Top 3 strengths and top 3 weaknesses are distinct (no item is
      both — pick whichever side of the ledger it belongs on).
- [ ] "How we sell against them" maps each bullet to a specific
      objection.
- [ ] Red-team section is honest — no straw-man competitors.
- [ ] Battle card fits one page.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <e.g. "Public sources only — do not reference user-only data
  (e.g. CRM win/loss notes) in the battle card; they may inform the
  weakness list but cite as 'internal'.">
- <e.g. "Avoid disparaging language in the battle card — focus on
  positioning differences, not company-bashing.">

## Instructions

1. Use capability `CT` (competitor teardown) from your SKILL.md.
2. Pull public material first: pricing page, product pages, analyst
   reports, recent press, G2/TrustRadius reviews (use as
   triangulation, not as ground truth — cite review counts).
3. Cross-reference our `icp.md` for overlap calculation.
4. Write to `{output_folder}/work/{brief_id}/v1.md`. Update
   `state.yaml` to `status: in-review` and notify the orchestrator.
