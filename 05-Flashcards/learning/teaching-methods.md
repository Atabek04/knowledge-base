TARGET DECK: Tech-KB::Pedagogy::Teaching Methods
Tags: pedagogy teaching
**Related:** [[Learning Strategies MOC]]

---

START
Coding Questions
What are Rosenshine's three research bases?
Back:
1. **Cognitive science** — working memory limits; instruction must manage load carefully
2. **Master teacher observations** — effective teachers question frequently, check understanding constantly, correct errors promptly
3. **Cognitive support studies** — scaffolds, worked examples, and models help learners manage difficult content

All three converge on the same instructional behaviors — that convergence is what makes the principles strong.
Tags: pedagogy rosenshine
END

START
Coding Questions
What is the core instructional loop from Rosenshine's most critical principles?
Back:
4 principles that form the loop:

1. **Small steps** (P2) — present one chunk; practice before advancing
2. **Ask many questions** (P3) — cold call, hinge questions, TPS — all students respond
3. **Guided practice** (P5) — work through examples together; reduce prompts gradually
4. **Check understanding frequently** (P6) — all-learner responses, exit tickets

→ teach small → question all → practice together → verify → repeat
Tags: pedagogy rosenshine
END

START
Coding Questions
What does Rosenshine's 80% success rate principle mean in practice?
Back:
During **guided practice**, most students should succeed ~80% of the time.

If success rate is lower → scaffolding is insufficient; reduce step size or add worked examples
If success rate is near 100% → material is too easy; advance or add complexity

It is a **calibration signal** for scaffold quality, not a performance target.
Tags: pedagogy rosenshine
END

START
Coding Questions
What changed from Bloom's 1956 original to the 2001 revised taxonomy?
Back:
Two changes:

1. **Nouns → action verbs** at each level (Knowledge → Remember, Comprehension → Understand, etc.)
2. **Synthesis removed; Create moved to apex** — producing original work requires evaluative judgment, making it more cognitively demanding than Evaluate alone

The verb change matters for lesson planning: verbs force you to specify observable, measurable behaviors.
Tags: pedagogy bloom
END

START
Coding Questions
How do you write a learning objective using Bloom's Taxonomy?
Back:
Format: **"Students will be able to [Bloom verb] [content]"**

The verb signals the cognitive level and determines what kind of evidence is needed:

- "list the 4 HTTP methods" → Remember → quiz works
- "explain why TCP is stateful" → Understand → short answer
- "compare REST vs. GraphQL" → Analyze → structured comparison
- "design a rate limiter" → Create → project/mock

Wrong verbs produce wrong assessments.
Tags: pedagogy bloom
END

START
Coding Questions
What are the 3 stages of Backward Design and why does the order matter?
Back:
1. **Desired Results** — what should students know, understand, be able to do?
2. **Acceptable Evidence** — what assessments prove Stage 1 was achieved? (designed *before* lessons)
3. **Learning Plan** — only now: what instruction and activities reach Stage 1 and prepare for Stage 2?

**Why order matters:** designing assessment before activities forces alignment.
Traditional design (content → activities → maybe a test) produces disconnected lessons where activities don't trace to outcomes.
Tags: pedagogy backward-design
END

START
Coding Questions
What is "coverage-first" teaching and why is it a problem?
Back:
Teaching that selects content first, then activities, then (sometimes) a test.

**Problems:**
- Activities fill time without producing lasting understanding
- Teachers optimize for "getting through" material, not for learning
- Assessment becomes an afterthought disconnected from instruction goals

Backward Design prevents this by forcing the teacher to define *what understanding looks like* before choosing *what to do*.
Tags: pedagogy backward-design
END

START
Coding Questions
What is the ConcepTest cycle in Peer Instruction?
Back:
1. Pose a conceptual multiple-choice question targeting a known misconception
2. **Individual think** (1–2 min) — silent commitment; triggers retrieval
3. **First vote** — all students respond simultaneously (no social influence)
4. **Peer discussion** (2–3 min) — only if 30–70% correct; find someone with a different answer
5. **Re-vote** — typically shows significant improvement
6. **Instructor explanation** — reveals answer, invites student explanations

Decision rule: >85% correct → move on. <30% correct → reteach before discussion.
Tags: pedagogy peer-instruction mazur
END

START
Coding Questions
Why does a student who just learned something explain it better than an expert?
Back:
The expert can no longer remember **not knowing** — they've lost access to the confusion state.

A student who just understood has:
- Fresh memory of the specific sticking point
- Language calibrated to the confusion level
- No expert blind spots from years of automation

