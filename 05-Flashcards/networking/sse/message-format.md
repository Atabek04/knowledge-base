TARGET DECK: Tech-KB::Networking::SSE::Message Format
Tags: networking sse
**Related:** [[SSE MOC]]

START
Coding Questions
How many fields does an SSE event have? Name them.
Back:
**4 fields** — all optional:

1. `data` — the payload; the only field that triggers a `message` event
2. `event` — names the event type so client can route it separately
3. `id` — marks position; browser sends it back as `Last-Event-ID` on reconnect
4. `retry` — overrides the browser's reconnect delay (in milliseconds)

A blank line (`\n\n`) terminates each event.
Tags: networking sse
<!--ID: 1780311501361-->
END

START
Coding Questions
What is the minimal valid SSE event?
Back:
```
data: hello\n\n
```

Just a `data:` line followed by a blank line. No other fields required.

The blank line (`\n\n`) is the event terminator — without it, the browser buffers the line and waits for more.
Tags: networking sse
<!--ID: 1780311501381-->
END

START
Coding Questions
What does the SSE `data` field do, and how does multiline data work?
Back:
`data:` is the **only field that triggers a `message` event** on the client.

**Single line:**
```
data: {"token": "Hello"}\n\n
```

**Multiline** — repeat `data:` for each line; browser joins with `\n`:
```
data: line one
data: line two\n\n
```
Client receives: `"line one\nline two"`

JSON is the most common payload — serialize the object, put the string in `data:`.
Tags: networking sse
<!--ID: 1780311501402-->
END

START
Coding Questions
What does the SSE `event` field do, and how does the client handle it?
Back:
`event:` **names the event type** so the client can route different events to different handlers.

Server sends:
```
event: token
data: Hello\n\n

event: done
data: \n\n
```

Client routes:
```js
es.addEventListener('token', (e) => appendToken(e.data));
es.addEventListener('done',  (e) => finalize());
```

**Key:** `onmessage` only catches **unnamed** events (no `event:` field). Named events bypass it entirely.
Tags: networking sse
<!--ID: 1780311501422-->
END

START
Coding Questions
What does the SSE `id` field do?
Back:
`id:` marks the **position** of an event in the stream.

The browser stores the last received `id`. On reconnect it sends:
```
Last-Event-ID: 42
```

The server reads this header and **replays only events after position 42** — the client misses nothing.

Without `id`, reconnect starts the stream from scratch.

IDs are arbitrary strings — sequential integers are conventional but not required.
Tags: networking sse
<!--ID: 1780311501443-->
END

START
Coding Questions
What does the SSE `retry` field do, and does it need to be on every event?
Back:
`retry:` **overrides the browser's reconnect delay** (default 3000 ms).

```
retry: 1000
data: fast reconnect stream\n\n
```

After this event, the browser waits 1 second before reconnecting on any disconnect.

**Persists** — send it once to change the delay; doesn't need to repeat on every event.

- Lower → for real-time feeds where gaps matter
- Higher → for expensive streams to reduce server load on flapping clients
Tags: networking sse
<!--ID: 1780311501464-->
END

START
Coding Questions
What is the full SSE event format showing all 4 fields?
Back:
```
id: 42
event: token
retry: 3000
data: Hello world\n\n
```

Field order doesn't matter. Blank line terminates the event.

| Field | Purpose |
|---|---|
| `data` | Payload — triggers `message` event |
| `event` | Names the event type for routing |
| `id` | Position marker for resume-on-reconnect |
| `retry` | Sets reconnect delay in ms |
Tags: networking sse
<!--ID: 1780311501486-->
END
