---
aliases: [reasoning models, o1 o3 training, RL reasoning]
---

OpenAI's o1/o3 and DeepSeek-R1 are not fundamentally different architectures from GPT-4 or Claude — they are the same transformer base, trained differently.

The key change is the training signal. Standard LLMs are trained on next-token prediction (imitate human text). Reasoning models are trained with reinforcement learning (RL): the model is rewarded for producing *correct final answers*, not for imitating any particular reasoning style.

The model generates a hidden chain-of-thought, arrives at an answer, receives a reward signal (correct/incorrect), and RL updates the policy to make successful reasoning paths more likely.

What makes this significant: the thinking strategies inside the scratchpad were not designed by engineers. They emerged from RL. For example, o3 independently discovered the strategy of writing a brute-force solution first, then using it to verify a more optimized solution — a technique found in competitive programming that no one explicitly taught the model.

This is different from CoT prompting, where the model imitates reasoning form from training data. Here, RL selects for strategies that *work*, regardless of whether they resemble human reasoning.

---

### Read more

- [[GRPO trains reasoning models by comparing outcome rewards across sampled response groups]]
- [[Thinking tokens create a bounded scratchpad that separates deliberation from final output]]
- [[Chain-of-thought prompting uses model output as a working memory scratchpad]]
- [[Autoregressive token prediction generates responses in a single forward pass without deliberation]]
