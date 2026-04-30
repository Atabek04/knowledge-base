---
created: 2026-04-28
tags: [networking/sse]
sr-due:
sr-interval:
sr-ease:
---

# SSE event field lets server label events so client routes them separately

Without `event:`, all events fire `onmessage`. With it, the client can listen to specific types.

Server sends:
```
event: token
data: Hello\n\n

event: done
data: \n\n
```

Client routes:
```js
es.addEventListener('token', (e) => appendToken(e.data));
es.addEventListener('done',  (e) => finalize());
```

`onmessage` only catches unnamed events (no `event:` field). Named events bypass it entirely.

## Read more
- [[SSE event has four optional fields: data, event, id, retry]]
- [[Browser EventSource API opens SSE connection and receives events]]
- [[SSE MOC]]
