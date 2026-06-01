TARGET DECK: Tech-KB::Networking::SSE::Client
Tags: networking sse
**Related:** [[SSE MOC]]

START
Coding Questions
How do you open an SSE connection in the browser?
Back:
```js
const es = new EventSource('/stream');
```

This immediately sends a GET request with `Accept: text/event-stream`. The browser keeps the connection open and fires events as they arrive.

`EventSource` is a **browser built-in** — no library needed.
Tags: networking sse
<!--ID: 1780311501197-->
END

START
Coding Questions
What are the three event handlers on `EventSource`, and what does each handle?
Back:
```js
es.onopen    = () => console.log('connected');  // connection established
es.onmessage = (e) => console.log(e.data);      // unnamed events (no event: field)
es.onerror   = (e) => console.error('error', e); // error or disconnect
```

For **named events** (with `event:` field), use `addEventListener`:
```js
es.addEventListener('token', (e) => append(e.data));
```

`onmessage` **does not** catch named events — only unnamed ones.
Tags: networking sse
<!--ID: 1780311501218-->
END

START
Coding Questions
How do you close an SSE connection, and what happens if you don't?
Back:
```js
es.close();  // stops reconnection too
```

Without `close()`, the browser **automatically reconnects** on any disconnect — indefinitely. This is built-in behavior, not something you code.

Call `es.close()` when the user navigates away or the stream is finished to stop reconnect loops.
Tags: networking sse
<!--ID: 1780311501239-->
END

START
Coding Questions
How does browser auto-reconnect work in SSE?
Back:
When an SSE connection drops, the browser automatically reopens it after a delay (default **3 seconds**).

On reconnect, it adds:
```
Last-Event-ID: <last received id>
```

The server reads this header and resumes from the right position — client misses nothing.

This is built into the `EventSource` spec. **WebSocket has no equivalent** — manual reconnect must be coded.
Tags: networking sse
<!--ID: 1780311501259-->
END

START
Coding Questions
What does `Last-Event-ID` allow the server to do on reconnect?
Back:
On reconnect, the browser sends the last `id` value it received:
```
Last-Event-ID: 42
```

The server reads this header and **replays only events after position 42**, so the client doesn't miss any events that arrived during the disconnection.

Without `id` fields in the stream, reconnect always starts from the beginning.
Tags: networking sse
<!--ID: 1780311501279-->
END

START
Coding Questions
Why is SSE's auto-reconnect an advantage over WebSocket?
Back:
**SSE:** auto-reconnect is built into the `EventSource` spec. On disconnect, browser waits (default 3 s, or the `retry:` value) and reconnects automatically — zero client code needed.

**WebSocket:** no built-in reconnect. You must code it manually: detect close event, wait, re-instantiate the connection.

For one-directional streams (notifications, LLM tokens), SSE's built-in resilience reduces client complexity.
Tags: networking sse
<!--ID: 1780311501299-->
END

START
Coding Questions
How does long-polling differ from SSE, and why does SSE win for continuous streams?
Back:
**Long-polling:** server holds connection open until data is ready → sends and closes → client immediately re-requests. Simulates push but with overhead at every event boundary.

**Problems with long-polling:**
1. Re-request cost — new HTTP handshake after every batch
2. No event framing — client must parse where one event ends
3. No built-in reconnect — manual code required

**SSE fixes all three:**
- One persistent connection for all events
- `key: value\n\n` protocol — browser knows where each event ends
- `EventSource` reconnects automatically

```
Long-polling: req → hold → data → close → req → hold → ...
SSE:          req → hold → chunk → chunk → chunk → ...
```
Tags: networking sse
<!--ID: 1780311501319-->
END

START
Coding Questions
What is `Content-Type: text/event-stream`, and what happens without it?
Back:
It tells the browser to **activate the SSE parser** instead of buffering the response as a normal body.

**Without it:** `EventSource` won't fire any events — the browser treats the response as a plain HTTP body and waits for it to complete.

Server must also send:
- `Cache-Control: no-cache` — prevents proxies from buffering the stream
- `Connection: keep-alive` — keeps the TCP connection open
Tags: networking sse
<!--ID: 1780311501340-->
END
