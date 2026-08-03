# Run Account Motion

<instructions>
Sequence the full new-customer prospecting motion for one named account,
issuing a brief to each specialist in order and reviewing each deliverable
before the next step consumes it. Output is a motion plan plus the chain of
briefs and reviews under `{output_folder}/work/{account-id}/`.
</instructions>

<process>
1. Establish the account. Ask for the account name or domain if not given.
   Set `{account-id}` = a short slug (e.g. `acme`). Create
   `{output_folder}/work/{account-id}/` and write `motion-plan.md` listing the
   stages below with their owner and current status.

2. Read whatever context is present (see On Activation step 3). Do not block on
   missing context — note gaps in the motion plan.

3. Issue briefs in this order, one at a time. For each: write `brief.md` (or
   `brief.md` inside a per-stage subfolder such as `research/`) from the
   matching `brief-templates/` file, hand off to the specialist, wait for
   `v{n}.md`, then run capability RV to review before proceeding.

   a. **account-sourcing-strategist** — only if the account came from a list
      request rather than a single named account; otherwise skip.
   b. **signal-monitor** (SCN) — optional early scan for a fresh why-now; can
      run in parallel with research.
   b2. **account-research-analyst → relationship layer** (RL) — **only if the
      account is warm/active.** Issue the `relationship-layer.md` brief first so the
      POC/relationship facts frame the public research; for an active POC, POC facts
      lead. Skip entirely for cold accounts.
   c. **account-research-analyst** — the account profile + why-now, built across the
      six research domains (may spin off field-scan.md as a separate brief). **Gate:
      do not proceed until its Exit Check passes** — every load-bearing claim is a
      Know/Assume/Don't-know, leaders/penalties/prices were verified live this
      session, no peer case-study detail is attributed to the target, the top
      Don't-know is named, and ≥1 confirmed pain candidate exists.
   d. **service-offering-advisor** — which offering(s) fit; can run in parallel
      with research once the segment and the field scan (§4) are known.
   e. **fit-scoring-strategist** — fit ✕ timing scorecard + action tier. If the
      tier is "deprioritize/drop", stop here and tell the user.
   f. **buying-committee-mapper** — the named committee.
   g. **account-storyline-developer** — the account storyline (Pierce review if
      installed).
   h. **contact-approach-writer** — per-contact messages.
   i. **outreach-sequence-planner** — the multi-touch cadence.
   j. **reply-objection-handler** — stand by for replies (invoked when a reply
      arrives).

4. Between stages, pass forward only the accepted `v{n}.md` of the prior stage
   as the next brief's Context (links). Keep each brief's mandate narrow.

5. When a brief hits `max_revisions` without passing, switch to capability ES
   (handle escalation) for that stage; do not silently proceed.

6. Keep `motion-plan.md` current (status per stage). At the end, summarize for
   the user: what was produced, the fit tier, the committee size, and the next
   action.
</process>
