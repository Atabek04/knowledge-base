---
created: 2026-02-19
aliases: [fit method, .fit()]
tags:
  - ml/training
  - ml/scikit-learn
---

> **`.fit()` tells any scikit-learn object: "Look at this data and learn what you need from it."**

Think of it like fitting a glove to your hand — the model adjusts itself to match the shape of your data.

---

### What `.fit()` learns depends on the object

**[[SimpleImputer replaces missing values using fit and transform pattern|SimpleImputer]]** — learns the mean (or median) of each column.

**[[Standardization centers features around zero using mean and standard deviation|StandardScaler]]** — learns the mean and standard deviation of each column.

**[[Simple linear regression predicts a target using one feature and a straight line|LinearRegression]]** — learns the best [[Weights define how much each feature matters|weight]] (slope) and [[Bias adds a baseline shift to all predictions|bias]] (intercept) that fit through the data points.

---

### Usage

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

<mark style="background: pink">Always fit on training data only.</mark> Fitting on test data causes [[Feature scaling must happen after train-test split to prevent data leakage|data leakage]] — the model would "see" answers it shouldn't know.

---

### The pattern

Every scikit-learn estimator follows the same two-step pattern:

1. `.fit(data)` — learn parameters from data
2. [[predict() uses learned parameters to compute outputs for new data|.predict(data)]] or `.transform(data)` — use those parameters on new data

---

Read more:
- [[predict() uses learned parameters to compute outputs for new data]]
- [[SimpleImputer replaces missing values using fit and transform pattern]]
- [[Standardization centers features around zero using mean and standard deviation]]
- [[Simple linear regression predicts a target using one feature and a straight line]]
- [[Weights define how much each feature matters]]
- [[Bias adds a baseline shift to all predictions]]
- [[Feature scaling must happen after train-test split to prevent data leakage]]
