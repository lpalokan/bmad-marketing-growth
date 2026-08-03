# Handle Escalation

<instructions>
Resolve a brief that hit `max_revisions` without passing (status: escalated).
Escalation means the brief or the constraints were likely wrong — not that the
specialist failed. Output is a decision recorded in the work folder.
</instructions>

<process>
1. Read the escalated `work/{deliverable-id}/`: `brief.md`, the latest `v{n}.md`,
   the latest `v{n}-review.md`, and `state.yaml`.
2. Diagnose why it stalled. Classify the root cause:
   - **Brief was wrong** — acceptance criteria were unachievable, contradictory,
     or under-specified → reissue a corrected/superseding brief (new
     `{deliverable-id}` or bump the brief), and reset revision.
   - **Missing input** — the specialist lacked a fact or upstream deliverable →
     obtain it (ask the user, or run the missing upstream stage first), then
     reissue.
   - **Genuine constraint conflict** — the goal isn't achievable as framed →
     surface the trade-off to the user and get a decision.
3. Present the diagnosis and recommended path to the user. Options: reissue with
   a corrected brief, accept `v{n}.md` with explicitly noted exceptions, or drop
   the deliverable.
4. Record the decision in `work/{deliverable-id}/escalation.md` and update
   `state.yaml` accordingly. Never quietly proceed as if the deliverable passed.
</process>
