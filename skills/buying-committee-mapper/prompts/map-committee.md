# Map the Buying Committee (DMU)

<instructions>
Turn one target account into a named, mapped decision-making unit using MEDDPICC
roles. Output is `v{n}.md` (in the protocol) or
`{output_folder}/work/{account-id}/buying-committee.md` (standalone). Design the
map to be multi-threaded and structured for reuse by storyline and outreach.
</instructions>

<process>
1. Confirm the account (name + domain). Read any brief and the context that
   exists: `icp.md` (buyer personas), the owned `buying-committee-model.md` (the
   role → typical-titles → criteria template), and — if present in the work
   folder — `account-profile.md` (org shape, plus Remy's §2 unit-from-JDs and §3
   leader-in-public sections: the buyer's hiring history and their public vocabulary
   are committee intel — reuse them rather than re-deriving).
2. Identify the people. Prefer Clay `find-and-enrich-contacts-at-company` to pull
   candidates and enrich them (title, seniority, tenure, reporting hints); use
   `find-and-enrich-list-of-contacts` to enrich names you already have. Fall back
   to LinkedIn / Sales Navigator and the company site when Clay is unavailable or
   thin. Every person must carry a source. **Verify live: confirm each named person
   is still in seat this session** — a stale name from memory or a prior map is worse
   than an admitted unknown; never inherit titles/seats without re-checking.
3. Map each person to a **MEDDPICC role** in the DMU:
   - **Economic Buyer** — controls the budget / can say the final yes.
   - **Champion** — sells for us when we are not in the room.
   - **Technical / evaluator buyer** — judges on technical or functional merit.
   - **Users** — live with the outcome day to day.
   - **Procurement / Security / Legal** — gatekeepers who can stall or block.
4. For each person record: name, title, role in committee, the **metrics they
   own**, likely **decision criteria** (technical / business / personal), and
   their **reporting line** — especially the **champion→EB path**.
5. Qualify the champion on **power + access-to-EB + personal motivation**, not
   title. A senior title with no access to the economic buyer and no personal win
   is not a champion — label it a potential coach or supporter instead.
6. Design for multi-threading: an enterprise DMU is typically ~13 stakeholders.
   A one-name map is a flag, not a finish — name who else must be reached and
   who is still `[UNKNOWN — needs input]`.
7. Label every person **confirmed** (sourced to a named page/record) or
   **inferred** (deduced from role/structure). Do not blur the two.
8. Write the map with a **Sources** section. State the acceptance items plainly:
   EB, champion, technical buyer, and users identified (or explicitly unknown);
   champion qualified on power+access+motivation; per-person role + owned metrics
   + criteria; reporting lines / champion→EB path noted.
9. Write the file; in the protocol, set `state.yaml` `status: in-review` and
   notify the orchestrator.
</process>
