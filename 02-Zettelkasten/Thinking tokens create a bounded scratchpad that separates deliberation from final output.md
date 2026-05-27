---
aliases: [thinking tokens, scratchpad tokens, reasoning trace]
---

Reasoning models like DeepSeek-R1 use special delimiter tokens — `<think>` and `</think>` — to create a distinct reasoning zone inside the generation sequence.

Everything between these tokens is the model's scratchpad: intermediate steps, self-corrections, alternative approaches, partial computations. The final answer is generated after the closing token and is what gets returned to the user.

This creates two properties:

**Separation of concerns.** The model can "think out loud" without that text being treated as the final answer. It can write "wait, that's wrong" mid-scratchpad and continue — something impossible in standard generation where every token is output.

**Variable depth.** The scratchpad length adapts to problem complexity. Simple prompts: a few hundred tokens. Hard competition math: tens of thousands of tokens. The model allocates more compute where it needs it.

The scratchpad is human-readable — users can inspect the reasoning trace. However, readability is not the same as auditability. Whether the chain-of-thought faithfully represents the actual computation happening inside the model is an open research question tied to [[Mechanistic interpretability reverse-engineers neural network computations into readable circuits|mechanistic interpretability]].

---

### Read more

- [[Reasoning models use reinforcement learning on outcome rewards to discover thinking strategies]]
- [[GRPO trains reasoning models by comparing outcome rewards across sampled response groups]]
- [[Inference-time compute scaling trades token cost for accuracy on hard reasoning tasks]]
- [[Mechanistic interpretability reverse-engineers neural network computations into readable circuits]]
- [[Black-box AI models prevent auditing of decision-making processes]]
