---
name: abm-program
description: "Quarterly ABM program workflow. Lead: Frank Field (Field Marketing). Tiering → orchestration → signals → measurement, with paired AE pods. Use when user says ABM program, named-account program, or quarterly ABM motion."
---

# ABM Program Workflow

## Overview
A 12-week ABM program: tier the named-account list, build the multi-
channel orchestration, wire signals-to-actions, define measurement
that doesn't double-count, run the program, retro at the end.

## Phases
1. **Tiering** — account list × tier (1:1 / 1:few / 1:many).
2. **Orchestration** — per-tier multi-channel calendar.
3. **Signals & instrumentation** — signals-to-actions matrix.
4. **Run** — execute with AE pods, weekly check-ins.
5. **Retro** — what to keep / drop next quarter.

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
4. Save outputs to `{output_folder}/work/{program-name}/`.
