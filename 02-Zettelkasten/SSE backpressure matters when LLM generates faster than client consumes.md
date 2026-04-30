---
created: 2026-04-28
tags: [networking/sse, ai-agents]
sr-due:
sr-interval:
sr-ease:
---

# SSE backpressure matters when LLM generates faster than client consumes

SSE has no built-in flow control. The server writes chunks; the client reads them. If the client is slow (slow network, tab in background), chunks pile up in the TCP send buffer.

When the buffer fills, the server's `write()` blocks — the LLM call stalls waiting for the client to drain it.

---

### What can go wrong

- Slow mobile client causes server thread/coroutine to hang
- Memory grows if tokens queue up before flush
- Agent tool calls get delayed because the loop is blocked on network I/O

---

### Mitigations

- Use async I/O (asyncio, Node streams) so a slow client doesn't block other requests
- Set a write timeout — drop the connection if client can't keep up
- For agents: decouple LLM generation from SSE delivery with an internal queue; let the LLM run free and flush to client separately

## Read more
- [[AI agents use SSE to stream LLM tokens to browser as they are generated]]
- [[SSE keeps HTTP response body open to push text chunks continuously]]
- [[SSE MOC]]
