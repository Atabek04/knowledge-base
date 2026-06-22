TARGET DECK: Tech-KB::Pedagogy::Active Learning
Tags: pedagogy active-learning self-study
**Related:** [[Learning Strategies MOC]]

---

START
Coding Questions
What did Roediger & Karpicke (2006) show about retrieval vs. re-reading?
Back:
Three conditions: SSSS (repeated study) vs. SSST (one test) vs. STTT (three tests).

- **5-minute delay:** re-study group performed best (short-term fluency)
- **1-week delay:** STTT group outperformed by ~**50%**

Short-term advantage of re-reading **reverses completely** at the week delay.

The more retrieval attempts during study, the better long-term retention — regardless of how it feels during practice.
Tags: pedagogy retrieval-practice testing-effect
<!--ID: 1782128730097-->
END

START
Coding Questions
Why does re-reading create an illusion of mastery?
Back:
Re-reading produces **familiarity** — the material feels known because it's recognized.

Familiarity ≠ retrievability. You can recognize a concept without being able to reconstruct it under exam conditions.

The illusion arises because fluent recognition *feels* like knowledge.

Retrieval practice breaks the illusion: if you can't produce it unprompted, you don't know it.
Tags: pedagogy retrieval-practice desirable-difficulties
<!--ID: 1782128730099-->
END

START
Coding Questions
What is the blank-page protocol for retrieval practice?
Back:
Before re-reading a topic:

1. Open a blank page
2. Write everything you can recall about the topic — unprompted
3. Check against the source — gaps are visible immediately
4. Study only the gaps, not the whole topic again

Forces active retrieval before passive review. Prevents re-reading from masking unknown gaps with familiarity.
Tags: pedagogy retrieval-practice study-method
<!--ID: 1782128730101-->
END

START
Coding Questions
What is the contextual interference effect in interleaved practice?
Back:
During **blocked practice:** correct strategy stays in working memory the whole block → you execute, not decide.

During **interleaved practice:** you must first **identify** the problem type, **retrieve** the right strategy, then **execute** — three operations instead of one.

This forced strategy identification is harder but builds **discrimination ability** — knowing which tool to reach for, not just how to use a tool you've already identified.
Tags: pedagogy interleaving contextual-interference
<!--ID: 1782128730104-->
END

START
Coding Questions
Why does blocked practice feel more effective than interleaving even when it isn't?
Back:
**Fluency illusion:** during blocked practice, the correct strategy is still loaded in working memory.

You feel competent because no retrieval is needed.

Researchers found this feeling "was so strong it overrode direct evidence of failure."

Interleaving forces retrieval each time → feels harder → feels less effective → IS more effective long-term.

The feeling of difficulty is the mechanism, not a side effect.
Tags: pedagogy interleaving desirable-difficulties
<!--ID: 1782128730106-->
END

START
Coding Questions
When should you use blocked practice and when interleaved?
Back:
**Blocked first:** when you have zero familiarity with a problem type — 3–5 problems to build minimal schema.

**Interleaved after:** once you have basic familiarity with each type → mix them to build discrimination.

Pure beginners need schema before they can benefit from discrimination pressure. Interleaving with no schema produces confusion, not learning.

Rule: short blocked acquisition → interleaved consolidation.
Tags: pedagogy interleaving blocked-practice
<!--ID: 1782128730109-->
END

START
Coding Questions
How do you apply interleaving to LeetCode practice?
Back:
**Don't do:** 50 array problems → 50 two-pointer → 50 graph (blocked by category).

**Do this:**
- Use topic groupings for short blocked phase (3–5 problems per pattern)
- Then switch to cross-topic mixed sessions
- One session: one sliding window + one BFS + one binary search variant

This forces pattern *recognition* (which pattern applies here?) not just pattern *execution* (execute sliding window).

Recognition is the skill tested in real interviews.
Tags: pedagogy interleaving dsa leetcode
<!--ID: 1782128730111-->
END

START
Coding Questions
What is the core question of elaborative interrogation?
Back:
**"Why does this work? Why would this be the case?"**

Not: "What is X?" (recall)
Not: "How does X work?" (mechanism)
But: "Why does X work this way and not another way?"

Forces the learner to connect a new fact to their existing schema — creating multiple retrieval pathways rather than an isolated node.
Tags: pedagogy elaborative-interrogation study-method
<!--ID: 1782128730113-->
END

START
Coding Questions
Why does the quality of elaboration matter in elaborative interrogation?
Back:
Generating **any** answer is not enough — the answer must invoke **relevant prior knowledge**.

An accurate "why" that connects to existing schema → creates genuine retrieval pathways.
A vague or incorrect "why" → creates false connections or none.

Implication: learners with richer schemas get **more** out of this technique — more prior knowledge available to connect to.

Beginners need more guided elaboration; experts can self-interrogate more effectively.
Tags: pedagogy elaborative-interrogation
<!--ID: 1782128730115-->
END

START
Coding Questions
What are the 4 steps of the Feynman Technique?
Back:
1. **Explain as if teaching a child** — plain language, no jargon; struggle reveals gaps
2. **Identify gaps** — where explanation falters, becomes vague, or requires unexplained jargon
3. **Return to source** — go back only to fill the identified gaps (not re-read everything)
4. **Simplify and iterate** — revise until clear, concrete, jargon-free; optionally transmit to a real person

