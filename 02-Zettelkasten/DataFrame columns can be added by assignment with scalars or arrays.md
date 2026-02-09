Pandas creates new columns through bracket assignment.
The assignment can use a single value (scalar) or a sequence of values (array).

## Adding a Column with Scalar Value

Assign a single value — Pandas **broadcasts** it to all rows automatically.

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 28]
})

# Add column with same value for all rows
df['country'] = 'USA'
df['active'] = True
df['score'] = 0

# Result: all 3 rows get the same value
```

No need to worry about row count — the scalar repeats for every row.

## Adding a Column with Array

Assign a list or NumPy array with values for each row.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 28]
})

# Must know row count first
num_rows = len(df)  # or df.shape[0]

# Generate array with EXACT same length
df['salary'] = np.random.randint(50000, 100000, size=num_rows)
df['rating'] = [4.5, 3.8, 4.2]  # manual list
```

The array **must match the DataFrame row count** exactly.

## Why Row Count Matters

Pandas requires **length alignment** between the DataFrame and the new column array.

```python
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie']})  # 3 rows

# ✓ Works: 3 elements match 3 rows
df['age'] = [25, 30, 28]

# ✗ Error: 2 elements don't match 3 rows
df['salary'] = [50000, 60000]  # ValueError: Length mismatch

# ✓ Works: scalar broadcasts to all rows
df['country'] = 'USA'  # No length requirement
```

**Check row count before generating arrays**:
- `len(df)` — number of rows
- `df.shape[0]` — first dimension (rows)

This ensures your random data or calculated values align perfectly with existing rows.

---

**Links**:
- [[Pandas MOC]]
- [[DataFrame bracket notation is more flexible than dot notation for column selection]]
