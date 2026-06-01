TARGET DECK: Tech-KB::Networking::SSE::Core
Tags: networking sse
**Related:** [[SSE MOC]]

START
Coding Questions
What is SSE (Server-Sent Events)?
Back:
**SSE** is a standard for pushing data from server to client over a plain HTTP connection that stays open indefinitely.

- Client makes **one GET request**
- Server responds with headers and keeps the body open, writing text chunks over time
- Each chunk is an **event** — plain text the browser parses and delivers to JS

Key traits:
- Unidirectional: server → client only
- Plain HTTP: no protocol upgrade, no new port
- Persistent: one connection for the session
- Text-based: UTF-8 plain text events
Tags: networking sse
<!--ID: 1780311501507-->
END

START
Coding Questions
How is SSE fundamentally different from normal HTTP?
Back:
**Normal HTTP:** server sends full response body → closes connection.

**SSE:** server sends headers → keeps body open → writes chunks over time → never closes (until done).

```
Normal:  Client → GET  →  Server: 200 + full body → TCP FIN

SSE:     Client → GET  →  Server: 200 + headers → chunk → chunk → chunk → ...
```

The body never finishes until the server decides to close it.
Tags: networking sse
<!--ID: 1780311501528-->
END

START
Coding Questions
Why does SSE matter for LLM / AI agent UX?
Back:
LLMs generate output **token by token**. Without streaming, users wait seconds staring at a blank screen, then see the full response appear at once.

SSE lets the server forward each token the moment the LLM produces it → users see text appear word by word (the "typewriter" effect seen in ChatGPT and Claude).

One SSE connection handles the full response stream.
Tags: networking sse ai-agents
<!--ID: 1780311501549-->
END

START
Coding Questions
Is SSE unidirectional or bidirectional? What does that mean in practice?
Back:
**Unidirectional: server → client only.**

The client cannot send data back over the same SSE connection. If the client needs to send messages (e.g. user input), it uses separate **POST requests**.

WebSocket is bidirectional — both sides send and receive freely over the same connection.
Tags: networking sse
<!--ID: 1780311501569-->
END

START
Coding Questions
When should you choose SSE over WebSocket?
Back:
| Need | Use |
|---|---|
| Server pushes updates, client just reads | **SSE** |
| Client also sends messages (chat, games) | WebSocket |
| Auto-reconnect out of the box | **SSE** |
| Binary data (audio, video frames) | WebSocket |
| Simple proxy-friendly deployment | **SSE** |

SSE is right when data flows one direction — notifications, live feeds, LLM token streaming.
Tags: networking sse
<!--ID: 1780311501590-->
END

START
Coding Questions
Why does SSE work through HTTP proxies but WebSocket sometimes doesn't?
Back:
**SSE** is a plain HTTP response — no `Upgrade` header, no protocol switch, no special port. HTTP proxies and load balancers see it as a normal long-running request and pass it through without special config.

**WebSocket** requires an `Upgrade: websocket` handshake. Some corporate proxies block or mishandle this, causing connection failures.

SSE over HTTPS also means the stream is encrypted automatically — same as any HTTPS request.
Tags: networking sse
<!--ID: 1780311501610-->
END
