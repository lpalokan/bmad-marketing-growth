# Refresh / Re-tier an Existing Target List

<instructions>
Re-score an existing target-account list against current fit and fresh signals,
promote/demote tiers, and log what changed. Output is `v{n}.md` (in the protocol)
or an updated `{output_folder}/work/target-accounts/target-accounts.md` (standalone).
</instructions>

<process>
1. Load the existing list (from the brief, `query-objects`, or the work folder).
   Read the context that exists (`icp.md`, `icp-fit-model.md`, `signal-library.md`).
2. Re-score **fit** against the current fit model — the ICP or rubric may have
   shifted since the list was built. Keep it separate from timing.
3. Pull **fresh signals**: Sage's `signal-library.md` and any recent scans, plus
   Clay `ask-question-about-accounts` / `find-and-enrich-company` for new intent.
   Re-score timing on what's changed.
4. Recompute priority = Fit × Signal-strength × Strategic-value. Suppress any
   accounts that have since become customers or fallen under an exclusion.
5. Promote or demote tiers from the new priority. Cite the data source for any
   changed firmographic — no invented updates.
6. Log what changed: a **Changes since last version** section listing each
   promotion/demotion/add/drop with the one-line reason (new signal, fit change,
   suppression).
7. Write the file; in the protocol, set `state.yaml` `status: in-review` and
   notify the orchestrator.
</process>
