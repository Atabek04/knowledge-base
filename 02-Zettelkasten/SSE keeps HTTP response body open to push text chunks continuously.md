---
created: 2026-04-28
tags:
  - networking/sse
---

In a normal HTTP response the server sends a full body and closes the connection. SSE breaks that contract: the server writes headers, then keeps [[Python generator produces values one at a time on demand|yielding]] chunks without ever closing the body. Each [[Python generator produces values one at a time on demand#What "yielding" means|flush]] reaches the client immediately as an event.

**Normal HTTP flow:**
1. Client: `GET /data`
2. Server: headers + full body → closes

**SSE flow:**
1. Client: `GET /stream`
2. Server: headers → chunk → chunk → chunk → (never closes until done)

---

### Server implementation sketch

```python
# FastAPI example
async def stream():
    yield "data: first event\n\n"
    await asyncio.sleep(1)
    yield "data: second event\n\n"
```

Each `yield` flushes immediately to the client.

### Read more
- [[Python generator produces values one at a time on demand#What "yielding" means|What "yielding" and "flushing" mean]]
- [[SSE uses event-stream content type to signal streaming response]]
- [[SSE event has four optional fields - data, event, id, retry]]
- [[SSE streams server events to client over a single persistent HTTP connection]]
- [[FastAPI StreamingResponse wraps an async generator to flush each yield as an SSE chunk]]
- [[HTTP response flushing sends buffered bytes immediately instead of waiting to accumulate]]
- [[Nginx buffers proxied responses by default and X-Accel-Buffering disables this for SSE]]
- [[SSE MOC]]
