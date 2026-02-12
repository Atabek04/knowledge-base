---
created: 2026-02-12
aliases: [SimpleImputer, Imputer]
tags:
  - ml/preprocessing
  - python/sklearn
---

> `SimpleImputer` from [[Scikit-learn provides ready-to-use ML algorithms and preprocessing tools|sklearn]] replaces missing values with a calculated statistic (mean, median, or most frequent).

```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="mean")
```

---

### Fit → Transform pattern

This follows sklearn's universal two-step pattern:

1. **`fit(data)`** — scans the data and **learns** the statistic (e.g. calculates the [[Mean is the sum of all values divided by the count|mean]] of each column)
2. **`transform(data)`** — **applies** that learned statistic to replace `NaN` values

```python
imputer.fit(X)            # learns: col 1 mean=30, col 2 mean=50...
X = imputer.transform(X)  # replaces NaN with those learned means
```

Or combine both in one call:

```python
X = imputer.fit_transform(X)
```

---

### Watch out for column types

<mark style="background: #FF5582A6">strategy="mean" or "median" only works on numerical columns — you can't calculate a mean of "France".</mark>

Pass only the numerical columns to fit/transform:

```python
imputer.fit(X.iloc[:, 1:])              # skip categorical column 0
X.iloc[:, 1:] = imputer.transform(X.iloc[:, 1:])
```

For categorical columns, use `strategy="most_frequent"` separately or handle them with encoding.

---

### Why two separate steps?

<mark style="background: #FF5582A6">You must `fit` on training data only, then `transform` both train and test separately.</mark>

If you fit on test data too, you leak future information into your model.

```python
imputer.fit(X_train)                # learn from train only
X_train = imputer.transform(X_train)
X_test = imputer.transform(X_test)  # apply train's stats to test
```

---

Read more:
- [[Missing data must be handled because most ML algorithms cannot compute with NaN]]
- [[Scikit-learn provides ready-to-use ML algorithms and preprocessing tools]]
- [[Train-test split evaluates model performance on unseen data]]
- [[Mean is the sum of all values divided by the count]]
- [[Median is the middle value when data is sorted]]
- [[Machine Learning MOC]]
