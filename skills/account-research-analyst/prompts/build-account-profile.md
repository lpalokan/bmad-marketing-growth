# Build Account Profile

<instructions>
Produce a comprehensive, sourced profile of one prospect account, structured by the
six research domains of the opportunity-brief method. Every load-bearing fact is
sorted into **Know** (sourced, about them — cite), **Assume** (benchmark/experience —
`[confirm]`), or **Don't-know** (a named gap — `[gap — meeting objective: …]`).
Output is `v{n}.md` (in the protocol) or
`{output_folder}/work/{account-id}/account-profile.md` (standalone). Structure it for
reuse by scoring, committee-mapping, and storyline.
</instructions>

<process>
1. Confirm the account (name + domain). Read any brief and the context that exists
   (`icp.md`, `offerings.md`, `signal-library.md`), the method
   (`docs/opportunity-brief-method.md`) if present, and a `docs/overlays/` file if one
   matches the target's domain (buyer seats, obligations, competitor classes).

2. **§1 · The target itself** — primary sources first, each field cited:
   - *Identity & scale*: legal form, listing/ownership, group structure, recent
     demerger/merger/carve-out; revenue, headcount, customers/volumes, geo footprint.
   - *Business mix*: where transactions, customers, money, models or users
     concentrate — where a control/quality/throughput failure would hurt most.
   - *Leadership* (**verify live** — see Live Verification): the likely buyer seat and
     its off-ICP equivalents; name, exact title, start date, background (built the
     function themselves? external hire?), **and whether still in seat**.
   - *Financial & strategic trajectory*: growth curve vs function capacity (volume up +
     team flat = "keep pace"); cost/offshoring/restructuring moves ("afford"); strategic
     shifts — new markets, products, pivots, M&A in flight.
   - *Regulatory / enforcement record* (**verify live**, where the domain has one):
     findings, penalties, non-conformities and **what specifically failed**; penalty
     status (appealed/paid/deadline); in-force obligations with clocks; who assures
     their reporting.
   - *Governance & control shape* (usually a Don't-know — name it): how the relevant
     function is structured, central vs distributed, the published governance
     description, and their external assurance provider.

3. Enrich firmographics/technographics inside §1 using Clay `find-and-enrich-company`
   where useful; fall back to web + filings. Tag relevant systems (CRM/ERP/cloud/
   category-adjacent) as greenfield / complementary / competitive-displacement vs
   `offerings.md`. Cite each field.

4. Bring in the other domains at the depth the brief asks for (each has its own
   capability for a deep pass; here, capture at least a first read and cite sources):
   - **§2 the unit** — jobs-to-be-done from their JDs (capability **JD**).
   - **§3 leaders in public** — speaker/event intel (capability **LP**).
   - **§4 the field** — who is circling the segment (capability **FS**).
   - **§5 relationship layer** — warm/active accounts only (capability **RL**);
     keep it in a clearly separated section, never blended with public facts.
   - **§6 our corpus** — the account's Drive folder, prior brief, canonical
     positioning (retrieve, don't invent), partner material.

5. Map org shape at a high level (divisions, where the relevant function sits) —
   detailed committee mapping is Cleo's job; hand the shape forward.

6. Capture triggers/intent for the why-now (capability **WN**): a confirmed pain
   candidate from the growth curve, an open role, a live obligation, a finding, or the
   leader's own public words.

7. Write the profile with a **Sources** section, and label every fact by column:
   **Know** (cited), **Assume** (`[confirm]`), **Don't-know** (`[gap — meeting
   objective: …]`). Name the single most decision-relevant Don't-know explicitly.

8. Run capability **XC** (exit check) before handing off. Write the file; in the
   protocol, set `state.yaml` `status: in-review` and notify the orchestrator.
</process>
