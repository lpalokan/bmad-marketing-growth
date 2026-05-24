---
name: product-launch
description: "Product launch workflow (T-6 weeks through T+2 weeks). Lead: Priya Position (PMM). Replaces v1 launch-sequence; B2B-tech-shaped with explicit PR / Digital / Field hand-offs. Use when user says product launch, launch motion, or T-6w through T+2w launch workflow."
---

# Product Launch Workflow

## Overview
Full launch motion from positioning to post-launch retro. Replaces
v1's launch-sequence (Product Hunt-centric). v2 lead is PMM (Priya
Position); the launch narrative is upstream of every downstream
brief (PR, Digital, Field, Content).

## Phases
1. **Narrative** — PMM owns the launch narrative + sales bundle.
2. **Down-stream briefs** — PR, Digital, Field, Content receive
   briefs anchored to the narrative.
3. **Launch day** — coordinated motion across domains.
4. **Post-launch** — 2-week wrap, retro, lessons.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## On Activation

1. Load configuration per template.
2. Confirm company-context exists; route to bootstrap if not.
3. Execute the sibling `workflow.yaml` phase by phase.
4. Save outputs to `{output_folder}/work/{launch-name}/`.
