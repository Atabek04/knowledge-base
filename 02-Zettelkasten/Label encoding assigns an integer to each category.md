---
created: 2026-02-12
aliases: [Label Encoding, LabelEncoder]
tags:
  - ml/preprocessing
---

> **Label encoding** assigns a unique integer to each category.

| Country | Encoded |
|---|---|
| France | 0 |
| Germany | 1 |
| Spain | 2 |

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
X[:, 0] = le.fit_transform(X[:, 0])
```

---

### The ordering problem

The model might think `Germany (1) < Spain (2)`, implying an order that doesn't exist.

Use label encoding when:

**1. The category has a natural order:**

| Size | Encoded |
|---|---|
| Small | 0 |
| Medium | 1 |
| Large | 2 |

Here `Small < Medium < Large` is real — the model should know this.

**2. Binary target variable (Yes/No):**

| Purchased | Encoded |
|---|---|
| No | 0 |
| Yes | 1 |

The ordering problem doesn't apply — there are only 2 values, and 0/1 is exactly what the model needs.

For **unordered features with 3+ categories**, use [[One-hot encoding creates a binary column for each category|one-hot encoding]] instead.

---

Read more:
- [[Categorical data must be encoded into numbers because ML algorithms only compute with numbers]]
- [[One-hot encoding creates a binary column for each category]]
- [[Machine Learning MOC]]
