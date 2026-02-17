---
created: 2026-02-16
aliases: [Dummy Variable, Dummy Variables]
tags:
  - ml/preprocessing
---

> A **dummy variable** is a binary (0/1) column that represents one category. It's just the statistics term for what [[One-hot encoding creates a binary column for each category|one-hot encoding]] creates.

When you OHE a column like Embarked (C, Q, S), you get three dummy variables:

| Emb_C | Emb_Q | Emb_S |
|-------|-------|-------|
| 1     | 0     | 0     |
| 0     | 0     | 1     |
| 0     | 1     | 0     |

Each column is a dummy variable — it "represents" one category with 0 or 1.

<mark style="background: pink">Keeping all dummy columns can cause the [[Dummy variable trap is multicollinearity from redundant one-hot encoded columns|dummy variable trap]].</mark>

---

Read more:
- [[One-hot encoding creates a binary column for each category]]
- [[Dummy variable trap is multicollinearity from redundant one-hot encoded columns]]
- [[Categorical data must be encoded into numbers because ML algorithms only compute with numbers]]
- [[Machine Learning MOC]]
