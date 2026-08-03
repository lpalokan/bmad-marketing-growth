# Write Per-Contact Outreach Messages

<instructions>
Write one personalized first-touch message per key contact on the buying
committee, each tailoring the ONE account storyline to that person's role, pain,
and owned metric. Output is `v{n}.md` (in the protocol) or
`{output_folder}/work/{account-id}/approach-messages.md` (standalone). Do NOT
invent a new value proposition per person — tailor the shared storyline.
</instructions>

<process>
1. Read the inputs that exist: the account storyline
   (`work/{account-id}/account-storyline.md` — the ONE shared value proposition),
   the buying committee map (`work/{account-id}/buying-committee.md` — the named
   people, roles, pains, and owned metrics), the why-now / signal scan (for
   company-specific openers), `brand-voice.md` (voice), `positioning.md`, and the
   owned `playbooks/message-frameworks.md`. Note what's absent and continue.

2. Anchor on the ONE storyline. There is a single account value proposition; every
   message tailors it. Never write a different value prop per contact — you are
   personalizing the shared one to each role, not inventing new ones.

3. For **each** contact in the committee, write one message using a framework from
   the playbook — PAS (Problem → Agitate → Solve) or Before-After-Bridge:
   - **Opener** — a COMPANY-SPECIFIC signal drawn from the why-now / signal scan
     (a real, recent, account-specific change), not a generic "I noticed you're
     growing" line.
   - **Value in the buyer's terms** — frame the storyline against this person's
     role pain and their **owned metric** from the committee map. The CFO's message
     leads on a different metric than the VP Eng's — same storyline, different lens.
   - **Proof** — a **named comparable in their vertical** plus a **specific
     metric**. This is the single biggest reply-rate lever. The comparable and its
     number must be sourced (user input, a cited `WebSearch` result, or a shared
     file). If you can't source a real one, mark `[UNKNOWN — needs input]` and ask
     — do not fabricate a customer name or a result.
   - **Ask** — one clear, low-friction next step.
   Keep every message tight — respect the reader's time.

4. Generate the variable fragments (opener, pain, owned metric, comparable,
   metric, ask) into a clean, reusable template rather than free-writing each
   message from scratch — so the shared storyline stays consistent and only the
   per-contact variables change.

5. Match `brand-voice.md` if it is present. If any sample or draft message
   contains numbers, prefix it `Example — illustrative, not benchmarks.`
   (Source Fidelity). Real, sourced proof metrics inside a live message are cited
   inline, not labeled as examples.

6. Write the file. Under a brief, output `v{n}.md`; standalone, output
   `{output_folder}/work/{account-id}/approach-messages.md`. Include a short
   **Sources** note for every proof metric and comparable used.

7. In the protocol, set `state.yaml` `status: in-review` and notify the
   orchestrator.
</process>
</content>
