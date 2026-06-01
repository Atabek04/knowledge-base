---
created: 2026-06-01
aliases: [SseEmitter, Spring SSE, Flux SSE]
tags:
  - java/spring
  - networking/sse
---

Java has two ways to hold an HTTP response open and push SSE events — one imperative (Spring MVC), one reactive (WebFlux). Both do exactly what FastAPI's `StreamingResponse` does: prevent the response from closing, then push chunks as they arrive.

---

### Approach 1: SseEmitter (Spring MVC — imperative)

```java
@GetMapping(value = "/stream", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
public SseEmitter stream() {
    SseEmitter emitter = new SseEmitter(Long.MAX_VALUE); // keep alive indefinitely

    executorService.submit(() -> {
        try {
            for (String token : llm.streamTokens()) {
                emitter.send(SseEmitter.event().data(token));
            }
            emitter.complete();  // close connection cleanly
        } catch (Exception e) {
            emitter.completeWithError(e);
        }
    });

    return emitter; // Spring keeps response open, doesn't close here
}
```

`SseEmitter` is returned immediately — the method exits — but Spring holds the HTTP response socket open. A background thread calls `emitter.send(...)` whenever a new chunk is ready. Spring flushes each `send()` call immediately.

**Key point:** the controller method returns fast; the actual streaming happens from a different thread.

---

### Approach 2: Flux\<ServerSentEvent\<T\>\> (WebFlux — reactive)

```java
@GetMapping(value = "/stream", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
public Flux<ServerSentEvent<String>> stream() {
    return llm.streamTokens()    // returns a Flux<String>
        .map(token -> ServerSentEvent.<String>builder()
            .data(token)
            .build());
}
```

No manual thread management. `Flux` is a reactive stream — it holds zero to N items that arrive over time. WebFlux subscribes to it, and for each emitted item it serializes to SSE format and flushes to the client.

The controller method still returns immediately (returns the `Flux` declaration, not actual data), but the pipeline is lazy — nothing runs until the browser connects.

---

### Python parallel

| Python (FastAPI) | Java MVC | Java WebFlux |
|---|---|---|
| `async def gen(): yield` | Thread calls `emitter.send()` | `Flux<ServerSentEvent<T>>` |
| `StreamingResponse(gen())` | `return new SseEmitter()` | `return flux` |
| `async for` drives generator | Background thread drives emitter | Reactor scheduler drives Flux |
| Generator pauses at `yield` | Thread blocks at `streamTokens()` | Non-blocking pipeline |

All three: hold the connection open → push chunks → flush each one → close when done.

---

### When to use which

- **SseEmitter** — existing Spring MVC app, simpler mental model, thread-per-request pattern already in use.
- **Flux SSE** — WebFlux app, high concurrency needed, non-blocking all the way through.

---

### Read more

- [[FastAPI StreamingResponse wraps an async generator to flush each yield as an SSE chunk]]
- [[SSE keeps HTTP response body open to push text chunks continuously]]
- [[HTTP response flushing sends buffered bytes immediately instead of waiting to accumulate]]
- [[AI agents use SSE to stream LLM tokens to browser as they are generated]]
- [[SSE MOC]]
- [[Spring Ecosystem - MOC]]
