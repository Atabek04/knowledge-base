---
created: 2025-12-11
tags: [topic/networking, topic/http]
sr-due:
sr-interval:
sr-ease:
---

Keep-Alive is managed by HTTP client/server automatically.

It keeps **one connection** alive between requests to the same server.

Main benefit: saves cost of TCP handshakes for sequential requests.

No application code needed — the HTTP layer handles it.

## Links
- [[HTTP Keep-Alive reuses TCP connections across multiple requests]]
- [[Connection pooling manages multiple pre-established connections]]
- [[Networking MOC]]
