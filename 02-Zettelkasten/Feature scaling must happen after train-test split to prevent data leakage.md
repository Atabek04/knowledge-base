---
created: 2026-02-16
aliases: [Scaling After Split, Data Leakage]
tags:
  - ml/preprocessing
---

> Always **fit** the scaler on training data only, then **transform** both train and test sets.

If you scale before splitting, the scaler calculates mean/std (or min/max) using the entire dataset — including test data. This is called **data leakage** — information from data the model shouldn't see leaks into training.

Your test set simulates real-world unseen data. In production, you won't have future data to compute statistics from. So during training, you shouldn't either.

```python
# WRONG — scaler learns from test data too
X_scaled = scaler.fit_transform(X)
X_train, X_test = train_test_split(X_scaled)
```

```python
# CORRECT — scaler learns only from training data
X_train, X_test = train_test_split(X)
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
```

### What "fit on train only" means

- **`fit`** = learn statistics (mean, std) from the data you give it
- **`transform`** = apply those already-learned statistics to scale data
- **`fit_transform`** = both in one step

```python
sc.fit_transform(X_train)  # learns mean=50, std=10 → scales using them
sc.transform(X_test)       # uses the SAME mean=50, std=10 from training
```

<mark style="background: pink">Never `fit_transform` on test data — it would calculate new statistics from the test set. Train and test would be scaled using different reference points, breaking consistency.</mark>

Both sets must be measured with the **same ruler** — the one built from training data.

---

> This applies to any preprocessing that learns statistics from data — scaling, imputation, encoding. Always fit on train only.

---

Read more:
- [[Feature scaling transforms features to similar ranges for efficient training]]
- [[Train-test split evaluates model performance on unseen data]]
- [[SimpleImputer replaces missing values using fit and transform pattern]]
- [[Machine Learning MOC]]
