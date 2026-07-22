---
created: 2026-06-23
tags: [databases/postgresql, linux/process]
aliases: [PostgreSQL process-per-connection]
---

PostgreSQL uses a **process-per-connection** model: for every client that connects, the `postmaster` supervisor process forks a new OS backend process dedicated to that client for the lifetime of the connection.

This is different from most web servers and MySQL, which use threads. Each backend is a full OS process with its own isolated memory.

### Memory cost per connection

Each backend process allocates:

| Source | Default | Notes |
|--------|---------|-------|
| Process overhead (stack, code, OS structures) | ~5 MB | idle connection baseline |
| `work_mem` | 4 MB | per sort/hash *operation*, not per connection — a complex query can use it multiple times |
| `temp_buffers` | 8 MB | only when the session uses temporary tables |

A rough rule of thumb: **~5–10 MB per idle connection**, more under active query load.

At 5 000 connections that's **~25–50 GB** just in process overhead — before any data is loaded into `shared_buffers`.

### Why processes, not threads?

PostgreSQL predates the era of mature kernel threading. Process isolation also gives hard memory boundaries — a misbehaving backend cannot corrupt another's memory. The downside is that fork overhead and per-process RAM cost scale linearly with connection count, which is why [[Connection pooling reuses connections at application level to reduce overhead|connection pooling]] is essential.

---

### Read more
- [[PostgreSQL max_connections sets the server-side ceiling on simultaneous connections]]
- [[Too many PostgreSQL connections cause CPU thrashing through excessive context switching]]
- [[Connection pooling reuses connections at application level to reduce overhead]]
- [[Process is an instance of a program in execution with isolated memory space and resources]]
- [[PostgreSQL - MOC]]
