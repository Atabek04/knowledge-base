---
created: 2026-04-30
aliases: [coroutine execution order, await yield point, event loop blocking]
tags:
  - python/async
---

> A coroutine runs **line by line**, top to bottom. It never skips lines or jumps ahead. The event loop can only switch to another coroutine at an `await` — nowhere else.

`await` suspends the **entire coroutine** — but only because the next lines depend on its result. Other coroutines (other requests) are not affected and run freely on the thread in the meantime.

### Execution order

```python
async def handle():
    x = 1 + 1              # (1) runs immediately
    y = x * 100            # (2) runs immediately — no chance for other coroutines
    result = await db.query()  # (3) yield point — event loop may run others
    z = result[0]          # (4) resumes here after DB responds, runs immediately
    return await llm.call(z)   # (5) second yield point
```

Between lines 1–2, the event loop has **zero opportunity** to run anything else. Code runs uninterrupted until the next `await`.

### The danger — blocking the event loop

If a coroutine has a long CPU-bound section with no `await`, it monopolizes the thread. Every other request is frozen until it finishes.

```python
async def bad():
    result = await db.query()
    for row in result:         # tight loop, no await
        heavy_compute(row)     # blocks event loop for entire duration
    return result
```

Fix: offload CPU-heavy work to a thread pool so the event loop thread stays free.

```python
import asyncio

async def good():
    result = await db.query()
    processed = await asyncio.get_event_loop().run_in_executor(None, heavy_compute, result)
    return processed
```

`run_in_executor` runs the function in a separate OS thread — the event loop is free to handle other coroutines while it executes.

### Summary

| Code type | Yields to event loop? |
|---|---|
| Regular statements (`x = 1 + 1`) | No — runs to completion |
| `await some_coroutine()` | Yes — event loop may run others |
| Long CPU loop (no `await` inside) | No — blocks everything |
| `await run_in_executor(fn)` | Yes — offloaded to thread |

---

Related:
- [[await suspends a coroutine and returns control to the event loop until IO completes]]
- [[The event loop is a Python runtime scheduler that drives async concurrency on one thread]]
- [[Python MOC]]
