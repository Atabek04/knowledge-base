---
created: 2026-04-28
tags: [moc]
---

# SSE MOC

Server-Sent Events — unidirectional server-to-client streaming over plain HTTP.
Covers the protocol, browser API, message format, reconnection mechanics, and AI agent use cases.

## Phase 1: Foundations

### What SSE Is
- [[SSE streams server events to client over a single persistent HTTP connection]] — core definition and model
- [[SSE is unidirectional server-to-client unlike WebSocket bidirectional channel]] — when to choose SSE vs WebSocket
- [[SSE reuses HTTP so it works through proxies and needs no protocol upgrade]] — deployment simplicity advantage

### How It Works Under the Hood
- [[SSE keeps HTTP response body open to push text chunks continuously]] — mechanics of the long-lived response
- [[SSE uses text/event-stream content type to signal streaming response]] — content negotiation signal
- [[Browser EventSource API opens SSE connection and receives events]] — client-side interface

## Phase 2: Message Format

### Event Fields
- [[SSE event has four optional fields: data, event, id, retry]] — full field reference
- [[SSE data field carries the payload and supports multiline values]] — sending structured content
- [[SSE event field lets server label events so client routes them separately]] — named event types
- [[SSE id field marks event position so client can resume after reconnect]] — position tracking
- [[SSE retry field lets server control reconnection delay in milliseconds]] — tuning reconnect interval

## Phase 3: Reconnection

- [[Browser auto-reconnects SSE after disconnect using Last-Event-ID header]] — built-in resume mechanism

## Phase 4: AI Agent Use Case

- [[AI agents use SSE to stream LLM tokens to browser as they are generated]] — token streaming + tool call events
- [[SSE backpressure matters when LLM generates faster than client consumes]] — flow control concern

## Relationships

- [[WebSocket MOC]] — bidirectional alternative; compare before choosing
- [[Networking MOC]] — parent navigation hub

## External Resources

- [MDN EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource)
- [HTML Living Standard — Server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html)
