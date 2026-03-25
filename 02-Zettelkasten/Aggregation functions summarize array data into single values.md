---
created: 2026-02-18
aliases: [NumPy Aggregations]
tags:
  - python/numpy
---

> **Aggregation functions** reduce an entire array into a <mark style="background: yellow">single summary value</mark> — sum, mean, max, min.

---

### Common aggregations

```python
a = np.array([10, 20, 30, 40, 50])

a.sum()    # 150
a.mean()   # 30.0
a.max()    # 50
a.min()    # 10
a.std()    # standard deviation
```

---

### Used daily in ML for

- **Preprocessing** — computing mean for [[Standardization centers features around zero using mean and standard deviation|standardization]], min/max for [[Normalization scales features to a fixed range using min and max|normalization]]
- **Feature engineering** — summarizing groups of values
- **Evaluation** — computing [[Ordinary Least Squares minimizes the sum of squared errors to find the best-fit line|MSE]] (mean of squared errors)

---

Read more:
- [[NumPy provides efficient array operations for numerical computing in Python]]
- [[Standardization centers features around zero using mean and standard deviation]]
- [[Normalization scales features to a fixed range using min and max]]
