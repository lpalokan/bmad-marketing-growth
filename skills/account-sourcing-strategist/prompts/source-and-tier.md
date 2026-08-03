# Source & Tier Target Accounts

<instructions>
Turn the ICP into a sourced, A/B/C-tiered target-account list. Output is
`v{n}.md` (in the protocol, under a brief) or
`{output_folder}/work/target-accounts/target-accounts.md` (standalone). Meet the
Acceptance Criteria in `brief-templates/source-accounts.md`.
</instructions>

<process>
1. Confirm the segment and target count. Read any brief and the context that
   exists (`icp.md`, `icp-fit-model.md`, `signal-library.md`). Note what's absent
   and continue.
2. Source candidate accounts: prefer Clay `find-and-enrich-company` (also
   `query-objects` for provided lists); fall back to user-supplied lists and web.
   Cite a data source for every account — no invented firmographics.
3. Enrich each candidate with firmographic anchors: name, domain, industry,
   employee band, revenue/funding, HQ + geos.
4. Score **fit** against `icp-fit-model.md` if present, else a stated rubric —
   how well the account matches the ICP. This is the "should we" question.
5. Score **timing** separately from intent/why-now signals (cross-reference
   `signal-library.md`) — recent, account-specific changes. Keep fit and timing
   as **separate inputs**; never merge them into one number.
6. Compute priority multiplicatively: **priority = Fit × Signal-strength ×
   Strategic-value**. A zero on any factor sinks the account.
7. Suppress current customers and any exclusions **before** ranking. Drop them
   from the list, don't just deprioritize.
8. Assign A/B/C tiers from priority, each with a one-line reason. Show fit,
   timing, priority, and source per account.
9. Write the file; in the protocol, set `state.yaml` `status: in-review` and
   notify the orchestrator.
</process>
