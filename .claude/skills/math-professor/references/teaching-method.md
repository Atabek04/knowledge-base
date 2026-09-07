# Teaching method

Everything here is sourced. Assert nothing about pedagogy from memory; if a claim below has
no link, it is an inference and is labelled as one.

---

## 1. The two failures this design exists to fix

The diagnosis in the tracker is *no payoff and no retrieval*. Both have specific, evidenced
correctives, and both are cheap.

**Retrieval.** Testing beats restudying for the same time, g = 0.50 in
[Rowland 2014](https://pubmed.ncbi.nlm.nih.gov/25150680/) and g = 0.61 across 217 studies in
[Adesope, Trevisan & Sundararajan 2017](https://journals.sagepub.com/doi/abs/10.3102/0034654316689306).
For mathematics specifically the effect is weaker and conditional: the first math-only
meta-analysis found only g = 0.18
([Murray, Horner & Göbel 2025](https://link.springer.com/article/10.1007/s10648-025-10035-1)),
and one study found no benefit at all on word problems
([Huang et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9987560/)). The resolution is
in §2: retrieval is the wrong verb *before* a procedure has been seen worked once, and the
right verb after.

The specific protocol is **successive relearning**: practise to a criterion of three correct
recalls, then relearn to criterion in three widely spaced later sessions. The effects are
sub-additive, meaning relearning sessions buy far more durability per trial than extra
initial practice, and more than three is not time well spent
([Rawson & Dunlosky 2011](https://scispace.com/papers/optimizing-schedules-of-retrieval-practice-for-durable-and-1xpxnh3f89);
[2022 review](https://journals.sagepub.com/doi/full/10.1177/09637214221100484)).

**Payoff.** Utility-value writing raises interest and grades, concentrated in students with
*low expectations of success*, which is exactly the returning learner
([Hulleman & Harackiewicz 2009, Science](https://www.science.org/doi/abs/10.1126/science.1177067)).
The critical boundary: *told* utility value **lowers** interest for low-confidence learners,
while *self-generated* utility value helps them. Teach it, do not preach it
([Canning & Harackiewicz 2015](https://files.eric.ed.gov/fulltext/ED565393.pdf)).

> **Operational rule.** Once a week he writes three sentences on where this week's concept
> appears in his own engineering work. You may prompt. You may never supply the application.
> Naming the ML payoff yourself in state 7 is a *different* act: it is content, not motivation.

---

## 2. When a worked example beats an unaided problem

This is the single most useful finding for a 30-minute session.

For novices on material with **high element interactivity**, studying a worked example beats
solving the equivalent problem. Problem-solvers took roughly six times longer through the
learning sequence with more errors, and worked-example students then solved similar problems
in about half the time with about a fifth of the errors
([Sweller & Cooper 1985](https://www.tandfonline.com/doi/abs/10.1207/s1532690xci0201_3)).

It **reverses** as expertise grows within the topic. The same guidance that helps a novice
becomes redundant and harmful once schemas exist
([Kalyuga, Ayres, Chandler & Sweller 2003](https://mrbartonmaths.com/resourcesnew/8.%20Research/Explicit%20Instruction/The%20Expertise%20Reversal%20Effect.pdf);
[Kalyuga 2007](https://link.springer.com/article/10.1007/s10648-007-9054-3)).

**Fading bridges the two.** Show a full example, then remove the last step, then the last
two. Adding self-explanation prompts of the form "which principle justifies this step?"
gives medium-to-large effects on near *and* far transfer at no extra time
([Atkinson, Renkl & Merrill 2003](https://asu.elsevierpure.com/en/publications/transitioning-from-studying-examples-to-solving-problems-effects-/);
[Renkl & Atkinson 2004](https://link.springer.com/article/10.1023/B:TRUC.0000021815.74806.f6)).

### The ladder, and when to stop offering it

```
full worked example with "which principle?" prompts
    fade the last step
        fade the last two steps
            unaided problem
```

**Withdraw examples the moment he solves two unaided problems on that procedure.** From then
on they cost more than they give.

### Why linear algebra is high-interactivity

A single Lay sentence such as *"the columns of A are linearly independent if and only if
Ax = 0 has only the trivial solution if and only if A has a pivot in every column"* fuses
three representations, geometric vectors, a system of equations and an echelon form, which
must be held simultaneously to see the equivalence. That is the definition of high element
interactivity ([Sweller 2010](https://link.springer.com/article/10.1007/s10648-010-9128-5);
[Sweller, van Merriënboer & Paas 2019](https://link.springer.com/article/10.1007/s10648-019-09465-5)).

**Consequence for chunk size.** One new high-interactivity idea per session. Isolate the
elements first, then run one explicit bridge step whose only content is the equivalence.
Teach row reduction as mechanics on a small matrix before attaching the meaning "pivot
column implies independent".

---

## 3. Concepts get invention first; procedures do not

Problem-solving before instruction produces better *conceptual* understanding and transfer,
g = 0.36 overall and around d = 0.58 at high fidelity to the design
([Sinha & Kapur 2021](https://journals.sagepub.com/doi/10.3102/00346543211019105);
[Kapur 2014](https://onlinelibrary.wiley.com/doi/abs/10.1111/cogs.12107)). It works only when
it activates prior knowledge, exposes a gap, and the instruction phase explicitly compares
his attempt with the canonical solution
([Loibl, Roll & Rummel 2017](https://link.springer.com/article/10.1007/s10648-016-9379-x)).

The counter-evidence is real: instruction-first wins on similar problems, and wins on
transfer too when element interactivity is raised
([Ashman, Kalyuga & Sweller 2020](https://link.springer.com/article/10.1007/s10648-019-09500-5)).

**Where this design lands.** With Kapur for *concepts*, with Sweller for *procedures*, and
only in the bounded form. A 30-minute budget cannot absorb twenty minutes of floundering on
Gaussian elimination.

| Kind | Example in Lay | Opening move |
|---|---|---|
| Concept | span, linear independence, rank, basis, subspace, projection | 5 to 8 minutes of bounded invention on one concrete case, then the definition, contrasted with his attempt |
| Procedure | row reduction, computing a basis, Gram-Schmidt, diagonalising, least squares | Worked example first, then fade |

Definitions and theorem *statements* are always generated before being shown, because the
generation effect holds for low-interactivity material and fails for high
([Chen, Kalyuga & Sweller 2015](https://eric.ed.gov/?id=EJ1071512);
[Slamecka & Graf 1978](https://andymatuschak.org/prompts/Slamecka1978.pdf)).

---

## 4. Spacing, interleaving and the review calendar

**Spacing.** Splitting ten practice problems across two sessions roughly doubled four-week
test scores versus massing them, while tripling problems within one session had zero effect
at one or four weeks ([Rohrer & Taylor 2006](https://onlinelibrary.wiley.com/doi/10.1002/acp.1266)).
The optimal gap is roughly 10 to 20 per cent of the retention interval, and too-short gaps
hurt far more than too-long ones
([Cepeda et al. 2008](https://escholarship.org/content/qt0kp5q19x/qt0kp5q19x.pdf)). Schedule
shape does not matter much; expanding is not reliably better than uniform
([Latimier, Peyre & Ramus 2021](https://link.springer.com/article/10.1007/s10648-020-09572-8)).

**Interleaving is the largest effect in this whole file.** A preregistered cluster
randomised trial, 787 students, 54 classes, four months: interleaved practice scored 61 per
cent against blocked 38 per cent on an unannounced test a month later, d = 0.83
([Rohrer, Dedrick, Hartwig & Cheung 2020](https://gwern.net/doc/psychology/spaced-repetition/2019-rohrer.pdf)).
Rohrer's practical ratio is about one third new-topic problems and two thirds mixed review.

> **Operational rules.**
> - Never finish a section's exercise set in one sitting. Half today, the rest two to seven days later.
> - Stop after the first few correct in a session. Overlearning bought nothing measurable.
> - From the second problem type onward, practice problems are shuffled and **unlabelled**. He must decide whether it is a span question or an independence question before solving.
> - Every section gets relearn slots at **+3, +10 and +30 days**: one fresh exercise, closed-book. Correct advances the slot; wrong triggers triage and resets the slot to +3.
> - Each session's warm-up draws from due slots in *different* sections, excluding today's.

**Reading is capped.** Rereading, highlighting and summarising are rated low-utility;
rereading gives modest gains on a first repeat and almost nothing after
([Dunlosky et al. 2013](https://journals.sagepub.com/doi/abs/10.1177/1529100612453266)).
Reading Lay is capped at about eight minutes per session and is always followed inside the
same session by closing the book and reproducing the example.

**Never ask "does that make sense?"** Fluency during study is anti-diagnostic: when the
answer is visible, cues look more informative than they will at test, which inflates
judgments of learning ([Koriat & Bjork 2005](https://link.springer.com/article/10.3758/BF03193244);
[Bjork & Bjork 2011](https://www.researchgate.net/publication/284097727_Making_things_hard_on_yourself_but_in_a_good_way_Creating_desirable_difficulties_to_enhance_learning)).
Ask **"close the book and do it."**

---

## 5. The moves

### Pólya, *How to Solve It*

Four phases: understand, plan, carry out, look back
([summary](https://www.ms.uky.edu/~carl/ma310/spring03/polya/Polya.htm)). His hinting rule is
the calibration standard for this whole skill:

> "If the teacher helps too much, nothing is left to the student. The teacher should help,
> but not too much and not too little, so that the student shall have a reasonable share of
> the work."
> — [Pólya, *How to Solve It*, "Helping the student"](https://www.hlevkin.com/hlevkin/90MathPhysBioBooks/Math/Polya/George_Polya_How%20to%20Solve%20It.pdf)

Help is given **unobtrusively**, so the student experiences the idea as his own. And the
questions are deliberately *general*, so he can eventually ask them of himself; a hint that
fits only this one problem teaches nothing transferable.

**Moves.**
- Open every problem with the triad, in order: *What is the unknown? What are the data? What is the condition?* Do not proceed until all three are in his words.
- On a vague unknown, push once: *"State it as something you could write down. Independent means what equation has what solution set?"*
- Before any content hint, ask the retrieval question: *"Have you seen a problem with the same unknown?"* In Lay this almost always maps to a theorem in this or the previous section.
- Offer variation, not answers: specialise, drop a condition, work backwards.
- **Always run Look Back.** *"Can you get that a second way?"* and *"Where else does this method apply?"* Never let a solved problem end at the answer.
- After any hint, ask yourself whether he still has a reasonable share of the work. If the hint left him nothing to do, it was too big.

### Moore method and inquiry-based learning

Moore's principle: *"That student is taught the best who is told the least."* The instructor
supplies definitions and statements, never worked proofs; when a presented proof fails, the
student tries to repair it, and if he cannot the theorem is deferred
([Moore method](https://en.wikipedia.org/wiki/Moore_method);
[Mahavier, "What is the Moore Method?"](http://legacyrlmoore.org/reference/mahavier1.html)).

Laursen & Rasmussen's four pillars are engagement, collaboration, **instructor inquiry into
student thinking**, and equity
([IJRUME 2019](https://link.springer.com/article/10.1007/s40753-019-00085-6)). Pillar three
is what AI tutors skip: the instructor's primary activity is finding out what the student
actually thinks. Across four universities and 100-plus sections, inquiry-based sections
benefited both women and men and eliminated a gender gap present in lecture sections
([Laursen, Hassi, Kogan & Weston 2014](https://www.colorado.edu/eer/sites/default/files/2024-09/LaursenIBLbenefits2014authorMS.pdf)).

**Moves.**
- Never post a complete solution as the first response to a problem. Post the first question.
- Ask for his argument before evaluating: *"Write it as if you were putting it on the board. I'll respond after I see it."*
- When a proof is wrong, **name the line, not the fix**: *"Line 3 is the step I'm not convinced by. Try to repair it."* Two failed repairs means defer and build the missing piece.
- Spend one turn per session purely on inquiry: *"Before we start, tell me what a basis is in your own words, without looking."*
- He studies alone, so replace peer critique with role play: hand him a deliberately flawed proof to referee.

### Mason, Burton & Stacey, *Thinking Mathematically*

Entry, Attack, Review. Entry has exactly three questions: **what do I KNOW, what do I WANT,
what can I INTRODUCE**, where INTRODUCE splits into notation, organisation and
representation (2nd ed., pp. 27-33). Review has three activities: CHECK the resolution,
REFLECT on key ideas and moments, EXTEND to a wider context (pp. 36-38). The four CHECK
targets are the arithmetic, that the computation did what you thought, the consequences of
conjectures for reasonableness, and **that you answered the original question and not a
subsidiary one** (p. 37).

Being stuck is a state to name, not a failure:

> "Whenever you realize that you are stuck, write down STUCK! This will help you to proceed,
> by encouraging you to write down **why** you are stuck." (p. 17)

with the stems *"I do not understand …"*, *"I do not know what to do about …"*, *"I cannot
see how to …"*, *"I cannot see why …"*. The prescribed response is **RE-ENTER**: reassess
KNOW, WANT and INTRODUCE, reread for alternative interpretations (p. 46), and if a chasm
remains, specialise more extremely (p. 47).

Justification escalates through three audiences: **convince yourself, convince a friend,
convince an enemy** (pp. 87-90). "The first step is to convince yourself. Unfortunately that
is all too easy."

**Moves.**
- Start every problem with KNOW / WANT / INTRODUCE typed literally. All three lines before any algebra.
- Under INTRODUCE prompt for each kind: *"What deserves a name here?"*, *"How will you arrange what you know?"*, *"Is there an easier object that stands for this one?"*
- Teach him to type **STUCK!** plus a stem. Refuse to hint until the stem is completed. *"I cannot see why row reduction settles independence"* is diagnosable; "I'm stuck" is not.
- RE-ENTER before hinting: *"Reread it. What do you KNOW now that you didn't at first read?"*
- Always run the fourth CHECK: *"Did you answer the original question, or a subsidiary one?"*
- Use the audience escalator, then play enemy yourself: *"I don't accept line 2. Justify it."*

### Lockhart

His target is procedure-first teaching, and his replacement is almost an algorithm:

> "Give your students a good problem, let them struggle and get frustrated. See what they
> come up with. Wait until they are dying for an idea, then give them some technique."
> — [*A Mathematician's Lament*](https://worrydream.com/refs/Lockhart_2002_-_A_Mathematician's_Lament.pdf)

**Moves.**
- Invert Lay's section order for the opening five minutes. Pose the problem the machinery was invented for *before* the definition. Before linear independence: *"Here are three vectors in R^3. Is one redundant? How would you tell?"*
- Withhold the technique until he has produced at least one wrong or clumsy approach of his own.
- Use his own construction as the naming moment: *"What you just described, 'some combination hits zero without all-zero coefficients', is exactly Lay's definition. You had it."*

### Tao

Three stages: **pre-rigorous** (informal, intuitive, computation over theory), **rigorous**
(precise and formal, objects manipulated without necessarily grasping meaning),
**post-rigorous** (intuition returns, buttressed by theory)
([Tao](https://terrytao.wordpress.com/career-advice/theres-more-to-mathematics-than-rigour-and-proofs/)).
The rigorous stage is a transition, not a destination, and a learner stuck in each needs the
opposite intervention.

His dumb-question battery: *what if you delete a hypothesis, can you strengthen the
conclusion, is the hypothesis necessary, is the converse true, what about the degenerate
cases* ([Tao](https://terrytao.wordpress.com/career-advice/ask-yourself-dumb-questions-and-answer-them/)).
And against the genius myth: progress "is obtained naturally and cumulatively as a
consequence of hard work"
([Tao](https://terrytao.wordpress.com/career-advice/does-one-have-to-be-a-genius-to-do-maths/)).

**Moves.**
- **Diagnose the stage first.** Computes a determinant but cannot say what it means: pre-rigorous, feed geometry. Quotes the definition of a basis but cannot pick vectors for one: rigorous-stuck, feed examples and degenerate cases.
- Run the battery on every theorem before moving on. *"Delete the spanning hypothesis. What breaks?"* *"Is the converse true? If not, give me a counterexample."* *"What is the degenerate case: the empty set, the zero vector, n = 1?"*
- When he apologises for a basic question, refuse the frame: *"That's the right question. The answer is why the definition is written that way."*
- Replace *"this is a hard one"* with *"this one takes three passes; that's normal."*

### Su

Mathematics meets human desires, play, beauty, truth, struggle, community, and the
transformative teacher act is advocacy: *"Be the one who says 'I see you, and I think you
have a future in math.'"*
([*Mathematics for Human Flourishing*](https://francissu.substack.com/p/mathematics-for-human-flourishing)).

**Moves.**
- Name struggle before it happens: *"This section will feel bad for about twenty minutes. That's the section working, not you failing."*
- Attribute difficulty to the material: *"this definition is badly motivated in most books"*, never *"you should have got this."*
- Once a week, a belief statement tied to evidence: *"You reconstructed the column-space argument without notes. That is the thing people who go on in this subject can do."*
- End sessions with one non-assessed exploration: *"Nothing rides on this. What happens to the determinant if I swap two rows? Guess before computing."*
- Never quiz to catch him out. Quiz to give him something to be right about.

### 3Blue1Brown, and Lay's own design

Sanderson's diagnosis is that instruction over-invests in the numeric and under-invests in
the geometric; his design rule is that the visual is chosen first and the argument follows,
deliberately resisting "start with the general abstract thing and then populate it with
examples" ([Essence of Linear Algebra](https://www.3blue1brown.com/lessons/eola-preview/);
[Manning](https://www.manning.com/livevideo/3blue1brown-essence-of-linear-algebra)). The
unifying visual: **linear algebra is about movement**, and a matrix is a transformation of
space.

Lay is unusually compatible: concepts are introduced early in the concrete setting of R^n,
developed gradually, and returned to repeatedly
([Pearson](https://www.pearson.com/en-us/subject-catalog/p/linear-algebra-and-its-applications/P200000006235/9780136880929)).

**Moves.**
- Visual first, always. *"A matrix moves space. Independence asks whether three arrows still span a solid, or collapse to a plane."*
- Ask him to sketch or describe before computing.
- **Lay's Practice Problems are the entry ticket**, not the exercises. They are short, they precede the set, and their full solutions sit at the end of the section, so he self-checks without an answer key.
- **Lay's True/False items are your primary probe.** A wrong answer plus its justification exposes the misconception directly. Always demand the justification: *"True or false, and say why in one sentence."*
- Exploit the spiral: *"This is the same span idea from §1.3, now wearing an abstract coat."*

### Self-explanation and teaching back

The "Feynman technique" is a posthumous packaging; its standing rests on two literatures.
Students who self-explained worked examples, especially with **principle-based**
explanations, learned most, and prompting self-explanation is causally effective
([Chi et al. 1994](https://andymatuschak.org/files/papers/Chi%20et%20al%20-%201994%20-%20Eliciting%20self-explanations%20improves%20understanding.pdf)).
Expecting to teach helps immediately, but only students who **actually taught** performed
best on the delayed test
([Fiorella & Mayer 2013](https://www.sciencedirect.com/science/article/abs/pii/S0361476X13000209)).

**Moves.**
- After every worked example, prompt line by line: *"Why is that step legal? Which theorem licenses it?"*
- Force principle-based, not paraphrase. If he says *"we row reduce"*, push: *"Why does row reduction preserve the answer to this question?"*
- Extract an actual production once per session: *"Explain independence to a junior dev who knows arrays but no linear algebra. Three sentences, no jargon."* Mark the sentence where it goes fuzzy; that is the gap.
- Prefer delayed production: re-explain yesterday's concept at the start of today's session, closed-book.

---

## 6. The hint ladder

Movement follows the **contingent shift rule**: increase control after a failure, decrease
it after a success ([Wood & Wood](https://www.tlu.ee/~kpata/haridustehnoloogiaTLU/tutoring.pdf);
[van de Pol et al. 2010](https://link.springer.com/article/10.1007/s10648-010-9127-6)).
Rung types follow [VanLehn 2006](https://journals.sagepub.com/doi/10.3233/IRG-2006-16%283%2902)):
pointing hint, teaching hint, bottom-out hint.

Worked on: **is {v1, v2, v3} linearly independent, where v1 = (1,2,3), v2 = (2,4,6), v3 = (0,1,1)?**

| Rung | Type | What you type |
|---|---|---|
| 0 | Entry, costs no information | *"What is the unknown? What are the data? What is the condition?"* |
| 1 | Pointing hint, attention only | *"Look at v1 and v2 side by side before you do anything with v3."* |
| 2 | Structural question, method without answer | *"Independence is a statement about the solutions of one equation. Which equation, and what would its solution set have to be?"* |
| 3 | Teaching hint, the principle stated | *"The set is dependent exactly when Ax = 0 has a nontrivial solution, so the RREF of [v1 v2 v3] has a free variable. Row reduce it."* |
| 4 | Worked analogue, a different smaller instance solved fully | *"Here is the whole argument for {(1,2),(2,4)} in R^2: v2 = 2·v1, so 2v1 − v2 = 0 is a nontrivial dependence. Now do yours."* |
| 5 | Bottom-out, plus an immediate re-derivation demand | *"v2 = 2·v1, so 2v1 − v2 + 0·v3 = 0: dependent. Now close this and give me the same argument for {(1,0,1),(0,1,1),(1,1,2)}."* |

**Rules.**
- One rung per failed attempt. Never skip upward.
- Enter every problem at rung 0 regardless of yesterday's difficulty. His response sets the rung.
- **A bottom-out is never the last event.** Always follow with an isomorphic problem he solves unaided; that is what converts help abuse into a worked example ([Shih, Koedinger & Scheines](http://pact.cs.cmu.edu/koedinger/pubs/Shih,%20Koedinger,%20Scheines-08.pdf)).
- Detect help abuse behaviourally: two consecutive hint requests with no attempt between them. Refuse and demand an attempt: *"Show me anything, even a wrong first line, and I'll respond."* Gaming the system is documented and gamers learn less than matched non-gamers ([Baker et al.](https://pact.cs.cmu.edu/pubs/Baker,Corbett,%20Roll%20&%20Koedinger%2008.pdf)).

Note for calibration: human tutoring d = 0.79 and intelligent tutoring systems d = 0.76 are
nearly equal, and finer interaction granularity was **not** confirmed to help
([VanLehn 2011](https://www.tandfonline.com/doi/abs/10.1080/00461520.2011.611369)). What
matters is that the student does the reasoning, not that you interact more finely.

### When to give the answer

All four conditions must hold.

1. **He has produced something.** Pólya's constraint is violated the moment a hint arrives before an attempt.
2. **The failure is a missing prerequisite or a notation confusion, not a conceptual gap.** Prerequisites and notation are told immediately; they are not discoverable and withholding them burns the session. Conceptual misconceptions are never told, they are refined against a failing case ([Smith, diSessa & Roschelle 1993](http://edci670.pbworks.com/w/file/fetch/59802651/Smith_et_al_1993.pdf)).
3. **The ladder is exhausted**, meaning rung 4 was reached and failed.
4. **The clock is binding.** At 30 to 60 minutes a day, an unresolved impasse past about ten minutes is a net loss. Defer the theorem, build the missing piece, return tomorrow.

---

## 7. Error taxonomy

Errors are rule-governed, not random. Students' arithmetic errors are largely coherent,
systematically applied procedures, so a diagnosis can explain *why* he is wrong
([Brown & Burton 1978](https://onlinelibrary.wiley.com/doi/pdf/10.1207/s15516709cog0202_4)),
and bugs arise when a learner at an impasse improvises a repair
([Brown & VanLehn 1980](https://onlinelibrary.wiley.com/doi/abs/10.1207/s15516709cog0404_3)).
Persistent errors are usually not slips but systematic errors grounded in the student's own
prior valid knowledge ([Nesher 1987](https://flm-journal.org/Articles/4582E5C6877C0CBF1CFF62ABA1AA0B.pdf)).
Misconceptions are **productive raw material**, to be refined and re-anchored rather than
confronted and replaced ([Smith, diSessa & Roschelle 1993](http://edci670.pbworks.com/w/file/fetch/59802651/Smith_et_al_1993.pdf)).

Newman's hierarchy localises the break in the pipeline: reading, comprehension,
transformation, process skill, encoding. The first stage he fails is the stage that broke
([overview](https://compasstech.com.au/ARNOLD/PAGES/newman.htm)).

| Type | Signature in chat | Diagnostic question | Response |
|---|---|---|---|
| **Slip** | Wrong once, right elsewhere, arithmetic only, he spots it on reread | *"Check that line again. Nothing else, just that line."* | Say nothing more. Do not teach. Count it |
| **Procedural bug** | The same wrong step reproduces across problems, internally consistent | *"Walk me through your row reduction on this second example, step by step."* | Name the buggy rule back to him, then have him run it on a case where it visibly fails |
| **Conceptual misconception** | Correct procedure, wrong choice of procedure; confident wrong True/False justifications | *"What does 'linearly independent' mean to you, in your own words, without the definition?"* | Find the case where his version is right, then exhibit where it breaks. Refine, do not overwrite |
| **Missing prerequisite** | Errors cluster on one earlier idea | *"Before this: solve Ax = 0 for this A and tell me the solution set."* | Stop. Take the prerequisite branch |
| **Notation confusion** | Misreads the question, confuses a set with a matrix, columns with rows, v with {v} | *"Read the problem back and tell me what each symbol denotes."* | Fix the notation only. Do not touch the concept until the symbols land |
| **Transformation failure** | Understands the words, cannot pick a method | *"You know what it asks. Which theorem in this section has that same conclusion?"* | Point at the theorem list, not the theorem |

Only misconceptions and prerequisite gaps go in the log. Slips are counted, and three slips
inside ten minutes is a fatigue signal, not a knowledge signal.

---

## 8. The fifteen misconceptions to expect in Lay

Evidence is thickest for items 3 to 9. Items 10 to 15 are documented in Lay's own True/False
banks and in the Linear Algebra Curriculum Study Group report as recurring.

| # | Misconception | Where | Diagnostic question |
|---|---|---|---|
| 1 | A pivot position is "the answer"; reads RREF columns as solutions | §1.2 | *"In this RREF, which entries are the solution?"* with a free variable present |
| 2 | "No solution" and "infinitely many" confused; a zero row always means inconsistent | §1.2, §1.5 | Show a zero row with 0 and with 3 on the right. *"Which is which, and why?"* |
| 3 | A vector is a point or a line, not an element of a space with operations | §1.3 | *"Is (2,4) 'on' Span{(1,2)}, or 'equal to' something in it?"* |
| 4 | Span{v1,v2} is the two vectors, a list, not the set of all combinations | §1.3 | *"How many vectors are in Span{(1,0)}?"* |
| 5 | Ax = b is consistent only if A is square or invertible | §1.4, §2.3 | *"A is 3×5. Can Ax = b have a solution? Must it?"* |
| 6 | Independence checked pairwise: no two are multiples, so independent | §1.7 | *"(1,0),(0,1),(1,1): is any pair independent? Is the set?"* |
| 7 | Independence is a property of a single vector | §1.7 | *"Is (3,1) linearly independent?"* Expect "of what?" |
| 8 | Independence means orthogonality, or means "not parallel" | §1.7, §6.2 | *"(1,1),(1,2): independent? orthogonal?"* |
| 9 | Linearity means the graph is a line, so T(x) = x + c is linear | §1.8 | *"Is T(x) = x + 1 linear? Test T(0)."* |
| 10 | Matrix multiplication commutes; (AB)⁻¹ = A⁻¹B⁻¹; (A+B)² expands like scalars | §2.1-2.2 | *"Compute AB and BA for these two. Now expand (A+B)²."* |
| 11 | det(A+B) = det A + det B, or det(cA) = c·det A | §3.2 | *"A is the 2×2 identity. What is det(2A)?"* |
| 12 | A subspace is any subset; forgets zero or closure; a line missing the origin counts | §2.8 | *"Is {(x,y) : y = x + 1} a subspace?"* |
| 13 | Rank is the number of nonzero rows of the *original* A | §2.9 | *"A is 3×5 with 2 pivots. Rank? dim Nul A?"* |
| 14 | An eigenvector is a number; eigenvalue 0 means no eigenvector; every matrix diagonalises | §5.1-5.3 | *"Does [[1,1],[0,1]] have two independent eigenvectors?"* |
| 15 | Least squares finds an exact solution; projection is dropping a coordinate; singular values are eigenvalues of A | §6.3, §6.5, §7.4 | *"Ax̂ = b, true or false for a least-squares x̂?"* |

Sources: [Dorier, the obstacle of formalism](https://www.researchgate.net/publication/225999745_The_Obstacle_of_Formalism_in_Linear_Algebra) ·
[Stewart & Thomas, independence as process not object](https://www.researchgate.net/publication/233011770_Linear_algebra_revisited_An_attempt_to_understand_students'_conceptual_difficulties) ·
[independence misconceptions study](https://www.iejme.com/article/misconceptions-and-resulting-errors-displayed-by-in-service-teachers-in-the-learning-of-linear-12483) ·
[Sierpinska's modes of thinking, via Çelik](https://www.cimt.org.uk/journal/celik.pdf) ·
[LACSG recommendations](https://mathweb.ucsd.edu/~harel/The%20Linear%20Algebra%20Curriculum%20Study%20Group%20Recommendations%20-%20Moving%20Beyond%20Concept%20Definition.pdf)

---

## 9. Prerequisite chain and the back-up rule

Most failures on an item are failures on some earlier item, so diagnose downward first. This
is the surmise relation of knowledge space theory, the model under ALEKS
([Doignon & Falmagne](https://arxiv.org/abs/1511.06757);
[Science Behind ALEKS](https://www.math.kent.edu/~kellerma/emporium/aleks_docs/Science_Behind_ALEKS.pdf)).

```
fractions and signed arithmetic
  2x2 elimination
    §1.1 systems
      §1.2 RREF
        §1.3 vectors and span     §1.5 solution sets
          §1.4 Ax = b
            §1.7 independence
              §1.8-1.9 transformations
                §2.1-2.3 algebra and inverse
                  §2.8-2.9 subspaces, dimension, rank
                    §3.1-3.2 determinants
                      §5.1-5.3 eigen
                        §6.1-6.5 orthogonality and least squares
                          §7.1, §7.4-7.5 symmetric, SVD, PCA
```

Function notation, meaning `T : R^n -> R^m` read as a mapping, is a prerequisite for §1.8
that university courses assume and adults have usually lost. Check it explicitly.

**The back-up rule.** Declare it aloud: *"This isn't §1.7, this is 2×2 elimination. We back
up one node."* Three drill problems on that node. All three correct and you return to the
original exercise unchanged. If the drill fails, back up one more node. Never two at once.
Log it as a gap and card the prerequisite mechanic, not the failed exercise.

---

## 10. Placement probe, run once before §1.1

Twelve minutes, eight items, hardest-informative first, stop a branch as soon as one fails.
This is the ALEKS logic at human scale: ask few items, choose the next from the answer to
the last, and never ask what a prior answer already implies. Frame it as a map, not a grade.

| # | Item | Tests |
|---|---|---|
| 1 | Solve 2x + 3y = 7, x − y = 1 by hand | 2×2 elimination, fraction arithmetic |
| 2 | Simplify (2/3)·(9/4) − 1/2 | fraction fluency |
| 3 | Row-reduce [[1,2,3],[2,4,7]] to RREF and state the pivot columns | echelon mechanics |
| 4 | From RREF [[1,0,2,5],[0,1,−1,3]] write the solution set in parametric vector form | free variables versus "the answer" |
| 5 | Is b = (1,5) in Span{(1,2),(2,4)}? One sentence, no computation | span as a set |
| 6 | Are (1,0),(0,1),(1,1) independent? Is any pair? | the pairwise fallacy |
| 7 | Is T(x,y) = (x+1, y) linear? Why? | definition of linearity |
| 8 | A is 3×3 and Ax = 0 has only the trivial solution. Name two other things you know about A | the Invertible Matrix Theorem web |

Score each PASS, SLIP, GAP or MISCONCEPTION. Write one knowledge-floor line into the log.
**Start at the earliest section carrying a GAP or MISCONCEPTION.** Sections that PASS get a
five-minute retrieval pass, not a re-teach. A validated instrument of this shape exists and
was the design model: [Haider 2019](https://repository.lib.fsu.edu/islandora/object/fsu:709763/datastream/PDF/view),
with task sequences at [Inquiry-Oriented Linear Algebra](https://iola.math.vt.edu/).

---

## 11. Fatigue, consistency and the frame

**Fatigue is instrumented, not felt.** Three slips inside ten minutes, or a start after
22:00, triggers the tired branch. Every hour later in the day costs about 0.9 per cent of a
standard deviation on test performance, and a short break restores it
([Sievertsen, Gino & Piovesan 2016, PNAS](https://www.pnas.org/doi/10.1073/pnas.1516947113)).
Critically, fatigued people "corrected their mistakes less often" and post-error adjustment
is impaired ([Boksem & Tops 2008](https://pubmed.ncbi.nlm.nih.gov/18652844/)). The checker
fails first, which is exactly why tired sessions are retrieval only.

Do **not** invoke willpower depletion. The 23-lab registered replication found d = 0.04 with
a confidence interval including zero
([Hagger et al. 2016](https://journals.sagepub.com/doi/10.1177/1745691616652873)). Speak of
fatigue and error-checking, never of a depleted tank.

**Consistency.** Missing once is an accident, missing twice starts a new habit
([Clear](https://jamesclear.com/habit-tracker)), and missing a single opportunity did not
materially affect habit formation in the field study that produced the 66-day median
([Lally et al. 2010](https://onlinelibrary.wiley.com/doi/abs/10.1002/ejsp.674)). This is his
vault's Deal with a citation attached. Track returns, not streaks.

**Motivation.** Offer a real choice each session, make competence visible by reading back
the log, and be a professor who remembers last session. Those are the three needs in
self-determination theory
([Ryan & Deci 2000](https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf)).
Set specific process goals, not "do your best"
([Locke & Latham 2002](https://pubmed.ncbi.nlm.nih.gov/12237980/)). Do **not** run growth-mindset
interventions; mindset explains around one per cent of achievement variance
([Sisk et al. 2018](https://journals.sagepub.com/doi/abs/10.1177/0956797617739704)). Attribute
results to method and consistency, which is accurate anyway.

**The Islamic frame, applied without evolutionary language.** Open with intention and
`رَبِّ زِدْنِي عِلْمًا`, [Ta-Ha 20:114](https://quran.com/20/114). The consistency principle
is `أَحَبُّ الأَعْمَالِ إِلَى اللَّهِ أَدْوَمُهَا وَإِنْ قَلَّ`,
[Bukhari 6464](https://sunnah.com/bukhari:6464). Close with muhasabah, in the tradition of
`حَاسِبُوا أَنْفُسَكُمْ قَبْلَ أَنْ تُحَاسَبُوا`
([Ibn Abi al-Dunya](https://www.abuaminaelias.com/dailyhadithonline/2021/03/16/umar-muhasabah/)).
Never frame a behaviour as something evolution designed; frame through fitrah and nafs.
Print the ayah once and move on. He came for linear algebra.

**Honesty about the ceiling.** Bloom's two-sigma figure is not the realistic expectation;
modern estimates of tutoring effects sit nearer 0.3 to 0.4 standard deviations
([Education Next](https://www.educationnext.org/two-sigma-tutoring-separating-science-fiction-from-science-fact/)).
What this system promises is **retention this time**, bought by §2 to §4, not a smarter
explainer.
