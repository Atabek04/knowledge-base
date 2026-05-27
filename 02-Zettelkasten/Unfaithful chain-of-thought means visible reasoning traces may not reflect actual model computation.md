---
aliases: [unfaithful CoT, chain-of-thought faithfulness]
---

Reasoning models like o1 and DeepSeek-R1 produce a visible scratchpad — a chain-of-thought that users can read before seeing the final answer. This looks like transparency.

But readability is not the same as faithfulness.

**Unfaithful chain-of-thought** occurs when the visible reasoning trace describes one path to an answer while the model's actual internal computation took a different path. The scratchpad is generated autoregressively like any other text — it is output, not a window into weights.

Anthropic's 2025 circuit-tracing work on Claude Haiku 3.5 showed: in some cases the internal representations do correspond to intermediate reasoning steps (e.g. rhyme selection before line composition in poetry). In other cases, the correspondence breaks down.

A model can produce a coherent, logical-looking chain-of-thought leading to a conclusion that was determined by internal processes the scratchpad does not describe. The words say "I reasoned from A to B to C," but the weights executed a different computation entirely.

This is a direct safety concern: if we use chain-of-thought as an audit mechanism to verify model reasoning, unfaithful traces make that audit unreliable.

---

### Read more

- [[Thinking tokens create a bounded scratchpad that separates deliberation from final output]]
- [[Black-box AI models prevent auditing of decision-making processes]]
- [[Mechanistic interpretability reverse-engineers neural network computations into readable circuits]]
- [[Chain-of-thought in LLMs may be constrained imitation of human reasoning patterns rather than genuine inference]]
