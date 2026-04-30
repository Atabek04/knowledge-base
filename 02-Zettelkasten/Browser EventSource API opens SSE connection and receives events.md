---
created: 2026-04-28
tags: [networking/sse]
aliases: [EventSource]
sr-due:
sr-interval:
sr-ease:
---

# Browser EventSource API opens SSE connection and receives events

`EventSource` is the browser's built-in SSE client. One line to connect:

```js
const es = new EventSource('/stream');
```

This immediately sends a GET request with `Accept: text/event-stream`.

---

### Event handlers

```js
es.onopen    = () => console.log('connected');
es.onmessage = (e) => console.log(e.data);       // unnamed events
es.onerror   = (e) => console.error('error', e);

es.addEventListener('token', (e) => append(e.data)); // named events
```

---

### Closing the connection

```js
es.close(); // stops reconnection too
```

Without `close()`, the browser reconnects automatically on any disconnect.

## Read more
- [[SSE event field lets server label events so client routes them separately]]
- [[Browser auto-reconnects SSE after disconnect using Last-Event-ID header]]
- [[SSE reuses HTTP so it works through proxies and needs no protocol upgrade]]
- [[SSE MOC]]
