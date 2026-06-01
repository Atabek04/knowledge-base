TARGET DECK: Tech-KB::Networking::SSE::Server Implementation
Tags: networking sse
**Related:** [[SSE MOC]]

START
Coding Questions
What is FastAPI's `StreamingResponse`? Is it a DTO you write, or something else?
Back:
**`StreamingResponse`** is a FastAPI built-in class (from `fastapi.responses`) — not a DTO.

Its job: hold the HTTP connection open and push each `yield` from your generator immediately to the client, instead of buffering the full response and sending it all at once.
Tags: networking sse python fastapi
<!--ID: 1780311500910-->
END

START
Coding Questions
What is passed as the first argument to `StreamingResponse`, and what does it do with it?
Back:
An **async generator** (or any async iterable).

FastAPI iterates it with `async for` and calls `flush()` after each item — so each `yield` becomes one SSE event sent to the browser immediately.

```python
StreamingResponse(
    content=my_async_generator(),   # ← async generator here
    media_type="text/event-stream",
)
```
Tags: networking sse python fastapi
<!--ID: 1780311500930-->
END

START
Coding Questions
Why is `media_type="text/event-stream"` set on `StreamingResponse`?
Back:
It tells the **client** (and any intermediaries) that this is an SSE stream — not a JSON blob or HTML page.

The browser's `EventSource` API checks for this content type to know it should parse the body as a stream of events rather than wait for the full response.
Tags: networking sse python fastapi
<!--ID: 1780311500951-->
END

START
Coding Questions
What is HTTP response **flushing**?
Back:
**Flushing** = emptying the output buffer and pushing its contents to the network right now, without waiting for more data.

Every I/O layer has a buffer that accumulates bytes before transmitting (batching is more efficient). Flushing bypasses that wait.

In SSE: `StreamingResponse` calls `flush()` after each `yield` → each token reaches the client immediately.
Tags: networking sse
<!--ID: 1780311500971-->
END

START
Coding Questions
What is an HTTP **output buffer**, and what problem does it cause for SSE?
Back:
An **output buffer** is a temporary RAM area in the I/O stack that accumulates bytes before sending them in one batch.

**Problem for SSE:** without flushing, the server holds all LLM tokens in the buffer until it fills (e.g. 8 KB) or the connection closes — the client sees nothing for seconds, then a wall of text.

**Fix:** flush after every `yield` so each token is sent the moment it's produced.
Tags: networking sse
<!--ID: 1780311500991-->
END

START
Coding Questions
Why is flushing at the app layer not always enough to make SSE work end-to-end?
Back:
Because **Nginx** (the reverse proxy) also has its own buffer.

Even if FastAPI flushes each token, Nginx accumulates them in its buffer before forwarding to the browser.

```
FastAPI (flushes ✓) → Nginx (buffers ✗) → Browser
```

Fix: `X-Accel-Buffering: no` header tells Nginx to pass chunks through immediately.
Tags: networking sse nginx
<!--ID: 1780311501011-->
END

START
Coding Questions
What does Nginx do by default with proxied responses, and why is this a problem for SSE?
Back:
**Default behavior:** Nginx buffers the full proxied response before forwarding it to the client.

**Problem for SSE:** all LLM tokens accumulate in Nginx's buffer — the browser sees nothing until Nginx flushes (when buffer fills or connection closes). Streaming is defeated.

**Fix:** `X-Accel-Buffering: no` response header switches Nginx to pass-through mode for that response.
Tags: networking sse nginx
<!--ID: 1780311501032-->
END

START
Coding Questions
What does `X-Accel-Buffering: no` do, and where does it go?
Back:
It's a response **header** sent by the app to Nginx:

```python
headers={"X-Accel-Buffering": "no"}
```

Effect: Nginx switches to **pass-through mode** — every chunk the app flushes is forwarded to the browser immediately, without accumulating.

Without it, Nginx holds chunks until its buffer fills or the connection closes.
Tags: networking sse nginx
<!--ID: 1780311501052-->
END

START
Coding Questions
What is the Nginx config alternative to the `X-Accel-Buffering: no` header?
Back:
```nginx
location /stream {
    proxy_buffering off;
    proxy_pass http://fastapi;
}
```

**Difference:** the header is controlled by the application (no ops config change needed per endpoint); `proxy_buffering off` is controlled by the Nginx config.

Prefer the header approach — the app knows which endpoints stream, not the reverse proxy config.
Tags: networking sse nginx
<!--ID: 1780311501072-->
END

START
Coding Questions
What are the two ways Spring implements SSE on the server side?
Back:
1. **`SseEmitter`** (Spring MVC — imperative): return an emitter immediately, push events from a background thread via `emitter.send(...)`.

2. **`Flux<ServerSentEvent<T>>`** (WebFlux — reactive): return a `Flux` declaration; the reactor scheduler drives it non-blocking.

Both hold the HTTP connection open and flush each event immediately — same as FastAPI's `StreamingResponse`.
Tags: networking sse java spring
<!--ID: 1780311501093-->
END

START
Coding Questions
How does `SseEmitter` work in Spring MVC?
Back:
```java
@GetMapping(value = "/stream", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
public SseEmitter stream() {
    SseEmitter emitter = new SseEmitter(Long.MAX_VALUE);

    executorService.submit(() -> {
        for (String token : llm.streamTokens()) {
            emitter.send(SseEmitter.event().data(token));
        }
        emitter.complete();
    });

    return emitter;  // method returns immediately
}
```

Key: the controller method exits fast. Spring holds the socket open. A **background thread** pushes events via `emitter.send()` whenever a chunk is ready.
Tags: networking sse java spring
<!--ID: 1780311501113-->
END

START
Coding Questions
How does `Flux<ServerSentEvent<T>>` work in Spring WebFlux for SSE?
Back:
```java
@GetMapping(value = "/stream", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
public Flux<ServerSentEvent<String>> stream() {
    return llm.streamTokens()
        .map(token -> ServerSentEvent.<String>builder()
            .data(token)
            .build());
}
```

- No manual thread management
- `Flux` is a reactive stream — zero to N items arriving over time
- WebFlux subscribes, serializes each emission to SSE format, flushes immediately
- Lazy: nothing runs until the browser connects
Tags: networking sse java spring webflux
<!--ID: 1780311501134-->
END

START
Coding Questions
Compare FastAPI `StreamingResponse`, Spring `SseEmitter`, and Spring `Flux<SSE>` — what's the same and what differs?
Back:
**Same across all three:**
- Hold HTTP connection open
- Push chunks as they arrive
- Flush each chunk immediately

**Differences:**

| | FastAPI | SseEmitter | Flux SSE |
|---|---|---|---|
| Style | async generator | imperative thread | reactive pipeline |
| Thread model | event loop | background thread | non-blocking scheduler |
| Framework | FastAPI / Starlette | Spring MVC | Spring WebFlux |
Tags: networking sse python java spring
<!--ID: 1780311501155-->
END

START
Coding Questions
When should you use `SseEmitter` vs `Flux<ServerSentEvent<T>>` in Spring?
Back:
- **`SseEmitter`** → existing Spring MVC app, simpler mental model, thread-per-request pattern already in use
- **`Flux<SSE>`** → WebFlux app, need high concurrency, want non-blocking all the way through

Both work for SSE. The choice follows the app's threading model, not the protocol.
Tags: networking sse java spring
<!--ID: 1780311501176-->
END
