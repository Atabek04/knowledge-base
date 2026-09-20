# Research Craft — MOC

How research is done, argued, and defended — from "what is a research question" to publishing and the viva. One map for now; split when a section outgrows a screen. Atomic notes go in `02-Zettelkasten/`. Thesis-side reading list: `~/master-thesis/LEARNING-PATH.md`; publication plan: `~/master-thesis/PUBLICATION-PLAN.md`; day-by-day schedule in the Ribaat vault's weekly plans.

Sources merged: Booth *Craft of Research* (5th) · SOAS *Understanding Research Methods* (Coursera) · Zobel *Writing for CS* (3rd) · Hevner 2004 + Wieringa 2014 (design science) · Lazar *Research Methods in HCI* (2nd) · Lakens *Improving Your Statistical Inferences* (Coursera). Chapter numbers verified against the publishers' front matter, 18 Sep 2026.

**Booth 5th ed. structure:** Intro *Your Research and Your Audience* · I *Asking Questions, Seeking Answers* (ch 1–2) · II *Sources and Resources* (ch 3–4) · III *Making Your Argument* (ch 5–9) · IV *Delivering Your Argument* (ch 10–16) · V *Some Last Considerations* (ch 17–18).

**Order matters.** Read top to bottom; each section assumes the one above. Paper A (due 25 Sep 2026) forces §1, §4, §5 first.

---

## 1. What research is

- Research = a written argument that something not previously known is now known, and that it was found out in a way others can check
- Systematic inquiry vs. building; your role and your audience's role — Booth Intro (I.1–I.4); SOAS M1
- Unsupervised research = you can pick a question worth asking, not only answer one someone gave you
- Why papers read as clean logic when the work was messy — Medawar, *Is the scientific paper a fraud?*
- Picking problems that matter — Hamming, *You and Your Research*

## 2. Degree levels and what each defence tests

- Bachelor project — can you build; graded on execution
- Master's dissertation — can you *find out*; graded on contribution + method; "we built a system" fails
- PhD — can you find out what the field did not know; publications are the gate
- Kazakhstan specifics: ГОСО minimum vs. university rules; предзащита → защита; document check by the учебный отдел

## 3. Dissertation types — which one is yours

| Type | You… | Contribution is… |
|---|---|---|
| Empirical | measure something in the world | a finding |
| Theoretical | build/extend a model, no new data | a framework |
| Systematic review | synthesise all existing studies | a map of what is known |
| Design science | build an artifact *to test an idea*, then evaluate it | knowledge from the evaluation — never the artifact |

- Bachelor trap = design science without the science: artifact built, evaluation skipped
- Design science: artifact is the *treatment*, knowledge from evaluating it is the *contribution* — Hevner 7 guidelines; Wieringa ch 1–2
- Engineering cycle: problem investigation → treatment design → validation → implementation → evaluation — Wieringa ch 3–7
- Empirical cycle inside design science — Wieringa ch 10–11; method road map ch 16
- Yours = design science with empirical validation (within-subjects study on Mutqin)

## 4. Anatomy of a paper and a dissertation

- IMRaD; what each section *claims*, not what it contains — Zobel ch 5 *Writing a Paper*; Peyton Jones talk
- Abstract → introduction → literature → method → results → discussion → conclusion
- Paper vs. dissertation: same argument, different length and audience; the two-articles rule
- Reading a paper in 20 minutes; reviewing — Zobel ch 3 *Reading and Reviewing*

## 5. The contribution — gap, question, claim

- Topic → question → problem → so-what; pure vs. applied — Booth ch 1–2; SOAS M1
- Claim → reason → evidence → warrant; acknowledgments and responses — Booth ch 5–9
- Falsifiable: what result would prove you wrong; hypotheses, questions, evidence — Zobel ch 4
- The one-sentence contribution test; mission vs. tested claim (never confuse)

## 6. Literature

- Why a review exists: mapping your place in the field, not summarising — SOAS M2; Booth ch 3–4 *Finding and Evaluating Sources*, *Engaging Sources*
- Synthesis vs. summary; surfacing tensions; each citation does work
- Finding, screening, note-taking; citation as evidence; APA 7
- Predatory and weak sources; correlational vs. experimental evidence

## 7. Methods

- Research design: between / within / quasi / crossover; why within-subjects at N = 25–30 — Lazar ch 2–3; Wieringa ch 11, ch 20
- Validity threats: internal, external, construct, conclusion; history, maturation, novelty, demand, attrition, tool dependence — Shadish et al.
- Instruments: questionnaires, telemetry, tests; reliability and validity — Lazar ch 5 *Surveys*, ch 12 *Automated Data Collection*
- Qualitative: interviews, thematic analysis — Lazar ch 8, ch 11; Braun & Clarke
- Ethics and human subjects; consent; withdrawal; data — Lazar ch 15; SOAS M4
- Usability testing as a methodological prerequisite — Lazar ch 10

## 8. Statistics for this thesis

- p-values, Type 1/2 errors; the null is always false — Lakens M1, M6
- Effect sizes: Cohen's d, correlations — Lakens M4
- Power and sample-size justification; pre-registration — Lakens M3, M5
- Mixed / multilevel models and GLMM for H1a/H1b — Field, *Discovering Statistics*; Lazar ch 4; Zobel ch 14–15
- Open science: replication, publication bias — Lakens M7

## 9. Writing

- Planning, drafting, organising, revising; introductions and conclusions — Booth ch 10–12, 14
- Scholarly voice: tense, hedging, no marketing; the "project report" failure — Booth ch 15; Zobel ch 6–7
- Figures, tables, algorithms, mathematics; visual evidence — Booth ch 13; Zobel ch 9–11
- Writing regularly beats writing well — Silvia, *How to Write a Lot*; SOAS M3

## 10. Publishing

- Venues: journal vs. conference; lists and indexing (КОКСНВО, Scopus, WoS); predatory signals
- Peer review: what reviewers look for; responding to reviews; one venue at a time
- Self-plagiarism between papers and dissertation; authorship; research ethics — Booth ch 17; Zobel ch 17
- → `~/master-thesis/PUBLICATION-PLAN.md`

## 11. Defence

- What examiners test: contribution in one sentence; falsifiability; scope; knowing the unknown
- Slides: one claim per slide, titles with verbs — `/thesis-supervisor` defence checklist
- Speaking — Winston, *How to Speak*; Booth ch 16 *Research Presentations*; Zobel ch 16
- Предзащита May 2027 · защита June 2027

---

## Trackers

- [ ] §1–5 read before Paper A draft (25 Sep 2026)
- [ ] §6–7 before the pilot protocol freezes (Nov 2026)
- [ ] §8 before the power section of the methods chapter (Jan 2027)
- [ ] §9–10 alongside Paper A revisions (Oct–Dec 2026)
- [ ] §11 in the защита block (May 2027)
