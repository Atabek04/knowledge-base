---
created: 2026-04-28
tags: [networking/sse, ai-agents]
---

<mark style="background: #ff6b6b">SSE has no built-in flow control.</mark> The server writes chunks; the client reads them. If the client is slow (slow network, tab in background), chunks pile up in the TCP send buffer.

When the buffer fills, [[TCP write() blocks when send buffer is full|the server's `write()` blocks]] — <mark style="background: #ff6b6b">the calling thread is blocked on I/O</mark>, unable to do anything until the client drains the buffer. The LLM generation loop stalls entirely.

---

### What can go wrong

- Slow mobile client causes server thread/coroutine to hang
- Memory grows if tokens queue up before flush
- Agent tool calls get delayed because the loop is blocked on network I/O

---

### Mitigations

- <mark style="background: #74c7ec">Use async I/O (asyncio, Node streams)</mark> — a slow client causes an I/O wait, not CPU work; async suspends the coroutine instead of blocking the thread, so the server keeps handling other requests
- Set a write timeout — drop the connection if client can't keep up
- For agents: decouple LLM generation from SSE delivery with an internal queue; let the LLM run free and flush to client separately

### Read more
- [[AI agents use SSE to stream LLM tokens to browser as they are generated]]
- [[SSE keeps HTTP response body open to push text chunks continuously]]
- [[TCP write() blocks when send buffer is full]]
- [[SSE MOC]]
