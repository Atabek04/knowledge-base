---
aliases: [ThreadLocal, per-thread storage, SecurityContextHolder ThreadLocal]
created: 2026-05-05
tags: [java, concurrency, spring, security]
---

<mark style="background: yellow">**`ThreadLocal<T>`** gives each thread its own independent copy of a variable. Read/write operations are invisible to other threads — no synchronization needed because there's no sharing.</mark>

### Why it exists

Shared mutable state between threads requires locks. For request-scoped data (current user, locale, transaction context) you don't *want* sharing — each request must see only its own data. `ThreadLocal` eliminates the problem by design: no sharing, no locks.

---

### How it works

```java
ThreadLocal<String> local = new ThreadLocal<>();

// Thread A
local.set("user-A");
local.get(); // → "user-A"

// Thread B (same ThreadLocal instance, different thread)
local.set("user-B");
local.get(); // → "user-B"  ← Thread A's value unaffected
```

The JVM maintains a map inside each `Thread` object: `ThreadLocal instance → value`. `get()`/`set()` operate on the current thread's map.

---

### Spring Security uses it for `SecurityContext`

```java
// JwtAuthenticationFilter sets it:
SecurityContextHolder.getContext().setAuthentication(auth);

// UserContextResolver reads it (same request, different class):
SecurityContextHolder.getContext().getAuthentication();
```

`SecurityContextHolder` wraps a `ThreadLocal<SecurityContext>`. Every request thread gets its own `SecurityContext` — user A's JWT claims never leak to user B's thread.

<mark style="background: pink">If you spawn a child thread inside a request handler, that child thread does **not** inherit the `ThreadLocal` value. You must explicitly propagate the context — Spring's `DelegatingSecurityContextRunnable` handles this.</mark>

---

### 1K concurrent users — memory model

| Model | Thread count | Memory per thread | Ceiling |
|---|---|---|---|
| OS threads (classic) | 1 per request | ~1 MB stack | ~1K–10K |
| Virtual threads (Spring Boot 4) | 1 per request | ~few KB | 100K+ |

Virtual threads (Project Loom) are JVM-managed. When one blocks on I/O, the JVM parks it and reuses the OS carrier thread. `ThreadLocal` works identically on virtual threads — each has its own copy.

At 500 concurrent users, neither model is a bottleneck. The `ThreadLocal` isolation guarantee is identical in both.

---

### Must call `remove()` after use

Thread pools reuse threads. If you set a `ThreadLocal` and never clear it, the next request on that thread inherits stale data.

Spring Security clears `SecurityContextHolder` automatically after each request via `SecurityContextPersistenceFilter`. For your own `ThreadLocal` usage — always call `remove()` in a `finally` block.

---

### Read more

- [[Spring DispatcherServlet sits on top of Java Servlet API and routes requests through argument resolvers before calling controller methods]]
- [[Java MOC]]
