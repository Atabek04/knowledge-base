---
created: 2026-02-12
aliases: [X and y notation]
tags:
  - ml/fundamentals
---

> In ML code, **X** (uppercase) = [[Feature is an input variable the model uses to make predictions|features]], **y** (lowercase) = [[Target is the output variable the model learns to predict|target]].

Features are also called **independent variables** — they don't *depend* on anything in the model.
Target is also called the **dependent variable** — it *depends* on the features.

**X** is uppercase because it's a **matrix** — multiple columns (features) and rows (observations).

**y** is lowercase because it's a **vector** — a single column of values to predict.

```python
X = df[["age", "income", "experience"]]   # matrix (many columns)
y = df["price"]                            # vector (one column)
```

This convention comes from linear algebra, where uppercase = matrix and lowercase = vector.

---

Read more:
- [[Feature is an input variable the model uses to make predictions]]
- [[Target is the output variable the model learns to predict]]
- [[Machine Learning MOC]]
