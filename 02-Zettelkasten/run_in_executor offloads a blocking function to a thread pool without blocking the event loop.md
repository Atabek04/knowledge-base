---
aliases: [run_in_executor, ThreadPoolExecutor, executor, thread pool]
tags:
  - python/async
  - python/concurrency
---

> `run_in_executor` is the bridge between the async world and blocking (sync) code. It runs a blocking function in a thread pool and returns an awaitable — so the event loop stays free while the thread works.

## The Problem

Silero TTS (`tts_service.synthesize`) is a synchronous, blocking PyTorch call. You cannot `await` it. Calling it directly freezes the event loop:

```python
# WRONG — blocks the event loop thread for ~800ms
async def _flush(text):
    audio_bytes = tts_service.synthesize(text, language)  # all other requests freeze
```

## The Fix: `run_in_executor`

```python
# service.py:183
loop = asyncio.get_event_loop()
audio_bytes = await loop.run_in_executor(
    _tts_executor,          # which pool to use (None = default pool)
    tts_service.synthesize, # the blocking fn — called in a thread
    text,                   # positional args passed to the fn
    language,
)
```

Execution split:
```
event loop thread              |  tts thread (_tts_executor)
                               |
await run_in_executor ─────────┼──→ synthesize(text, language)  ← blocks here
  ↓ coroutine suspended        |    PyTorch computing, ~800ms
  ↓ event loop free            |
  handles other SSE streams    |
  handles other requests       |
                               |
  ← coroutine resumes ←────────┼── returns audio_bytes
```

## `ThreadPoolExecutor` — Custom vs Default

```python
# service.py:34
_tts_executor = ThreadPoolExecutor(max_workers=2, thread_name_prefix="tts")
```

`run_in_executor(None, fn)` uses asyncio's **default executor** — `min(32, cpu_count + 4)` workers. For most I/O work that's fine.

For TTS, a custom executor with `max_workers=2` is intentional:

| | Default (`None`) | Custom `max_workers=2` |
|--|--|--|
| Max concurrent TTS calls | up to 32 | 2 |
| Memory pressure | High (each thread holds PyTorch state) | Controlled |
| Thread names in stack traces | `ThreadPoolExecutor-0_0` | `tts_0`, `tts_1` |

**Rule:** Use a custom executor when the work is memory-heavy, GPU-bound, or needs to be distinguishable in profiling.

## Signature

```python
await loop.run_in_executor(executor, fn, *args)
# executor: ThreadPoolExecutor | None (default pool)
# fn:       sync callable — NOT a coroutine
# *args:    positional args only (no kwargs — use functools.partial for those)
```

For kwargs:
```python
from functools import partial
await loop.run_in_executor(executor, partial(fn, key=value))
```

## When to Use

Use `run_in_executor` when:
- You have a **sync library** that has no async equivalent (Silero, PIL, reportlab, etc.)
- A C extension **releases the GIL** during computation (PyTorch, NumPy) — threads give real concurrency
- You cannot `await` the call but it will **block for meaningful time** (>1ms)

Do NOT use for pure Python CPU loops — GIL prevents true parallelism; use `ProcessPoolExecutor` instead.

## Java Analogy

```java
// Java: CompletableFuture.supplyAsync(fn, executor)
CompletableFuture<byte[]> future = CompletableFuture.supplyAsync(
    () -> ttsService.synthesize(text, language),
    ttsExecutorService
);
byte[] audio = future.get();
```

Same pattern: submit blocking work to a thread pool, get a future back, await the result.

## Related

- [[IO-bound and CPU-bound work require different concurrency strategies]] — why you need threads for CPU/blocking work
- [[A coroutine executes line by line and only yields at an await point]] — blocking a coroutine freezes everything
- [[The event loop is a Python runtime scheduler that drives async concurrency on one thread]] — what run_in_executor protects
