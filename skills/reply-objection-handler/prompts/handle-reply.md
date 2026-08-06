# Handle a Prospect Reply

<instructions>
Take one inbound prospect reply and turn it into forward motion: classify it,
draft the response (handling any objection with reframe → proof), drive to a
specific booked-meeting ask, and set the CRM next step. Output is `v{n}.md` (in
the protocol) or a reply log `v{n}.md` under
`{output_folder}/work/{account-id}/` (standalone). Keep a human-in-the-loop gate
before anything is sent — Ricky drafts; the rep sends.
</instructions>

<process>
1. Confirm the account, the contact, and paste-in the **reply text**. Read any
   brief and the context that exists: `positioning.md`, `offerings.md`, the owned
   `playbooks/objections.md`, `account-storyline.md` (the account point of view),
   and `brand-voice.md` if present. Note what's absent and continue.
2. **Classify the reply** into one type — this drives the play:
   - **positive / interested** — wants to talk or learn more
   - **objection** — a stated concern (price, timing, incumbent, fit, authority, trust)
   - **referral / redirect** — points to someone else
   - **not-now** — interested in principle, wrong time
   - **negative** — a real "no" / unsubscribe / hostile
   - **out-of-office** — auto-reply / away
   Say the type out loud and, for objections, name which objection from the
   library it maps to (or flag a new one for capability OL).
3. **Draft the response** to fit the type:
   - For an **objection**, respond with **reframe → proof**: acknowledge and
     reframe the concern, then counter with proof drawn from
     `playbooks/objections.md`, `offerings.md`, and the account storyline. Every
     number in proof carries a source (Source Fidelity) — never invent one.
   - For **referral / redirect**, thank + ask for a warm intro and confirm the
     new contact.
   - For **not-now**, agree the timing, set a dated follow-up, leave one useful thing.
   - For **negative**, respect the no, close the loop cleanly, no pressure.
   - For **out-of-office**, hold and re-time to the return date.
   Mirror the prospect's own words. If `brand-voice.md` is present, match it.
4. **Always drive to a booked meeting** with **one specific, low-friction ask**:
   a concrete slot or a short scheduling link, a tight agenda, minimal cognitive
   load. One ask, not three. (For negative / out-of-office, the "ask" is the
   clean close or the re-time instead.)
5. **Set the CRM next step / follow-up**: the exact next action, the owner, and a
   date (e.g. "AE to send calendar link today; if no reply, follow-up on
   <date>"). No reply leaves without a next step.
6. **Human-in-the-loop gate.** State clearly that the draft is for the rep to
   review and send — Ricky never sends. Flag anything that needs the rep's
   judgment (pricing commitments, legal, exec escalation).
7. Write the reply handling as `v{n}.md` under
   `{output_folder}/work/{account-id}/` — the reply log lives at
   `work/{account-id}/reply-log.md` (`v{n}.md` under a brief). Record: the reply
   text, its classification, the drafted response, the booked-meeting ask, the
   CRM next step, and a **Sources** section for any proof numbers. In the
   protocol, set `state.yaml` `status: in-review` and notify the orchestrator.
</process>
