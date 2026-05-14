---
name: marketing-strategy
description: Comprehensive marketing strategy development workflow. Lead: marketing-orchestrator.
---

# Marketing Strategy Workflow

## Overview
Comprehensive marketing strategy development workflow.
Orchestrates all department leads to create a unified marketing plan.

## Phases
1. **Discovery & Analysis** — Gather context, analyze market, identify opportunities
2. **Strategy Development** — Define strategy across all marketing pillars
3. **Action Planning** — Create detailed execution plans
4. **Strategy Synthesis** — Compile final marketing strategy document

## On Activation

1. Load configuration (tolerant of missing files):
   - Try `{project-root}/_bmad/config.yaml`. If present, read `core.user_name`, `core.communication_language`, `core.document_output_language`, and `marketing-growth.output_folder`.
   - Try `{project-root}/_bmad/config.user.yaml`. If present, its `core.user_name` and `core.communication_language` override the shared values.
   - For any value still missing, use defaults: `user_name = there`, `communication_language = English`, `document_output_language = English`, `output_folder = {project-root}/_bmad-output`.

2. Ask the user for the inputs required by this workflow: product/service offering, target audience (ICP), current marketing status, budget range, and primary growth objective.

3. Load and execute the sibling `workflow.yaml` (colocated with this SKILL.md) phase by phase. Delegate to specialist agents as directed.

4. Save outputs to `{output_folder}/marketing-strategy/`.
