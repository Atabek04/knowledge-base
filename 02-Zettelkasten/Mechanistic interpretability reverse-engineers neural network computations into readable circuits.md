---
aliases: [mechanistic interpretability, mech interp]
---

Mechanistic interpretability is a research program (led notably by Chris Olah and the Anthropic interpretability team) that attempts to reverse-engineer what neural networks actually compute — not just describe their behavior statistically.

The core idea: instead of asking "what does this model do in aggregate?", ask "what specific computation does this specific set of neurons perform?"

Researchers have found that models develop interpretable internal structures:
- **Features** — individual neurons or directions in activation space that reliably represent recognizable concepts (e.g. "the concept of 'dog'", "the beginning of a sentence")
- **Circuits** — groups of neurons that work together to perform a specific computation (e.g. indirect object identification in a sentence)

This is analogous to reverse-engineering a compiled binary to understand the source logic — hard, painstaking, and not yet scalable to full models.

The practical goal: if we can read a model's internal reasoning, we can verify it is doing what we intend, catch deceptive behavior, and debug failures at their root cause — not just at the output level.

Mechanistic interpretability is the field's answer to the black-box problem.

---

### Read more

- [[Black-box AI models prevent auditing of decision-making processes]]
- [[Chollet's ARC benchmark exposes the gap between pattern memorization and genuine reasoning]]
