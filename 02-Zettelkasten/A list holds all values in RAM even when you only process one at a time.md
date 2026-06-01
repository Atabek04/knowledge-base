---
created: 2026-06-01
aliases: [idle RAM, idle data]
tags:
  - python/core
---

When you loop over a list, you process one value at a time in the loop body — `print(num)`, sum it, write to DB.

"Using" a value means that one operation in the loop body.

After that one operation, you never touch that value again.
But a list keeps every value in RAM until the list is deleted — in case you go back. You don't.

```python
# ALL 1B numbers created and loaded into RAM before the loop even starts
numbers = list(range(1_000_000_000))   # ~36 GB allocated here

for num in numbers:
    print(num)
```

All ~36 GB is allocated before the first iteration runs.

Even after printing 999,999,999 numbers, the list still holds every element — printed ones included.
The list keeps a reference to each, so none can be freed.

RAM releases the memory only when the list's reference count drops to zero:
- function ends → `numbers` goes out of scope
- `del numbers`
- `numbers = something_else`

Until then, all 1B objects stay alive — whether you've "used" them or not.

A [[Python generator produces values one at a time on demand|generator]] solves this: it never holds more than one value at a time.

---

### Read more

- [[Python generator produces values one at a time on demand]]
