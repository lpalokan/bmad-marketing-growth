# Competitive Teardown

<instructions>
Commission a competitive teardown against a named competitor. Output
ends as a battle card and an updated competitive landscape section.
</instructions>

<process>
1. Ask the user: which competitor (name + URL), what triggered the
   teardown (lost deal, new feature, new positioning shift), and what
   the deliverable will be used for (sales call, board update, content).
2. Load `icp.md`, `positioning.md`. Refuse to proceed if missing.
3. Issue a brief to `competitive-intelligence-pmm` using
   `brief-templates/competitive-teardown.md`. Acceptance criteria MUST
   include:
   - public-source claims only (cite each),
   - positioning frame, ICP overlap, pricing model, top 3 strengths and
     weaknesses,
   - explicit "how we sell against them" block,
   - red-team section: when the competitor wins,
   - battle card draft (1 page).
4. Review per `docs/protocol.md`. On APPROVED, freeze the folder and
   ask the user whether to update `positioning.md` Primary Alternatives.
</process>
