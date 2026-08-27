# Dossier structure

The canonical section order. Follow it exactly. The order is chronological from
the AE's point of view: who they are, who to talk to, what to say, what to ask.

Read `length-budget.md` alongside this file. A dossier is a 20 to 30 minute
read, which is 4,500 to 6,500 words. That file sets the budget per section and
the caps on how many pillars, seats, messages and objections a dossier carries.
The two files are one contract, and a structurally correct dossier that overruns
the budget fails the gate.

## The order

1. Executive summary
2. Account overview
3. Buying committee
4. The storyline
5. First-touch messages
6. Questions for discovery
7. Before you send
8. Sources

Eight sections. There is no section 0. A verdict block sitting above the
executive summary is a second summary, and one document gets one summary.

### When an opportunity portfolio is asked for

The portfolio goes **inside the document at section 5**, and everything below
section 4 shifts down by one. Nine sections in total.

1. Executive summary
2. Account overview
3. Buying committee
4. The storyline
5. **Opportunity portfolio**
6. First-touch messages
7. Questions for discovery
8. Before you send
9. Sources

It is never an appendix, a "Part Two", a companion file, or anything after the
sources. A reader who has just been told what to sell first is in the right
position to be shown what sits behind it, and that position is immediately
after the storyline. `opportunity-portfolio.md` owns the rest of the contract.

A portfolio kept in its own file is the failure this rule exists to prevent.
Two documents mean two things to keep in sync, and the one that goes stale is
always the one the seller did not open.

## What belongs in each

### 1. Executive summary

Written last, from the finished document. Around 350 words, so four short
paragraphs, then the scan table. It stays short while the document around it
grows, because a seller with ten minutes reads only this.

Answer four questions. What is this company. What has just happened. Why that
creates an opening for us. What the AE should do next, naming the person.

Where an earlier version of the dossier made a claim that has since been
withdrawn, one sentence here says so. It does not get its own section.

Close with the scan table: priority, why they fit, lead offering, lead buyer,
why now, the constraint, the next dated event. An AE who reads only this section
should be able to act.

### 2. Account overview

Five subsections, 1,700 words in total. The largest section in the dossier, and
still the first place to cut when the document overruns. It informs the
hypothesis rather than proving the researcher worked hard.

- **2.1 What they are and how they are built.** Entity, ownership, structure,
  market position, and the scale table with its comparatives. Include any
  structural fact that changes how the account behaves, such as a cooperative
  owner or a central body with a legal duty over subsidiaries. Two or three
  sentences read the shape of the figures. Do not restate the rows.
- **2.2 What they are trying to do.** What they say they are becoming, the
  measures they use, and the programmes in flight with their dates. State where
  an ambition is also a warning to us.
- **2.3 How the work runs today.** The technology estate: what we know, what we
  must not assert, and why the gap favours or hurts us. Where the account is
  regulated, the control environment goes here and decides the pitch, so take
  its words from elsewhere in this section rather than adding them.
- **2.4 What is hurting.** Their problems, in their terms, sourced.
- **2.5 Why now.** The dated signal table with a strength read, then two or three
  sentences on how to read the set.

Two things that used to live here have moved. The fit verdict is now a row in the
section 1 scan table, in four to six words. The pre-call reading list is now a
block in section 8, so links live in one place.

### 3. Buying committee

Four subsections, 900 words plus the tables. Placed after the overview because
people are part of understanding the account.

**The section opens with the committee chart**, before any table. It answers what
a table cannot: who sits above whom, and how much of that we actually know. The
diagram, its three encodings and how it breaks out of the prose column are owned
by `committee-chart.md`, and it is built with
`tools/build_committee_chart.py`. A dossier whose section 3 opens with a table
is missing the chart.

- **3.1 Who is on the committee.** The chart, then the verified leadership table
  with role for us and what each cares about. The layer beneath sits under it as
  a separately headed block with its provenance and freshness flagged.
- **3.2 The seats that matter.** At most four, with how each will behave.
- **3.3 The path to the buyer, and what blocks it.** The route in, the blockers
  and landmines, and the parallel threads by name. Threads are named, never
  sequenced. A cadence is not dossier content.
- **3.4 What they will weigh instead of us.**

### 4. The storyline

- **The value hypothesis first**, as a block quote. One paragraph. It states what
  we believe is true for this account and the outcome we can move.
- **Why we believe it.** The reasoning that produced the hypothesis, in the
  account's own facts. This is the teachable insight. Keep it readable and use at
  most one analogy.
