TARGET DECK: Tech-KB::Networking::TCP
Tags: networking tcp os

START
Coding Questions
What happens when the TCP send buffer is full and your app calls `write()`?
Back:
`write()` blocks — the calling thread suspends at that line until the peer reads enough data to free buffer space.

Flow: your app → kernel send buffer → network → peer's receive buffer → peer app.
If peer reads slow → peer buffer fills → TCP flow control signals stop → your send buffer fills → `write()` stalls.
Tags: networking tcp os
<!--ID: 1782128730437-->
END

START
Coding Questions
Why does a slow SSE client stall LLM token generation on the server?
Back:
Server writes tokens via `write()` into the TCP send buffer.
Slow client → buffer fills → `write()` blocks → server thread stuck → LLM loop halted.

Fix: async I/O — suspends the coroutine instead of the thread, so other requests keep running while waiting for buffer space.
Tags: networking tcp sse
<!--ID: 1782128730439-->
END
