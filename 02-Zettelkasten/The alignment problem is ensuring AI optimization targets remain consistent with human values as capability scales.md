---
aliases: [alignment problem, AI alignment]
---

The alignment problem is the core technical and philosophical challenge in AI safety: how do you ensure that what an AI system optimizes for remains consistent with what humans actually want — especially as the system becomes more capable?

It breaks into three distinct sub-problems:

**Value specification.** Human values are complex, contextual, and partly unconscious. Translating them into a precise objective function is unsolved. Any specification that misses an edge case becomes a loophole that a capable optimizer will exploit — maximally and literally.

**Value stability.** Even if the initial goal is correct, a system that improves itself or operates over time may drift from the original specification. Ensuring the optimization target remains stable under self-modification is an open problem.

**Verification.** We cannot currently inspect what goal a trained model has actually internalized. The model's stated behavior may diverge from its learned optimization target — especially under distribution shift or in novel situations. The black-box problem makes this impossible to audit reliably.

The stakes scale with capability. A misaligned calculator is harmless. A misaligned system with superhuman planning and resource acquisition is not.

Hinton estimates >50% probability of catastrophic outcome from misaligned AI within 20 years. Bengio estimates ~20%. A 2022 survey of AI researchers found the majority put the probability of AI-caused existential catastrophe above 10% — and considered it a global priority.

---

### Read more

- [[Instrumental convergence means sufficiently capable goal-seeking systems develop self-preservation sub-goals regardless of their original objective]]
- [[The paperclip maximizer illustrates how any terminal goal pursued without constraint conflicts with human survival]]
- [[Black-box AI models prevent auditing of decision-making processes]]
- [[Mechanistic interpretability reverse-engineers neural network computations into readable circuits]]
