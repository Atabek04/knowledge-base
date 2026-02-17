---
created: 2026-02-16
aliases: [Dropping Columns, Drop Columns]
tags:
  - ml/preprocessing
---

> Not every column in a dataset is useful for prediction. Columns with unique values per row (names, IDs, ticket numbers) don't generalize — the model can't learn patterns from them. Columns with too many missing values also add noise rather than signal.

Drop them before training so the model only learns from [[Feature is an input variable the model uses to make predictions|features]] that actually help.

```python
df = df.drop(columns=["Name", "Cabin", "Ticket", "PassengerId"])
```

`drop()` returns a new DataFrame without those columns. The original stays unchanged unless you reassign it.

---

Read more:
- [[Categorical data must be encoded into numbers because ML algorithms only compute with numbers]]
- [[Feature is an input variable the model uses to make predictions]]
- [[Machine Learning MOC]]
