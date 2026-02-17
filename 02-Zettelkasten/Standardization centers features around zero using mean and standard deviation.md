---
created: 2026-02-12
aliases: [Standardization, StandardScaler, Z-score Scaling]
tags:
  - ml/preprocessing
---

> **Standardization** (Z-score) centers data around 0 with standard deviation of 1.

$$x_{scaled} = \frac{x - \mu}{\sigma}$$

Where:

$$\mu = \frac{1}{n} \sum_{i=1}^{n} x_i$$

$$\sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2}$$

- $\mu$ = mean — average of all values
- $\sigma$ = standard deviation — how spread out values are from the mean

---

### When to use

> Preferred when your data has outliers.

Unlike [[Normalization scales features to a fixed range using min and max|normalization]], standardization doesn't bound values to a fixed range — outliers won't compress the rest of your data into a tiny interval.

### How to apply with sklearn

```python
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train[:, numerical_cols] = sc.fit_transform(X_train[:, numerical_cols])
X_test[:, numerical_cols] = sc.transform(X_test[:, numerical_cols])
```

- `fit_transform(X_train)` — calculates mean and std from training data, then scales it
- `transform(X_test)` — scales test data using the **same** mean and std from training

> Never `fit_transform` on test data — that would use test statistics instead of training statistics. Always [[Feature scaling must happen after train-test split to prevent data leakage|fit on train only]].

<mark style="background: green">Only scale numerical features — leave encoded (dummy/label) columns as-is, they're already 0/1.</mark>

---

Read more:
- [[Feature scaling transforms features to similar ranges for efficient training]]
- [[Feature scaling must happen after train-test split to prevent data leakage]]
- [[Normalization scales features to a fixed range using min and max]]
- [[Scikit-learn provides ready-to-use ML algorithms and preprocessing tools]]
