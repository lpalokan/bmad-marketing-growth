---
name: annual-planning
description: "Annual marketing plan workflow. Lead: Max Growth (CMO Orchestrator). Produces a domain-by-domain plan, quarterly sequencing, budget split, and the brief packs each domain needs to start the year."
---

# Annual Planning Workflow

## Overview
The kickoff-of-year workflow. Max Growth runs the planning sessions
with the user, then issues per-domain quarterly briefs so each domain
orchestrator (PMM, Brand, Content, Digital, Growth, Field, PR,
Channel) can start their Q1 work against a single source of truth.

## Phases
1. **Inputs** — Refresh company-context (run bootstrap if missing).
2. **Strategy** — Pick the 2-3 dominant motions per quarter.
3. **Resourcing** — Budget split + headcount + dependency map.
4. **Domain briefs** — Issue annual brief packs to each domain.
5. **Cadence** — Set the quarterly re-plan ritual.

## On Activation

1. Load configuration (tolerant of missing files):
   - Try `{project-root}/_bmad/config.yaml`. If present, read `core.user_name`, `core.communication_language`, `core.document_output_language`, and `marketing-growth.output_folder`.
   - Try `{project-root}/_bmad/config.user.yaml`. If present, its `core.user_name` and `core.communication_language` override the shared values.
   - For any value still missing, use defaults: `user_name = there`, `communication_language = English`, `document_output_language = English`, `output_folder = {project-root}/_bmad-output`.

2. Confirm company-context exists: `{output_folder}/company-context/icp.md`, `positioning.md`, `kpis.md`. If any missing, route the user to `/company-context-bootstrap` first.

3. Load and execute the sibling `workflow.yaml` phase by phase. Delegate to specialist agents as directed.

4. Save outputs to `{output_folder}/work/{yyyy}-annual-plan/`.
