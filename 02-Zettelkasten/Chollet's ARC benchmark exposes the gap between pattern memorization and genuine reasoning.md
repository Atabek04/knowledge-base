---
aliases: [ARC benchmark, ARC-AGI, Chollet ARC]
---

François Chollet (creator of Keras) published the Abstraction and Reasoning Corpus (ARC) in 2019 as a direct challenge to the claim that LLMs reason.

ARC tasks show a human a small set of input-output grid examples — typically 3–5 — and ask them to infer the transformation rule and apply it to a new input. Humans solve most tasks in seconds. GPT-4 fails the majority.

The key property: each task requires novel generalization from minimal examples, not retrieval from a training distribution.

Chollet's argument: LLMs succeed by compressing and interpolating patterns from enormous training sets. That is not the same as reasoning — it is sophisticated memorization. ARC measures the boundary.

A 7-year-old with no prior exposure to a task category can solve ARC tasks intuitively. Trillion-parameter models struggle because they are optimized for pattern matching, not for building abstract models of new problems.

ARC-AGI became a public benchmark. Solving it convincingly is Chollet's proposed criterion for genuine general reasoning.

---

### Read more

- [[Searle's Chinese Room shows that symbol manipulation without understanding cannot constitute thought]]
- [[LeCun argues LLMs lack world models needed for general intelligence]]
- [[Gary Marcus argues deep learning lacks compositionality required for systematic generalization]]
