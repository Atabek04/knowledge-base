When you select a column with `df['column']`, you get a **Series object** (see [[DataFrame bracket notation is more flexible than dot notation for column selection]]).

Series support **vectorized operations** — math that applies to all elements at once without explicit loops.

This is fundamentally different from Python lists.

## Arithmetic Operations

Apply operations directly to the entire column.

```python
import pandas as pd

df = pd.DataFrame({
    'age': [25, 30, 28],
    'salary': [50000, 65000, 55000],
    'price': [19.99, 29.99, 24.99]
})

# Add/subtract/multiply/divide by scalar
df['age'] + 5           # [30, 35, 33]
df['salary'] * 1.1      # 10% raise for all
df['price'] / 2         # Half price for all
df['age'] ** 2          # Square each age
```

No loops needed — operates on all values simultaneously.

## Aggregation Methods

Calculate summary statistics for the entire column.

```python
df['age'].mean()        # Average age
df['salary'].sum()      # Total salary
df['age'].max()         # Oldest person
df['age'].min()         # Youngest person
df['salary'].std()      # Standard deviation
df['age'].median()      # Middle value
```

Returns a **single scalar value**, not a Series.

### Quick Summary with `.describe()`

Get multiple statistics at once for numerical columns.

```python
df['age'].describe()    # Stats for one column
df.describe()           # Stats for all numerical columns
```

Returns: count, mean, std, min, 25%, 50% (median), 75%, max.

## Operations Between Columns

Combine multiple columns with arithmetic.

```python
df = pd.DataFrame({
    'price': [10, 20, 15],
    'quantity': [2, 3, 5],
    'discount': [0.1, 0.2, 0.15]
})

# Create new column from calculation
df['total'] = df['price'] * df['quantity']
df['final_price'] = df['price'] * (1 - df['discount'])
```

Element-wise operation — row 0 price × row 0 quantity, and so on.

## Comparison Operations

Generate boolean Series for filtering.

```python
df['age'] > 30          # [False, False, False]
df['salary'] >= 60000   # [False, True, False]
df['age'] == 28         # [False, False, True]
```

Commonly used with boolean indexing: `df[df['age'] > 30]`.

## Why Vectorized Operations Matter

**Pandas/NumPy** (vectorized):
```python
df['age'] * 2  # Fast, concise, operates on all rows
```

**Python list** (requires loop):
```python
ages = [25, 30, 28]
doubled = [x * 2 for x in ages]  # Manual iteration
```

Vectorized operations are:
- **Faster** — implemented in optimized C code
- **Cleaner** — no explicit loops
- **Standard** — expected syntax in data analysis

---

⚠️ **Note**: Pay attention! `df['column']` returns a **Series object**, not a Python list.
You're using Pandas methods, not list methods.

---

**Links**: 
- [[Pandas MOC]]
- [[Pandas provides data manipulation and analysis for tabular data in Python]]