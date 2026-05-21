# Java Concurrency — MOC

> **Phase 2** of [[00 - IT Career - MOC]]
> Master multithreading and concurrent programming

---

## Progress

- [ ] Threading basics
- [ ] Synchronization, Locks
- [ ] java.util.concurrent
- [ ] CompletableFuture
- [ ] Thread safety patterns
- [ ] Virtual Threads (Java 21+)

---

## Topics

### Threading Basics
- [ ] Thread creation (Thread class, Runnable, Callable)
- [ ] Thread lifecycle and states
- [ ] Thread priorities
- [ ] Daemon vs user threads
- [ ] Thread.sleep(), join(), yield()
- [ ] Thread interruption

### Synchronization
- [ ] Race conditions
- [ ] synchronized keyword (methods, blocks)
- [ ] Intrinsic locks and monitors
- [ ] wait(), notify(), notifyAll()
- [ ] Deadlock, livelock, starvation
- [ ] volatile keyword

### java.util.concurrent
- [ ] Executor framework
- [ ] ExecutorService, ThreadPoolExecutor
- [ ] ScheduledExecutorService
- [ ] Future and Callable
- [ ] ForkJoinPool

### Locks & Conditions
- [ ] ReentrantLock
- [ ] ReadWriteLock
- [ ] StampedLock
- [ ] Condition objects
- [ ] Lock fairness

### Concurrent Collections
- [ ] ConcurrentHashMap
- [ ] CopyOnWriteArrayList
- [ ] BlockingQueue implementations
- [ ] ConcurrentLinkedQueue
- [ ] ConcurrentSkipListMap

### Synchronizers
- [ ] CountDownLatch
- [ ] CyclicBarrier
- [ ] Semaphore
- [ ] Phaser
- [ ] Exchanger

### CompletableFuture
- [ ] Creating CompletableFutures
- [ ] Chaining (thenApply, thenCompose, thenCombine)
- [ ] Exception handling (exceptionally, handle)
- [ ] Combining futures (allOf, anyOf)
- [ ] Async execution

### Atomic Classes
- [ ] AtomicInteger, AtomicLong, AtomicBoolean
- [ ] AtomicReference
- [ ] Compare-and-swap (CAS)
- [ ] LongAdder, LongAccumulator

### Thread Safety Patterns
- [ ] Immutability
- [ ] Thread confinement
- [ ] Safe publication
- [ ] Happens-before relationship
- [ ] Memory visibility

### Virtual Threads (Java 21+)
- [ ] Virtual vs platform threads
- [ ] Creating virtual threads
- [ ] Structured concurrency
- [ ] When to use virtual threads
- [ ] Migration from thread pools

---

## Books

| Book | Priority | Status |
|------|----------|--------|
| **Java Concurrency in Practice** — Brian Goetz | 🔴 Critical | ⏳ |

---

## Project Tasks

**E-Commerce:** Apply concurrency patterns
- [ ] Implement async product search
- [ ] Use CompletableFuture for parallel API calls
- [ ] Implement rate limiting with Semaphore
- [ ] Use virtual threads for high-throughput endpoints

---

## Related
- [[Java MOC]]
- [[Testing - MOC]]
- [[00 - IT Career - MOC]]