This is why peer discussion in ConcepTests produces explanations the instructor cannot replicate.
Tags: pedagogy peer-instruction
END

START
Coding Questions
What makes an assessment formative rather than summative?
Back:
**Not the format — the use of evidence.**

Assessment is formative when the evidence **changes what happens next** during learning.

Same quiz can be:
- **Formative:** teacher reads results, regroups by misconception, adjusts next 10 minutes
- **Summative:** teacher records grade, moves to next topic

Formative = assessment *for* learning. Summative = assessment *of* learning.
Tags: pedagogy formative-assessment wiliam
END

START
Coding Questions
What are Wiliam's 5 strategies for formative assessment?
Back:
1. **Clarify learning intentions** — share goals, show exemplars, co-construct rubrics
2. **Engineer effective discussions** — design questions that make thinking visible
3. **Feedback that moves forward** — tells students *what to do next*, not just how they did
4. **Peers as resources** — structured peer feedback, peer marking
5. **Students as owners** — self-assessment, metacognitive reflection

Strategy 3 is often misapplied: grades and scores are not formative feedback unless they specify a next action.
Tags: pedagogy formative-assessment wiliam
END

START
Coding Questions
What is a hinge question and what makes it effective?
Back:
A question at a critical lesson pivot point — the lesson **hinges** here because the teacher's next move depends entirely on the class response.

Requirements:
- Students answer in **1–2 minutes**
- Teacher reads whole-class result in **under 30 seconds**
- Multiple choice where **each wrong option reveals a specific misconception** (not just "wrong")

The diagnostic precision of wrong answers is what makes it a hinge question, not just a check question.
Tags: pedagogy formative-assessment hinge-questions
END

START
Coding Questions
What are the 6 types of Socratic questions?
Back:
1. **Conceptual clarification** — "What do you mean by that? Can you give an example?"
2. **Probing assumptions** — "What are you assuming? Could that be wrong?"
3. **Probing evidence** — "What supports this? What's a counter-example?"
4. **Exploring perspectives** — "What would someone who disagrees say?"
5. **Probing implications** — "If that were true, what would follow?"
6. **Meta questions** — "Why do you think I asked this? What does this question assume?"

Use the type that fits the current moment — don't cycle through all six sequentially.
Tags: pedagogy socratic-questioning
END

START
Coding Questions
Why is the Think step in Think-Pair-Share non-negotiable?
Back:
Without individual think time, only **already-confident students** engage.

Fast responders dominate. Slow processors never articulate their thinking.

The Think step (1–3 min, silent) forces **every** student to process before exposure to peer ideas.

Skipping it turns TPS into a discussion where one student answers and others wait passively — no different from unstructured Q&A.
Tags: pedagogy think-pair-share
END

START
Coding Questions
What are the 4 core desirable difficulties and why does each work?
Back:
1. **Spacing** — gaps let retrieval strength decay; retrieving after decay produces bigger memory gain
2. **Interleaving** — forces strategy identification before execution; builds discrimination, not just execution
3. **Retrieval Practice** — active reconstruction strengthens the memory trace; re-reading only boosts short-term fluency
4. **Generation Effect** — attempting an answer before instruction pre-activates schemas; creates curiosity gap

All four produce worse short-term performance and dramatically better long-term retention.
Tags: pedagogy desirable-difficulties bjork
END

START
Coding Questions
What is the performance–learning paradox and why must teachers communicate it?
Back:
**The paradox:** conditions that produce the best in-session performance (blocked practice, re-reading, massed repetition) produce the worst long-term retention.

**Why communicate it:** students use fluency as a proxy for learning. When interleaving or retrieval practice makes them feel less capable, they abandon the technique — not because it isn't working, but because it *is* working.

Without understanding the paradox, students self-sabotage by switching to comfortable, ineffective methods.
Tags: pedagogy desirable-difficulties bjork metacognition
END

START
Coding Questions
How does the tension between CLT and desirable difficulties resolve?
Back:
They target **different things**:

- **CLT** targets *extraneous* load — eliminate presentation noise that serves no learning purpose
- **Desirable Difficulties** target *intrinsic* load — create productive struggle through spacing, retrieval, interleaving

CLT says: don't waste capacity on bad presentation.
Desirable Difficulties say: use that freed capacity for effortful retrieval and discrimination.

They are complementary: reduce extraneous → use freed working memory for desirable difficulty operations.
Tags: pedagogy desirable-difficulties clt
END
