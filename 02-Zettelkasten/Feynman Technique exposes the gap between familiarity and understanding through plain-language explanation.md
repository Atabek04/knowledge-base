---
aliases: [Feynman Technique, Feynman method]
created: 2026-05-28
tags: [learning, study-method, understanding, active-learning]
---

### What it is

The Feynman Technique is a 4-step active learning method that uses the act of explanation to expose gaps between *familiarity* with a topic and genuine *understanding* of it.

Feynman's core insight: <mark style="background: yellow">knowing the *name* of something and knowing the *thing itself* are different cognitive states.</mark>

Jargon masks the gap — you can say "TCP uses a three-way handshake for connection establishment" without understanding what is being negotiated or why three steps are necessary.

---

### The 4 steps

**Step 1 — Explain as if teaching a child**
Write everything you know about the concept in plain language, no jargon.
The constraint is clarity: if a non-expert would be confused, you have not understood it clearly enough yourself.

**Step 2 — Identify gaps**
Where your explanation falters, becomes vague, or requires jargon you cannot unpack — those are the gaps.
These are not rhetorical gaps; they are genuine holes in your schema.

**Step 3 — Return to source and fill gaps**
Go back to the textbook, documentation, or paper specifically to resolve the identified gaps.
Do not re-read everything — target only what you could not explain.

**Step 4 — Simplify and iterate**
Revise your explanation until it is clear, concrete, and jargon-free.
Optionally transmit: explain to a real person, a rubber duck, or write it as a public note.

---

### Application to technical concepts

- **System design:** Explain consistent hashing without using "ring" or "virtual nodes." Explain what a user would actually experience during a node failure.
- **Algorithms:** Explain Dijkstra's without using "greedy," "relaxation," or "priority queue." What is actually happening step-by-step?
- **Backend:** Explain eventual consistency without using "CAP theorem." What would a user actually observe?
- **Atomic notes (Zettelkasten):** Writing note titles as complete statements is a Feynman-aligned practice — you cannot write "WebSocket provides full-duplex communication over TCP" if you don't understand what full-duplex means or why TCP matters.

---

### Relation to other techniques

[[Elaborative interrogation deepens schema by asking why facts are true during study|Elaborative interrogation]] applies to individual facts ("why is X true?").

The Feynman Technique applies to whole concepts ("can I explain all of X without hiding behind the name?").

Both target the boundary between familiarity and genuine understanding. [[Metacognition regulates learning by monitoring whether study methods are actually working|Metacognition]] is what notices when you're on the wrong side of that boundary.

---

### Best workflow

Write explanations in a scratch note → convert what holds up into permanent Obsidian notes.

The permanence test: if you cannot write an atomic note with a complete-statement title, you probably haven't Feynman-d it yet.

---

Read more:
- [[Elaborative interrogation deepens schema by asking why facts are true during study]]
- [[Metacognition regulates learning by monitoring whether study methods are actually working]]
- [[Deliberate practice builds expert mental representations through focused effort at the edge of current ability]]
