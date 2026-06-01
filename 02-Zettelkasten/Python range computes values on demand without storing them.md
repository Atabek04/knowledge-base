---
created: 2026-06-01
aliases: [range, python range]
tags:
  - python/core
---

`range` looks like it produces a sequence of numbers, but it never stores them.
It's a lazy object that computes each value from `start`, `stop`, and `step` math on demand.

```python
for i in range(1_000_000_000):
    print(i)   # fine — no RAM explosion, each value computed as needed
```

This is safe because `range` holds only three integers internally: start, stop, step.

---

### The trap: converting range to a list

```python
list(range(1_000_000_000))   # ~36 GB — forces all values into RAM at once
```

`list()` exhausts the range eagerly, allocating every element.

---

### range vs generator

Both are lazy, but `range` supports more:

| Feature | `range` | generator |
|---------|---------|-----------|
| `len()` | ✓ | ✗ |
| Random access `range(10)[5]` | ✓ | ✗ |
| Iterate multiple times | ✓ | ✗ exhausted after first pass |
| Memory | constant | constant |

`range` is not a [[Python generator produces values one at a time on demand|generator]] — it's a dedicated sequence type with lazy evaluation built in.

---

### Read more

- [[Python generator produces values one at a time on demand]]
- [[A list holds all values in RAM even when you only process one at a time]]
- [[Python MOC]]
