---
aliases: [TTFB, Time to First Byte]
created: 2026-06-25
tags: [networking, http, performance, observability]
---

==Time to First Byte (TTFB) is the elapsed time from the client issuing a request to the moment the **first byte** of the response arrives.== It captures everything that must happen *before* the server can start streaming a response, so it is the canonical measure of **backend/server responsiveness** and connection setup cost — distinct from how long the full body then takes to download or render.

## What TTFB includes

TTFB is a sum of sequential phases, not a single number:

1. **Redirects** — any 3xx hops add their own round-trips before the real request.
2. **Cache / service worker** — a local hit can make TTFB near-zero.
3. **DNS lookup** — resolving the hostname to an IP.
4. **TCP connect** — the three-way handshake (see [[TCP provides reliable ordered error-checked data delivery over networks|TCP delivery]]).
5. **TLS handshake** — key exchange, only over HTTPS.
6. ==**Server processing**== — the application generating the response: routing, auth, DB queries, template rendering. This is usually the dominant and most actionable slice.

> [!warning] TTFB ≠ total latency
> A fast TTFB with a slow body download still feels slow. And a slow TTFB on a *warm* connection isolates the cause to **server processing**, because DNS/TCP/TLS were already paid. Always ask *which phase* dominates before optimizing.

## Why it matters for performance & monitoring

- **It isolates the server from the frontend.** A high TTFB points at the backend (slow query, cold pool, lock contention); rendering metrics point at the client. This makes TTFB the first metric to check when "the page is slow."
- **It is a leading indicator.** TTFB gates every downstream metric — a page cannot render before its first byte arrives, so it sets the floor for First Contentful Paint and Core Web Vitals.
- **Measurable in lab and field.** Synthetic checks (`curl -w '%{time_starttransfer}'`, Lighthouse, DevTools) catch regressions pre-release; ==Real User Monitoring (RUM)== captures real-world TTFB across geographies and network conditions that synthetics miss.
- **Rule-of-thumb thresholds (web):** ==good ≤ 0.8s, poor > 1.8s==. Backend API SLOs are often far tighter (tens of ms).

## How to reduce it

Attack the dominant phase: CDN/edge caching and `Keep-Alive` cut connection overhead (see [[HTTP Keep-Alive reuses TCP connections across multiple requests|Keep-Alive]] and [[Connection pooling reuses connections at application level to reduce overhead|connection pooling]]); for server processing, optimize queries, add caching, and avoid materializing more data than the response needs.

> [!note] Connection cost vs. server cost
> Geographic distance inflates the DNS/TCP/TLS phases regardless of server speed — [[High bandwidth does not guarantee low latency|bandwidth doesn't fix latency]]. Edge/CDN placement attacks that; query tuning attacks server processing. Diagnose which one before choosing the fix.

### Read more
- [[High bandwidth does not guarantee low latency]]
- [[HTTP Keep-Alive reuses TCP connections across multiple requests]]
- [[Connection pooling reuses connections at application level to reduce overhead]]
- [[Networking MOC]]
- [web.dev — Time to First Byte](https://web.dev/articles/ttfb)
- [MDN — Time to first byte](https://developer.mozilla.org/en-US/docs/Glossary/Time_to_first_byte)
