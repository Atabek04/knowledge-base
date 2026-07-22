---
created: 2026-07-13
aliases: [SSE initial comment, SseEmitter header flush, force SSE open, SSE stuck CONNECTING]
tags: [networking/sse, java/spring]
---

A browser's `EventSource` treats a connection as open only once it receives the HTTP status line and headers. A streaming endpoint that registers the client but writes nothing leaves it hanging forever.

---

### Why an idle stream never opens

Spring MVC — like async HTTP responses in general — writes the status line and headers only when the **first byte of the body** is written, i.e. the first `emitter.send()`.

Register the `SseEmitter`, attach `onCompletion` / `onTimeout` / `onError`, but send nothing, and the response is <mark style="background: #ff6b6b">never committed</mark>. If no real event fires for a while, nothing is ever sent.

The two sides disagree about what happened:

- **Server** thinks the client is subscribed — the emitter is registered, `subscriberCount()` grows.
- **Client** sees nothing — `EventSource` sits at `readyState = CONNECTING`, `onopen` never fires. Even a raw `fetch()` to the URL never resolves its headers, which proves the bytes never left the server.

<mark style="background: #74c7ec">Registration is not connection. The client is "open" only after the first flush reaches it.</mark>

### The fix — send one byte on subscribe

Immediately after registering the emitter, send a <mark style="background: yellow">no-op comment</mark> (`: connected`). That first `send()` forces Spring to commit the status and `Content-Type: text/event-stream` headers, so `onopen` fires at subscribe time instead of waiting for the first real event.

---

### Open vs keep-open

Two different no-op comments do two different jobs:

- **Initial comment** *opens* the stream — flushes the headers so the client sees the connection.
- The periodic [[SSE heartbeat proves the socket is still writable, not that the client is still watching|heartbeat comment]] *keeps it open* — resets proxy/LB idle timers.

One without the other is a half-fix: a stream that opens but is then idle-closed, or one that never opens at all.

---

### Read more
- [[SSE heartbeat proves the socket is still writable, not that the client is still watching]]
- [[Spring SseEmitter and Flux ServerSentEvent hold response open like FastAPI StreamingResponse]]
- [[HTTP response flushing sends buffered bytes immediately instead of waiting to accumulate]]
- [[Nginx buffers proxied responses by default and X-Accel-Buffering disables this for SSE]]
- [[SSE MOC]]
