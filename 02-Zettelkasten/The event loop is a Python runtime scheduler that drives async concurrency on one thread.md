---
created: 2026-04-30
aliases: [event loop, asyncio event loop]
tags:
  - python/async
---

> The event loop is a **Python-level scheduler** (not OS-level) that runs on a single OS thread. It decides which coroutine runs next and when.

### What it is

- A **Python object** — `asyncio.get_event_loop()` returns it.
- Lives entirely in userspace. The OS knows nothing about coroutines — it only sees one thread.
- Internally: a loop that checks a queue of "ready to run" callbacks and an I/O poller (`select`/`epoll` — OS primitives).

```
Event loop (one thread):
┌─────────────────────────────────────┐
│  1. run next ready coroutine        │
│  2. coroutine hits await → suspend  │
│  3. register I/O callback with OS   │
│  4. ask OS: "any I/O ready?" (poll) │
│  5. OS says yes → mark coroutine    │
│     ready, go to step 1             │
└─────────────────────────────────────┘
```

### OS role — only I/O notification

The OS is involved only at the I/O layer (`epoll`/`select`): Python asks "tell me when this socket has data." The OS delivers the signal. The event loop decides what to do with it — the OS never touches coroutines.

### Java analogy

Closest equivalent: **Netty's event loop** (used inside Spring WebFlux). One `NioEventLoop` thread polls for I/O and dispatches callbacks. Same model.

---

Related:
- [[await suspends a coroutine and returns control to the event loop until IO completes]]
- [[asynccontextmanager splits startup and shutdown logic at the yield]]
- [[Python MOC]]
