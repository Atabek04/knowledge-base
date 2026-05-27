---
aliases: [GRPO, Group Relative Policy Optimization]
---

GRPO (Group Relative Policy Optimization) is the RL algorithm used to train DeepSeek-R1 and related reasoning models.

For a given prompt, the model generates a *group* of candidate responses. Each response is evaluated: did it reach the correct final answer? The model is then updated to make high-reward responses more likely and low-reward responses less likely, using the relative advantage within the group.

GRPO differs from PPO (the algorithm behind earlier RLHF) in that it does not rely on a learned value function — it estimates advantage directly from intra-group reward distribution. This simplifies training and reduces compute.

A subtle but important finding (2025 research): even though GRPO rewards only correct *final* answers, it implicitly acts as a *process* reward model. Because trajectories in the same group share overlapping prefixes, the credit assignment propagates backward through intermediate reasoning steps. The model learns to self-correct mid-chain without being explicitly rewarded for it.

This is why reasoning models learn behaviors like catching their own errors, backtracking, and trying alternative approaches — not because those behaviors were directly incentivized, but because they appear in the trajectories of correct answers.

---

### Read more

- [[Reasoning models use reinforcement learning on outcome rewards to discover thinking strategies]]
- [[Thinking tokens create a bounded scratchpad that separates deliberation from final output]]
