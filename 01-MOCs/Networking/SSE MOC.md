---
created: 2026-04-28
tags: [moc]
---

Server-Sent Events — unidirectional server-to-client streaming over plain HTTP.
Covers the protocol, browser API, message format, reconnection mechanics, and AI agent use cases.

### What SSE Is
- [[SSE streams server events to client over a single persistent HTTP connection|SSE streams events over one persistent HTTP connection]]
- [[SSE is unidirectional server-to-client unlike WebSocket bidirectional channel|SSE is unidirectional server→client (vs WebSocket)]]
- [[SSE reuses HTTP so it works through proxies and needs no protocol upgrade|SSE reuses HTTP: works through proxies, no upgrade]]

### How SSE Differs from REST and Long-Polling
- [[SSE keeps HTTP response body open to push text chunks continuously|SSE keeps the response body open to push chunks]]
- [[Long-polling holds HTTP open but forces re-request after each batch unlike SSE|Long-polling re-requests after each batch (unlike SSE)]]
- [[SSE uses event-stream content type to signal streaming response|text/event-stream signals a streaming response]]
- [[Browser EventSource API opens SSE connection and receives events|Browser EventSource API receives SSE events]]

### Server Implementation
- [[FastAPI StreamingResponse wraps an async generator to flush each yield as an SSE chunk|FastAPI StreamingResponse flushes each generator yield]]
- [[HTTP response flushing sends buffered bytes immediately instead of waiting to accumulate|Flushing sends buffered bytes immediately]]
- [[Nginx buffers proxied responses by default and X-Accel-Buffering disables this for SSE|Nginx buffers proxies; X-Accel-Buffering: no for SSE]]
- [[Spring SseEmitter and Flux ServerSentEvent hold response open like FastAPI StreamingResponse|Spring SseEmitter (MVC) and Flux (WebFlux) for SSE]]

### Event Message Format
- [[SSE event has four optional fields - data, event, id, retry|SSE event fields: data, event, id, retry]]
- [[SSE data field carries the payload and supports multiline values|data field carries the payload (multiline)]]
- [[SSE event field lets server label events so client routes them separately|event field names events for client routing]]
- [[SSE id field marks event position so client can resume after reconnect|id field marks position for resume]]
- [[SSE retry field lets server control reconnection delay in milliseconds|retry field sets reconnect delay (ms)]]

### Reconnection and Resilience
- [[Browser auto-reconnects SSE after disconnect using Last-Event-ID header|Browser auto-reconnects via Last-Event-ID]]

### AI Agent Streaming
- [[AI agents use SSE to stream LLM tokens to browser as they are generated|AI agents stream LLM tokens over SSE]]
- [[SSE backpressure matters when LLM generates faster than client consumes|Backpressure when the LLM outpaces the client]]
- [[TCP write() blocks when send buffer is full|TCP write() blocks when the send buffer is full]]

## Relationships

- [[WebSocket MOC]] — bidirectional alternative; compare before choosing
- [[Networking MOC]] — parent navigation hub

## External Resources

- [MDN EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource)
- [HTML Living Standard — Server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html)
