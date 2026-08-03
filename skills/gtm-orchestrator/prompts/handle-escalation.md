# Handle a Cross-Suite Escalation

<instructions>
An ESCALATED brief has already been through its wing's escalation owner
(Max Growth for marketing, Sam Sell for sales) — or names Rae directly as
its escalation target. Rae is the last stop before the user. Decide;
never bounce it back down un-decided.
</instructions>

<process>
1. Read the whole work folder: `brief.md`, every `v{n}.md` and
   `v{n}-review.md`, and `state.yaml`. Confirm `status: escalated`.
2. Diagnose which of the three escalation causes applies
   (`docs/protocol.md` §6 — escalation signals the brief or constraints
   were wrong, not that the specialist failed):
   - **Wrong brief** — objective or acceptance criteria don't describe
     the work actually needed.
   - **Wrong constraints** — the criteria are right but impossible under
     the stated budget/tone/scope, or required context is missing.
   - **Good enough** — the deliverable serves the objective despite
     failing criteria that turn out not to matter.
3. Decide, and say which cause drove it:
   - **Reissue** — a corrected, superseding brief (new `brief_id`,
     reference the old one). Route it back through the wing's
     orchestrator — Rae does not brief specialists directly.
   - **Accept with exceptions** — approve the latest version, list the
     waived criteria and why in a final review, set `state.yaml`
     `frozen: true`.
   - **Drop** — close the deliverable; record the rationale so the wing
     doesn't re-open it blind.
4. If the decision needs a call only the user can make (budget, risk,
   strategy), present the options with a recommendation — one question,
   not a menu of maybes.
5. Record the decision as `escalation-decision.md` in the work folder and
   update `state.yaml`.
</process>
