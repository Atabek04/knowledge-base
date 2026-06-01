---
created: 2026-04-28
tags: [moc]
---

# SSE MOC

Server-Sent Events — unidirectional server-to-client streaming over plain HTTP.
Covers the protocol, browser API, message format, reconnection mechanics, and AI agent use cases.

### What SSE Is
- [[SSE streams server events to client over a single persistent HTTP connection]] — core definition and model
- [[SSE is unidirectional server-to-client unlike WebSocket bidirectional channel]] — when to choose SSE vs WebSocket
- [[SSE reuses HTTP so it works through proxies and needs no protocol upgrade]] — deployment simplicity advantage

### How SSE Differs from REST and Long-Polling
- [[SSE keeps HTTP response body open to push text chunks continuously]] — mechanics of the long-lived response
- [[Long-polling holds HTTP open but forces re-request after each batch unlike SSE]] — why long-polling falls short
- [[SSE uses event-stream content type to signal streaming response]] — content negotiation signal
- [[Browser EventSource API opens SSE connection and receives events]] — client-side interface

### Server Implementation
- [[FastAPI StreamingResponse wraps an async generator to flush each yield as an SSE chunk]] — Python/FastAPI: wraps async generator, flushes each yield
- [[HTTP response flushing sends buffered bytes immediately instead of waiting to accumulate]] — what flushing means and why it matters
- [[Nginx buffers proxied responses by default and X-Accel-Buffering disables this for SSE]] — why X-Accel-Buffering: no is required in prod
- [[Spring SseEmitter and Flux ServerSentEvent hold response open like FastAPI StreamingResponse]] — Java MVC and WebFlux equivalents

### Event Message Format
- [[SSE event has four optional fields - data, event, id, retry]] — full field reference
- [[SSE data field carries the payload and supports multiline values]] — sending structured content
- [[SSE event field lets server label events so client routes them separately]] — named event types
- [[SSE id field marks event position so client can resume after reconnect]] — position tracking
- [[SSE retry field lets server control reconnection delay in milliseconds]] — tuning reconnect interval

### Reconnection and Resilience
- [[Browser auto-reconnects SSE after disconnect using Last-Event-ID header]] — built-in resume mechanism

### AI Agent Streaming
- [[AI agents use SSE to stream LLM tokens to browser as they are generated]] — token streaming + tool call events
- [[SSE backpressure matters when LLM generates faster than client consumes]] — flow control concern
- [[TCP write() blocks when send buffer is full]] — why a slow client freezes the server thread

## Relationships

- [[WebSocket MOC]] — bidirectional alternative; compare before choosing
- [[Networking MOC]] — parent navigation hub

## External Resources

- [MDN EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource)
- [HTML Living Standard — Server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html)
