
Pandas provides two sorting methods for DataFrames.
They sort by different criteria: column values vs. index labels.

## `sort_values()` — Sort by Column Data

Sorts rows based on values in one or more columns.

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Charlie', 'Alice', 'Bob'],
    'age': [28, 25, 30],
    'salary': [55000, 50000, 65000]
})

# Sort by single column
df.sort_values('age')           # Sorted by age: 25, 28, 30
df.sort_values(by='salary')     # 'by=' is optional

# Sort by multiple columns (priority left to right)
df.sort_values(['age', 'name'])  # First by age, then by name
```

**Note**: The `by=` parameter is optional — you can pass the column name directly.

### Sorting Order

```python
df.sort_values('age', ascending=False)  # Descending: 30, 28, 25
df.sort_values(['age', 'salary'], ascending=[True, False])  # Mixed
```

## `sort_index()` — Sort by Index Labels

Sorts rows by their index (row labels), not by data values.

```python
# After sort_values, index is out of order
df_sorted = df.sort_values('age')
print(df_sorted.index)  # [1, 0, 2] (not sequential)

# Restore index order
df_sorted.sort_index()  # Index back to [0, 1, 2]
```

Useful when:
- Index is shuffled after filtering or sorting
- Custom index needs alphabetical/chronological order
- Working with time series (date index)

## Key Difference

**`sort_values`**: "Sort by what's **in the column**"
```python
df.sort_values('age')  # 25, 28, 30
```

**`sort_index`**: "Sort by the **row label**"
```python
df.sort_index()  # Index 0, 1, 2
```

---

**Links**:
- [[Pandas MOC]]
- [[DataFrame bracket notation is more flexible than dot notation for column selection]]
