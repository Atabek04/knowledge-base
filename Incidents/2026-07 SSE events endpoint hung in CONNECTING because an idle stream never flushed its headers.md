---
created: 2026-07-13
tags: [incident]
aliases: [SSE CONNECTING hang, EventSource never opens, idle SSE never flushes]
severity: medium
status: resolved
---

> The operator `/events` SSE channel sat in `CONNECTING` forever whenever a center was quiet — the response headers were never flushed until the first real event.

---

### Symptom

In `exam-booking-admin-web`, the `/slots` live-connection indicator showed "Подключение…" forever (or, with the newer 10s front-end timeout, "Сервер не отвечает").

`EventSource` to `GET /api/v1/centers/{unitCode}/events` never received `open` **or** `error` — stuck at `readyState = CONNECTING`. A raw `fetch()` to the same URL never resolved its `Promise` either. Meanwhile `GET /slots` (plain REST) returned `200` normally — the fault was the SSE channel alone.

### Impact

Operator live-updates dead in the admin panel. No data loss — REST reads worked, so the grid still loaded, just never updated in real time. Found during an admin-web live review, 2026-07-10.

### Investigation

The BFF proxy was ruled out first: `route.ts` streams `upstream.body` correctly and already sets `X-Accel-Buffering: no` for `text/event-stream`.

The decisive clue was that a bare `fetch()` never resolved its **headers**. Headers resolving is upstream of any body buffering — so the bytes never left the server. That localized the fault to the backend, not the proxy or the client.

Reading `SseEmitterRegistry.subscribe()` / `register()`: it created the `SseEmitter`, attached `onCompletion` / `onTimeout` / `onError`, and returned — **without sending anything on subscribe**.

### Root cause

Spring MVC commits the HTTP response (status line + `Content-Type: text/event-stream`) only on the **first** `emitter.send()`. With no `send()` at subscribe time, an idle center (no `capacity_updated` / `slot_status_changed` / `outage_created` event) meant the headers were never written. The emitter was registered and `subscriberCount()` grew, but the browser never saw the connection open. → [[Spring flushes SSE response headers only on the first send, so an idle stream never opens|headers flush only on first send]]

### Fix

Send an initial `: connected` comment in `register()` right after adding the emitter — the first `send()` forces the header flush, so `onopen` fires at subscribe time. Paired it with a 20s heartbeat comment (`SseHeartbeatScheduler` → `broadcastHeartbeat()`) so the now-open but idle stream isn't idle-closed by the proxy/LB before a real event arrives.

### Prevention

Any async/streaming endpoint must emit at least one byte at subscribe time. Never treat "emitter registered" as "connection open" — the client only opens after the first flush.

---

### Lessons

- **A streaming HTTP response is not "open" to the client until the first byte flushes its headers.** Registering the emitter is invisible to the browser. → [[Spring flushes SSE response headers only on the first send, so an idle stream never opens]]
- **A heartbeat keeps an open stream alive but cannot open it** — it needs a first flush to exist first. Two jobs, two comments. → [[SSE heartbeat proves the socket is still writable, not that the client is still watching]]
- **`fetch()`/`EventSource` never resolving *headers* localizes the fault to the server**, above any proxy body-buffering. Header resolution is the cleaner probe than waiting on the body.

### Read more
- [[Spring flushes SSE response headers only on the first send, so an idle stream never opens]]
- [[Spring SseEmitter and Flux ServerSentEvent hold response open like FastAPI StreamingResponse]]
- [[SSE MOC]]
- [[Debugging & Troubleshooting - MOC]]
