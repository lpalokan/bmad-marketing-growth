---
name: competitive-teardown
description: "Single-competitor teardown workflow. Lead: Priya Position (PMM). Produces a teardown + battle card + landscape-section update. Use when user says competitive teardown workflow, single-competitor deep-dive, or battle card production."
---

# Competitive Teardown Workflow

## Overview
A 1-week motion to produce a full teardown of one competitor: teardown
doc, battle card, landscape-section update in `positioning.md`.

## Phases
1. **Commission** — Priya issues CT brief to Connor.
2. **Teardown** — Connor produces v1.
3. **Battle card** — Connor produces 1-page derivative.
4. **Adopt** — update positioning.md Primary Alternatives section.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## On Activation

1. Load configuration per template.
2. Confirm company-context exists.
3. Execute the sibling `workflow.yaml`.
4. Save outputs to `{output_folder}/work/{yyyy-mm-competitor-X-teardown}/`.
