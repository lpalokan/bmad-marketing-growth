---
type: Account Dossier
title: <"<Account>: account dossier and opportunity portfolio" when merged. Delete otherwise.>
account: <Full legal entity name>
not_to_be_confused_with: <internal only, never rendered. Delete if not needed.>
domain: <example.com>
created: <YYYY-MM-DD>
supersedes: <./dossier.md, or delete if this is the first>
audience: Account Executive
status: Draft, prospecting-ready
lead_offering: <offering>
secondary_offering: <offering, or delete>
commercial_model: <the shape the first engagement takes. Merged form only, delete otherwise.>
fit: <High | Medium | Low>
timing: <High | Medium | Low>
action_tier: <A | B | C>
structure_version: <2, or "merged dossier, nine sections with the opportunity portfolio at section 5">
---

# <Account name>

**How to read this.** Every figure carries a named source and a link. Facts we
verified are marked **KNOW**. Our own reasoning is marked **ASSUME**. What we do
not know is written as a question in the discovery section rather than filled in with a
guess.

<One line only when superseding: what changed and why, naming the retained file.>

---

## 1. Executive summary

<What this company is, in two sentences.>

<What has just happened, dated.>

<Three bolded facts that define the opportunity, one short paragraph each.>

<**The recommendation**, naming the tier, the offering and the person to
approach. Then the timing, with the next dated event.>

| | |
|---|---|
| **Priority** | |
| **Lead offering** | |
| **Lead buyer** | |
| **Why now** | |
| **The constraint** | |
| **Next dated event** | |

---

## 2. Account overview

### 2.1 What they are
### 2.2 Scale and financial frame
### 2.3 Goals and ambitions
### 2.4 Current plans
### 2.5 Control and regulatory environment
### 2.6 Technology estate
### 2.7 Challenges
### 2.8 Why they fit
### 2.9 Why-now signals at a glance

| # | Signal | Date | Domain | Strength |
|---|---|---|---|---|

### 2.10 Sources to read before the call

---

## 3. Buying committee

<The section opens with the chart, before any table. Write the spec as
`committee.json` beside the account record, build it with `python
tools/build_committee_chart.py committee.json`, and paste the whole `<figure>`
here so the page stays self-contained. `reference/committee-chart.md` owns the
three encodings and the eyebrow. A section 3 that opens with a table is missing
the chart.>

<figure class="orgfig" style="--natural:<the SVG's own width>px">
<The SVG, inline.>
<figcaption><What the encodings mean, and why the figure runs wider than the
prose column. Written for the reader who arrives at the diagram first.></figcaption>
</figure>

### 3.1 Who is on the committee

<How the list was verified, and on what date.>

| Person | Title on their own page | In seat since | Role for us and what they care about |
|---|---|---|---|

#### The layer beneath the executive team

> Provenance and date. Re-verify before use.

### 3.2 The seats that matter

<At most four, with how each will behave.>

### 3.3 The path to the buyer, and what blocks it

<The route in, the blockers and landmines, and the parallel threads by name.
Threads are named, never sequenced. A cadence is not dossier content.>

### 3.4 What they will weigh instead of us

---

## 4. The storyline

### 4.1 The value hypothesis

> <One paragraph. What we believe is true for this account and the outcome we can
> move.>

### 4.2 Why we believe it
### 4.3 The things to say
### 4.4 Which point leads for whom
### 4.5 Objections you will hit, and the answer
### 4.6 The ask

---

## 5. Opportunity portfolio

<No portfolio was asked for: delete this whole section and renumber 6 to 9 back
to 5 to 8. One was asked for: read `reference/opportunity-portfolio.md` before
writing a word of it, and set the three merged-form frontmatter fields. Nine
opportunities across three tiers, built only from this account's own facts. No
values, no probabilities, no close dates, ever.>

### 5.1 The portfolio at a glance

| ID | Tier | Opportunity | Sponsor | Our shape | Time to first value | Label | Qualifier |
|---|---|---|---|---|---|---|---|
| S1 | Small | | | | Weeks | ASSUME | |
| S2 | Small | | | | Weeks | | |
| S3 | Small | | | | Weeks | | |
| L1 | Large | | | | Quarters | | |
| L2 | Large | | | | Quarters | | |
| L3 | Large | | | | Quarters | | |
| T1 | Transformative | | | | Years | SPECULATIVE | |
| T2 | Transformative | | | | Years | | |
| T3 | Transformative | | | | Years | | |

<One paragraph reading the shape of the set. What the pattern across the rows
tells a seller, not a summary of the rows.>

### 5.2 How the three tiers differ

| Axis | Small | Large | Transformative |
|---|---|---|---|
| The question it answers | | | |
| Sponsor level | | | |
| Scope | | | |
| Our shape | | | |
| Time to first value | Weeks | Quarters | Years |
| Risk to the customer | | | |
| What it buys us | | | |

### 5.3 <Small, and a conclusion about the tier>

#### S1. <Complete sentence naming the work>

What it is. <The work, as the customer would recognise it.>

Why this account. <This account's own sourced facts. If this block would survive
being pasted into another dossier, the opportunity is not real yet.>

What it needs from them. <Access, a decision, a named owner, a timebox.>

What would kill it. <The honest failure mode. Every opportunity has one.>

<ASSUME | SPECULATIVE>. The qualifier is <the single question that confirms or
closes it>.

#### S2. <...>
#### S3. <...>

### 5.4 <Large, and a conclusion about the tier>

#### L1. <...>
#### L2. <...>
#### L3. <...>

### 5.5 <Transformative, and a conclusion about the tier>

#### T1. <...>
#### T2. <...>
#### T3. <...>

### 5.6 What we ran and excluded, with the reasons

<Prose, not a table. Every offering and capability considered and rejected, each
with its reason. Where one is real but premature, mark it held back rather than
excluded and say what would unlock it.>

---

## 6. First-touch messages

> *Examples, illustrative. Every claim and figure must be re-checked against the
> source before sending. Nothing has been sent. Each message is a recommendation
> for a human to review, edit and send.*

### <Name, title> (lead)
### <Name, title>
### Note for <champion> to forward internally
### LinkedIn connection note, <name>
### Pre-send checklist

---

## 7. Questions for discovery

> *Five buckets, two questions each at most, in this order. Every question
> carries one line saying what the answer changes. Delete any bucket heading you
> did not fill.*

### Strategic context, why now

1. <question>
   *Why we ask: <what the answer changes>.*
2. <question>
   *Why we ask: <what the answer changes>.*

### Priorities and scope

3. <question>
   *Why we ask: <what the answer changes>.*
4. <question>
   *Why we ask: <what the answer changes>.*

### Current operating model

5. <question>
   *Why we ask: <what the answer changes>.*
6. <question>
   *Why we ask: <what the answer changes>.*

### Pain, risk and exposure

7. <question>
   *Why we ask: <what the answer changes>.*
8. <question>
   *Why we ask: <what the answer changes>.*

### Change readiness and next step

9. <question>
   *Why we ask: <what the answer changes>.*
10. <question>
    *Why we ask: <what the answer changes>.*

### To close

11. <synthesis question, handing them the bridge to the next step>
    *Why we ask: <what the answer changes>.*

---

## 8. Before you send

---

## 9. Sources

### Observed, primary, dated
### Inherited, needs re-verification
### Our own material
### Gaps, left open on purpose
