---
created: 2026-04-28
tags: [networking/sse]
---

`data:` is the only field that triggers a `message` event on the client.

Single line:
```
data: {"token": "Hello"}\n\n
```

Multiline — repeat `data:` for each line, browser joins them with `\n`:
```
data: line one
data: line two\n\n
```

Client receives: `"line one\nline two"`

JSON is the most common payload format — serialize the object, put the string in `data:`.

### Read more
- [[SSE event has four optional fields - data, event, id, retry]]
- [[SSE MOC]]
