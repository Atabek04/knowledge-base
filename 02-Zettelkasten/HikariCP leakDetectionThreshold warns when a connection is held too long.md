---
created: 2026-06-23
tags: [databases/connection-pool, hikaricp]
aliases: [leakDetectionThreshold]
---

`leakDetectionThreshold` is the time (in ms) a borrowed connection can stay out of the pool before HikariCP logs a warning that it may have been leaked.

Default: **0 (disabled)**. Minimum to enable: **2 000 ms**.

### What a "leak" looks like

A connection is borrowed but never returned — usually because:
- a `Connection` is opened without a `try-with-resources` block
- an exception exits the method before `close()` is called
- a long-running query or transaction holds the connection far beyond normal operation time

Over time, leaked connections exhaust the pool and new requests start queuing at `connectionTimeout`.

### What HikariCP logs

When the threshold is exceeded, HikariCP logs the stack trace of the thread that borrowed the connection — pinpointing exactly where the leak originated.

```
WARN  HikariPool - Connection leak detection triggered for ...
      java.lang.Exception: Apparent connection leak detected
          at com.example.UserRepository.findAll(UserRepository.java:42)
          ...
```

### Recommended value

Set to a value slightly above your longest expected query/transaction time.
For a typical REST service where queries take < 1 s, `leakDetectionThreshold = 5000` (5 s) is a good starting point.

Disable it in production only if the log noise from intentionally long-held connections is a problem.

---

### Read more
- [[HikariCP maximumPoolSize caps the total number of live database connections]]
- [[HikariCP connectionTimeout is the max wait before throwing an exception]]
- [[Databases - MOC]]
