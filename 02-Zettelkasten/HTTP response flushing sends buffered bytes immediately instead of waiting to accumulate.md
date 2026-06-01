---
created: 2026-06-01
aliases: [flushing, HTTP flush]
tags:
  - networking/http
  - networking/sse
---

**Flushing** = emptying a buffer and pushing its contents downstream right now, without waiting for more data to arrive.

Every I/O layer has a buffer — a small RAM area that accumulates bytes before transmitting them. Buffers exist because writing many small chunks is slower than writing one big chunk. But for streaming, that optimization is the enemy: you want each chunk delivered the moment it's produced.

---

### Buffer vs flush — concrete model

```
Producer (LLM token)
     ↓
  [ buffer ]   ← bytes accumulate here
     ↓ flush() called
  [ network ]  ← bytes go to client
```

**Without flush:** buffer fills to its size limit (e.g. 8 KB), then transmits. The client sees nothing until 8 KB of tokens accumulate — could be seconds.

**With flush after each yield:** buffer is emptied after every chunk, even if it's 20 bytes. Client gets each token the moment the server produces it.

---

### In Python (FastAPI)

```python
async def generator():
    yield "data: token1\n\n"   # FastAPI flushes here
    await asyncio.sleep(0)
    yield "data: token2\n\n"   # FastAPI flushes here
```

`StreamingResponse` calls `flush()` after each `yield`. Each flush is one syscall that tells the OS "send what you have now."

---

### Layered flush problem

Flushing at the app layer is not enough if something upstream also buffers:

```
FastAPI (flushes ✓) → Nginx (buffers by default ✗) → Browser
```

Even if FastAPI flushes each token, Nginx accumulates them in its own buffer before forwarding to the browser. The fix: `X-Accel-Buffering: no` header tells Nginx to pass chunks through immediately. See [[Nginx buffers proxied responses by default and X-Accel-Buffering disables this for SSE]].

---

### Relation to existing buffer concept

The general [[Buffers store data during transfers between components with speed mismatches|buffer concept]] applies to disk↔RAM speed mismatches. HTTP flushing applies the same idea to the network layer: the buffer absorbs speed differences between app and network, but SSE needs it bypassed.

---

### Read more

- [[Nginx buffers proxied responses by default and X-Accel-Buffering disables this for SSE]]
- [[FastAPI StreamingResponse wraps an async generator to flush each yield as an SSE chunk]]
- [[SSE keeps HTTP response body open to push text chunks continuously]]
- [[Buffers store data during transfers between components with speed mismatches]]
- [[SSE MOC]]
