---
created: 2026-06-04
aliases: [tuple unpacking in for loop, loop unpacking, multiple loop variables]
tags:
  - python/core
---

When a [[Python for loop works with any iterable not just lists|for loop]] iterates over an iterable whose elements are **tuples**, you can write several variables after `for` — Python <mark style="background: #FFF3A3A6;">unpacks each tuple into those variables on every iteration</mark>.

```python
pairs = [(1, "a"), (2, "b"), (3, "c")]

for number, letter in pairs:
    print(number, letter)   # 1 a → 2 b → 3 c
```

There is no special "two-parameter for loop" — it's ordinary **tuple unpacking** (`x, y = (1, "a")`) applied once per element.

---

### Where you meet it daily

Three stdlib staples yield tuples, so they're almost always consumed with unpacking:

```python
for idx, value in enumerate(arr):       # (index, value)
for key, value in counts.items():       # (key, value)
for left, right in zip(list1, list2):   # paired elements
```

`enumerate` is the index-tracking one — see [[enumerate yields index-value pairs so you never manage a counter manually|enumerate]].

---

### Variable count must match

<mark style="background: #FF5582A6;">Python raises `ValueError` if the tuple size and variable count differ</mark> — unpacking is strict:

```python
for a, b in [(1, 2, 3)]:   # ValueError: too many values to unpack
```

A `*rest` catch-all relaxes it: `for first, *rest in rows:`.

---

### Read more

- [[Python for loop works with any iterable not just lists]]
- [[enumerate yields index-value pairs so you never manage a counter manually]]
- [[Python MOC]]
