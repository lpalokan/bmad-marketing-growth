# Maintain the Signal Library

<instructions>
Maintain the canonical trigger taxonomy the whole suite reasons from. It is a
single OKF `Signal Library` concept at
`{output_folder}/company-context/signal-library.md`. Remy is the **single
writer** of this file. It structures the narrative triggers in `icp.md` into a
weighted, sourced taxonomy. Follow the OKF frontmatter schema in
`docs/company-context.md` exactly.
</instructions>

<process>
1. Read the context that exists: `icp.md` (its narrative triggers and segments)
   and the current `signal-library.md`. Note what's absent and continue.
2. Enumerate the **signal types** across the taxonomy — funding rounds,
   leadership hires, headcount changes, job postings, M&A, geographic expansion,
   tool churn, regulatory/compliance deadlines, migrations, product launches,
   public OKRs, and first-/third-party intent. Structure `icp.md`'s narrative
   triggers into these types (don't rewrite `icp.md`).
3. For **each** signal type, capture:
   - **What it means for buying readiness** — why it predicts a purchase, for whom.
   - **Where to find it** — the sources / feeds / queries that surface it
     (news, filings, job boards, Clay, intent providers).
   - **How to weight it** — a strength weight and a recency decay (how fast it
     goes stale), so scans can rank signals consistently. Any numeric weight the
     user hasn't supplied is marked `[UNKNOWN — needs input]`, not invented.
   - **Stacking notes** — which signals combine into a credible why-now, and
     which are single-signal false positives on their own.
4. Write the file with OKF frontmatter: `type: Signal Library`,
   `owner: account-research-analyst`, `schema_version: 2`, a `Status:` line, and the other
   required fields per `docs/company-context.md`. Use bundle-relative links (e.g.
   `[ICP](/icp.md)`).
5. Keep single-writer discipline — never edit `icp.md`. Append the change to the
   bundle-root `log.md`.
6. In the protocol, write `v{n}.md` describing the changes, set `state.yaml`
   `status: in-review`, and notify the orchestrator.
</process>
