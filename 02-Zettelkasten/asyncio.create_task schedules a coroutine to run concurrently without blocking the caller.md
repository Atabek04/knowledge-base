---
aliases: [create_task, asyncio task, fire and forget]
tags:
  - python/async
---

> `await coro()` runs it and waits. `create_task(coro())` starts it now, lets you do other work, wait later.

## The Pattern

```python
# Start TTS concurrently — don't block the SSE stream
tts_task = asyncio.create_task(
    self._run_tts_buffer(token_queue, audio_queue, locale, self._tts)
)

# Stream LLM text while TTS works in parallel (both on event loop)
async for frame in self._tool_loop(...):
    yield frame

# Now wait for TTS to finish
await tts_task
```

`service.py:137-157` — text streaming and audio synthesis run concurrently on the same event loop.

## vs `await` directly

```python
await coro()          # runs coro, caller pauses until done — sequential
asyncio.create_task(coro())  # schedules coro, caller continues — concurrent
```

Both run on the **same event loop thread** — not in parallel like threads. Concurrency comes from interleaving at `await` points.

## Must You Always `await` Async Functions?

Yes — with one exception. Without `await` or `create_task`, calling `async def fn()` returns a **coroutine object**; the body never runs:

```python
result = fn()        # coroutine object — fn DID NOT execute
result = await fn()  # fn executes, result holds return value
task   = asyncio.create_task(fn())  # fn scheduled to run, returns Task
```

## Related

- [[await suspends a coroutine and returns control to the event loop until IO completes]] — sequential await
- [[A coroutine executes line by line and only yields at an await point]] — why concurrency requires await points
