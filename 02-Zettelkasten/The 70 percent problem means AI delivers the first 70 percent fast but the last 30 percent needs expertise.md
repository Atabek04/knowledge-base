---
aliases: [70 percent problem, the last 30 percent, house of cards code, knowledge paradox]
---

Addy Osmani (Google) gave the AI-coding gap its canonical name in Dec 2024: the **70% problem**. AI gets you most of the way there astonishingly fast — then stalls exactly where real engineering lives.

The name is the lesson: the *first* 70% is cheap; the *last* 30% is where the cost, and the expertise, concentrate.

---

### The wall non-engineers hit

Osmani's observation: <mark style="background: yellow;">"Non-engineers using AI for coding... can get 70% of the way there surprisingly quickly, but that final 30% becomes an exercise in diminishing returns."</mark>

That last 30% is edge cases, integration, security, and debugging — the parts that need a mental model of the whole system, not just the next plausible line.

#### The two-steps-back pattern

It compounds the wrong way. You ask the AI to fix a small bug; the fix looks reasonable and breaks something else. Each "fix" introduces a new fault because <mark style="background: pink;">early misunderstandings cascade</mark> and the person driving can't see where the model went off the rails.

---

### House of cards code

When someone without the expertise accepts the output uncritically, Osmani calls the result <mark style="background: yellow;">"house of cards code — it looks complete but collapses under real-world pressure."</mark>

This is the same defect as [[AI-generated code is harder to review because it looks clean even when the logic is wrong|clean-looking code whose logic is wrong]], seen from the builder's side rather than the reviewer's.

---

### The knowledge paradox

The counterintuitive twist: AI helps <mark style="background: cyan;">experienced developers *more* than beginners</mark>, the opposite of "democratization."

> "Seniors use AI to accelerate what they already know how to do. Juniors try to use AI to learn what to do."

The senior already owns the last-30% expertise and uses AI to skip the typing. The junior is missing exactly the knowledge needed to close the gap — which is why [[AI-native juniors miss the foundational knowledge that came from struggling through problems manually|AI-native juniors miss the foundations the struggle used to build]].

The hard parts — requirements, system design, edge cases — <mark style="background: green;">"still require human judgment."</mark> That judgment is what [[Verification becomes the scarce engineering skill as AI makes generating code cheap|becomes the scarce, valued skill]].

---

### Read more
- [[Verification becomes the scarce engineering skill as AI makes generating code cheap]]
- [[AI-native juniors miss the foundational knowledge that came from struggling through problems manually]]
- [[The Expert Generalist gains value as AI writes more code because fundamentals decomposition and judgment compound]]
- [[Agentic Engineering MOC]]

### External Resources
- [Addy Osmani (2024) — The 70% problem: hard truths about AI-assisted coding](https://addyo.substack.com/p/the-70-problem-hard-truths-about)
