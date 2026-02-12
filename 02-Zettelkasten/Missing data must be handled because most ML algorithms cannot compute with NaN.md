---
created: 2026-02-12
aliases: [Handling Missing Data, Missing Values]
tags:
  - ml/preprocessing
---

> Most ML algorithms **cannot handle missing values** — they'll either crash or produce garbage results. The math breaks when you try to compute with `NaN`.

Even if a library doesn't crash, keeping nulls causes:
- **Biased model** — missing data often isn't random (e.g. high-income people skip income fields)
- **Lost rows** — some algorithms silently drop rows with any null, shrinking your dataset

---

### Two main strategies

#### 1. Delete — remove rows or columns

```python
df.dropna()            # drop rows with any NaN
df.dropna(axis=1)      # drop columns with any NaN
```

Use when: very few values are missing (< 1-2%) and your dataset is large enough.

#### 2. Impute — replace with a substitute

```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="mean")
```

| Strategy | When to use |
|---|---|
| `mean` | Numerical, no big outliers |
| `median` | Numerical, has outliers |
| `most_frequent` | Categorical data |

Use when: you can't afford to lose rows, or missingness is significant.

<mark style="background: #FF5582A6">Never impute blindly — check **why** data is missing first. If 80% of a column is null, imputing makes it mostly fake data.</mark>

---

Read more:
- [[SimpleImputer replaces missing values using fit and transform pattern]]
- [[Mean is the sum of all values divided by the count]]
- [[Median is the middle value when data is sorted]]
- [[Feature scaling transforms features to similar ranges for efficient training]]
- [[Train-test split evaluates model performance on unseen data]]
- [[Machine Learning MOC]]
