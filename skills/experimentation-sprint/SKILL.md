---
name: experimentation-sprint
description: "2-week experimentation sprint. Lead: Greta Growth (Growth Marketing). Picks 1-3 hypotheses from the backlog, designs experiments, ships, reads out, decides rollout. Use when user says experimentation sprint, AB test sprint, or 2-week experimentation cycle."
---

# Experimentation Sprint Workflow

## Overview
A focused 2-week sprint that takes 1-3 hypotheses from the experiment
backlog, designs them rigorously, ships them, reads results against
the pre-registered rollout criteria, and decides scale / discard /
extend.

## Phases
1. **Select** — pick from the experiment backlog (impact × confidence × effort).
2. **Design** — Eli Experiment specs each experiment.
3. **Ship** — implementation hand-off (Web/CRO or Lifecycle).
4. **Read-out** — apply pre-registered rollout criteria.

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
4. Save outputs to `{output_folder}/work/{sprint-name}/`.
