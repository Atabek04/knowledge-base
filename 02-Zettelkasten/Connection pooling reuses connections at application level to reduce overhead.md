---
created: 2025-12-08
tags: [networking/patterns]
sr-due:
sr-interval:
sr-ease:
---

**Connection pooling** is an application-level pattern that maintains a **pool of reusable connections** to reduce the cost of creating new connections.

Common examples:
- **HikariCP** for database connections
- **Apache HttpClient** connection pool for HTTP client requests

Instead of creating a new connection for each operation (which is expensive), you:
1. **Borrow** a connection from the pool
2. **Use** it for your operation
3. **Return** it to the pool for reuse

**Example:** Your Java app has 10 database connections in HikariCP pool. Each request borrows one, executes a query, and returns it to the pool. The next request can reuse that same connection.

This is different from HTTP Keep-Alive, which operates at the **protocol level** (TCP connection stays open between client and server).

Connection pooling operates at the **application level** and can apply to HTTP client connections, database connections, or any connection-based resource.

Both connection pooling and Keep-Alive aim to **avoid the overhead of establishing new connections** repeatedly.

## Links

- [[HTTP Keep-Alive reuses TCP connections across multiple requests]]
- [[Networking MOC]]
