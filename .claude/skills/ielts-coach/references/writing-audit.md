# Writing audit

Audit a Task 1 or Task 2 answer against the band descriptors. The output is a list of
located faults, never a score.

Official sources, worth re-reading if anything here looks stale:
[Writing descriptors T1+T2 (PDF)](https://assets.ctfassets.net/unrdeg6se4ke/19SJoSvnUYjrHgVhWvuMnC/42f1b0cb0d7709646a1392d8418646d0/writingbanddescriptorstask1and2.pdf) ·
[Key assessment criteria (PDF)](https://ielts.org/cdn/Guides/ielts-writing-key-assessment-criteria.pdf)

## Before you start

Ask for the task prompt if it wasn't supplied. Task Response cannot be audited without it —
half the criterion is whether the answer addresses *this* question, and guessing the prompt
from the essay produces confident nonsense.

Note the word count and whether it was written to time. Both change what the findings mean:
an over-length essay's error density is a different problem from a rushed one's.

## The procedure

Work criterion by criterion. For each, the question is always the same shape: **which
band-7 clause does this answer fail, and which band-8 clause does it not yet reach?**

The rubric is a floor, not an average — a criterion sits at the lowest band whose features
the answer fully fits. So one recurring fault holds the criterion down regardless of what
else is strong. That is why the output is a list of specific faults rather than a summary
impression: the user needs to know which single habit is doing the holding.

### Task Response (Task 2)

Band 7 already gives: all parts addressed, a clear position throughout, ideas presented,
extended and supported. If any of those is missing, that's the finding and it's a band-6
problem, not a band-8 one.

The clause that usually caps a band-7 writer is the qualifier on the third bullet — *"a
tendency to over-generalise and/or supporting ideas may lack focus"*. Band 8 replaces it
with *"a well-developed response ... with relevant, extended and supported ideas"*.

So the audit question per body paragraph: **does it contain one concrete, specific instance,
or does it assert a claim and then restate it?** A paragraph that says a thing, says it
again in different words, and closes is the over-generalisation fault. Quote the restating
sentence — that's the evidence.

If the user defends a vague sentence on the grounds that they didn't know the real figure,
that defence doesn't hold: IDP states that statistics and facts "don't have to be accurate
in the context of the IELTS exam" — examiners assess relevance and correct use, not truth.
An invented specific carries no accuracy risk; the vague sentence it replaces carries a real
Task Response cost.

Check the prompt type against what the answer actually did:
- *Discuss both views and give your own opinion* — two instructions. The opinion must be
  present from the introduction, not arrive in the conclusion. Reporting "some people argue"
  without extending it is the same over-generalisation fault wearing a different hat.
- *Do the advantages outweigh...* demands a verdict; the plain advantages/disadvantages
  prompt does not.
- Two-part questions need both parts answered directly.

### Task Achievement (Task 1 Academic)

Check the overview first, because its absence is the one hard gate: *"recounts detail
mechanically with no clear overview"* is the band 5 wording. Band 6 requires an overview at
all, band 7 requires a *clear* one of main trends, differences or stages.

Then check whether the answer is comparing or describing. The official guide is explicit
that Task 1 rewards *"comparing or contrasting ... rather than mechanical description
reporting detail"*, and that it is an information-transfer task — speculative explanation
outside the data earns nothing. Quote any sentence that explains *why* the data moved.

Band 7 → 8 on this criterion is two changes, both about data rather than language: band 8
drops band 7's *"could be more fully extended"* and adds *illustrates* to *presents and
highlights*. So every feature named in the overview should carry a figure in the body.

Both extremes are penalised — no data is a band 5 marker, and so is listing every number.
Roughly two key features per chart, each with one or two figures, is the working shape.
Past ~210 words the answer is usually reporting rather than grouping.

### Coherence and Cohesion (both tasks)

The common misdiagnosis is that this criterion is about linking words. Band 7 already
tolerates *"some under-/over-use"* of cohesive devices, so adding more cannot move it.

Check instead:
- **One central topic per paragraph.** This is the literal band-7 clause. A paragraph
  carrying two competing topics fails it outright.
- **Reference and substitution** — the official criteria name *"flexible use of reference
  and substitution (e.g. definite articles, pronouns)"*. This is what carries cohesion at
  band 8 and almost nobody drills it.
- Run the deletion test mentally: strip every sentence-initial connector. If the argument
  still reads in order, cohesion was structural. If it collapses, the connectors were doing
  work the sentences should have done — report that.

Be accurate about connectors rather than reflexively hostile to them. The official criteria
*do* assess "the appropriate use of discourse markers to clearly mark the stages in a
response", giving *First of all* and *In conclusion* as examples — so telling the user those
phrases are disliked is wrong. The fault to report is **density**: band 6 is where cohesion
becomes "faulty or mechanical", and band 7's under-/over-use clause is what disappears at
band 8. A marker at a paragraph transition is fine; one opening every sentence is not.

### Lexical Resource (both tasks)

Two independent axes, and band 8 forgives one of them: it permits *"occasional inaccuracies
in word choice and collocation"* but requires a *wide* range used *"fluently and flexibly to
convey precise meanings"*.

So a wrong word occasionally is not the blocker; a narrow range is. And a rare word in the
wrong slot is scored as an inaccuracy while buying no range — flag thesaurus substitutions
that break collocation (*make a crime*, *do a decision*, *strong rain*) as lexical faults,
not as attempts.

Spelling and word-formation errors count here, assessed by density.

### Grammatical Range and Accuracy (both tasks)

This is the one criterion with something close to a countable target: band 7 is *"frequent
error-free sentences"*, band 8 is *"the majority of sentences are error-free"*.

So count. Number the sentences, mark each as clean or carrying an error, and report the
ratio. That is the single most useful number the audit produces, and unlike a band it is
verifiable — the user can check every mark.

Then group the error-carrying sentences by category. The official guide assesses errors by
*"density and communicative effect"*, not raw count, which means **one fault repeated eight
times is worse than eight different one-off slips** — it reads as an absent rule rather than
a lapse. Report the dominant category by name.

For this user the dominant category is very likely articles. See `l1-priors.md`.

## Output format

Use this structure. It stays scannable and keeps the evidence next to every claim.

```
## Task Response
**Fails band 7:** [clause] — or "clears band 7"
> [quoted sentence from the essay]
[one line: what specifically is wrong]

**Not yet band 8:** [clause]
> [quote]
[one line]

## Coherence and Cohesion
...

## Grammatical Range and Accuracy
Error-free sentences: 14 of 22.
Dominant error category: articles (7 of 8 flagged sentences).
> [quote] — missing definite article before a specific referent
> [quote] — generic plural taking "the"

## The one thing to fix next
[a single named habit, with the reason it was chosen]
```

Close on one item, not a list. A user with six hours a week can change one habit per
fortnight; a nine-point improvement plan is a plan to do nothing. Pick the fault with the
highest density or the one gating a criterion, and say why you picked it.

## If anchors exist

If `IELTS-Log.md` holds two or more externally marked scripts, add a comparative section:
which anchor this essay reads closest to, on which criterion, and what differs. Comparative
judgement is far more reliable than absolute scoring, which is the whole reason to bother
collecting anchors.

With fewer than two anchors, say so in one line and skip the section. Do not substitute a
published band-8 sample — it is not calibrated to this writer, which is the entire point of
an anchor.

## After the audit

The unit of work is **essay plus rewrite** — an unrewritten marked essay changes nothing.
Close by inviting the rewrite on the same prompt, targeting the one named habit.

Append to the log: date, task type, prompt, error-free ratio, dominant category, the habit
named. The pattern across essays is the real signal; any single audit is one noisy sample.
