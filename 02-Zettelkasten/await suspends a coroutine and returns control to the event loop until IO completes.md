---
created: 2026-04-30
aliases: [await, async await, event loop, coroutine suspension]
tags:
  - python/async
---

**Glossary**
- **[[The event loop is a Python runtime scheduler that drives async concurrency on one thread|Event loop]]** — a Python-level scheduler running on one OS thread. It is always running — it decides which coroutine executes next.
- **Coroutine** — an `async def` function that can hand control back to the event loop mid-execution and be resumed later.
	- You yield control when you're waiting for I/O (DB, network, disk) — the thread would otherwise sit idle doing nothing useful.
- **Suspend** — the coroutine is no longer being actively executed by the thread. Its local state is preserved in memory.
- **Resume** — the event loop puts the coroutine back into execution; it continues from the exact line after `await`.
- **Yield control** — the coroutine hands ownership of the thread back to the event loop.

> ⚠️ "Suspended" does NOT mean the process stopped. The coroutine is idle — waiting for an I/O response it already sent. The thread is busy running other coroutines in the meantime.

---

> `await` suspends the current coroutine and yields control back to the event loop. The event loop schedules other coroutines. When the awaited I/O completes, the event loop resumes this coroutine from the exact point it paused.

### What happens step by step

```python
async def handle_request():
    result = await db.query("SELECT ...")   # (1)
    summary = await llm.summarize(result)   # (3)
    return summary
```

1. `await db.query(...)` — coroutine suspends. OS is told: "notify me when DB responds." Control returns to the event loop.
2. Event loop picks up another coroutine (another request, another task) and runs it.
3. DB responds → OS notifies the event loop → event loop schedules this coroutine to resume.
4. Coroutine continues from line after `await` — `result` now holds the DB response.
5. Same cycle repeats for `await llm.summarize(...)`.

### One thread — many concurrent coroutines

Python's async I/O runs on a **single thread** with an **event loop**. No thread-per-request.

```
Thread 1 (event loop):

t=0ms  Request A: await db.query()      ← suspended, waiting for DB
t=0ms  Request B: await redis.get()     ← suspended, waiting for Redis
t=5ms  Redis responds → Request B resumes, runs until next await or return
t=12ms DB responds  → Request A resumes, runs until next await or return
```

All interleaved on one thread. No parallel execution — but no idle blocking either.

### Blocking vs suspending — precise difference

| | Blocking (sync) | Suspending (await) |
|---|---|---|
| Thread during I/O | **held** — cannot do anything else | **free** — event loop runs other coroutines |
| Other requests | must wait for a free thread | handled immediately on the same thread |
| CPU usage during wait | 0% but thread is occupied | 0% and thread is free |

### The rule

- `await` only works inside `async def`
- calling `async def` without `await` returns a coroutine object — the function body never executes
- I/O-bound code benefits from `async/await`; CPU-bound code does not (use `ProcessPoolExecutor` for that)

### Java analogy

`await` ≈ non-blocking `CompletableFuture` — the calling thread is not parked, the continuation runs when the result arrives. Closer still to **Project Loom virtual threads** (Java 21): the virtual thread is unmounted from the carrier thread during I/O, carrier thread is free, virtual thread is rescheduled when I/O completes.

---

Related:
- [[The event loop is a Python runtime scheduler that drives async concurrency on one thread]]
- [[A coroutine executes line by line and only yields at an await point]]
- [[asynccontextmanager splits startup and shutdown logic at the yield]]
- [[Python MOC]]
