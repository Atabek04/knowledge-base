---
created: 2026-02-12
aliases: [Data Splitting to Train and Test Set]
tags:
  - ml/evaluation
---

> **Train-Test Split** (or **Data Partitioning**) divides your dataset so the model is tested on data it has never seen.

---

### Why split

- Prevent overfitting — test on unseen data
- Evaluate real-world performance
- Ensure model generalizes beyond training examples

If the model trains on data it will later see, it memorizes answers instead of learning patterns — like a student given exam questions before the test.

---

### Popular split ratios

- **80/20** — 80% train, 20% test
- **70/30** — for smaller datasets
- **60/20/20** — train/validation/test (when tuning hyperparameters)

### How to split with sklearn

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

- `test_size=0.2` → 20% for testing, 80% for training
- `random_state=42` → fixes the random shuffle so results are [[random_state is a seed that makes random operations reproducible|reproducible]]

Always split **before** preprocessing (scaling, imputation). 
[[Feature scaling must happen after train-test split to prevent data leakage|Fit on train only]] to avoid data leakage.

---

Read more:
- [[Machine learning follows five stages from problem framing to deployment]]
- [[Feature is an input variable the model uses to make predictions]]
- [[iloc selects DataFrame rows and columns by integer position]]
- [[random_state is a seed that makes random operations reproducible]]
- [[Feature scaling must happen after train-test split to prevent data leakage]]]
