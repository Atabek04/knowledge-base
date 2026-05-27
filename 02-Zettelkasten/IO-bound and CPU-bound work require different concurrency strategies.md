---
aliases: [io-bound, cpu-bound, concurrency strategy]
tags:
  - python/async
  - python/concurrency
---

> The bottleneck determines the tool. I/O-bound work waits for external systems — the thread is idle. CPU-bound work burns the processor — the thread is busy.

## The Distinction

```
I/O-bound                         CPU-bound
─────────────────────────────     ─────────────────────────────
DB query          (wait for DB)   Image processing  (math)
HTTP call         (wait for net)  ML inference      (matrix ops)
Redis get         (wait for net)  Compression       (algorithm)
File read         (wait for disk) Report generation (loops)
TTS synthesis*    ← PyTorch CPU   Encryption        (compute)

* Silero TTS: CPU math → CPU-bound despite being "audio"
```

## Why It Matters

During I/O-bound work the thread sits **idle** — waiting for a response it already sent. The CPU is free. `async/await` exploits this: suspend the coroutine, let the event loop run others on the same thread.

During CPU-bound work the thread is **actively computing**. Nothing to yield. A coroutine with CPU work and no `await` monopolizes the event loop thread — every other request freezes.

## Correct Tool per Type

| Work type | Tool | Why |
|-----------|------|-----|
| I/O-bound | `async/await` | Thread is idle anyway; event loop fills the gap |
| CPU-bound (blocking) | `ThreadPoolExecutor` + `run_in_executor` | Offload to thread; event loop stays free |
| CPU-bound (heavy parallel) | `ProcessPoolExecutor` | Bypasses GIL; true parallelism across cores |

## The GIL Factor

Python's GIL (Global Interpreter Lock) allows only one thread to execute Python bytecode at a time. This means threads don't give true parallelism for pure Python CPU work. But:
- I/O operations **release the GIL** while waiting → threads work fine for I/O-bound
- C extensions (NumPy, PyTorch) **release the GIL** during computation → `ThreadPoolExecutor` works for them too
- Pure Python CPU loops → need `ProcessPoolExecutor` for real parallelism

## Related

- [[The event loop is a Python runtime scheduler that drives async concurrency on one thread]]
- [[await suspends a coroutine and returns control to the event loop until IO completes]]
- [[run_in_executor offloads a blocking function to a thread pool without blocking the event loop]]
