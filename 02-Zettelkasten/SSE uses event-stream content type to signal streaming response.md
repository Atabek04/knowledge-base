---
created: 2026-04-28
tags:
  - networking/sse
---
<mark style="background: #ffd400">`Content-Type: text/event-stream`</mark> tells the browser to activate the SSE parser instead of buffering the response as a normal body.

<mark style="background: #ff6b6b">Without it, `EventSource` won't fire any events</mark> — the browser just sees a plain HTTP response.

Server must also send:
- `Cache-Control: no-cache` — prevents proxies from buffering the stream
- `Connection: keep-alive` — keeps the TCP connection open

### Read more
- [[SSE keeps HTTP response body open to push text chunks continuously]]
- [[SSE MOC]]
