---
created: 2026-02-12
tags:
  - ml/preprocessing
---

> **Standardization** (Z-score) centers data around 0 with standard deviation of 1.

$$x_{scaled} = \frac{x - \mu}{\sigma}$$

Where:
- $\mu$ = mean of the feature
- $\sigma$ = standard deviation of the feature

---

### When to use

<mark style="background: yellow">Preferred when your data has outliers.</mark>

Unlike [[Normalization scales features to a fixed range using min and max|normalization]], standardization doesn't bound values to a fixed range — outliers won't compress the rest of your data into a tiny interval.

---

Read more:
- [[Feature scaling transforms features to similar ranges for efficient training]]
- [[Normalization scales features to a fixed range using min and max]]
