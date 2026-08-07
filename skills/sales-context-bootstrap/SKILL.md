---
name: sales-context-bootstrap
description: "Optional workflow that extends the shared company-context OKF bundle with the sales layer — offerings, case studies, scoring model, buying-committee model, signal library, and playbooks — building on the existing marketing context rather than duplicating it. Scratch, import, or ingest modes. Never required for the Sales Prospecting agents to work. Lead: sales-prospecting-orchestrator. Use when user says set up sales context, add offerings, seed the scoring model or playbooks, or ingest sales collateral."
---

# Sales Context Bootstrap Workflow

## Overview
Optionally extends the **shared** `company-context/` OKF bundle with the
**sales layer** — the durable, reusable-across-accounts knowledge the Sales
Prospecting Suite reads: `offerings.md` (+ `offerings/<slug>.md`),
`case-studies/<slug>.md`, `icp-fit-model.md`, `buying-committee-model.md`,
`signal-library.md`, and the `playbooks/` (`sequences.md`, `objections.md`,
`message-frameworks.md`). It **builds on** the marketing core
(`icp.md`, `positioning.md`, `brand-voice.md`, `kpis.md`, `tech-stack.md`) by
linking it, and it **never rewrites** those files. The folder **is a Google OKF
v0.1 bundle** — the same bundle `/company-context-bootstrap` writes; there is no
separate sales bundle. See `docs/company-context.md` for the schema and the
sales-layer ownership table, and `workflow.yaml::okf_conventions` for the
authoring rules.

**This workflow is OPTIONAL and never a prerequisite.** The Sales Prospecting
agents work without it — each reads whichever concepts are present and asks a
focused question when one is missing, and each owner agent can self-create its
concept on first use. Running this workflow only pre-seeds the layer so the
agents start better-grounded.

Three modes:

