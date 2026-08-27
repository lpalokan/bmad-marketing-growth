# Length budget

**A dossier is a 20 to 30 minute read.** That is the design constraint, set by
the user, and everything in this file follows from it. It is a product
requirement rather than a matter of taste, because a document nobody finishes
has failed whatever else it did well.

Account Executive feedback that produced this file: the dossier was too long to
read, and the formatting gave no way to tell a headline from body text. Both
were caused by the standard, so both are fixed in the standard.

## Turning the reading time into a word budget

Assumed reading rate: **220 words per minute.** That is slower than plain prose
because a dossier carries tables, figures, labels and links, and a seller stops
on each one. The rate is an assumption and it is stated here so it can be
argued with. It is not measured.

| Reading time | Words |
|---|---|
| 20 minutes | About 4,400 |
| 30 minutes | About 6,600 |

**The budget is 4,500 to 6,500 words** for the whole dossier. Tables count.
Frontmatter and section 8 do not.

A drawn figure does not count. The committee chart in section 3 is inline SVG,
and its markup is several hundred tokens that no one reads. Strip
`<figure>...</figure>` before counting, or a correctly-sized dossier fails the
gate for carrying a diagram it was told to carry.

Treat 6,500 as the hard cap and 4,500 as the floor. A dossier under the floor is
not a prize. It usually means the account overview skipped something a seller
needed, or the storyline never earned its hypothesis.

## The split

The section budgets below sum to about 5,450 words, mid-band. They are shares
rather than quotas.

| Section | Words |
|---|---|
| 1. Executive summary | 350, plus the scan table |
| 2. Account overview | 1,700 |
| 3. Buying committee | 900, plus the tables |
| 4. The storyline | 1,100 |
| 5. First-touch messages | 600, being three at 120 plus the notes and checklist |
| 6. Questions for discovery | 550 |
| 7. Before you send | 250 |
| 8. Sources | Links and labels, with no commentary |

The executive summary stays deliberately short while the document around it
grows. It is the scan layer, and a seller who has ten minutes reads only this.

Budget moves between sections. A heavily regulated account can spend 400 of the
overview's words on its control environment by taking them from the technology
estate. A thin committee gives its words to the storyline. The total holds.

An opportunity portfolio, where one is built, sits inside the document as
section 5 and carries **2,500 to 3,500 words** of its own, taking the whole
dossier to 7,000 to 10,000. See `opportunity-portfolio.md`.

The section budgets above do not move to make room for it. A portfolio is not a
licence to write a longer dossier, and a dossier that grew to accommodate one
has failed both budgets. If the total overruns, cut a whole opportunity and
record why in section 5.6.

## Hard caps

Countable things, capped so the budget is met by removing whole items rather
than by shaving every sentence.

| Thing | Cap |
|---|---|
| Summaries in the document | 1 |
| Account overview subsections | 5 |
| Committee seats given prose detail | 4 |
| Storyline pillars | 3 |
| Objections | 5 |
| First-touch messages | 3, at the 120 words `message-craft.md` sets |
| Discovery questions | 11, including the synthesis question |
| Any verbatim quote | 40 words, with the rest behind the link |
| Consecutive prose paragraphs before a heading, table or list | 4 |

Three of these are rhetorical rather than dimensional. Pillars, discovery
questions and the single summary stay capped at any length, because a fourth
pillar weakens the three and a twelfth question is the eleventh reworded.

## What to cut, in this order

Meet the budget by deleting whole things. Compressing every sentence to reach a
number produces telegraphese, which is shorter and worse.

1. **The second summary.** A dossier that opens with a verdict section and then
   an executive summary has written its argument twice. One summary. The tier,
   the withdrawal of an earlier claim, and the recommendation all live inside
   it.
2. **Anything the reader already met.** A fact belongs in one section. Its
   consequence belongs in another. Restating the fact to introduce the
   consequence is the single largest source of length here.
3. **Quotes past 40 words.** Take the phrase that carries the meaning and link
   the source. A block quote is not evidence of rigour.
4. **The reasoning that produced a fact.** The reader wants the finding and the
   link. How the researcher arrived at it belongs in the record.
5. **Sections that prove effort.** A financial table with five comparatives
   where two decide the pitch. A committee layer nobody will call. An
   alternatives analysis for an alternative the account has not named.
6. **Hedging.** One clear sentence with a label beats three careful ones.

If the document still overruns after all six, the account overview is where the
words are. Cut there before touching the storyline or the questions.

## The budget is a band, never a score

`house-style.md` holds the anti-metric rule and it still governs. This file adds
one dimensional constraint and changes nothing else.

- A word count inside the band proves the dossier is publishable. It proves
  nothing about whether it is good.
- Never report the count as evidence of quality, in the document or to the
  user.
- Never reach the number by chopping sentences, dropping articles, or turning
  prose into fragments. Cut items, then read what is left.
- A dossier at 6,400 words that repeats itself has failed this file. A dossier
  at 4,700 words a seller can act on has passed it.

The count is checked once, at the pre-publish gate, and only to catch a document
that has run away or a document that was never really written.
