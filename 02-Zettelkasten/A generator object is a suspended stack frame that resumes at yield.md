---
created: 2026-06-01
aliases: [generator suspended frame, generator stack frame]
tags:
  - python/core
---

Normally when a method returns, its [[Call stack is a LIFO structure that tracks active method frames|stack frame]] is destroyed — locals gone, execution position gone.

A generator function breaks this rule. When it hits `yield`, the frame is **frozen** instead of destroyed.

```python
def count_up(n):
    i = 0
    while i < n:
        yield i   # frame FREEZES here — i stays alive in memory
        i += 1    # execution resumes exactly here on next next()
```

The **generator object** is a reference to that frozen frame. Calling `next()` thaws it, runs until the next `yield`, then freezes again.

| | Normal method | Generator |
|---|---|---|
| After call | frame destroyed | frame frozen |
| Locals | gone | preserved |
| Resume | impossible | picks up at `yield` line |
| Memory | freed immediately | held until exhausted |

This is why locals like `i` survive between iterations — they're sitting in a suspended frame on the heap, not on an active stack.

---

Read more:
- [[Call stack is a LIFO structure that tracks active method frames]]
- [[Python generator produces values one at a time on demand]]
- [[yield in Python is one keyword with three different jobs]]
