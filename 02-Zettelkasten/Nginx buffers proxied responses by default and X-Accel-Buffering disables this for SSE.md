---
created: 2026-06-01
aliases: [X-Accel-Buffering, Nginx SSE buffering]
tags:
  - networking/sse
  - devops/nginx
---

In production, your FastAPI app rarely talks directly to the browser. Nginx sits in between as a reverse proxy: it receives the response from FastAPI, then forwards it to the client.

```
Browser ←→ Nginx ←→ FastAPI (Uvicorn)
```

Nginx buffers by default — it waits to accumulate a full response before forwarding. For normal JSON endpoints this is fine (the response is complete). For SSE it breaks streaming: Nginx holds all the LLM tokens, then dumps them all at once when the connection closes.

---

### What X-Accel-Buffering does

```python
headers={"X-Accel-Buffering": "no"}
```

This header is a directive from the app to Nginx: "do not buffer this response — forward each chunk immediately."

When Nginx sees `X-Accel-Buffering: no`, it switches to **pass-through mode** for that response: every chunk FastAPI flushes reaches the browser without delay.

---

### What happens with vs without it

**Without `X-Accel-Buffering: no`:**
```
FastAPI yields "token1" → flushes to Nginx
FastAPI yields "token2" → flushes to Nginx
...
[Nginx buffer accumulates 10 KB]
Nginx → browser: "token1 token2 token3 ..."   ← all at once
```
Client sees nothing for seconds, then a wall of text.

**With `X-Accel-Buffering: no`:**
```
FastAPI yields "token1" → flushes → Nginx → browser: "token1"
FastAPI yields "token2" → flushes → Nginx → browser: "token2"
```
Client sees each token as it's produced.

---

### Cache-Control: no-cache

Also needed alongside `X-Accel-Buffering`:

```python
headers={
    "Cache-Control": "no-cache",   # ← browser/proxy: don't cache events
    "X-Accel-Buffering": "no",     # ← Nginx: don't buffer
}
```

`Cache-Control: no-cache` prevents the browser and any HTTP cache layer from caching the stream — each event must reach the browser fresh.

---

### Nginx config alternative

You can also set this globally in the Nginx config instead of per-response header:

```nginx
location /stream {
    proxy_buffering off;   # same effect as X-Accel-Buffering: no
    proxy_pass http://fastapi;
}
```

The header approach is preferred because it's controlled by the application, not the ops team — no config change needed to enable streaming on a new endpoint.

---

### Read more

- [[HTTP response flushing sends buffered bytes immediately instead of waiting to accumulate]]
- [[FastAPI StreamingResponse wraps an async generator to flush each yield as an SSE chunk]]
- [[SSE keeps HTTP response body open to push text chunks continuously]]
- [[SSE reuses HTTP so it works through proxies and needs no protocol upgrade]]
- [[SSE MOC]]