The cycle repeats until you can explain without any jargon you cannot unpack.
Tags: pedagogy feynman-technique study-method
<!--ID: 1782128730118-->
END

START
Coding Questions
What is the core distinction between knowing a name and knowing a thing?
Back:
Knowing the **name**: you can say "TCP uses a three-way handshake for connection establishment."

Knowing the **thing**: you can explain what is being negotiated in each step, why three steps are necessary, and what would break if one step were skipped.

Jargon masks the gap — fluent use of terminology gives the appearance of understanding.

The Feynman Technique forces decomposition until you hit primitives you genuinely understand.
Tags: pedagogy feynman-technique metacognition
<!--ID: 1782128730120-->
END

START
Coding Questions
What are Flavell's two components of metacognition?
Back:
**Component 1 — Metacognitive Knowledge**
What you know *about* learning:
- *Person:* your strengths, weaknesses, prior knowledge
- *Task:* some tasks are harder than others; recall is harder than recognition
- *Strategy:* which study methods work and when

**Component 2 — Metacognitive Regulation**
Active control of your own cognitive processes:
- *Planning:* selecting strategies, setting goals before studying
- *Monitoring:* "Do I actually understand this or just recognize it?"
- *Evaluation:* "Could I reproduce this? Where did I go wrong?"
Tags: pedagogy metacognition flavell
<!--ID: 1782128730123-->
END

START
Coding Questions
What is the metacognitive explanation for the Dunning-Kruger effect?
Back:
The skills required to **perform** a task well are the **same skills** required to **evaluate** whether you performed it well.

Incompetence prevents recognition of incompetence.

Those at the 12th percentile believed they were performing at the 62nd percentile (Kruger & Dunning, 1999).

**Critical finding:** training in the skill simultaneously improved both performance AND metacognitive accuracy — you break the trap by practicing more deliberately, not by trying to think more clearly in the abstract.
Tags: pedagogy metacognition dunning-kruger
<!--ID: 1782128730125-->
END

START
Coding Questions
What is familiarity bias in self-study and how do you counter it?
Back:
**Familiarity bias:** testing comprehension immediately after reading — short-term memory makes everything feel known.

The material is still in working memory, so retrieval feels effortless. This is not long-term retention.

**Counter:** wait at least 30 minutes after reading before testing yourself.

Better: use spaced intervals (next day, 3 days, 1 week) so retrieval is genuinely effortful.
Tags: pedagogy metacognition retrieval-practice
<!--ID: 1782128730127-->
END

START
Coding Questions
What are the three levels of practice in Ericsson's hierarchy?
Back:
| Level | Description | Outcome |
|---|---|---|
| **Naive** | Repeat what you already know, comfortably | Plateau — skill may degrade |
| **Purposeful** | Focused goals, outside comfort zone, with feedback — but no established training method | Improvement, inefficient |
| **Deliberate** | Purposeful practice within an established training methodology | Maximum skill development |

Most people plateau at naive practice and call it "10,000 hours of experience."
Tags: pedagogy deliberate-practice ericsson
<!--ID: 1782128730130-->
END

START
Coding Questions
What are mental representations and why do they determine the gap between junior and senior engineers?
Back:
**Mental representations** are internal cognitive structures that allow experts to rapidly perceive patterns, anticipate consequences, and respond to novel situations.

Built through deliberate practice at the edge of ability — not through repeating comfortable tasks.

**Junior → Senior gap:** not primarily tool knowledge.
Primarily the richness of mental representations of:
- Common system patterns and their failure modes
- Design trade-offs under real constraints
- Code smell recognition at a glance

You cannot build these by re-doing problems you already know how to solve.
Tags: pedagogy deliberate-practice ericsson
<!--ID: 1782128730132-->
END

START
Coding Questions
What did Ericsson actually find about 10,000 hours vs. Gladwell's claim?
Back:
**Ericsson found:** elite performers had ~10,000 hours of **deliberate** practice — structured, feedback-rich, at the edge of ability.

**Gladwell claimed:** 10,000 hours of any practice produces expertise.

**Ericsson publicly disputed this.**

A 2014 meta-analysis found deliberate practice accounts for:
- 26% of skill variation in chess
- 21% in music
- 18% in sports

Significant, but genetics, starting age, and domain structure also matter. Quality, not quantity, is the lever.
Tags: pedagogy deliberate-practice ericsson
<!--ID: 1782128730135-->
END

START
Coding Questions
What are the 4 elements of a well-designed deliberate practice session?
Back:
1. **Specific goal** — not "study graphs"; "implement Dijkstra's from memory, identify exactly where I get stuck on priority queue init"
2. **Edge of ability** — problems one level above current solved rate, no hints
3. **Immediate feedback** — compare to optimal solution; note complexity gap; read editorial for pattern name
4. **Full focus** — 25-min Pomodoro, one problem, no music, no multitasking

Without all four: it's purposeful practice at best, naive practice at worst.
Tags: pedagogy deliberate-practice ericsson
<!--ID: 1782128730137-->
END
