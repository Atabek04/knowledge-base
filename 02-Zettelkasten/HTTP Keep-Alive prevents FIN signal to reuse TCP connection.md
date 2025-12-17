---
created: 2025-12-17
tags: [networking/tcp, networking/http]
sr-due:
sr-interval:
sr-ease:
---

# HTTP Keep-Alive prevents FIN signal to reuse TCP connection

When **`Connection: Keep-Alive`** header is present (default in **HTTP/1.1**), the server **does not send FIN** after completing the HTTP response.

**Normal flow without Keep-Alive:**
1. TCP handshake
2. Receive HTTP request
3. Process request
4. Send HTTP response
5. **Send FIN** — connection closes

**Flow with Keep-Alive:**
1. TCP handshake
2. Receive HTTP request
3. Process request
4. Send HTTP response
5. **Keep TCP connection open** — wait for next request

This avoids the overhead of establishing a new TCP connection for each request, improving performance for multiple requests to the same server.

---

## Links

- [[HTTP Keep-Alive reuses TCP connections across multiple requests]]
- [[Either side can initiate TCP connection termination with FIN]]
- [[FIN terminates TCP connections through graceful shutdown handshake]]
- [[TCP MOC]]
