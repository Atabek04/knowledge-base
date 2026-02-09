
Pandas offers two ways to select columns from a DataFrame.

Bracket notation handles both single and multiple columns, while dot notation only works for single columns.

## Bracket Notation (Recommended)

Access columns using square brackets with the column name as a string.

```python
import pandas as pd

df = pd.DataFrame({
    'gender': ['M', 'F', 'M'],
    'first name': ['John', 'Jane', 'Bob'],
    'age': [25, 30, 28]
})

# Select column
gender_series = df['gender']

# Chain methods
print(df['gender'].head())
print(df['first name'].value_counts())
```

Works with **any column name** — including names with spaces, special characters, or Python keywords.

### Selecting Multiple Columns

Pass a **list of column names** inside brackets to get a DataFrame subset.

```python
# Select multiple columns (returns DataFrame, not Series)
subset = df[['gender', 'age']]

# Works with spaces and special characters
subset = df[['first name', 'age', 'gender']]

# Chain methods on the result
print(df[['age', 'gender']].head())
```

Notice the **double brackets**: outer for indexing, inner for the list.

## Return Type Matters

**Single column** returns a **Series** (1D array):
```python
df['age']        # Series
df.age           # Series (same result)
```

**Multiple columns** returns a **DataFrame** (2D table):
```python
df[['age', 'gender']]    # DataFrame (2+ columns)
df[['age']]              # DataFrame (even with 1 column!)
```

The double bracket syntax **always** returns a DataFrame, even for one column.
This affects method behavior — Series and DataFrame have different methods.

## Dot Notation (Limited)

Access columns as object attributes.

```python
# Works only for simple column names
gender_series = df.gender
print(df.age.mean())
```

**Limitations**:
- Fails for column names with **spaces** (`df.first name` → syntax error)
- Fails for column names with **special characters** (`df.user-id` → tries subtraction)
- Fails if column name matches **DataFrame method** (`df.count` → returns method, not column)
- **Cannot select multiple columns** — no syntax exists for this
- Not usable in variable-based selection

## Why Bracket Notation Wins

Bracket notation is the **standard approach** because it:
- Handles all column names consistently
- Allows dynamic column selection with variables: `df[col_name]`
- Prevents naming conflicts with DataFrame methods
- Matches standard Python dictionary syntax

Use dot notation only for quick interactive exploration, not in production code.

---

**Links**:
- [[Pandas MOC]]
- [[DataFrame can be created from arrays, dictionaries, or CSV files]]
