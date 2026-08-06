---
brief_id: <slug-field-scan>
issued_by: sales-prospecting-orchestrator
issued_to: account-research-analyst
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. What must exist and why now — e.g. "Map who is already circling
{account} and its segment, with what frame and what language the buyer has been sold,
so fit scoring, offering advice, and the storyline differentiate against the real
competitive water — and establish whether anyone has published a customer story naming
{account}.">

## Context (links)

- `{output_folder}/company-context/icp.md` (if present — the segment definition)
- `{output_folder}/company-context/offerings.md` (if present — what we differentiate)
- `{output_folder}/work/{account-id}/account-profile.md` (if present — the target)
- `docs/opportunity-brief-method.md` §4 (if present — the field method + gate rule)
- `docs/overlays/<domain>.md` (if one matches — the sector-specific competitor classes)

## Deliverable

Write the field scan as `v1.md` under `{output_folder}/work/{account-id}/` (or append a
**§4 The field** section to `account-profile.md`). Include: the field mapped **by
entity class** (with any skipped class and why), who is circling this target/segment and
their frame, the language the buyer has already been sold, and the **negative-search**
result (is there a published customer story naming this target?). Add a **Sources**
section.

## Acceptance Criteria

- [ ] The field is scanned **across entity classes**, not a fixed name list; any skipped class is named with a reason.
- [ ] For the segment: which use cases are already landing, who is circling this target, and with what frame — each sourced.
- [ ] The language/vocabulary the buyer has already been sold is captured (what is already burned).
- [ ] The **negative** is run: a search for a published customer story naming the target, with the result stated ("none found → be-first proof" or who is inside).
- [ ] The **gate rule** holds: every peer artefact is treated as market pattern (**Assume**, `[confirm]`), never as a **Know** about this target; no reference customer's detail is attributed to the target.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <e.g. which competitor classes matter most here; regions; confidentiality of sources>

## Instructions

1. Read the Context (links) that exist. Do not block on missing context.
2. Use capability FS (scan the field).
3. Sweep by entity class (see the overlay for the sector roster); run the negative.
4. Apply the gate rule to every peer artefact; keep market pattern separate from target fact.
5. Write `v1.md`; set `state.yaml` `status: in-review`; notify the orchestrator.
