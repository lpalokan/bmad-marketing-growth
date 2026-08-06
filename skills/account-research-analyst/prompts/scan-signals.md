# Scan an Account for Signals + Refresh Why-Now

<instructions>
Scan one prospect account for buying triggers and intent, rank them by strength
and recency, filter them through the ICP, and produce a refreshed why-now. Output
is `v{n}.md` (in the protocol) or a signal scan `v{n}.md` under
`{output_folder}/work/{account-id}/` (standalone). Structure it for reuse by
scoring, committee-mapping, and storyline.
</instructions>

<process>
1. Confirm the account (name + domain). Read any brief and the context that
   exists: `icp.md` (narrative triggers) and the owned `signal-library.md` (the
   trigger taxonomy and its weights). Note what's absent and continue.
2. Scan for **triggers** across the taxonomy — each dated and sourced:
   - funding rounds, leadership hires, headcount changes, job postings, M&A,
     geographic expansion, tool churn, regulatory/compliance deadlines,
     migrations, product launches, and public OKRs.
   - **Obligations with clocks** are their own dated why-now class: an in-force
     deadline the account must meet (e.g. a regulation phasing in, an assurance /
     surveillance cycle, a remediation deadline — see `docs/overlays/` for
     domain-specific examples). Each carries its own date; that date is the signal.
   Prefer `WebSearch` / `WebFetch` for news, filings, job posts, and leadership
   moves; use Clay `ask-question-about-accounts` to probe when available.
   **Verify live:** leaders, penalty/finding status, and prices are re-checked this
   session, never inherited from memory, a prior scan, or training data — a stale
   leader name or a wrong penalty status is worse than an admitted unknown.
3. Scan for **intent**: first-party (site visits, content, replies the user has
   shared) and third-party (category-level intent signals). Source each; mark
   `[UNKNOWN — needs input]` where you cannot.
4. **Rank** every signal by **strength** (how strongly it predicts buying
   readiness, per `signal-library.md` weights) **and recency** (how fresh it is).
   A strong stale signal can outrank a weak fresh one — say which and why.
5. **KEY PRINCIPLE — never act on a single signal.** Require **stacked signals**
   and filter them through the ICP: a why-now stands only when multiple triggers
   point the same way *and* the account fits the ICP. Reject single-signal false
   positives explicitly.
6. Write a **refreshed why-now** statement grounded in the stacked signals — or
   state **"timing cold"** plainly if the signals don't stack through the ICP.
   Note **which signals should re-fire the motion** (and to whom the why-now
   points).
7. Optionally record observed signals with Clay `track-event` when available.
8. Write the signal scan as `v{n}.md` under `{output_folder}/work/{account-id}/`
   with a **Sources** section (every signal sourced and dated). In the protocol,
   set `state.yaml` `status: in-review` and notify the orchestrator.
</process>
