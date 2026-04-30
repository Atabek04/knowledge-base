---
created: 2026-04-28
tags: [networking/sse]
aliases: [SSE event format, SSE message format]
sr-due:
sr-interval:
sr-ease:
---

# SSE event has four optional fields: data, event, id, retry

Each SSE event is plain text. Fields are `key: value` lines. A blank line (`\n\n`) terminates the event.

```
id: 42
event: token
retry: 3000
data: Hello world

```

| Field | Purpose |
|---|---|
| `data` | The payload. Required to fire a `message` event. Multiline: repeat `data:` lines — browser joins with `\n` |
| `event` | Names the event type. Client uses `addEventListener('token', ...)` instead of `onmessage` |
| `id` | Marks position. Browser sends it back as `Last-Event-ID` on reconnect |
| `retry` | Overrides reconnect delay (milliseconds) |

All fields are optional. A minimal event is just:

```
data: hello\n\n
```

## Read more
- [[SSE data field carries the payload and supports multiline values]]
- [[SSE event field lets server label events so client routes them separately]]
- [[SSE id field marks event position so client can resume after reconnect]]
- [[SSE retry field lets server control reconnection delay in milliseconds]]
- [[SSE MOC]]
