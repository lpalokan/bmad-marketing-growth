---
name: abm-program
description: "Quarterly ABM program workflow. Lead: Frank Field (Field Marketing). Tiering → orchestration → signals → measurement, with paired AE pods."
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

## On Activation

1. Load configuration per template.
2. Confirm company-context exists.
3. Execute the sibling `workflow.yaml`.
4. Save outputs to `{output_folder}/work/{program-name}/`.
