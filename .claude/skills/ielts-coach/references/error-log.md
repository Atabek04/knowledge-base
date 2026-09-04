# Listening and Reading: log and drill

Two modes share this file, because the drill is chosen from the log and makes no sense
without it.

Unlike Writing and Speaking, these sections are objectively marked out of 40 against a
published conversion — so here you **do** give numbers. Band 7 is 30/40 and band 8 is 35/40
in both papers. The official caveat is that the marks required vary slightly by test
version, which is why Cambridge prints a table inside each test: use the table from the
volume the user actually sat, and plan for 36 rather than exactly 35.

## Why the log exists

The most recurrent method in accounts of people who reached the 8s is not more mocks — it
is logging every wrong answer by category and attacking only the categories. One 7.0 → 8.0
write-up found the Reading loss was almost entirely False-versus-Not-Given and the Listening
loss was almost entirely word form. Two mechanical fixes worth roughly a band, and **both
invisible to anyone tracking their score**.

So the mock is the measuring instrument and the review is the training. A four-hour mock
without the review has consumed most of a week's budget and produced a number.

This mode is also, bluntly, the one an LLM is unambiguously good at: it is bookkeeping and
pattern-counting over data the user supplies, with no judgement call to get wrong.

## Logging a mock

Ask for: the test source and number, raw scores, and the wrong answers with the question
type. If the user only has the scores, log those and say what's missing — a score alone
can't drive a drill.

Tag each wrong answer with exactly one category. Reuse these names; consistency is what
makes the counts mean something across weeks.

**Listening**
- `word-form` — heard right, written in the wrong form (*travel* / *travelling*)
- `plural` — singular/plural mismatch with the stem's grammar
- `spelling`
- `word-limit` — over the limit, or articles counted in ("the bus" under ONE WORD)
- `two-answers` — gave two where one was asked
- `distractor` — followed a value that was later cancelled
- `lost-place` — missed the question entirely, didn't recover
- `paraphrase` — didn't recognise the paraphrase of the key
- `attribution` — Part 3, assigned the opinion to the wrong speaker

**Reading**
- `tfng-false-for-ng` — chose False where Not Given was right
- `tfng-other`
- `headings`
- `matching-features`
- `sentence-endings`
- `summary-completion`
- `mcq`
- `ran-out-of-time` — unattempted or rushed at the end
- `keyword-trap` — matched a planted word rather than the meaning

Then report:
- Raw score and the band from the test's own table.
- The gap to the route target (8.5, so 37/40).
- Categories ranked by marks lost, and — this is the part that matters — **which categories
  are recurring across the last few logged tests**, not just this one. A category appearing
  once is noise; the same one appearing three times is next fortnight's work.
- How much of the gap is mechanical (`word-form`, `plural`, `spelling`, `word-limit`,
  `two-answers`) versus comprehension. At 34/40 a disproportionate share is usually
  mechanical, and mechanical marks are the cheapest in the exam — they cost the same one
  mark each as a genuine listening failure.

Append the entry to `06-Planning/Trackers/IELTS-Log.md`.

## Choosing the drill

Drill the top one or two recurring categories. Not the lowest score, not everything — the
budget is six hours a week and a scattered drill is indistinguishable from another mock.

Some categories don't want drills at all, and saying so is more useful than manufacturing
one:
- `word-limit`, `two-answers`, `plural` are rule failures, not skill failures. The fix is
  re-reading the rule once and a checking habit, not twenty practice items.
- `lost-place` and `ran-out-of-time` are pacing. The fix is a timing rule — abandon a
  question after ~2 minutes and come back — not more questions.
- `spelling` wants a personal misspelling list built from the log, not generic drilling.

The categories that genuinely reward drilling are `tfng-false-for-ng`, `headings`,
`matching-features`, `paraphrase`, `distractor` and `attribution`.

## Generating a drill

For a comprehension category, produce 8–10 items in the real question format, then — and
this is the part that does the teaching — **for each item, name the sentence in the passage
that decides it and why the tempting wrong answer is wrong.** An item without that
explanation is just another test.

Use passages from authentic material where you can (Cambridge volumes, the British Council
library). If you write practice items yourself, say so plainly: they are useful for
rehearsing the decision procedure and they are not calibrated to real test difficulty, so
the user should not read a score off them.

For `tfng-false-for-ng` specifically, the drill that works is contrastive: take one passage
sentence and write three statements against it — one True, one False, one Not Given — and
have the user justify each. The confusion is a decision-rule problem, and mixed practice
without the contrast doesn't surface it.

## The relevant vault notes

Link rather than restating:
`[[Log wrong answers by error category because the score tells you nothing about what to fix]]` ·
`[[False requires a contradiction while partial coverage of the statement is Not Given]]` ·
`[[A matching heading must summarise the whole paragraph which is why keyword matching fails]]` ·
`[[An over-limit Listening answer scores zero even when the content heard was correct]]` ·
`[[Listening distractors work by stating an answer and then withdrawing it]]` ·
`[[Matching features is the one Reading type whose answers do not follow passage order]]` ·
`[[Locating the answer then reading carefully beats the skim-then-scan ritual]]` ·
`[[Computer-delivered Listening removes the transfer time so typing accuracy becomes part of the score]]`
