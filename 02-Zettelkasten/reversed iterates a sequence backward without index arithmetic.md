---
created: 2026-06-04
aliases: [reversed, iterate backwards, reverse iteration]
tags:
  - python/core
---

Walking a list backward by index means the error-prone `range(len(nums) - 1, -1, -1)` incantation. When you <mark style="background: #FFF3A3A6;">only need the *values* in reverse order, `reversed()` removes the index math entirely</mark>:

```python
for n in reversed(nums):
    print(n)               # last → first

for i in range(len(nums) - 1, -1, -1):
    print(nums[i])         # same output, three chances for an off-by-one
```

---

### Lazy, not a copy

`reversed()` returns an iterator that <mark style="background: #BBFABBA6;">walks the existing sequence from the back — no reversed copy is built</mark>. Contrast the two look-alikes:

- `reversed(nums)` — lazy iterator, original untouched
- `nums[::-1]` — new reversed **list**, full copy
- `nums.reverse()` — reverses **in place**, returns `None`

Same mutate-vs-new split as [[Python sorted() returns a new sorted list while list.sort() mutates in place|sorted() vs list.sort()]].

---

### When you still need range

`reversed` gives values only. When the loop body needs the *index* — writing into another array at position `i`, comparing `nums[i]` with `nums[i+1]` — fall back to [[range takes start stop step with stop always exclusive|range with a negative step]]:

```python
for i in range(len(nums) - 2, -1, -1):
    right[i] = right[i + 1] * nums[i + 1]   # needs i, not just the value
```

Index needed → `range(..., -1, -1)`. Values only → `reversed()`.

---

### Read more

- [[range takes start stop step with stop always exclusive]]
- [[Python sorted() returns a new sorted list while list.sort() mutates in place]]
- [[Python for loop works with any iterable not just lists]]
- [[Python MOC]]
