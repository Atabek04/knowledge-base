
> Most Pandas DataFrame methods return a **new DataFrame** and leave the original unchanged.

You must reassign the result to keep changes.

## Default Behavior — Returns New Copy

Operations create a modified copy without changing the original.

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Charlie', 'Alice', 'Bob'],
    'age': [28, 25, 30]
})

# This creates new DataFrame but doesn't change df
df.sort_values('age')
print(df)  # Still in original order!

# Must reassign to keep changes
df = df.sort_values('age')
print(df)  # Now sorted
```

This applies to most methods: `sort_values()`, `drop()`, `fillna()`, `reset_index()`, etc.

## Using `inplace=True` — Modifies Original

Pass `inplace=True` to modify the DataFrame directly without reassignment.

```python
df.sort_values('age', inplace=True)  # Modifies df directly
print(df)  # Changed, no reassignment needed
```

**Common methods with `inplace` parameter**:
- `sort_values(inplace=True)`
- `drop(inplace=True)`
- `fillna(inplace=True)`
- `reset_index(inplace=True)`
- `rename(inplace=True)`
- `dropna(inplace=True)`

## Best Practice — Prefer Reassignment

Most Python developers prefer reassignment over `inplace=True`.

**Reassignment** (recommended):
```python
df = df.sort_values('age')
df = df.drop('column', axis=1)
df = df.fillna(0)
```

**Inplace** (less common):
```python
df.sort_values('age', inplace=True)
df.drop('column', axis=1, inplace=True)
df.fillna(0, inplace=True)
```

**Why reassignment is better**:
- **Clearer intent** — explicit that df is being updated
- **Easier debugging** — can inspect intermediate results
- **Method chaining** — can chain multiple operations: `df.sort_values('age').drop('col')`
- **Safer** — harder to accidentally modify shared DataFrames

Use `inplace=True` sparingly, mainly for performance in very large datasets.

---

**Links**:
- [[Pandas MOC]]
- [[DataFrame sort_values sorts by column data while sort_index sorts by row labels]]
