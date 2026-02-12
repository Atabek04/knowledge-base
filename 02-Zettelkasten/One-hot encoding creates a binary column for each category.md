---
created: 2026-02-12
aliases: [One-Hot Encoding, OneHotEncoder]
tags:
  - ml/preprocessing
---

> **One-hot encoding** creates a separate binary column (0 or 1) for each category.
> The name comes from digital electronics — exactly **one** bit is "**hot**" (1) and all others are "cold" (0).

| France | Germany | Spain |
|---|---|---|
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 1 |

No fake ordering. The model treats each category independently.

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(
    transformers=[("encoder", OneHotEncoder(), [0])],
    remainder="passthrough"
)
X = ct.fit_transform(X)
```

---

### Breaking down ColumnTransformer

#### transformers

`transformers` takes a **list of tuples**, each with 3 elements:

```python
transformers=[("name", TransformerObject, columns)]
```

| Element           | What it is                                                                         | In our case                              |
| ----------------- | ---------------------------------------------------------------------------------- | ---------------------------------------- |
| `"encoder"`       | Identifier for debugging — used to inspect via `ct.named_transformers_["encoder"]` | Just a name — could be `"ohe"`, anything |
| `OneHotEncoder()` | The transformer to apply                                                           | The class that does the encoding         |
| `[0]`             | Which column(s) to transform                                                       | Column at index 0 (Country)              |
#### remainder

`remainder="passthrough"` — keep all columns you didn't specify (Age, Salary stay untouched). Without it, they'd be **dropped**.

---

### When to use

Use for categories with **no natural order** — which is most cases (countries, colors, product types).

For ordered categories (low/medium/high), [[Label encoding assigns an integer to each category|label encoding]] is simpler and appropriate.

---

Read more:
- [[Categorical data must be encoded into numbers because ML algorithms only compute with numbers]]
- [[Label encoding assigns an integer to each category]]
- [[Machine Learning MOC]]
