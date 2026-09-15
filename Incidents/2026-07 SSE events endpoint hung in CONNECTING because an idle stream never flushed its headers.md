---
created: 2026-07-13
tags: [incident]
aliases: [SSE CONNECTING hang, EventSource never opens, idle SSE never flushes]
severity: medium
status: resolved
---

> An operator SSE channel sat in `CONNECTING` forever whenever nothing was happening. The response headers were never flushed until the first real event.

### Symptom

`EventSource` never received `open` or `error`; `readyState` stayed at `CONNECTING`. A raw `fetch()` to the same URL never resolved its headers either. Plain REST endpoints on the same service returned 200.

### Root cause

Spring MVC commits the SSE response (status line and `Content-Type: text/event-stream`) only on the first `SseEmitter.send()`. The subscribe handler registered the emitter and returned without sending anything, so an idle stream never opened. The fix was an initial `: connected` comment at registration, paired with a 20s heartbeat so the proxy does not idle-close the now-open stream.

### Where to look next time

- `fetch()` never resolving its headers localises the fault to the server, above any proxy body buffering.
- "Emitter registered" is invisible to the client; only the first flush opens the connection.
- A heartbeat keeps a stream alive but cannot open it. Two jobs, two comments.

### Lessons

- [[Spring flushes SSE response headers only on the first send, so an idle stream never opens]]
- [[SSE heartbeat proves the socket is still writable, not that the client is still watching]]

### Read more
- [[Spring SseEmitter and Flux ServerSentEvent hold response open like FastAPI StreamingResponse]]
- [[SSE MOC]]
- [[Debugging & Troubleshooting - MOC]]
