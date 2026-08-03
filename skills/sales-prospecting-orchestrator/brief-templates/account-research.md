---
brief_id: <slug-account-research>
issued_by: sales-prospecting-orchestrator
issued_to: account-research-analyst
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. What must exist and why now — e.g. "Build a comprehensive,
sourced profile of {account} to ground fit scoring, committee mapping, and the
account storyline for the Q3 motion.">

## Context (links)

- `{output_folder}/company-context/icp.md` (if present)
- `{output_folder}/company-context/offerings.md` (if present — what we're matching to)
- `{output_folder}/company-context/signal-library.md` (if present)
- `docs/opportunity-brief-method.md` (if present — the six-domain research method)
- `docs/overlays/<domain>.md` (if one matches the target's domain — sector examples)
- <add: anything the user already shared about the account>

## Deliverable

Write `{output_folder}/work/{account-id}/account-profile.md` (as `v1.md` in the
work folder), structured by the six research domains: **§1 the target** (identity &
scale, leadership [verify live], financial/strategic trajectory, regulatory/enforcement
record [verify live], governance & control shape), **§2 the unit** (jobs-to-be-done
from JDs), **§3 leaders in public** (speaker intel), **§4 the field** (who's circling),
**§5 relationship layer** (warm accounts only, kept separate), **§6 our corpus**.
Include a **why-now** (confirmed pain candidate), a **Sources** section, and an
**Exit Check** block. Sort every fact into **Know** / **Assume** / **Don't-know**.

## Acceptance Criteria

- [ ] §1 present: identity & scale, business mix, leadership (name/title/start/still-in-seat), trajectory, regulatory record where applicable, governance/control shape.
- [ ] Technographics tagged greenfield / complementary / displacement vs offerings.
- [ ] §2 unit read from the target's own JDs (or comparable JDs marked `[confirm]`); §3 at least one leader searched by name for public/speaker intel.
- [ ] §4 field scanned by entity class + the negative run (any customer story naming the target?); §5 captured only if warm and kept separate.
- [ ] A single **why-now** written (or "no why-now found") backed by ≥1 confirmed pain candidate.
- [ ] Every fact sorted **Know** (sourced, cited) / **Assume** (`[confirm]`) / **Don't-know** (`[gap — meeting objective]`); no peer case-study detail attributed to the target.
- [ ] **Verify-live** honoured: leaders, penalty status, prices sourced this session, not inherited from memory/prior brief/training.
- [ ] **Exit Check** block present and passing (or residual gaps named as meeting objectives); the single most decision-relevant Don't-know is named.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <e.g. Clay credit budget; regions; depth vs speed; confidentiality of sources>

## Instructions

1. Read the Context (links) that exist. Do not block on missing context.
2. Use capability BP (build profile — the six domains), pulling in JD, LP, FS and,
   if the account is warm, RL at the depth this brief asks for; then WN (why-now).
3. Prefer Clay `find-and-enrich-company`; fall back to web when unavailable. Use the
   Google Drive MCP for §6 corpus if connected. Verify leaders/penalties/prices live.
4. Run capability XC (exit check) before handing off.
5. Write `v1.md`; set `state.yaml` `status: in-review`; notify the orchestrator.
