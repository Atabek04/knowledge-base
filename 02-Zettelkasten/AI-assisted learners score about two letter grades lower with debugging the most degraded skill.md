---
aliases: [Anthropic coding RCT, two-grade gap, debugging atrophy]
---

AI coding tools speed up delivery, but a controlled trial measured what they cost the *learner* — and the loss landed hardest on the one skill you most need to supervise AI.

This is the hard-data version of the general warning that [[Using AI to bypass work causes skill atrophy while using it for inquiry builds skill|bypassing the work atrophies skill]].

---

### The study

Anthropic ran a randomized controlled trial (published Jan 2026, n=52 mostly-junior engineers) where both groups learned the same unfamiliar Python library — one group hand-coding, one group AI-assisted.

On a follow-up mastery quiz the AI-assisted group averaged <mark style="background: pink">50% versus 67% for the hand-coders</mark> — roughly <mark style="background: yellow">two letter grades lower</mark> (Cohen's d ≈ 0.74, p = 0.01).

Same task, same time, same exposure. The only difference was *who did the thinking*.

---

### Debugging degraded most

The gap between the groups was <mark style="background: yellow">largest on the debugging questions</mark> — understanding *when* code is wrong and *why* it fails.

#### The supervision paradox

This is the sharp edge of the result. Debugging is exactly the skill the AI era demands *more* of, because your job shifts toward reviewing machine-written code.

<mark style="background: cyan;">The skill AI erodes fastest is the skill you most need to catch AI's mistakes.</mark>

Hand-coders build that judgment by failing and fixing; the AI group never paid that tuition.

---

### How the AI group used it decided the score

The researchers sorted the AI group by how each person interacted with the assistant. The averages split cleanly in two.

#### Patterns that scored below 40%

- **AI delegation**: let the AI write the code outright. Fastest to finish.
- **Progressive AI reliance**: started with questions, then gradually handed over all the code writing.
- **Iterative AI debugging**: pasted each error back to the AI instead of working out why it happened.

#### Patterns that scored 65% or more

- **Conceptual inquiry**: asked only conceptual questions and fixed every error themselves. The largest group, and the second fastest overall.
- **Hybrid code-explanation**: asked for code together with an explanation of it.
- **Generation-then-comprehension**: generated code, then asked follow-up questions until they understood it.

<mark style="background: #ABF7F7A6;">Asking the AI only conceptual questions and resolving errors yourself kept quiz scores near the hand-coders' level while staying almost as fast as full delegation.</mark>

<mark style="background: #FF5582A6;">Each pattern held only 2 to 7 people and the patterns were observed, not assigned, so they show a strong hint rather than a proven cause.</mark>

---

### The honest caveat

<mark style="background: pink">One small, short-horizon study</mark> — 52 people, a single library, measured immediately. It shows immediate skill *formation*, not whether the gap persists or whether deliberate review closes it.

Notably, the study is unflattering to Anthropic's own product, which cuts against hype bias.

---

### Read more
- [[Using AI to bypass work causes skill atrophy while using it for inquiry builds skill]]
- [[Experienced developers were measured 19 percent slower with AI while believing they were faster]]
- [[AI-native juniors miss the foundational knowledge that came from struggling through problems manually]]
- [[Effective AI learning removes friction from busywork and adds friction to thinking]]
- [[Ten minutes of AI help makes people give up sooner on problems they then face alone]]
- [[Routine AI assistance erodes an expert's existing skill, not only a learner's skill formation]]
- [[Agentic Engineering MOC]]

### External Resources
- [Anthropic — Does AI assistance affect coding skill development?](https://www.anthropic.com/research/AI-assistance-coding-skills)
