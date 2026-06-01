---
created: 2026-06-01
tags: [inbox, concurrency]
---

## Core question
What is the difference between a thread and a coroutine? And how does each language solve the "don't waste a thread on I/O" problem?

## Thread vs coroutine (rough notes)
- Thread: OS-managed, preemptive, expensive (~1MB stack, kernel context switch)
- Coroutine: runtime-managed, cooperative — suspends only at explicit yield/await points, cheap
- Key insight: I/O wait ≠ CPU work → wasting a thread on it is wasteful → coroutines fix this

## Per language

### Python — asyncio coroutines
- `async def` + `await` — coroutines on a single-threaded event loop
- One thread, many coroutines; I/O wait → coroutine suspends → event loop runs another
- Also: `gevent` (greenlets, monkey-patching) — older alternative, less common now

### Kotlin — coroutines (kotlinx.coroutines)
- `suspend fun` + `launch`/`async` builders
- Compiled to state machines, not OS threads
- Can run on a thread pool (Dispatchers.IO) or single thread (Dispatchers.Main)
- Structured concurrency: child coroutines tied to a scope, auto-cancelled on failure

### Go — goroutines
- `go func()` — lightest of all (~2KB stack, grows dynamically)
- Scheduled by Go runtime (M:N threading — many goroutines on fewer OS threads)
- Communication via channels (`chan`), not shared memory
- Not coroutines exactly — preemptive since Go 1.14, but still lightweight

### Java — virtual threads (Project Loom, Java 21)
- `Thread.ofVirtual().start(...)` or via ExecutorService
- Look like threads, but JVM-managed — block on I/O without blocking OS thread
- Unlike coroutines: no `async/await` syntax — existing blocking code works as-is
- Huge deal for Java: no rewrite needed, just swap thread pool for virtual threads

## Questions to explore when writing atomic notes
- How does Go scheduler differ from Python event loop?
- Kotlin coroutines vs Java virtual threads — when to use which?
- Is goroutine truly a coroutine or something in between?
- Python GIL — how does it interact with asyncio?
