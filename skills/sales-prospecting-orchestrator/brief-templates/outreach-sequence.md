---
brief_id: <slug-outreach-sequence>
issued_by: sales-prospecting-orchestrator
issued_to: contact-approach-writer
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. What must exist and why now — e.g. "Build the multi-touch,
multi-channel outreach cadence for {account}: assemble Aria's per-contact
messages into a sequenced, multi-threaded plan with explicit timing and
per-role entry points, ready for a human to run for the Q3 motion.">

## Context (links)

- `{output_folder}/company-context/brand-voice.md` (if present — keep cadence on-voice)
- `{output_folder}/work/{account-id}/approach-messages.md` (Aria's per-contact messages — each step maps to one)
- `{output_folder}/work/{account-id}/buying-committee.md` (the named DMU — for per-role entry points)
- `{output_folder}/company-context/playbooks/sequences.md` (if present — reusable cadence templates + channel rules)
- <add: anything the user already shared about channels, timing, or constraints>

## Deliverable

Write `{output_folder}/work/{account-id}/sequence-plan.md` (as `v1.md` in the
work folder). Include: a multi-touch, multi-channel cadence table (channel +
day/spacing + contact/role + mapped Aria message per step), per-role entry
points across the committee, a multi-threading view, and a human-in-the-loop
send-gate note.

## Acceptance Criteria

- [ ] A **multi-touch, multi-channel** sequence (email / LinkedIn / call).
- [ ] **Explicit timing** per step (day / spacing relative to step 1).
- [ ] **Per-role entry points** — a named first touch for each committee role.
- [ ] **Multi-threaded** across the committee, not single-threaded.
- [ ] A **human-in-the-loop send gate** — recommends sends, never auto-sends.
- [ ] **Each step maps to one of Aria's messages** — no invented copy.
- [ ] No invented open-/reply-rate benchmarks; illustrative numbers labelled `Example — illustrative, not benchmarks.`
- [ ] Gaps are marked `[UNKNOWN — needs input]`, not filled with guesses.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <e.g. channels available; sending limits / etiquette; cadence length; timezone; confidentiality>

## Instructions

1. Read the Context (links) that exist. Do not block on missing context.
2. Use capability PS (plan the sequence); consult the `sequences.md` playbook (SP) for reusable templates.
3. Rank personalization by signal strength; design per-role entry points and multi-thread across the committee.
4. Map every step to one of Aria's messages; add the human-in-the-loop send gate.
5. Write `v1.md`; set `state.yaml` `status: in-review`; notify the orchestrator.
