---
created: 2026-02-12
aliases: [iloc]
tags:
  - python/pandas
---

> `iloc` = **i**nteger **loc**ation. It selects rows and columns by their **position number** (0-based index).

It's not a method — it's a **property with bracket indexing** (an indexer). Methods use `()`, indexers use `[]`.

```python
df.iloc[row, column]
```

---

### Common patterns

```python
df.iloc[0, 2]       # row 0, column 2 (single value)
df.iloc[:, 0]       # all rows, first column
df.iloc[:, :-1]     # all rows, all columns except last
df.iloc[:, -1]      # all rows, last column only
```

`:-1` is standard Python slicing — "everything except the last element."

---

### Splitting features and target

By convention, the [[Target is the output variable the model learns to predict|target]] column is placed last. So `iloc` is commonly used to split [[X represents features and y represents target in ML notation|X and y]]:

```python
X = df.iloc[:, :-1]    # all columns except last → features
y = df.iloc[:, -1]     # last column → target
```

---

### `.values` converts to NumPy array

`iloc` returns a DataFrame (or Series). Adding `.values` strips labels and returns a raw [[NumPy provides efficient array operations for numerical computing in Python|NumPy]] array.

```python
df.iloc[:, :-1]          # → DataFrame
df.iloc[:, :-1].values   # → numpy.ndarray (just numbers)
```

Most ML libraries work with both, but NumPy arrays are lighter — no column names, no index, just the raw numbers the math runs on.

---

### iloc vs loc

| | Selects by | Example |
|---|---|---|
| `iloc[]` | **Position** (numbers) | `df.iloc[0, 2]` |
| `loc[]` | **Label** (names) | `df.loc[0, "price"]` |

---

Read more:
- [[DataFrame rows represent observations and columns represent features in machine learning]]
- [[Train-test split evaluates model performance on unseen data]]
- [[X represents features and y represents target in ML notation]]
- [[Pandas MOC]]
