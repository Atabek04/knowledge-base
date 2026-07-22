---
created: 2026-07-13
aliases: [SSE heartbeat, heartbeat comment, SSE keep-alive]
tags: [networking/sse]
---

An SSE server periodically sends a no-op comment line (`: heartbeat`) down every open stream. It does two jobs.

---

### Job 1 — reset the idle timer

Reverse proxies and load balancers close a connection that's been quiet too long. A heartbeat is bytes-on-the-wire, so it resets that idle clock and keeps the stream open even when no real event has fired.

### Job 2 — surface a dead connection sooner

Sending is a `write()` on the underlying socket. If the client already closed cleanly (tab shut, browser killed), that write throws right away and the server evicts the connection — instead of holding a dead emitter until the next real event would have tried to use it.

---

### The gotcha

<mark style="background: #ff6b6b">A heartbeat write succeeding only proves the socket was writable at that moment — it does not prove a person is watching.</mark>

A peer that vanished without closing (laptop sleep, network cut) can still silently accept buffered writes for a while before the OS finally errors, per [[A vanished TCP peer only surfaces on the next write or read, not immediately|a vanished TCP peer]]. During that window, heartbeat "succeeds" for a connection nobody is looking at — same as it does for one someone left idle on purpose.

<mark style="background: #74c7ec">Heartbeat answers "is the pipe still open?" — never "is anyone on the other end paying attention?"</mark>

So a heartbeat-only design still needs a hard, time-based ceiling (e.g. [[Spring SseEmitter and Flux ServerSentEvent hold response open like FastAPI StreamingResponse|SseEmitter]]'s own timeout) to force-evict long-idle streams regardless of whether writes keep succeeding.

---

### Read more
- [[A vanished TCP peer only surfaces on the next write or read, not immediately]]
- [[Spring flushes SSE response headers only on the first send, so an idle stream never opens]]
- [[Spring SseEmitter and Flux ServerSentEvent hold response open like FastAPI StreamingResponse]]
- [[Ping-Pong frames detect dead connections and prevent timeouts]]
- [[SSE MOC]]
