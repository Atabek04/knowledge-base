---
aliases: [visibility problem, JMM visibility, cross-thread synchronization, volatile]
created: 2026-08-19
tags: [java, concurrency]
---

Two threads sharing a plain variable sounds simple — one writes, the other reads. In reality, Java's memory model makes no promise about *when*, or even *whether*, the reading thread ever sees the write.

<mark style="background: #FFF3A3A6;"><b>A CPU core can cache a variable's value locally, and the compiler/JVM can reorder instructions for optimization. Without an explicit synchronization mechanism, a write on one thread is not guaranteed to become visible to another thread — the reader can keep seeing a stale value indefinitely.</b></mark>

---

### The bug, concretely

```java
class Worker {
    boolean running = true;   // plain field, no synchronization

    void work() {
        while (running) { /* do stuff */ }   // may loop forever!
    }
}
```

If another thread runs `worker.running = false;`, the thread inside `work()` is **not guaranteed** to ever notice. It might keep reading a cached `true` and loop forever — not a hypothetical, this is a real, reproducible class of bug.

### Fixing it requires synchronization

<mark style="background: #FF5582A6;"><b>"Synchronization" here means an explicit mechanism that forces a write to become visible to other threads, in a defined order — Java gives you several:</b></mark>

- `volatile` — every read of a `volatile` field goes straight to main memory, skipping any per-thread cache.
- `synchronized` — entering/exiting a synchronized block forces visibility of everything written before it.
- Atomic classes (`AtomicBoolean`, `AtomicInteger`, …) — bundle the value with built-in visibility and atomicity guarantees.

None of these exist for a **local variable** — there's no `volatile` local, no way to `synchronize` a stack slot. Locals were designed to be private to one method call on one thread; the tools above only apply to fields, which live on the shared heap.

### Read more

- [[A Java lambda closure captures references to variables from its enclosing scope, which must be final or effectively final]]
- [[Each Java thread has its own call stack, so a local variable is never directly visible to another thread]]
- [[Java MOC]]
