The `.value_counts()` method shows **how many times each unique value appears** in a column.

```python
import pandas as pd

df = pd.DataFrame({
    'gender': ['M', 'F', 'M', 'F', 'M'],
    'city': ['NYC', 'LA', 'NYC', 'Chicago', 'LA']
})

df['gender'].value_counts()
# M    3
# F    2

df['city'].value_counts()
# NYC        2
# LA         2
# Chicago    1
```

Returns a **Series** sorted by frequency (most common first).

## Normalize Parameter

Use `normalize=True` to get **proportions** instead of counts.

```python
df['gender'].value_counts(normalize=True)
# M    0.6  (60%)
# F    0.4  (40%)
```

Values sum to 1.0 — useful for percentages.

## Not the Same as `.count()`

- `.count()` — total rows (5)
- `.value_counts()` — frequency per value (M: 3, F: 2)

---

**Links**:
- [[Pandas MOC]]
- [[DataFrame columns support vectorized mathematical operations]]
