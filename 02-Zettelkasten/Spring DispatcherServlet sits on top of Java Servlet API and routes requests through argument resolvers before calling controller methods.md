---
aliases: [DispatcherServlet, Spring MVC lifecycle, request lifecycle, argument resolution lifecycle]
created: 2026-05-05
tags: [spring, servlet, web-mvc, lifecycle]
---

<mark style="background: yellow">Every Spring MVC request passes through `DispatcherServlet` — a standard Java Servlet that acts as the single entry point and orchestrates the full lifecycle before your controller method runs.</mark>

### Full lifecycle

```
HTTP request
  → Tomcat (Servlet container) receives it
  → HttpServlet.service()
  → DispatcherServlet.doDispatch()
      → HandlerMapping — finds which controller method matches the URL
      → HandlerAdapter — prepares to invoke the method
          → HandlerMethodArgumentResolver — builds each parameter value
              → supportsParameter() per resolver, per parameter
              → resolveArgument() on match → value injected
      → Controller method executes (all args already resolved)
      → HandlerMethodReturnValueHandler — serializes the return value
  → HTTP response sent
```

<mark style="background: cyan">Argument resolvers run inside `DispatcherServlet`, before your method body. By the time `generate(userContext, request)` executes, `userContext` is already fully built.</mark>

---

### Connection to Servlet API

`DispatcherServlet` extends `HttpServlet` (Java EE / Jakarta EE). Spring MVC doesn't replace the Servlet API — it builds on top of it. Tomcat (or Jetty, Undertow) manages the Servlet lifecycle. `DispatcherServlet` is just one servlet registered in that container, but it catches all requests and routes them internally to Spring controllers.

---

### ThreadLocal and concurrent users

Each request runs on a thread (OS thread or virtual thread in Spring Boot 4). `SecurityContextHolder` stores `SecurityContext` in a `ThreadLocal` — one copy per thread. This means:

- 500 concurrent requests → 500 threads → 500 independent `SecurityContext` instances
- Thread A's JWT claims are invisible to Thread B — no cross-user data leakage

<mark style="background: pink">Without `ThreadLocal`, all threads would share one `SecurityContext` — user A's token would be readable by user B's request. Critical security requirement, not an optimization.</mark>

---

### Thread limits and virtual threads

Traditional model: 1 OS thread per request. OS threads ≈ 1MB stack each. Practical ceiling: ~1K–10K threads before memory and context-switching hurt.

Spring Boot 4 with `spring.threads.virtual.enabled=true` uses **JVM virtual threads** (Project Loom). Virtual threads are cheap (~few KB), JVM-managed. When one blocks on I/O (DB, HTTP call), JVM parks it and runs another on the same OS thread. `ThreadLocal` still works identically — each virtual thread has its own copy.

At 500 DAU, neither model is a bottleneck. Virtual threads matter when you hit thousands of concurrent blocked I/O operations.

---

### Read more

- [[Spring HandlerMethodArgumentResolver injects custom objects into controller parameters by type]]
- [[Java ThreadLocal stores per-thread values to isolate state in concurrent environments]]
- [[Spring Ecosystem - MOC]]
