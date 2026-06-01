---
created: 2026-06-01
aliases: [StreamingResponse]
tags:
  - python/fastapi
  - networking/sse
---

`fastapi.responses.StreamingResponse` is a FastAPI built-in class. 

Its job is to hold the HTTP connection open and push each `yield` from your generator immediately to the client.

Without it, FastAPI would buffer the full response body and send it all at once when the function returns — which defeats streaming entirely.

---

### Anatomy

```python
from fastapi.responses import StreamingResponse

@app.get("/stream")
async def stream_endpoint():
    return StreamingResponse(
        content=my_async_generator(),   # ← 1st arg: async generator
        media_type="text/event-stream", # ← signals SSE to the client
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",  # ← tells Nginx not to buffer
        },
    )
```

**First argument** — an async generator (or any async iterable), exact same [[Python generator produces values one at a time on demand|Python generator]].

FastAPI iterates it with `async for`, and calls `flush()` after each chunk.

---

### Same Python generator object

```python
async def agent_svc_stream_chat(...):
    async for token in llm.astream(...):
        yield f"data: {token}\n\n"   # SSE format
```

Calling this function returns a generator object — no code runs yet. `StreamingResponse` drives it: 
- calls `__anext__()` 
- → gets one chunk 
- → flushes it 
- → calls `__anext__()` again.

Each `yield` is one SSE event reaching the browser. Nothing waits. Nothing accumulates.

---

### Java parallel

`StreamingResponse` ≈ Spring's `SseEmitter` (imperative) or `Flux<ServerSentEvent<T>>` (reactive). See [[Spring SseEmitter and Flux ServerSentEvent hold response open like FastAPI StreamingResponse]].

---

### Read more

- [[Python generator produces values one at a time on demand]]
- [[SSE keeps HTTP response body open to push text chunks continuously]]
- [[HTTP response flushing sends buffered bytes immediately instead of waiting to accumulate]]
- [[Nginx buffers proxied responses by default and X-Accel-Buffering disables this for SSE]]
- [[Spring SseEmitter and Flux ServerSentEvent hold response open like FastAPI StreamingResponse]]
- [[SSE MOC]]
