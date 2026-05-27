---
aliases: [autoregressive prediction, next-token prediction]
---

Standard LLMs generate output by predicting one token at a time, left to right, based on all preceding tokens.

Each token is committed as it is generated. The model cannot go back, reconsider, or revise an earlier decision — the context window accumulates and becomes the input for the next prediction, but nothing is erased or rethought.

This architecture has a critical weakness for multi-step reasoning: if the model starts down a wrong path in token 10, every subsequent token is conditioned on that error. There is no mechanism to detect and abort the wrong trajectory.

This is why standard LLMs fail reliably on problems requiring more than one logical step — not because they lack knowledge, but because their generation process has no deliberation phase baked in.

Reasoning models (o1, o3, DeepSeek-R1) address this by introducing an explicit thinking phase before final output generation.

---

### Read more

- [[Chain-of-thought prompting uses model output as a working memory scratchpad]]
- [[Reasoning models use reinforcement learning on outcome rewards to discover thinking strategies]]
- [[Turing Test replaces the question of machine thinking with behavioral indistinguishability]]
