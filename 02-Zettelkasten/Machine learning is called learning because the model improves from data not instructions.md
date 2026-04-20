---
created: 2026-03-27
aliases: [Why machine learning]
tags:
  - ml/fundamentals
---

> It's called "machine **learning**" because the system **discovers patterns from data on its own**, instead of following human-written rules.

---

### Traditional programming vs ML

In traditional programming, a human writes explicit rules:

```
if email contains "free money" → spam
if email contains "meeting" → not spam
```

The programmer must think of every rule. Miss one? The system fails.

In machine learning, you give the system **examples** and it figures out the rules itself:

```
Input: thousands of emails labeled spam/not spam
Output: model that learned its own rules from patterns
```

<mark style="background: yellow">The "learning" is this: the model adjusts its internal parameters to get better at the task, based on the data it sees.</mark>

---

### Why "machine"

Because a **computer** does the learning — not a human.

A human provides the data and chooses the algorithm.
The machine does the pattern discovery, parameter tuning, and generalization.

---

### The learning process

1. Model sees training data
2. Makes predictions
3. Measures how wrong it is ([[Loss function - formula that measures how wrong the model is|loss function]])
4. Adjusts [[Weights define how much each feature matters|weights]] to reduce error
5. Repeats until it gets good enough

Each cycle makes the model slightly better — that's the "learning."

---

Read more:
- [[Differences of - AI, ML, DL, GenAI]]
- [[Types of ML]]
- [[Loss function - formula that measures how wrong the model is]]
- [[Weights define how much each feature matters]]
