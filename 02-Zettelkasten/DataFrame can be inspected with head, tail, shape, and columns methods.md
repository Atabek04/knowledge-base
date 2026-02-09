After loading a dataset, use these methods to quickly explore its structure.

## View Rows

**First rows** — `df.head()` shows first 5 rows by default:

```python
df.head()      # First 5 rows
df.head(10)    # First 10 rows (specify number)
```

**Last rows** — `df.tail()` shows last 5 rows by default:

```python
df.tail()      # Last 5 rows
df.tail(8)     # Last 8 rows (specify number)
```

## Get Dimensions

**Shape** — returns `(observations, features)` as a tuple:

```python
df.shape       # Output: (1000, 5) means 1000 rows, 5 columns
```

This is a **property**, not a method — no parentheses needed.

**Length** — returns number of rows only:

```python
len(df)        # Output: 1000 (just row count)
```

Use `len(df)` when you only need row count, or `df.shape[0]` to get rows from shape tuple.

## Display All Data

**Set display options** to show all rows/columns:

```python
pd.set_option('display.max_rows', None)     # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
```

Useful for small datasets, but avoid for large ones (performance issue).

## List Column Names

**Columns** — shows all feature names:

```python
df.columns     # Output: Index(['Age', 'Income', 'City', ...])
```

Also a **property** — no parentheses.

**Data types** — shows data type of each column:

```python
df.dtypes      # Output:
               # Age        int64
               # Income     int64
               # City      object
               # dtype: object
```

"dtypes" stands for **"data types"**.
Common types: `int64`, `float64`, `object` (strings), `bool`, `datetime64`.

## View Row Labels

**Index** — shows row labels/identifiers:

```python
df.index       # Output: RangeIndex(start=0, stop=1000, step=1)
```

`RangeIndex(start=0, stop=1000, step=1)` means:
- Rows labeled: 0, 1, 2, ..., 999
- 1000 total rows (starts at 0, stops before 1000)
- Increments by 1

This is the **default index** (sequential numbers).
You can also set custom indices (dates, names, IDs).

## Get Summary Information

**Info** — shows concise summary with column names, non-null counts, and data types:

```python
df.info()      # Displays:
               # - Total rows and columns
               # - Column names with non-null counts
               # - Data types
               # - Memory usage
```

Useful for spotting missing data quickly.

**Describe** — shows statistical summary for numerical columns:

```python
df.describe()  # Shows for each numeric column:
               # - count (number of values)
               # - mean, std (standard deviation)
               # - min, 25%, 50%, 75%, max
```

Gives quick overview of data distribution and range.

---

**Links**: [[Pandas MOC]]
