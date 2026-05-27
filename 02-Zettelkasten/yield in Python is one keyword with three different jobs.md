---
created: 2026-05-04
aliases: [yield, generator, yield keyword]
tags:
  - python/core
  - python/async
---

> `yield` in Python is like a Swiss Army knife. Same keyword, three very different jobs.

---

### Job 1 — Generator (lazy sequence)

Produces values one at a time without loading everything into memory.

```python
def count_up():
    yield 1
    yield 2
    yield 3

for n in count_up():
    print(n)   # 1, 2, 3
```

Function pauses at each `yield`, returns the value, resumes on next iteration. Java equivalent: `Iterator<T>` — but `yield` is far less painful.

---

### Job 2 — Resource lifecycle (context manager)

Open something, `yield` to hand control back, close it after. Used in `@asynccontextmanager` and FastAPI's `Depends()`.

```python
@asynccontextmanager
async def lifespan(app):
    app.state.db = await connect()   # setup
    yield                            # app runs here
    await app.state.db.close()       # teardown
```

Everything before `yield` = startup. Everything after = shutdown. See: [[asynccontextmanager splits startup and shutdown logic at the yield]].

---

### Job 3 — Async streaming (SSE / real-time)

In the agent module, `yield` pushes each LLM token to the browser as it arrives — no waiting for the full response.

```python
async def stream_response():
    async for token in llm.stream():
        yield token   # sent to browser immediately
```

One token arrives from LLM → `yield` pushes it to the user. Browser renders it live.

---

### Summary

| Job | Pattern | Use case |
|---|---|---|
| Generator | `yield value` | lazy sequences, memory-efficient iteration |
| Lifecycle | `yield` (no value) | resource setup/teardown, `Depends()` |
| Streaming | `yield value` in `async def` | SSE, real-time token streaming |

---

Related:
- [[asynccontextmanager splits startup and shutdown logic at the yield]]
- [[await suspends a coroutine and returns control to the event loop until IO completes]]
- [[Python MOC]]
