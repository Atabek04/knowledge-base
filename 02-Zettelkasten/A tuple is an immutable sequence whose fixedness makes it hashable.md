---
created: 2026-06-04
aliases: [tuple, tuple vs list, immutable sequence]
tags:
  - python/core
---

Python has two ordered sequences: `list` and `tuple`. They look almost identical — indexing, slicing, iteration all work the same. The whole difference is one property: <mark style="background: #FFF3A3A6;">a tuple cannot be changed after creation — no append, no item assignment, no removal</mark>.

```python
nums = [1, 2]      # list — mutable
nums[0] = 9        # fine
nums.append(3)     # fine

point = (1, 2)     # tuple — immutable
point[0] = 9       # TypeError
point.append(3)    # AttributeError — method doesn't exist
```

For a Java developer: a tuple is closest to `List.of(...)` — a fixed, unmodifiable sequence.

---

### Immutability is what makes it hashable

A dict key must be **hashable** — its hash must stay constant for the lifetime of the dict, or lookups break. <mark style="background: #8ED1FCA6;">Mutation would change the hash, so Python makes mutable collections unhashable and immutable ones hashable</mark>:

```python
{(1, 2): "ok"}     # tuple as dict key — works
{[1, 2]: "no"}     # TypeError: unhashable type: 'list'
```

This is *the* practical reason tuples exist as a separate type — coordinates, (row, col) grid positions, composite keys.

---

### Tuples as lightweight records

A tuple's positions carry meaning — `("Alice", 30)` is a name *and* an age, not just two values. That's why stdlib functions return tuples: `dict.items()` yields `(key, value)` pairs, `enumerate` yields `(index, value)`. Consumed with [[Python for loop unpacks tuples into multiple loop variables|tuple unpacking]], positions get names back:

```python
for name, age in people:
```

---

### Converting between them

Each type's constructor accepts the other — <mark style="background: #BBFABBA6;">`list(t)` makes a mutable copy, `tuple(l)` freezes one</mark>:

```python
list((1, 2, 3))    # [1, 2, 3] — now mutable
tuple([1, 2, 3])   # (1, 2, 3) — now hashable
```

---

### Read more

- [[Python for loop unpacks tuples into multiple loop variables]]
- [[dict keys values and items return live views not lists]]
- [[Python MOC]]
