---
created: 2026-06-04
aliases: [range arguments, range start stop step, range step]
tags:
  - python/core
---

`range` accepts one, two, or three arguments — and the only one that is always present is `stop`, which is <mark style="background: #FFF3A3A6;">always *exclusive*: the sequence stops one step before it</mark>.

```python
range(5)           # 0 1 2 3 4        — stop only, starts at 0
range(2, 5)        # 2 3 4            — start, stop
range(0, 10, 3)    # 0 3 6 9          — start, stop, step
```

For a Java developer, the three-arg form is the classic for-loop header compressed: `range(start, stop, step)` ≡ `for (int i = start; i < stop; i += step)`.

---

### Negative step — counting down

<mark style="background: #BBFABBA6;">`step=-1` walks backward</mark>; `stop` stays exclusive, just from the other side:

```python
range(3, -1, -1)   # 3 2 1 0 — stop is -1 so 0 is included
```

The pattern for traversing a list right-to-left by index:

```python
for i in range(len(nums) - 1, -1, -1):   # last index → 0
```

Reads as: start at the last index, stop *before* -1 (so 0 included), step backward. When you don't need the index at all, [[reversed iterates a sequence backward without index arithmetic|reversed]] is the cleaner tool.

<mark style="background: #FF5582A6;">With a negative step, start must be *greater* than stop</mark> — `range(0, 5, -1)` is silently empty, not an error. `step=0` does raise `ValueError`.

---

### Why stop is exclusive

`range(len(nums))` yields exactly the valid indexes of `nums` — no `-1` adjustment, no off-by-one. Exclusive stop makes length and stop the same number. Same convention as slicing: `nums[0:3]` is 3 elements.

---

### Read more

- [[Python range computes values on demand without storing them]]
- [[reversed iterates a sequence backward without index arithmetic]]
- [[Python MOC]]
