---
created: 2026-02-16
aliases: [Dummy Variable Trap, Multicollinearity]
tags:
  - ml/preprocessing
---

> The **dummy variable trap** occurs when all [[Dummy variable is a binary column created by one-hot encoding|dummy variables]] are kept — one column becomes perfectly predictable from the others. This redundancy is called **multicollinearity**.

If Emb_C = 0 and Emb_Q = 0, you already know Emb_S = 1. The third column adds no information — it confuses models (especially linear regression) because they can't tell which column is actually contributing.

### The fix

Drop one column. Two columns are enough to represent three categories:

| Emb_C | Emb_Q | Meaning |
|-------|-------|---------|
| 1     | 0     | C       |
| 0     | 1     | Q       |
| 0     | 0     | S (neither C nor Q) |

```python
OneHotEncoder(drop='first')
```

<mark style="background: green">`drop='first'` automatically removes the first dummy column, avoiding the trap.</mark>

---

Read more:
- [[Dummy variable is a binary column created by one-hot encoding]]
- [[One-hot encoding creates a binary column for each category]]
- [[Categorical data must be encoded into numbers because ML algorithms only compute with numbers]]
- [[Machine Learning MOC]]
