# Marketing Growth Suite

An AI-powered marketing team for B2B SaaS — 15 agents (6 orchestrators + 9 specialists), 6 workflows, and Ultimate SEO & GEO.

Distributed as **both** a native [Claude Code plugin](https://code.claude.com/docs/en/plugins.md) and a [BMAD framework](https://github.com/bmadcode/bmad-method) module. One physical copy of every skill; pick whichever installer you prefer.

Forked from [**MatthiasMRC/bmad-marketing-growth**](https://github.com/MatthiasMRC/bmad-marketing-growth) — original Marketing Growth Suite by Matthias ([@matthias_mrc](https://x.com/matthias_mrc)). This fork removes the DWF tone-of-voice analyzer and the BMAD setup wizard skill, and adds the Source Fidelity guardrail described below.

## Source Fidelity

Every agent enforces a **Source Fidelity** rule (see the dedicated section in each `SKILL.md`):

- No invented metrics, benchmarks, conversion rates, or audience sizes. Numbers must come from the user's input or a cited `WebSearch` result.
- Missing data triggers a focused question, not a plausible default.
- Sample emails / posts / dashboards with numbers are explicitly labeled `Example — illustrative, not benchmarks.`
- Persona backstory is treated as tone calibration, not authority — agents won't invent past clients, study results, or proprietary stats to fit the character.

This is the main behavioral difference from a generic AI marketing assistant.

---

## What's included

### Agents

| Agent | Persona | Role |
|-------|---------|------|
| `/marketing-orchestrator` | Max Growth | Head of Marketing — strategy, prioritization, agent delegation |
| `/content-architect` | Milo Page | Editorial calendars, content briefs, long-form content |
| `/seo-strategist` | Quinn Crawler | Keyword research, technical audits, organic growth |
| `/social-media-strategist` | Nova Reach | Multi-platform social strategy coordinator |
| `/launch-coordinator` | Luna Blast | Product launch orchestration J-14 to J+7 |
| `/growth-analyst` | Pixel Metrics | Funnel analysis, KPIs, growth metrics |
| `/linkedin-creator` | Ivy Pro | LinkedIn content and paid ads |
| `/twitter-ghostwriter` | Vex Thread | Twitter/X threads and viral content |
| `/instagram-strategist` | Indy Grid | Instagram visual content strategy |
| `/youtube-strategist` | Yuri Views | YouTube growth and video SEO |
| `/tiktok-creator` | Tikko Viral | TikTok short-form content |
| `/discord-community-manager` | Disco Dave | Discord community building |
| `/reddit-growth-hacker` | Karma Ken | Reddit community marketing |
| `/pinterest-strategist` | Penny Pin | Pinterest SEO and visual discovery |
| `/email-nurture` | Ember Flow | B2B email nurture sequences (TOFU → BOFU) |

### Workflows

| Workflow | Lead | Description |
|----------|------|-------------|
| `/marketing-strategy` | Max Growth | Full strategy from research to go-to-market |
| `/content-pipeline` | Milo Page | Brief to published content |
| `/social-campaign` | Nova Reach | Multi-platform campaign from strategy to publication |
| `/launch-sequence` | Luna Blast | Full launch coordination J-14 to J+7 |
| `/growth-audit` | Pixel Metrics | Comprehensive growth metrics audit |
| `/seo-sprint` | Quinn Crawler | SEO audit to quick-win implementation |

### Utility Skills

| Skill | Description |
|-------|-------------|
| `/ultimate-seo-geo` | Universal SEO + GEO audits — scored full-site audits, Core Web Vitals, schema/JSON-LD, entity signals, and AI-citation optimization for AI Overviews, ChatGPT, Perplexity. Encapsulated from [mykpono/ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo) (MIT, by Myk Pono) |

---

## Installation

### Option A — Native Claude Code plugin

No Python, no generation step. Claude Code reads the 22 skills directly from the plugin folder.

**Claude Desktop (zip upload):**
1. Zip the repo root:
   ```bash
   cd /path/to/marketing-growth
   zip -r ../marketing-growth.zip .
   ```
2. In Claude Desktop, open the plugin install dialog and select the zip. Claude Desktop unpacks it, reads `.claude-plugin/plugin.json`, and loads all 22 skills.

**Claude Code CLI (local development):**
```bash
claude --plugin-dir /path/to/marketing-growth
```

**From a marketplace** (once published): add this repo as a marketplace in Claude Code, then:
```bash
claude plugin install marketing-growth@<your-marketplace-name>
```

All 22 skills appear as `/marketing-growth:<skill-name>` (or the short name if overridden in each SKILL.md's frontmatter). No further setup is required — the skills work immediately.

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

## Updating

The plugin is version-controlled via `git`. To update, pull the latest version of the repo.

There is no skill regeneration step — every SKILL.md is canonical source, maintained in `skills/` directly.

---

## Customizing

### Add a new agent

1. Create `skills/your-agent/SKILL.md` (copy an existing agent as a template)
2. Create `skills/your-agent/customize.toml` with an `[agent]` block (code, name, title, icon, description)
3. If the agent has capability-specific prompts, add them under `skills/your-agent/prompts/<code>.md` and reference each in the SKILL.md Capabilities table
4. Add the skill path to `.claude-plugin/marketplace.json`
5. Add an `agents:` entry to `module.yaml` (for BMAD installs)

### Add a new workflow

1. Create `skills/your-workflow/SKILL.md` (copy an existing workflow as a template)
2. Create `skills/your-workflow/workflow.yaml` with `phases:` and `steps:` (copy from an existing workflow)
3. Add the skill path to `.claude-plugin/marketplace.json`

---

## Repository structure

```
marketing-growth/
├── .claude-plugin/
│   ├── plugin.json                    ← Native Claude Code plugin manifest
│   └── marketplace.json                ← Marketplace distribution manifest
├── module.yaml                         ← BMAD module manifest (agent roster + install questions)
├── skills/                             ← All 22 skills — single source of truth
│   ├── marketing-orchestrator/         ← Orchestrator agent
│   │   ├── SKILL.md
│   │   ├── customize.toml              ← [agent] metadata
│   │   └── prompts/                    ← Per-capability instruction bodies
│   │       ├── marketing-strategy.md
│   │       ├── agent-recommendation.md
│   │       └── ...
│   ├── content-architect/              (same shape — 5 other orchestrators follow)
│   ├── linkedin-creator/                ← Specialist agent
│   │   ├── SKILL.md
│   │   └── customize.toml
│   │                                    (same shape — 8 other specialists follow)
│   ├── marketing-strategy/              ← Workflow skill
│   │   ├── SKILL.md
│   │   └── workflow.yaml                ← Phase/step structure
│   │                                    (same shape — 5 other workflows follow)
│   └── ultimate-seo-geo/
│       ├── SKILL.md
│       └── scripts/…                    ← 23 Python audit scripts
└── README.md
```

Every skill is canonical source. No hidden YAML generators, no pre-render step — what you see under `skills/` is what both installers consume.

---

## Credits

Original Marketing Growth Suite by **Matthias** ([@matthias_mrc](https://x.com/matthias_mrc)) — [MatthiasMRC/bmad-marketing-growth](https://github.com/MatthiasMRC/bmad-marketing-growth). This fork is maintained by [@lpalokan](https://github.com/lpalokan).

The `ultimate-seo-geo` utility skill is encapsulated from [**mykpono/ultimate-seo-geo**](https://github.com/mykpono/ultimate-seo-geo) by **Myk Pono** ([lab.mykpono.com](https://lab.mykpono.com), [LinkedIn](https://www.linkedin.com/in/mykolaponomarenko/)), MIT-licensed. The skill itself further credits Bhanunamikaze, AgriciDaniel, and aaron-he-zhu — see `skills/ultimate-seo-geo/SKILL.md` frontmatter for the full attribution chain.

## License

MIT — use freely, adapt as needed.

---

*Built with the [BMAD Method](https://github.com/bmadcode/bmad-method) — AI agent framework for Claude Code. Also installable as a native [Claude Code plugin](https://code.claude.com/docs/en/plugins.md).*
