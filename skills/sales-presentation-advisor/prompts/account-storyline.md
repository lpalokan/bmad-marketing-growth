# Develop the Account-Level Storyline (sales motion)

<instructions>
Build ONE account-level point of view — a single value hypothesis — for a
named target account, expressed as a Challenger teachable insight and 3–5 ABM
message pillars. This is the sales wing's approach pitch: the spine that every
per-contact message is later a tailoring of. Output is `v{n}.md` (in the
protocol) or `{output_folder}/work/{account-id}/account-storyline.md`
(standalone). Structure it so `contact-approach-writer` (Aria Approach) can
tailor every touch and sequence step from it.
</instructions>

<process>
1. Confirm the account. Read the brief and the context/artifacts that exist:
   `account-profile.md` (triggers, pains, initiatives, why-now), `fit-scorecard.md`
   (why they fit and how timely), `offerings.md` (what we're matching to),
   `positioning.md` (our pillars and differentiation), `brand-voice.md` (how we
   sound), `buying-committee.md` (the named roles to tailor to), and
   `case-studies/` (proof). Do not block on anything missing — note the gap.

2. Frame the **Challenger teachable insight** — the spine of the storyline:
   - **Teach:** a reframe of the account's *own* situation. Take a real trigger or
     pain from `account-profile.md` and show the account a non-obvious cost,
     risk, or opportunity in it they aren't naming today. This is not a market
     truism and not a product pitch — it must be *about them*.
   - **Tailor:** shape the insight to the buying committee's roles from
     `buying-committee.md` (what the economic buyer, the champion, and the
     blockers each stand to lose or gain).
   - **Take Control:** point the insight at a concrete next step / decision the
     account should make.

3. Write the **top-line value hypothesis** — one or two sentences stating what we
   believe is true for this account and the outcome we can move. Every pillar
   ladders up to this single line.

4. Break the insight into **3–5 ABM message pillars.** Each pillar carries:
   - **Headline** — a complete declarative sentence in active voice (the house
     headline standard), stating the idea, not labelling a topic.
   - **Value prop** — what changes for the account if this is true.
   - **Proof point** — a **named comparable** (a specific company/segment, drawn
     from `case-studies/` or a cited source) plus a **specific metric**. No
     comparable, no metric → mark `[PROOF NEEDED — <what>]`; never fabricate a
     number or a logo (Source Fidelity).

5. Ground every pillar in the account's real situation: tie it back to a trigger,
   pain, or initiative in `account-profile.md`, and to the offering in
   `offerings.md` it advances. Match the voice to `brand-voice.md` if present.

6. Add a short **Committee map** note: which pillar leads for which role, so the
   contact writer can tailor without re-deriving the point of view.

7. Self-check the storyline against the review lenses before handing it back:
   the three-act structure (capability SR), headline craft (HD), and the
   Challenge ↔ Desire tension (TX). Fix what fails; note what was tightened.

8. Write the storyline with a **Sources** section (each proof point traced to its
   case study or cited source) and a **Missing/assumptions** list. In the
   protocol, set `state.yaml` `status: in-review` and notify the orchestrator.
</process>
