---
created: 2026-04-28
tags: [networking/sse]
sr-due:
sr-interval:
sr-ease:
---

# SSE keeps HTTP response body open to push text chunks continuously

Server writes headers, then keeps yielding chunks without ever closing the body. Each flush reaches the client immediately as an event.

**Normal HTTP flow:**
1. Client: `GET /data`
2. Server: headers + full body → closes

**SSE flow:**
1. Client: `GET /stream`
2. Server: headers → chunk → chunk → chunk → (never closes until done)

---

### Required response headers

```
Content-Type: text/event-stream
Cache-Control: no-cache
Connection: keep-alive
```

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

## Read more
- [[SSE uses text/event-stream content type to signal streaming response]]
- [[SSE event has four optional fields: data, event, id, retry]]
- [[SSE streams server events to client over a single persistent HTTP connection]]
- [[SSE MOC]]
