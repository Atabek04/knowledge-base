---
created: 2025-12-11
tags: [topic/networking]
sr-due:
sr-interval:
sr-ease:
---

Both HTTP Keep-Alive and database connection pools enforce limits on connection reuse.

**HTTP/1.1 Keep-Alive limits:**
- Timeout: server terminates after idle time (60-120 seconds)
- Max requests: servers can cap requests per connection

**Database connection pool limits:**
- Max lifetime: connection closed after total lifetime (e.g., 30 minutes)
- Max idle time: closed if unused too long (e.g., 10 minutes)
- Validation: pool tests if connection is alive before lending it

These limits prevent stale connections and resource exhaustion.

## Links
- [[Connection pooling reuses connections at application level to reduce overhead]]
- [[HTTP Keep-Alive reuses TCP connections across multiple requests]]
- [[Networking MOC]]
