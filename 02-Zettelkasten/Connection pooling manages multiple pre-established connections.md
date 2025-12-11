---
created: 2025-12-11
tags: [topic/networking, topic/databases]
sr-due:
sr-interval:
sr-ease:
---

Connection pooling manages **multiple connections** in a collection.

Unlike Keep-Alive, you write code to manage the pool (or use libraries like HikariCP).

Connections are created **beforehand** and kept ready for use.

Main benefit: eliminates connection establishment overhead for high-throughput scenarios.

## Links
- [[Connection pooling reuses connections at application level to reduce overhead]]
- [[Keep-Alive maintains single TCP connection between requests]]
- [[Networking MOC]]
