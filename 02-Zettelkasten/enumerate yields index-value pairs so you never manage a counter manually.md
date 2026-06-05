---
created: 2026-06-04
aliases: [enumerate, index in for loop, loop with index]
tags:
  - python/core
---

Python's `for` loop gives you values, not positions. When you also need the index, the manual fix is a counter variable you increment yourself — `enumerate` <mark style="background: #FFF3A3A6;">wraps any iterable and yields `(index, value)` tuples</mark>, killing the counter entirely.

```python
# Manual counter — noise, easy to forget the += 1
i = 0
for char in "abc":
    print(i, char)
    i += 1

# enumerate — index comes with the value
for i, char in enumerate("abc"):
    print(i, char)   # 0 a → 1 b → 2 c
```

The two-variable `for i, char` is [[Python for loop unpacks tuples into multiple loop variables|tuple unpacking]] — `enumerate` yields tuples, the loop splits them.

For a Java developer: this replaces the classic `for (int i = 0; i < arr.length; i++)` indexed loop, which Python deliberately doesn't have.

---

### start parameter

Counting begins at 0 by default; <mark style="background: #BBFABBA6;">`start=` shifts the first index</mark> — handy for 1-based output like line numbers:

```python
for line_no, line in enumerate(lines, start=1):
    print(f"{line_no}: {line}")
```

---

### Lazy, like range

`enumerate` returns an iterator, not a list — it computes pairs on demand, the same trick as [[Python range computes values on demand without storing them|range]]. Wrap in `list()` only if you actually need all pairs at once.

---

### Read more

- [[Python for loop unpacks tuples into multiple loop variables]]
- [[Python for loop works with any iterable not just lists]]
- [[Python range computes values on demand without storing them]]
- [[Python MOC]]
