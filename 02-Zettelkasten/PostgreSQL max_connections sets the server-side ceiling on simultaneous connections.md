---
created: 2026-06-23
tags: [databases/postgresql]
aliases: [max_connections]
---

`max_connections` is the PostgreSQL server parameter that caps the total number of client connections the server will accept at once.

Default: **100**. Requires a server restart to change (cannot be reloaded live).

### Reserved slots

Out of the 100, PostgreSQL quietly reserves **3 slots** for superusers (`superuser_reserved_connections`). Normal client connections can only fill the remaining 97, so that admins can always get in even under connection pressure.

### Not the same as HikariCP's maximumPoolSize

| Parameter | Layer | Scope |
|-----------|-------|-------|
| `max_connections` | PostgreSQL server | total across all apps + tools + admin |
| `maximumPoolSize` | HikariCP (app) | one application's pool only |

Your pool size must be **well below** `max_connections`, leaving room for:
- other application instances
- migration tools (Flyway, Liquibase)
- admin psql sessions
- monitoring agents

A common rule: set `max_connections` slightly above the sum of all pool sizes, not to match them.

### Why not just set it to 5000?

Each connection = a new OS process (~5–10 MB RAM). 5 000 connections → ~25–50 GB overhead before any real data. Beyond RAM, thousands of OS processes compete for CPU cores, causing [[Too many PostgreSQL connections cause CPU thrashing through excessive context switching|context-switch thrashing]].

---

### Read more
- [[PostgreSQL spawns a dedicated OS process for each client connection]]
- [[Too many PostgreSQL connections cause CPU thrashing through excessive context switching]]
- [[HikariCP maximumPoolSize caps the total number of live database connections]]
- [[PostgreSQL - MOC]]
