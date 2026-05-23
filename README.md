# Marketing Growth Suite

> **v2.0 — international B2B technology marketing.** The suite is being
> refactored from a PLG/indie-SaaS roster to an 8-domain B2B marketing
> org with a brief-driven delegation protocol. This README describes the
> v2 target state. The rollout is phased — see **Rollout status** below.

An AI-powered marketing team for international B2B technology
companies — a CMO orchestrator coordinating 8 domain orchestrators and
~33 specialists, plus Tier-1 workflows that string them together.

Distributed as **both** a native [Claude Code plugin](https://code.claude.com/docs/en/plugins.md) and a [BMAD framework](https://github.com/bmad-code-org/BMAD-METHOD) module. One physical copy of every skill; pick whichever installer you prefer.

Forked from [**MatthiasMRC/bmad-marketing-growth**](https://github.com/MatthiasMRC/bmad-marketing-growth) — original Marketing Growth Suite by Matthias ([@matthias_mrc](https://x.com/matthias_mrc)).

## Source Fidelity

Every agent enforces a **Source Fidelity** rule (see the dedicated section in each `SKILL.md`):

- No invented metrics, benchmarks, conversion rates, or audience sizes. Numbers must come from the user's input or a cited `WebSearch` result.
- Missing data triggers a focused question, not a plausible default.
- Sample emails / posts / dashboards with numbers are explicitly labeled `Example — illustrative, not benchmarks.`
- Persona backstory is treated as tone calibration, not authority — agents won't invent past clients, study results, or proprietary stats to fit the character.

This is the main behavioral difference from a generic AI marketing assistant.

---

## v2 architecture

### Org chart

```
Max Growth — CMO Orchestrator
Pixel Metrics — Measurement & Attribution Staff   (scope: attribution, forecasting, dashboards, scoring model design)

├── Product Marketing
│   ├── Positioning & Messaging PMM
│   ├── Competitive Intelligence PMM
│   └── Launch & Sales Enablement PMM
│
├── Brand
│   ├── Brand Narrative & Voice Strategist
│   └── Localization & International Lead
│
├── Content Marketing  (Milo Page, elevated)
│   ├── Content SEO Strategist (Quinn, renamed)
│   └── Technical Content Writer
│
├── Digital Marketing
│   ├── Web & CRO Specialist
│   ├── Paid Search Specialist                (Google/Bing, PMax)
│   ├── Paid Social & Demand Specialist        (LinkedIn/Meta/Google Demand Gen/YouTube Ads)
│   ├── Marketing Automation Engineer          (HubSpot/Marketo workflows, lead routing)
│   └── Technical SEO Engineer                 (infra, schema, Core Web Vitals, hreflang)
│
├── Growth Marketing
│   ├── Lifecycle & Activation  (Ember, repositioned)
│   └── Experimentation & Funnel Lead
│
├── Field Marketing
│   ├── ABM Strategist
│   ├── Events & Webinars Producer
│   ├── Customer Advocacy & References
│   └── Social Media Strategist (Nova; orchestrator, logically nested)
│       ├── LinkedIn Creator (Ivy)
│       └── YouTube Strategist (Yuri)
│       (Twitter and Reddit are Nova's capabilities, not standalone agents)
│
├── PR & Communications
│   ├── Media Relations Specialist
│   └── Analyst Relations Specialist           (Gartner, Forrester, IDC)
│
└── Channel & Partner Marketing
    └── Partner & Marketplace Manager
```

### Brief-driven delegation protocol

Orchestrators don't dispatch via chat — they write a `brief.md` under
`_bmad-output/work/{deliverable-id}/`. The specialist reads the brief,
produces `v1.md`, and the orchestrator reviews against the acceptance
criteria. Verdicts are `APPROVED`, `NEEDS_REVISION` (with a numbered
list of required changes), or `ESCALATED` (after `max_revisions` is
hit). On approval, `state.yaml` is written with `frozen: true` and the
folder becomes part of the company's marketing record.

Full schemas, state machine, and rules: **[`docs/protocol.md`](docs/protocol.md)**.

### Three memory tiers

| Tier                                            | Purpose                                          | Owned by         | Lifecycle                |
|-------------------------------------------------|--------------------------------------------------|------------------|--------------------------|
| `_bmad-output/company-context/`                 | Shared, durable facts (ICP, positioning, KPIs…) | Per-file owner   | Read-mostly, refreshed    |
| `_bmad-output/work/{id}/`                       | Per-deliverable trail (brief, versions, review) | Issuing orch.    | Frozen on accept          |
| `_bmad/_memory/{code}-sidecar/memories.md`      | Per-agent private notes                          | The agent itself | Free-form, append on save |

The sidecar pattern is **unchanged** from v1. See **[`docs/company-context.md`](docs/company-context.md)** for the company-context schema and ownership table.

### One-time setup: bootstrap company context

Before invoking any v2 agent, run the bootstrap workflow once. It fills
the five shared `company-context/` files every agent reads on
activation:

```
/company-context-bootstrap
```

Agents that find `company-context/` missing will refuse to act and ask
you to run this first.

---

## Rollout status

The v2 refactor lands in phases. Each phase keeps `module.yaml`,
`.claude-plugin/marketplace.json`, and `.claude-plugin/plugin.json` in
lockstep so installs never break mid-sequence.

| Phase | Scope                                         | Status      |
|-------|-----------------------------------------------|-------------|
| 0     | Foundations: docs, bootstrap, version bump    | In progress |
| 1     | Product Marketing (4 skills)                  | Pending     |
| 2     | Digital Marketing (6 skills)                  | Pending     |
| 3     | Growth Marketing (2 new + 1 rename)           | Pending     |
| 4     | Brand + Content refresh (3 new + 1 rename)    | Pending     |
| 5     | Field + PR + Channel (10+ new, 6 retired)     | Pending     |
| 6     | Tier-1 workflows (7 workflows)                | Pending     |
| 7     | Tier-2 workflows (incremental)                | Deferred    |

Until a phase is marked Complete, the corresponding v1 agents remain in
place. Where v2 retires a v1 agent, the v1 agent stays installed until
the phase that retires it lands.

---

## Installation

### Option A — Native Claude Code plugin

No Python, no generation step. Claude Code reads the skills directly from the plugin folder.

**Claude Desktop (zip upload):**
1. Zip the repo root:
   ```bash
   cd /path/to/marketing-growth
   zip -r ../marketing-growth.zip .
   ```
2. In Claude Desktop, open the plugin install dialog and select the zip. Claude Desktop unpacks it, reads `.claude-plugin/plugin.json`, and loads all skills declared in `marketplace.json`.

**Claude Code CLI (local development):**
```bash
claude --plugin-dir /path/to/marketing-growth
```

**From a marketplace** (once published): add this repo as a marketplace in Claude Code, then:
```bash
claude plugin install marketing-growth@<your-marketplace-name>
```

All skills appear as `/marketing-growth:<skill-name>` (or the short name if overridden in each SKILL.md's frontmatter). No further setup is required.

### Option B — BMAD module

Install with the BMAD framework's installer, which reads `module.yaml` at the repo root:

```bash
npx bmad-method install --custom-source /path/to/marketing-growth
```

The installer prompts for the 4 questions declared in `module.yaml` (user name, communication language, document output language, output folder) and writes the answers into your project's `_bmad/config.yaml` (shared) and `_bmad/config.user.yaml` (personal, gitignore-worthy). Agents read these at activation.

Optional — gitignore personal settings:
```bash
echo "_bmad/config.user.yaml" >> .gitignore
```

Agents self-create their memory sidecars on first activation and fall back to sensible defaults if no config is present.

---

## BMAD compliance posture

The v2 refactor preserves full BMAD compliance:

- `module.yaml` at repo root with `code`, `name`, `module_version`, `module_greeting`, `questions[]`, `agents[]`.
- Per-skill `SKILL.md` (frontmatter `name` + `description`, `## On Activation` block) and `customize.toml` (`[agent]` block).
- `agent_type` is one of the two existing values: `"orchestrator"` or `"specialist"`. No new types introduced — Nova stays `"orchestrator"` despite being logically nested under Field.
- `workflow.yaml` keeps its existing shape. v2 adds **one optional field per step**: `brief_template: "brief-templates/NN-name.md"`. Older BMAD validators that don't know it will ignore it; v2 orchestrators consume it.
- Per-skill `brief-templates/` directories are convention-based (analogous to `prompts/`); BMAD doesn't validate their contents.
- Sidecar memory at `_bmad/_memory/{code}-sidecar/memories.md` is unchanged.
- The Source Fidelity block is **deliberately duplicated** per SKILL.md — no `skills/_shared/`.

Run `Validate Module (VM)` after every phase to catch drift.

---

## Updating

The plugin is version-controlled via `git`. To update, pull the latest version of the repo.

There is no skill regeneration step — every SKILL.md is canonical source, maintained in `skills/` directly.

---

## Customizing

### Add a new agent

1. Create `skills/your-agent/SKILL.md` — copy `docs/on-activation-template.md` for the `## On Activation` block; copy the Source Fidelity block verbatim from any existing SKILL.md.
2. Create `skills/your-agent/customize.toml` with an `[agent]` block (code, name, title, icon, description, agent_type).
3. If the agent has capability-specific prompts, add them under `skills/your-agent/prompts/<code>.md` and reference each in the SKILL.md Capabilities table.
4. If the agent is an orchestrator, add `skills/your-agent/brief-templates/<template>.md` for each delegation pattern.
5. Add the skill path to `.claude-plugin/marketplace.json`.
6. Add an `agents:` entry to `module.yaml`.

### Add a new workflow

1. Create `skills/your-workflow/SKILL.md` (copy an existing workflow as a template).
2. Create `skills/your-workflow/workflow.yaml` with `phases:` and `steps:`. For v2 workflows, reference brief templates via the `brief_template:` field on each step.
3. Add per-step brief templates under `skills/your-workflow/brief-templates/`.
4. Add the skill path to `.claude-plugin/marketplace.json`.

---

## Repository structure

```
marketing-growth/
├── .claude-plugin/
│   ├── plugin.json                    ← Native Claude Code plugin manifest
│   └── marketplace.json                ← Marketplace distribution manifest
├── module.yaml                         ← BMAD module manifest (agent roster + install questions)
├── docs/                               ← v2 protocol & schemas
│   ├── protocol.md                     ← Brief/review/state schemas + state machine
│   ├── company-context.md              ← Company-context file table + ownership
│   └── on-activation-template.md       ← Drop-in template for new agents
├── skills/                             ← All skills — single source of truth
│   ├── marketing-orchestrator/         ← Orchestrator (CMO)
│   │   ├── SKILL.md
│   │   ├── customize.toml              ← [agent] metadata
│   │   ├── prompts/                    ← Per-capability instruction bodies
│   │   └── brief-templates/            ← (orchestrators only) brief templates for delegations
│   ├── {domain}-orchestrator/          ← One per domain (PMM, Brand, Content, Digital, Growth, Field, PR, Channel)
│   ├── {specialist-code}/              ← Specialist agents under a domain
│   │   ├── SKILL.md
│   │   ├── customize.toml
│   │   └── prompts/
│   ├── company-context-bootstrap/      ← One-time intake workflow
│   └── {workflow-code}/                ← Tier-1 workflow (annual-planning, product-launch, content-pipeline, paid-campaign-launch, experimentation-sprint, abm-program, growth-audit)
│       ├── SKILL.md
│       ├── workflow.yaml
│       └── brief-templates/            ← Per-step brief templates
└── README.md
```

Every skill is canonical source. No hidden YAML generators, no pre-render step — what you see under `skills/` is what both installers consume.

---

## Credits

Original Marketing Growth Suite by **Matthias** ([@matthias_mrc](https://x.com/matthias_mrc)) — [MatthiasMRC/bmad-marketing-growth](https://github.com/MatthiasMRC/bmad-marketing-growth). This fork is maintained by [@lpalokan](https://github.com/lpalokan).

## License

MIT — use freely, adapt as needed.

---

*Built with the [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) — AI agent framework for Claude Code. Also installable as a native [Claude Code plugin](https://code.claude.com/docs/en/plugins.md).*
