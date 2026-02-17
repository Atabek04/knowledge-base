---
created: 2026-02-12
aliases: [Target, Label, Dependent Variable]
tags:
  - ml/fundamentals
---

> **Target** (also called **label** or **dependent variable**) = the output value the model learns to predict.

It's the opposite of a [[Feature is an input variable the model uses to make predictions|feature]]. Features are what goes **in**, target is what comes **out**.

It's called "dependent" because its value *depends* on the features (independent variables).

- Predicting house price → target: **price**
- Spam detection → target: **spam or not spam**
- Image recognition → target: **cat or dog**

In code, the convention is `X` for features and `y` for target.

---

### Regression vs Classification

The target type determines the problem type:

- **Continuous** target (e.g. price, temperature) → regression
- **Categorical** target (e.g. spam/not spam, cat/dog) → classification

---

Read more:
- [[Feature is an input variable the model uses to make predictions]]
- [[X represents features and y represents target in ML notation]]
- [[Machine Learning MOC]]
