---
created: 2026-02-18
aliases: [NumPy Slicing, NumPy Indexing]
tags:
  - python/numpy
---

> NumPy slicing uses <mark style="background: yellow">`[rows, columns]`</mark> syntax to select parts of an array.

---

### 1D slicing

```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]      # 10        (single element)
arr[1:4]    # [20 30 40] (index 1 to 3)
```

---

### 2D slicing

```python
mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

mat[:, 1]      # [2, 5, 8]     → entire column 2
mat[1:, :2]    # [[4, 5],      → rows 1+ , columns 0-1
               #  [7, 8]]
```

The key pattern: `mat[row_range, col_range]`

- `:` alone means "all"
- `1:` means "from index 1 to end"
- `:2` means "from start to index 1"

Similar to [[iloc selects DataFrame rows and columns by integer position|Pandas iloc]] — same `[row, col]` logic.

---

Read more:
- [[NumPy provides efficient array operations for numerical computing in Python]]
- [[iloc selects DataFrame rows and columns by integer position]]