- **Scratch** — answer focused intake questions per sales concept.
- **Import & adapt** — point at another project's context folder (or a parent
  folder of projects); the workflow discovers which sales concepts are
  available, lets you pick a source and which to bring over, copies each in
  (upgrading frontmatter to OKF, preserving each concept's fixed owner), and
  walks you through adapting the project-specific parts and re-pointing every
  marketing-core link at this bundle. Offerings, case studies, and playbooks
  port well; scoring / committee / signal models are usually project-specific.
- **Ingest** — read the input folder, refactor dropped sales collateral
  (offering decks, battlecards, case-study PDFs, pricing sheets) into OKF
  concepts under `offerings/`, `case-studies/`, and `sources/`, cross-link
  them, and propose **gated** edits to the owner of any sales concept the new
  knowledge bears on. Run anytime.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## On Activation

1. Load configuration (tolerant of missing files; for each value, the first file that provides it wins):
   - Try `{project-root}/_bmad/custom/config.user.toml`, then `{project-root}/_bmad/custom/config.toml` (pinned overrides -- always win when present).
   - Try `{project-root}/_bmad/marketing-growth/config.yaml` (BMAD 6.x module config; flat keys `user_name`, `communication_language`, `document_output_language`, `output_folder`).
   - Try `{project-root}/_bmad/config.user.toml`, then `{project-root}/_bmad/config.toml` (BMAD 6.x root config; `[core]` keys, e.g. `output_folder`, `document_output_language`).
   - Legacy fallback: try `{project-root}/_bmad/config.yaml` (`core.user_name`, `core.communication_language`, `core.document_output_language`, `output_folder` at root or `marketing-growth.output_folder`), with `{project-root}/_bmad/config.user.yaml` overriding `user_name` and `communication_language`.
   - For any value still missing, use defaults: `user_name = there`, `communication_language = English`, `document_output_language = English`.
   - Resolve `output_folder` **silently — never ask the user**. Normalize a relative value against `{project-root}`. Then use the first of these that already contains a `company-context/` folder: the configured value, `{project-root}/output`, `{project-root}/_bmad-output` (legacy name, retired in v2.4). If none does, glob the project for `**/company-context/index.md` and `**/company-context/icp.md` (excluding `.git/`, `node_modules/`, `_bmad/`, `**/work/**`) and use its parent when there is exactly one match. Still nothing: use `{project-root}/output`. `output/` is the canonical name; `_bmad-output/` is read-only compatibility — never create it.

2. Greet the user in `{communication_language}` as Sam Sell and explain: this
   workflow **optionally** pre-seeds the **sales layer** of the shared
   **OKF v0.1 bundle** under `{output_folder}/company-context/` (offerings,
   case studies, the fit/scoring model, the buying-committee model, the signal
   library, and the playbooks). Make clear it is a convenience, not a
   requirement — the sales agents run without it. A full scratch intake takes
   20–40 minutes depending on how much is already documented; import and ingest
   are shorter.

3. **Soft prerequisite check — never blocks.** Look under
   `{output_folder}/company-context/` for the marketing core. If `icp.md` and
   `positioning.md` are present, note that the sales layer will link to them and
   proceed. If either is **missing**, tell the user the sales layer will still
   be created and will **link to them as forward-links** (OKF tolerates broken
   links), and that they can run `/company-context-bootstrap` anytime to fill
   the marketing core — then **proceed anyway**. Never hard-stop; never require
   the marketing bootstrap. This mirrors the suite principle that bootstraps are
   never required.

4. Locate the bundle before assuming there isn't one. Check
   `{output_folder}/company-context/`; if that is empty or absent, glob the
   project for `**/company-context/icp.md` and `**/company-context/index.md`,
   excluding `.git/`, `node_modules/`, `_bmad/` and `**/work/**`. One hit — use
   it and say which path you found, in one line, without asking anything.
   Several hits — list them and ask which to use. No hits — a new bundle goes
   in `{output_folder}/company-context/`.

   Then, for each existing sales-layer concept, show the user the current
   content and ask: keep / refresh / skip-this-concept. Never touch the
   marketing-core files.

5. Ask which mode to use: **scratch**, **import & adapt**, or **ingest** (see
   the three `## Overview` modes).

   - **Import & adapt**: ask for a folder path and resolve it (tolerant, never
     guess content). Use it directly if it contains recognized sales-layer
     concepts (`offerings.md`, `icp-fit-model.md`, `buying-committee-model.md`,
     `signal-library.md`, a `playbooks/` or `case-studies/` folder); otherwise
     glob up to **three levels** below it for any folder holding two or more
     recognized concepts. That finds `output/company-context/`,
     `_bmad-output/company-context/`, a bare `company-context/`, and the
     `context/<company>/` layout the companion `dwf-marketing-skills` repo
     uses — without needing the folder to be named anything in particular.
     One match: use it. Two or more: list each as
     `<relative path> (N recognized concepts)` and ask the user to choose one.
     If nothing resolves, say where you looked and offer to switch to
     scratch. Report which
     recognized sales concepts are present vs missing (ignore the
     marketing-core files and anything unrecognized), let the user
     include/exclude each, then for each included concept: copy it in (upgrade
     frontmatter to OKF — **preserve the concept's fixed owner**, add the OKF
     fields, `schema_version` 2, `last_updated` today, `last_updated_by: user`,
     Status `In progress`), re-point every marketing-core link at this bundle,
     and walk the user through adapting the project-specific fields. Apply
     **Source Fidelity**: never carry a client name, result, or metric from the
     source project as this project's — confirm or replace each. Concepts
     missing from the source fall back to the from-scratch intake or are
     skipped, per the user's choice.

   - **Ingest**: resolve the input folder silently, same rule as
     `output_folder` — the first of these that exists and is non-empty: a
     configured `input_folder` (flat key, or legacy
     `marketing-growth.input_folder`), `{project-root}/input`,
     `{project-root}/_bmad-input` (legacy). Default `{project-root}/input`. Refactor
     each file into OKF concept docs — offering material into `offerings/`,
     case studies into `case-studies/`, everything else into `sources/`
     (`resource` = original path) — cross-link to the relevant hubs, then
     propose **gated** edits to the owner of any sales concept the new knowledge
     bears on. Apply **Source Fidelity** to every number. Leave the original
     input files untouched. Never edit a marketing-core file — if a source
     bears on one, suggest `/company-context-bootstrap` and keep the knowledge
     in `sources/`.

6. Execute the sibling `workflow.yaml` phase by phase for the chosen mode (skip
   any intake phase whose concept was imported & adapted in step 5; ingest skips
   intake entirely). Write every concept per `workflow.yaml::okf_conventions`
   and the schema in `docs/company-context.md` (OKF frontmatter + `owner`,
   `last_updated`, `last_updated_by`, `schema_version: 2`; Status line in the
   body). Never change a concept's **owner** — ownership is fixed by the table
   in `docs/company-context.md` (note: `case-studies/` ownership defers to the
   `customer-advocacy-references` / Cara Customer agent, part of this suite).

7. Always finish in the **handoff** phase: refresh the root `index.md`
   (`okf_version: "0.1"`) by **adding** the sales sections/subfolders while
   preserving any existing marketing sections, append a dated `log.md` entry,
   and refresh the `sales-prospecting:okf` block in `{project-root}/AGENTS.md`
   (idempotent, gated with a diff — read it from the sibling
   `templates/agents-okf-block.md`), leaving any `marketing-growth:okf` and
   `bmad-manager:bmad` blocks untouched. Outputs: see `docs/company-context.md`
   for the file table and bundle layout.
