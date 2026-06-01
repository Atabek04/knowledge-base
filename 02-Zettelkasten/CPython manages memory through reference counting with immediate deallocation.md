---
created: 2026-06-01
tags: [python, memory, cpython, garbage-collection]
aliases: [Python reference counting, CPython refcount, Python GC]
---

CPython's primary memory management mechanism is **reference counting**.

Every object on the heap stores an internal counter (`ob_refcnt`) — how many name bindings currently point to it.
When that counter drops to **zero**, CPython frees the object **immediately** — no GC pause, no scheduler.

```python
x = [1, 2, 3]   # refcount = 1
y = x            # refcount = 2
x = None         # refcount = 1
y = None         # refcount = 0 → object freed right now
```

### Contrast with Java GC

Java uses a **generational mark-and-sweep** garbage collector that runs on a schedule.
It traces live objects from GC roots, marks unreachable ones, then sweeps them in a batch.
This causes **stop-the-world pauses** — the application freezes briefly during collection.

| | CPython | Java JVM |
|---|---|---|
| Mechanism | Reference counting | Generational mark-and-sweep |
| When freed | Immediately at refcount = 0 | At next GC cycle |
| GC pauses | No (for refcount path) | Yes |
| Handles cycles | No — needs backup cyclic GC | Yes |

### The weakness: reference cycles

Reference counting cannot free objects that reference each other, even if nothing else points to them.

```python
a = []
b = []
a.append(b)   # a → b
b.append(a)   # b → a (cycle — refcount never reaches 0)
del a, del b  # both still alive, refcount = 1 each
```

CPython's **cyclic garbage collector** runs periodically to catch these.
It is a generational collector (3 generations) — similar in structure to Java's GC, but secondary.

---

### Read more

- [[Python has no primitives because every value is a heap-allocated object]]
- [[Python variables are name bindings to heap objects not value containers]]
- [[Java objects always live on heap; reference location depends on declaration site]]
