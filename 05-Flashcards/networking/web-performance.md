TARGET DECK: Tech-KB::Networking::Web Performance
Tags: networking http performance

START
Basic
What does TTFB (Time to First Byte) measure?
Back:
The elapsed time from issuing a request to the arrival of the **first byte** of the response.

It captures everything before the server can start streaming: redirects, cache/worker, DNS, TCP, TLS, and server processing. It is the canonical measure of server responsiveness — not full download or render time.
Tags: networking http performance
END

START
Basic
Which phases make up TTFB?
Back:
Redirects → cache/service worker → DNS lookup → TCP connect → TLS handshake → **server processing**.

Server processing (routing, auth, DB queries, rendering) is usually the dominant and most actionable slice.
Tags: networking http performance
END

START
Basic
Why is TTFB the first metric to check when "a page is slow"?
Back:
It isolates the server from the frontend. A high TTFB points at the backend (slow query, cold pool, lock contention); rendering metrics point at the client.

It also gates every downstream metric — nothing renders before the first byte arrives, so TTFB sets the floor for FCP and Core Web Vitals.
Tags: networking http performance
END

START
Basic
A request has fast TTFB on a warm connection but is still slow overall. What does that tell you?
Back:
The bottleneck is the **response body** (download size or render), not the server or connection setup.

Conversely, a slow TTFB on a warm connection (DNS/TCP/TLS already paid) isolates the cause to server processing. Always ask which phase dominates before optimizing.
Tags: networking http performance
END

START
Basic
Rule-of-thumb web thresholds for a good vs. poor TTFB?
Back:
Good ≤ 0.8s, poor > 1.8s (web pages).

Backend API SLOs are usually far tighter — tens of milliseconds.
Tags: networking http performance
END
