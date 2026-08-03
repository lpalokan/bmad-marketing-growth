# Define / Tune the Scoring Model

<instructions>
Define or tune the reusable scoring model the whole suite scores against:
`{output_folder}/company-context/icp-fit-model.md`. This is a Google OKF concept
of `type: Scoring Model`, owned by fit-scoring-strategist — Mira is its single
writer; every other agent reads it. This is the one `company-context/` file Mira
may write.
</instructions>

<process>
1. Read `icp.md` (the model builds on it) and `offerings.md`. If an
   `icp-fit-model.md` already exists, read it and tune in place rather than
   rewriting from scratch — preserve what still holds.

2. Define the model's four parts, keeping the central split explicit:
   - **Weighted fit categories + weights** — firmographic / technographic /
     persona, each with its factors, scale, and weight (weights sum to 100%).
   - **The fit-vs-timing split** — state that fit and timing are scored and
     reported SEPARATELY, and define the timing signal set (triggers/intent) that
     feeds the timing score. Never define a formula that blends them into one.
   - **Tier cutoffs (A/B/C)** — the score bands that map to the action tiers
     prioritize now / into sequences / nurture / deprioritize.
   - **Strategic-value definition** — what makes an account strategically valuable
     beyond fit (e.g. logo, expansion path, reference potential), used in the
     Priority = Fit × Signal-strength × Strategic-value formula.

3. Every factor and cutoff must trace to `icp.md`, offerings, or the user's stated
   priorities — do not invent thresholds or benchmark numbers (Source Fidelity).
   Ask one focused question if a weight or cutoff has no basis.

4. Write `icp-fit-model.md` with the frontmatter from `docs/company-context.md`:
   ```yaml
   ---
   type: Scoring Model
   title: ICP Fit & Propensity Scoring Model
   description: <one sentence>
   tags: [company-context, scoring, fit, propensity]
   timestamp: <ISO 8601>
   owner: fit-scoring-strategist
   last_updated: <YYYY-MM-DD>
   last_updated_by: fit-scoring-strategist
   schema_version: 2
   ---
   Status: <Bootstrapped | In progress | Stable | Stale (needs refresh)>
   ```
   Link out to `icp.md` and `offerings.md` with bundle-relative Markdown links.

5. Because this is a `company-context/` write, append the change to the bundle
   `log.md` (newest first) and update the root `index.md` entry if the concept is
   new. This is the single exception to Mira's read-only stance on the bundle.
</process>
