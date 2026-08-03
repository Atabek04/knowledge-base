---
created: 2026-06-26
aliases: [transformer, sklearn transformer]
tags:
  - ml/scikit-learn
  - ml/preprocessing
---

In scikit-learn, the objects that clean and prepare data — imputers, scalers, encoders — all share one shape. That shared shape has a name.

> A **transformer** is any scikit-learn object that reshapes data through the <mark style="background: #FFF3A3A6; font-weight: bold;">`fit` / `transform` API</mark>.

It's a kind of *estimator* (anything with [[fit() trains the model by learning parameters from training data|`.fit()`]]), specialized for processing data rather than predicting:

- <mark style="background: #ADCCFFA6;">`fit(X_train)`</mark> — learn the parameters from the data (a mean, a min/max, the set of categories)
- <mark style="background: #ADCCFFA6;">`transform(X)`</mark> — apply those learned parameters to reshape the data

This is why `SimpleImputer` and `StandardScaler` look identical to use — they're the **same API**, just learning a different statistic. (Contrast a *predictor*, whose second step is `.predict()`.)

---

### Why one shared API matters

Because every transformer exposes the same two methods, any of them <mark style="background: #D2B3FFA6;">drops into the same workflow interchangeably</mark> — including a scikit-learn `Pipeline`. You write the steps once; the data flows through each transformer's `fit`/`transform` the same way.

It also makes the [[Feature scaling must happen after train-test split to prevent data leakage|leakage rule]] universal: `fit` is always the step that *learns from data*, so it must only ever see the training set.

---

### The main categories

| Category | What it does | Examples |
|---|---|---|
| **Imputation** | fill missing values | `SimpleImputer`, `KNNImputer` |
| **Scaling** | rescale feature ranges | `StandardScaler`, `MinMaxScaler` |
| **Encoding** | categories → numbers | `OneHotEncoder`, `OrdinalEncoder` |
| **Dimensionality reduction** | fewer features | `PCA` |

---

### Read more
- [[fit() trains the model by learning parameters from training data]]
- [[SimpleImputer replaces missing values using fit and transform pattern]]
- [[Standardization centers features around zero using mean and standard deviation]]
- [[One-hot encoding creates a binary column for each category]]
- [[Feature scaling must happen after train-test split to prevent data leakage]]
- [[Scikit-learn provides ready-to-use ML algorithms and preprocessing tools]]
- [[Machine Learning MOC]]
