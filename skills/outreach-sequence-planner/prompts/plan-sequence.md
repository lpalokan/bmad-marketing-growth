# Plan the Multi-Touch Outreach Sequence

<instructions>
Assemble Aria's per-contact messages into a multi-touch, multi-channel cadence —
email / LinkedIn / call — with explicit timing and spacing per step, per-role
entry points across the buying committee, and a human-in-the-loop send gate.
Output is `v{n}.md` (in the protocol) or
`{output_folder}/work/{account-id}/sequence-plan.md` (standalone). Design the
cadence to be multi-threaded and structured so reply-handling can run against it.
</instructions>

<process>
1. Confirm the account (name + domain). Read any brief and the context that
   exists: `brand-voice.md`, the owned `playbooks/sequences.md` (reusable cadence
   templates + channel rules), and — from the work folder — `approach-messages.md`
   (Aria's per-contact messages) and `buying-committee.md` (the named DMU). Note
   what's absent and continue.
2. Inventory the inputs. List each of Aria's messages and each committee member
   with their role. Every step in the cadence must map to one of Aria's messages
   — the sequence tailors and orders copy, it never invents new copy.
3. Rank personalization by **signal strength** (personalization-waterfall style):
   sort contacts / signals from strongest, most specific signal to weakest, and
   decide how much effort each contact earns. Spend deep personalization where the
   signal is strongest; use lighter, template-leaning touches where it is thin.
4. Set **per-role entry points**. For each committee role (economic buyer,
   champion, technical/evaluator, users, and any gatekeeper), name the first touch
   that opens that thread and the message it carries. Do not funnel the whole
   committee through one door.
5. Design the cadence as **multi-touch, multi-channel**. For each step record:
   step number, **channel** (email / LinkedIn / call), the **day / spacing**
   relative to step 1 (e.g. Day 1, Day 3, Day 8), the **contact/role** it targets,
   and the **Aria message** it uses. Give each channel a distinct job; vary
   channel across steps rather than repeating one.
6. **Multi-thread across the committee.** Show how threads run in parallel across
   roles and where they reinforce each other (e.g. a champion touch followed by an
   economic-buyer touch that references it). A single-threaded plan is a flag, not
   a finish.
7. Add a **human-in-the-loop send gate**: the plan **recommends** sends and the
   order — it never auto-sends. State plainly that a human reviews and triggers
   each step, and note any per-channel limits or etiquette (e.g. connection
   requests) that a human should respect.
8. Do **not** invent open- or reply-rate benchmarks. If you show illustrative
   numbers to explain the shape of a cadence, prefix them
   `Example — illustrative, not benchmarks.`
9. Write the plan with the cadence table, the per-role entry points, the
   multi-threading view, and the send-gate note. State the acceptance items
   plainly: multi-touch + multi-channel; explicit timing per step; per-role entry
   points; multi-threaded; human-in-loop gate; every step mapped to an Aria
   message. Mark gaps `[UNKNOWN — needs input]`, don't fill them.
10. Write the file; in the protocol, set `state.yaml` `status: in-review` and
    notify the orchestrator.
</process>
