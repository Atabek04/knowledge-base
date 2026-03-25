NumPy is the fundamental package for **numerical computing** in Python.

## Primary Purpose

NumPy provides the **ndarray** (n-dimensional array) — a fast, memory-efficient container for large datasets.

Unlike Python lists, NumPy arrays:
- Store elements of **one data type only** (homogeneous)
- Enable **vectorized operations** (apply operations to entire arrays without loops)
- Are **50-100x faster** than Python lists for numerical computations

## Common Use Cases

**Mathematical operations**: Element-wise addition, multiplication, trigonometry on arrays.

**Array manipulation**: Reshape, slice, stack, split arrays efficiently.

**Random number generation**: Create arrays of random values for simulations.

**Foundation for other libraries**: Pandas, scikit-learn, TensorFlow all build on NumPy arrays.

## Example

```python
import numpy as np

# Create array
arr = np.array([1, 2, 3, 4])

# Vectorized operation (no loop needed!)
result = arr * 2  # [2, 4, 6, 8]
```

---

Read more:
- [[NumPy exists because Python lists are too slow for numerical computing]]
- [[Pandas provides data manipulation and analysis for tabular data in Python]]