- **The things to say.** Three pillars. Each is a headline sentence plus what
  changes for the account, with its proof or an honest `[PROOF NEEDED]`. Three
  is the cap and not a target. Two strong pillars beat three where the third is
  padding.
- **Which point leads for whom.** A short table against the committee.
- **Objections you will hit, and the answer.** Five at most, including the ones
  we answer badly.
- **The ask.** Specific, small, and dated where possible.

### 5. First-touch messages

Three at most, one per load-bearing seat, at the 120 words `message-craft.md`
sets. Where four
seats matter, write to the two that carry the opening and name the others in
section 3 as parallel threads. Add a note the champion can forward internally, a
LinkedIn connection note, and a pre-send checklist. See `message-craft.md`.

### 6. Questions for discovery

Numbered, specific, and answerable by a person in the room. Ten at most, in five
buckets of two, plus one synthesis question to close.

#### Bucket by altitude

Topic is the wrong axis. Sort every question into one of five stages instead.
They mirror how trust builds across a call.

1. Strategic context. Why now.
2. Priorities and scope.
3. Current operating model. How the work runs today.
4. Pain, risk and exposure.
5. Change readiness and next step.

If a question does not obviously belong to a stage, ask whether it needs an
earlier stage answered first. The answer tells you its depth.

#### Order broad to narrow

Keep the buckets in the order above. Never open on process or on pain. Open on
why now, because it reframes everything after it. Objections and next steps come
last, because they only make sense once the detail has been earned.

#### Two per bucket, at most

The cap forces the highest signal question per angle. Two questions that are the
same question reworded count as one, so cut the weaker.

#### Where the questions come from

Render them from the GAP entries in the record rather than inventing them at the
end. The buckets decide the shape. The gaps decide the content. Where the two
disagree:

- A bucket holding more than two gaps keeps the two highest signal. The rest stay
  in the gaps list in section 8, so nothing is lost.
- A bucket holding no gap still earns a question when that stage matters for the
  call. Write it, and know it came from the conversation rather than from the
  research.
- The synthesis question is never gap derived.

#### Neutral, never leading

A question that states its conclusion inside itself buys a confirmation, and a
confirmation is worth nothing. The prospect reaches the conclusion. You do not
hand it to them.

Leading: "Control testing is your big transformation priority this year, right?"
Neutral: "Where does control testing sit against your other priorities this year?"

#### One line of "why we ask" under each

Every question carries a single line saying what the answer changes. If you
cannot say what it changes, the question does not belong in the dossier. This is
the test that cuts the list down.

#### Close with a synthesis question

The last item is not discovery. It hands the AE the bridge to the next step by
asking the prospect to direct the conversation instead of disclosing one more
fact. "What would you want us to cover when we come back, and what would you
want us to stay away from."

#### Specific and answerable

Weak: "Current control-testing and GRC tooling."
Strong: "What tooling supports control testing and workpapers today, or does the
team work in documents and spreadsheets?"

### 7. Before you send

Standing instructions for this account. Sensitivities, forbidden framings,
factual traps, and anything time-boxed such as an offer period or a results date.

### 8. Sources

Five blocks. The first is the short list an AE should actually open before the
call, at five links or so. Then observed and dated, inherited and needing
re-verification, our own material, and gaps left open on purpose.

Links live here. A link inside the argument is fine where the sentence stands on
it. A second list of the same links elsewhere in the document is not.

## What is not in a dossier

- **The outreach sequence.** AE feedback removed it. If a runner wants a cadence
  it goes to `cadence-internal.md` in the same folder.
- **Process narration.** No version numbers, no reversed verdicts, no agent
  names, no "what changed in this pass" except a single sentence inside the
  executive summary when a dossier supersedes another.
- **Internal caveat apparatus in reader prose.** Bracket flags belong in the
  record and in the sources block, not scattered through the argument.
- **The full fit scorecard.** A row in the section 1 table only.
- **Bold in body text.** Emphasis is structural here. See the emphasis rules in
  `house-style.md`.
- **A second summary.** See the note under "The order".
- **Any claim that the document is not invented.** The "How to read this" note
  explains the KNOW and ASSUME labels and says where the gaps went. It stops
  there. Sentences like "Nothing here is invented" assert the thing the labels
  already demonstrate, and an assurance a reader did not ask for reads as one
  they should have. Source fidelity is proved by the labels, the links and the
  named gaps on every page, never by a sentence at the top claiming it.

  This does not soften the rules. `source-fidelity.md` and the pre-publish
  checklist still forbid an invented number, person, title, customer, metric or
  comparable. Those stay as enforcement. What goes is the reader-facing boast.
