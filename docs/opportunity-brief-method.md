# The Opportunity-Brief Method — Research Before Framing

This is the shared research methodology the account-facing agents follow **before**
anything gets framed, scored, pitched, or written. It is domain-neutral: the
technique below applies to any prospect in any segment. For a worked, sector-specific
instantiation (buyer seats, obligations, competitor classes), see the optional
overlays under `docs/overlays/` — e.g. `regulated-industries.md`. The overlays are
**examples**, not requirements; the real domain comes from the installed project's
`company-context/icp.md`.

> This doc is the canonical, fuller reference. The agent prompts embed the
> essentials so they work even when this file was not copied to the project root
> (the installer does not copy a module's `docs/`). Mirror any change here into
> the prompts that quote it — the same way `protocol.md` is mirrored.

---

## 1. Every fact lands in one of three columns

Classify **every** load-bearing claim. This replaces a flat "observed vs inferred"
split with an actionable one:

| Column | What it is | How to mark it | What it becomes |
|---|---|---|---|
| **Know** | Sourced, and *about them* | Cite the source inline | A fact you can lead with |
| **Assume** | From experience, a benchmark, or a comparable — **not** about them | `[confirm]` (or `[Inference]` when it's our own inference) | A hypothesis to test |
| **Don't-know** | A named, specific gap | `[gap — meeting objective: …]` | A meeting objective |

The point of the third column is that a gap is not an embarrassment to hide — it is
the **agenda item** that earns the meeting. Name the gap precisely; do not paper over
it with an Assume dressed up as a Know.

---

## 2. Verify live, every session — never inherit

**Leaders, penalties, prices, and org facts must be verified live every time.**
Never inherit them from a prior brief, a memory sidecar, a cached profile, or model
training data. These decay fastest and a stale one is actively harmful:

- A **stale leader name** is worse than an admitted unknown — you pitch a person who
  left. "Still in seat?" is part of the check, not an afterthought.
- A **penalty / finding** changes meaning with its status: appealed? paid?
  remediation deadline passed?
- A **price** quoted from memory is a commercial error.

A memory sidecar may store a *pointer* ("last time, the buyer was the CRO — re-verify")
but never the volatile fact as if still true. Treat everything time-sensitive in
memory or a prior brief as a lead to re-confirm, not a source to reuse.

---

## 3. The six research domains

A complete opportunity brief covers these six. Not all apply to every account (§5 is
warm-accounts-only); skip a domain deliberately and say why.

**§1 · The target itself** — primary sources first.
- *Identity & scale*: legal form, listing/ownership, group structure, recent
  demerger/merger/carve-out; revenue, headcount, customers/volumes, geographic
  footprint; **business mix** — where transactions, customers, money, models or
  users concentrate (that is where the pain, if any, hurts most).
- *Leadership* (verify live): the likely buyer seat and its off-ICP equivalents;
  name, exact title, start date, background (built the function themselves? external
  hire? — it changes the pitch); whether they are still in seat.
- *Financial & strategic trajectory*: growth curve vs function capacity (volume up +
  team flat = a "keep pace" signal); cost/efficiency mandates, offshoring,
  restructuring ("afford" signals); strategic shifts — new markets, products, pivots,
  M&A in flight.
- *Regulatory / enforcement record* (verify live, where the domain has one):
  findings, penalties, non-conformities and **what specifically failed**; penalty
  status; in-force obligations with clocks; who assures their reporting.
- *Governance & control shape* (usually a Don't-know — name it): how the relevant
  function is structured, whether a central team exists or work is distributed, the
  published governance description, and their external assurance provider (that firm
  will pitch them too).

**§2 · The unit — jobs-to-be-done from job descriptions.** Their own open/recent
postings for the relevant function name the unit's real tasks, size and shape (a
single maternity-cover posting = a lean team). The tools a JD names reveal automation
appetite (a JD asking for the category you sell = an open door). The buyer's own
hiring history shows whether they *built* the function — respect that; don't pitch
cutting the headcount they fought for. Where their own postings are thin, use
comparable-industry JDs as a benchmark only — mark `[confirm]`.

**§3 · The leaders in public — event/speaker intel.** **Search the name, not the
topic.** Conference agendas, panels, webinars, podcasts, posts about appearances,
association roles. Collect three things: *what* they chose to speak about (classifies
the opening posture), *when* (a recent talk is a live why-now), and their *exact
vocabulary* (mirror it downstream). Their own public words about a pain are the
strongest lead-in material that exists. The fact they spoke and on what = **Know**;
any inference about *why* = `[confirm]`.

**§4 · The field — who is circling this problem space.** Scan across *classes* of
entity, not a fixed name list, and know why you skipped a class. Collect: which use
cases are already landing in the segment; who is circling this target/segment and
with what frame; what language the buyer has already been sold. Then **run the
negative** — has anyone published a customer story naming this target? A clean "no"
is a "be the first proof" offer. **Gate rule:** every peer artefact is about *their*
client — usable as a market pattern, **never** as a fact about this target. (For the
competitor classes to sweep in a regulated-industry context, see the overlay.)

**§5 · The relationship layer — warm / active accounts only.** Ask whoever holds the
relationship: Who asked, from which function? What POC/workshop already happened and
what did it prove? What data/evidence/systems were used? What did they like, reject,
or want to explore next? What operating-model decision is now in play? What scale
facts are known? Keep this layer **separate** from public facts; label unsupported
estimates `[Account note — needs verification]`. For active POCs, POC facts lead and
public research is context. The strongest unlocks are usually partner/internal
material the open web doesn't have — always ask for it.

**§6 · Our own corpus.** The account's Drive folder and any prior brief (re-verify
everything time-sensitive — §2). The canonical positioning sources — **retrieve** the
value prop, don't invent it. Any partner-supplied material (an email, a client-story
URL) — read it carefully; it is often the pivot.

---

## 4. The exit check — the gate before framing

Do not hand a profile to scoring, storyline, or outreach until every box is true:

- [ ] Every load-bearing claim about the target is a **Know** with a source about
      them, or carries `[Inference]` / `[confirm]`.
- [ ] Leaders, penalty status, and prices were **verified live this session** (§2).
- [ ] **No** reference customer's or peer case-study's detail is attributed to the
      target (§4 gate rule).
- [ ] The single most decision-relevant **Don't-know** is named (often: the shape of
      their relevant function).
- [ ] At least **one confirmed pain candidate** is identified — from their growth
      curve, an open role, a live obligation, a finding, or the leader's own public
      words.

A brief that fails the exit check is not done. In the brief-driven protocol
(`protocol.md`), the orchestrator scores these items in its review; standalone, the
research agent self-checks before handing off.
