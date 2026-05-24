---
name: positioning-workshop
description: "Positioning workshop workflow. Lead: Priya Position (PMM). Refreshes positioning.md and messaging pillars via a focused workshop."
---

# Positioning Workshop Workflow

## Overview
A focused 1-2 week workshop to refresh `company-context/positioning.md`
and the supporting messaging pillars. Lead is Priya; delegates to
Mona Message for execution.

## Phases
1. **Inputs** — load current positioning + win/loss + analyst views.
2. **Statement** — refresh positioning statement.
3. **Pillars** — refresh 3 messaging pillars.
4. **Adopt** — update `positioning.md` (with user sign-off).

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
4. Save outputs to `{output_folder}/work/{yyyy-qN-positioning-workshop}/`.
