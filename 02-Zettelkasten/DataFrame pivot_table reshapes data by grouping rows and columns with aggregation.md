
Pandas provides two methods to reshape long-format data into cross-tabulated format: `pivot()` and `pivot_table()`.

The key difference is **aggregation** — whether duplicate combinations need to be summarized.

## `pivot()` — Reshape Without Aggregation

Use when you have **unique** index/column combinations.
Simply reorganizes existing data without calculations.

### Example: Product Prices by Date

```python
import pandas as pd

# Clean data - each date+product combination appears once
prices = pd.DataFrame({
    'date': ['2024-01', '2024-01', '2024-02', '2024-02'],
    'product': ['Laptop', 'Phone', 'Laptop', 'Phone'],
    'price': [1000, 500, 1050, 520]
})

#      date  product  price
# 0  2024-01  Laptop   1000
# 1  2024-01   Phone    500
# 2  2024-02  Laptop   1050
# 3  2024-02   Phone    520

# Reshape into cross-tabulated format
pivot = prices.pivot(
    index='date',       # Rows
    columns='product',  # Columns
    values='price'      # Values to display
)

print(pivot)
```

### Result

```
product   Laptop  Phone
date
2024-01     1000    500
2024-02     1050    520
```

Just reorganizes the data — no aggregation needed.

### Syntax

```python
df.pivot(
    index='column_for_rows',
    columns='column_for_columns',
    values='column_to_display'
)
```

**No `aggfunc` parameter** — assumes unique combinations.

## `pivot_table()` — Reshape With Aggregation

Use when you have **duplicate** combinations that need to be aggregated.
Handles multiple entries by summarizing them (sum, mean, count, etc.).

### Example: Sales Transactions by Salesperson

```python
import pandas as pd

# Messy data - multiple transactions per person+product
sales = pd.DataFrame({
    'salesperson': ['Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Bob'],
    'product': ['Laptop', 'Phone', 'Laptop', 'Phone', 'Tablet', 'Tablet'],
    'region': ['North', 'North', 'South', 'South', 'North', 'South'],
    'amount': [1000, 500, 1200, 600, 800, 750]
})

#   salesperson  product  region  amount
# 0       Alice   Laptop   North    1000
# 1       Alice    Phone   North     500
# 2         Bob   Laptop   South    1200
# 3         Bob    Phone   South     600
# 4       Alice   Tablet   North     800
# 5         Bob   Tablet   South     750

# Aggregate sales per person per product
pivot = sales.pivot_table(
    values='amount',           # What to aggregate
    index='salesperson',       # Rows
    columns='product',         # Columns
    aggfunc='sum'             # How to aggregate
)

print(pivot)
```

### Result

```
product     Laptop  Phone  Tablet
salesperson
Alice         1000    500     800
Bob           1200    600     750
```

Summarizes multiple transactions into totals per person/product.

### Syntax

```python
df.pivot_table(
    values='column_to_aggregate',
    index='column_for_rows',
    columns='column_for_columns',
    aggfunc='sum'  # or 'mean', 'count', 'max', etc.
)
```

**Common aggregation functions**:
- `'sum'` — total
- `'mean'` — average
- `'count'` — number of entries
- `'max'` / `'min'` — highest/lowest value

### Multiple Dimensions

You can use multiple columns for hierarchical grouping.

```python
pivot = sales.pivot_table(
    values='amount',
    index=['salesperson', 'region'],  # Multi-level rows
    columns='product',
    aggfunc='sum'
)
```

## Comparison: `pivot()` vs `pivot_table()`

| Feature | `pivot()` | `pivot_table()` |
|---------|-----------|-----------------|
| **Aggregation** | No | Yes (`aggfunc` parameter) |
| **Handles duplicates** | No — errors if duplicates exist | Yes — aggregates them |
| **Use case** | Unique, clean data | Real-world data with duplicates |
| **Speed** | Faster (no calculation) | Slower (aggregation overhead) |
| **Flexibility** | Simple reshaping only | Can summarize and reshape |

### When Each Works

```python
# Unique data - both work
clean = pd.DataFrame({
    'date': ['2024-01', '2024-01'],
    'product': ['A', 'B'],  # No duplicates
    'price': [100, 200]
})

clean.pivot(index='date', columns='product', values='price')        # ✓
clean.pivot_table(index='date', columns='product', values='price')  # ✓

# Duplicate data - only pivot_table works
messy = pd.DataFrame({
    'person': ['Alice', 'Alice', 'Bob'],
    'product': ['Laptop', 'Laptop', 'Phone'],  # Alice+Laptop twice!
    'sales': [1000, 1200, 600]
})

messy.pivot(index='person', columns='product', values='sales')  # ✗ Error!
messy.pivot_table(index='person', columns='product', values='sales', aggfunc='sum')  # ✓
```

**Rule of thumb**: Use `pivot()` only when certain there are no duplicates.
For most real-world data, use `pivot_table()`.

---

**Links**:
- [[Pandas MOC]]
- [[DataFrame columns support vectorized mathematical operations]]
