---
created: 2026-02-19
aliases: [predict method, .predict()]
tags:
  - ml/training
  - ml/scikit-learn
---

> **`.predict()` takes new features and returns predicted targets — using the parameters the model learned during [[fit() trains the model by learning parameters from training data|.fit()]].**

You pass in features only (`X`) — no targets. The model already knows the [[Weights define how much each feature matters|weight]] and [[Bias adds a baseline shift to all predictions|bias]] from training.

---

### Usage

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)       # learn weight and bias

y_pred = model.predict(X_test)    # predict targets for new data
```

`y_pred` is an array of predicted values — one per row in `X_test`.

---

### What `.predict()` does NOT do

<mark style="background: pink">It does not tell you how accurate the model is.</mark>

It only returns predictions. To measure accuracy, you compare `y_pred` against `y_test` using evaluation metrics (R-squared, MSE, etc.) — that's a separate step.

---

### The full pattern

1. `.fit(X_train, y_train)` — learn from training data
2. `.predict(X_test)` — use what was learned on new data
3. **Evaluate** — compare `y_pred` vs `y_test` (separate step)

---

Read more:
- [[fit() trains the model by learning parameters from training data]]
- [[Simple linear regression predicts a target using one feature and a straight line]]
- [[Weights define how much each feature matters]]
- [[Bias adds a baseline shift to all predictions]]
