---
name: launch-sequence
description: "Comprehensive product/feature launch workflow coordinating all marketing activities from J-14 to J+7. Lead: launch-coordinator."
---

# Launch Sequence Workflow

## Overview
Comprehensive product/feature launch workflow.
Coordinates all marketing activities from J-14 to J+7.

## Phases
1. **Launch Preparation (J-14 to J-7)** — Prepare all launch assets and strategies
2. **Pre-Launch (J-7 to J-1)** — Build anticipation and final preparations
3. **Launch Day (J-Day)** — Execute launch with coordinated activities
4. **Post-Launch (J+1 to J+7)** — Maintain momentum and optimize

## On Activation

1. Load configuration (tolerant of missing files):
   - Try `{project-root}/_bmad/config.yaml`. If present, read `core.user_name`, `core.communication_language`, `core.document_output_language`, and `marketing-growth.output_folder`.
   - Try `{project-root}/_bmad/config.user.yaml`. If present, its `core.user_name` and `core.communication_language` override the shared values.
   - For any value still missing, use defaults: `user_name = there`, `communication_language = English`, `document_output_language = English`, `output_folder = {project-root}/_bmad-output`.

2. Ask the user for the inputs required by this workflow: product/feature name, launch date target, launch type (new product, feature, major update, campaign), and target platforms.

3. Load and execute the sibling `workflow.yaml` (colocated with this SKILL.md) phase by phase. Delegate to specialist agents as directed.

4. Save outputs to `{output_folder}/launch-sequence/`.
