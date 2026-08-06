# Run the Exit Check — Readiness Gate Before Framing

<instructions>
The gate between research and framing. Do not hand a profile to scoring, storyline, or
outreach until every box below is true. Run this on the profile (or `v{n}.md`) as the
last step before handoff. If any box fails, the profile is **not done** — fix it or
name the gap explicitly. In the brief-driven protocol the orchestrator scores these
same items in its review; this capability is the self-check that gets you there.
</instructions>

<process>
1. Walk the profile against the five exit criteria and mark each pass/fail:
   - [ ] Every load-bearing claim about the target is a **Know** with a source about
         them, or carries `[Inference]` / `[confirm]`. (No Assume dressed as a Know.)
   - [ ] Leaders, penalty status, and prices were **verified live this session** — not
         inherited from memory, a prior brief, or training data.
   - [ ] **No** reference customer's or peer case-study's detail is attributed to the
         target (the §4 gate rule holds).
   - [ ] The single most decision-relevant **Don't-know** is named as a meeting
         objective (often: the shape of their relevant function).
   - [ ] At least **one confirmed pain candidate** is identified — from the growth
         curve, an open role, a live obligation, a finding, or the leader's own public
         words.

2. For every failing box, either fix it (do the missing research / re-verify) or, if it
   genuinely cannot be closed now, convert it into a **named Don't-know / meeting
   objective** — never leave it implicit.

3. Write a short **Exit Check** block at the top or bottom of the profile: each
   criterion with ✓/✗ and a one-line justification, plus the named top Don't-know and
   the confirmed pain candidate. This is the artefact scoring and storyline rely on.

4. Only when all five pass (or the residual gaps are explicitly named as objectives)
   set the profile ready. In the protocol, then set `state.yaml` `status: in-review`.
</process>
