---
created: 2026-02-18
aliases: [Broadcasting]
tags:
  - python/numpy
---

> **Broadcasting** lets NumPy <mark style="background: yellow">automatically expand smaller arrays</mark> to match the shape of larger arrays during operations.

---

### Example

```python
a = np.array([1, 2, 3])
b = 5

a + b    # [6, 7, 8]
```

`b` is a scalar, `a` is an array of 3 elements. NumPy "broadcasts" `b` to `[5, 5, 5]` internally, then adds element-wise.

---

### 2D example

```python
mat = np.array([[1, 2, 3],
                [4, 5, 6]])    # shape (2, 3)

row = np.array([10, 20, 30])   # shape (3,)

mat + row
# [[11, 22, 33],
#  [14, 25, 36]]
```

NumPy stretches `row` to match each row of `mat` — no manual looping or copying.

---

Read more:
- [[Vectorized operations apply math to entire arrays without loops]]
- [[NumPy provides efficient array operations for numerical computing in Python]]
