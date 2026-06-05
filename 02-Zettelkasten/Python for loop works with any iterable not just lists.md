---
created: 2026-06-01
aliases: [python for loop, iterable, iterator protocol]
tags:
  - python/core
---

`for` doesn't care about lists specifically. It only requires the object to be **iterable** — able to hand out values one at a time.

Python checks under the hood: *"does this implement `__iter__` and `__next__`?"* If yes, it works.

```python
for n in [1, 2, 3]:      # list
for n in (1, 2, 3):      # tuple
for n in "abc":           # string — one character at a time
for n in open("f.txt"):   # file — one line at a time
for n in count_up():      # generator — one yielded value at a time
```

All share the same `for` syntax because all implement the **iterator protocol**.

A [[Python generator produces values one at a time on demand|generator]] is just one type of iterable — it generates values lazily instead of storing them.

---

### Read more

- [[Python generator produces values one at a time on demand]]
- [[Python for loop unpacks tuples into multiple loop variables]]
- [[Python MOC]]
