# Overlay — Regulated Industries (GRC / risk / audit / compliance)

An **optional, illustrative** instantiation of the generic
`docs/opportunity-brief-method.md` for a regulated-industry buyer — the kind of
account where an agentic-AI / GRC / controls-assurance offering is sold. It is an
**example**, not a requirement. Nothing in the module depends on it; the real domain
for an installed project comes from that project's `company-context/icp.md`,
`offerings.md`, and `signal-library.md`. Use this overlay when the target's domain
actually matches — otherwise ignore it, or write your own overlay alongside it.

Read this **with** the generic method, not instead of it. The six domains, the
three-column epistemics, the verify-live rule, and the exit check all still govern —
this only fills in the domain-specific *examples* the generic doc deliberately leaves
blank.

---

## §1 · Leadership — the likely buyer seat (and off-ICP equivalents)

Verify live, every time. The ICP seat is typically one of:

- **CRO** (Chief Risk Officer) · **Head of Internal Audit & Controls** · **CCO**
  (Chief Compliance Officer).

Off-ICP equivalents worth mapping to the same job-to-be-done:

- Chief Compliance / Ethics Officer · **CISO** · Head of Model Risk · VP Quality /
  Regulatory.

Capture: name, exact title, start date, background (ex-Big-4? built the function
themselves?), and **whether they are still in seat**.

## §1 · Regulatory & enforcement record

- Supervisor / certifier findings, penalties, warning letters, non-conformities —
  and **what specifically failed** (a penalty names its own controls).
- Penalty status: appealed? paid? remediation deadline?
- **In-force obligations with clocks** (each is a dated why-now if it applies):
  DORA · CSRD wave · AML deadlines · SOC 2 observation periods · ISO surveillance
  cycles · Solvency II · sector equivalents.
- Their first/latest CSRD or sustainability report and **who assures it**.

## §1 · Governance & control shape (usually a Don't-know — name it)

- **2LoD / 3LoD** structure; whether a central testing/assurance team exists or the
  work is distributed across the business.
- The published internal-control and risk-management description (investor /
  governance pages).
- Their external auditor and sustainability-assurance provider — **that firm will
  pitch them agentic tooling too**.

## §2 · The unit — automation-appetite tells in JDs

Tools a JD names that signal an open door: SAP GRC, continuous controls monitoring
(CCM), analytics, RPA, Copilot, agentic tooling. A JD asking for CCM means you are
pushing an open door.

## §4 · The field — competitor classes to sweep

Scan across these *classes* (not a fixed name list); know why you skipped a class:

- **Consultancies** broadly — Big-4, MBB, Nordic/Benelux boutiques, specialist risk
  advisories.
- **Tech-services players** moving up-stack with agentic AI — Accenture, TCS,
  Genpact, Infosys BPM…
- **Hyperscalers** with regulated-industry plays — Microsoft, AWS, Google Cloud.
- **Foundation-model providers** going vertical — OpenAI, Anthropic, Mistral…
- **LLM-native vertical AI** in compliance / legal / risk.
- **Established GRC platforms** — Archer, ServiceNow GRC, MetricStream, Workiva…
- **Specialist RegTech** beyond GRC — AML/fincrime, identity, privacy/TPRM, data
  lineage.
- **Geographic equivalents** — Chinese hyperscalers / vertical AI, Indian services,
  regional RegTech.
- **Adjacent-industry equivalents** when the target is off-ICP.

Still run the negative (§4): has anyone published a customer story naming this
target? A clean "no" is a "be the first proof" offer.

## §3 · Pain-candidate framing

The strongest lead-in is the leader's own public words about a pain ("hard work, some
frustration…"). Confirmed-pain candidates in this domain typically come from: a
volume-up / team-flat growth curve (**keep pace**), a cost/offshoring mandate
(**afford**), a live obligation with a clock, a named finding, or the leader's own
talk.

---

*To adapt this module to a different vertical, copy this file to
`docs/overlays/<your-domain>.md` and swap the seats, obligations, and competitor
classes. The generic method never changes.*
