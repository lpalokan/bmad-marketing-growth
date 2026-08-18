# Pre-publish gate

Run item by item before an Account Executive sees the dossier. Any failure blocks
publication. The orchestrator owns this gate and no agent passes its own work.

## Sourcing

- [ ] Every load-bearing fact is KNOW, ASSUME or GAP.
- [ ] Every KNOW has a working link.
- [ ] Every figure has been traced to the entity it belongs to, not to a
      similarly named company.
- [ ] Leaders, penalties, prices and offers were verified live this session.
- [ ] Conflicting sources are shown and flagged rather than silently resolved.
- [ ] No invented number, person, title, customer, metric or comparable.
- [ ] Our own proof points are presented as site claims, with `[PROOF NEEDED]`
      left visible where a named reference would carry the argument.
- [ ] Absences are recorded as findings with their basis and date.

## Enrichment

- [ ] Every enrichment-derived fact names the tool and the pull date.
- [ ] Every person in the reader-facing committee table is corroborated against a
      public source.
- [ ] Uncorroborated people sit in a separately headed block with a re-verify
      flag.
- [ ] No business figure is sourced from enrichment.
- [ ] Enrichment older than about thirty days is flagged stale.
- [ ] No write-back was performed without explicit approval.
- [ ] No personal contact detail appears in the dossier body.

## Grounding in context

Skip this block only when no company-context bundle exists.

- [ ] The bundle was read to its full depth: `index.md`, the core, the sales
      layer, and the layers under the hubs that are present (`offerings/`,
      `personas/`, `playbooks/`, `case-studies/`).
- [ ] Any nested sub-bundle was read as a bundle in its own right.
- [ ] Which concepts were present and which were absent is recorded.
- [ ] The lead offering names an entry point and, where the offering has more
      than one, a commercial tier.
- [ ] The offering recommendation cites something about *this* account that
      decided it, and names what would have pointed elsewhere. A recommendation
      that could have been written before reading the account fails this gate.
- [ ] Where the fit model routes across offering lines or business areas, the
      routing was run and its outcome stated.
- [ ] Objections start from `playbooks/objections.md` where it exists, rather
      than being written from scratch alongside an unread playbook.
- [ ] First-touch messages follow `playbooks/message-frameworks.md` where it
      exists.
- [ ] Committee seats map onto `personas/` where it exists.

## Length

The dossier is a 20 to 30 minute read. Checked once, here, to catch a document
that has run away or one that was never really written. A count inside the band
proves the dossier is publishable and proves nothing about whether it is good.
Never report the number as evidence of quality.

- [ ] The dossier body is between 4,500 and 6,500 words, counting tables and
      excluding frontmatter and section 8.
- [ ] An opportunity portfolio, where one exists, is between 2,500 and 3,500
      words.
- [ ] Every hard cap in `reference/length-budget.md` holds: five overview
      subsections, four detailed seats, three pillars, five objections, three
      messages, eleven questions, no quote past 40 words.
- [ ] The budget was met by cutting whole items. No section reads as compressed
      fragments or dropped articles.
- [ ] No section restates a fact the reader already met in order to introduce
      its consequence.

## Emphasis and hierarchy

- [ ] No bold anywhere in body text. The only bold is a table's label column,
      the `KNOW` / `ASSUME` / `GAP` labels, and `[PROOF NEEDED]`.
- [ ] No paragraph opens with a bolded lead-in doing a heading's job.
- [ ] Every heading level matches its depth, with no level skipped to reach a
      size.
- [ ] Headings are complete sentences in active voice, with no terminal period.
- [ ] Italics appear only in the standing instruction blocks and the "why we
      ask" lines.
- [ ] Read the rendered page and confirm you can tell a heading from body text
      at a glance, without reading the words.

## Structure

- [ ] Section order matches `reference/structure.md`.
- [ ] Eight sections. There is no section 0 and no second summary above the
      executive summary.
- [ ] The fit verdict is a row in the section 1 table rather than a section.
- [ ] The pre-call reading list appears in section 8 only.
- [ ] The executive summary was written last and stands alone.
- [ ] The value hypothesis comes before the reasoning that produced it.
- [ ] Discovery questions are numbered, specific and answerable, and derive from
      the recorded gaps.
- [ ] They sit in the five altitude buckets, in order, opening on why now and
      ending on change readiness.
- [ ] No bucket holds more than two questions, and no two questions are the same
      question reworded.
- [ ] No question states its own conclusion. Each one is open and neutral.
- [ ] Every question carries one line saying what the answer changes.
- [ ] The list closes with a synthesis question that asks the prospect to direct
      the next step.
- [ ] Gaps that lost a bucket slot still appear in the gaps list in section 8.
- [ ] No outreach sequence in the dossier.
- [ ] No process narration, version numbers, agent names or reversed verdicts.
- [ ] Sources are split into observed, inherited, our own, and gaps.

## Style

- [ ] Zero em dashes and zero en dashes.
- [ ] Zero "X, not Y" constructions.
- [ ] No mid-sentence interrupter splits a subject from its verb.
- [ ] Bullet lists carry a period on the last item only.
- [ ] Jargon is expanded on first use.
- [ ] At most one analogy carries the insight, and it is businesslike.
- [ ] The prose was read, not scored. Nobody has claimed a word count as proof.

## Third parties

- [ ] No company other than the account is named, unless materially inside the
      account's own situation.
- [ ] Where one is named, the relationship is stated plainly.
- [ ] No third party appears in any message, forward note or LinkedIn note.
- [ ] `not_to_be_confused_with` exists only in frontmatter and does not render.

## Safety

- [ ] No existing dossier was overwritten. A dated file was written and
      `supersedes:` is set.
- [ ] The standing "nothing has been sent" label is present.
- [ ] Nothing has been sent, posted or written back to any external system.
- [ ] The render was viewed before it was shown to anyone.
- [ ] No other account's render was overwritten by the build command.
- [ ] `python tools/build_dossier_html.py --check` exits zero. Every Finnish and
      Swedish name, title and quotation reads correctly on the page, with no
      `Ã¤` standing where an `ä` belongs.
- [ ] No rendered page was piped through the shell after the build.
