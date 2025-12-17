---
created: 2025-12-17
tags: [networking/websocket]
sr-due:
sr-interval:
sr-ease:
---

# WebSocket frames are binary data chunks, not HTTP requests

After the HTTP upgrade completes, **WebSocket communication is fundamentally different from HTTP**.

## HTTP structure

- Each request/response = **separate HTTP transaction**
- Has HTTP headers, method, status code
- Transactions can be independent

## WebSocket structure

- Frames are **data chunks in a continuous stream**
- **No HTTP headers per frame**
- Not "requests" — just **messages flowing over one persistent connection**

This is why proxies switch to **pass-through mode** after the upgrade — they can't inspect WebSocket frames as HTTP because they're not HTTP. 
The proxy just forwards raw bytes without understanding the content.

---

## Links

- [[WebSocket piggybacking works, because initial request is valid]]
- [[WebSocket maintains persistent TCP connection for bidirectional messaging]]
- [[WebSocket upgrades HTTP connection to enable bidirectional communication]]
- [[WebSocket MOC]]
