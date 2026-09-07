---
created: 2026-07-05
tags: [networking/proxy]
aliases: [reverse proxy, CDN edge]
sr-due:
sr-interval:
sr-ease:
---

A reverse proxy sits **in front of the server**, between the internet and the origin. Every client request hits the reverse proxy first; the proxy then forwards it to the real origin server, or answers it directly from cache.

### Acts on behalf of the server

<mark style="background: #FFF3A3A6;">A reverse proxy represents the server to the outside world</mark> — the client sees the proxy's identity, never the origin's real IP address.

#### Why hiding the origin IP matters

An attacker who doesn't know the origin's IP can't flood it directly with a DDoS attack — they can only attack the reverse proxy, which is built to absorb that load. This isn't unbreakable: if the real IP ever leaks (stale DNS record, misconfigured subdomain), the origin's [[Firewall filters incoming connections by rule before they reach a server|firewall]] should be locked down to accept traffic only from the reverse proxy's known IP ranges — real-IP rotation is the last resort, not the main defense.

#### Caching

Because the reverse proxy sits physically closer to clients and in front of the origin, it can **cache** responses and serve repeat requests without ever contacting the origin again.

- Origin marks freshness with `Cache-Control: max-age=...`, or `ETag` / `Last-Modified`.
- While fresh, the reverse proxy serves the cached copy directly.
- Once stale, it re-fetches or revalidates (a cheap "has this changed?" check via ETag) before serving again.

Example: Cloudflare in front of a website is a reverse proxy — it caches, filters bot traffic, and shields the origin's real IP, all without the client ever knowing the origin exists.

---

### Contrast with forward proxy

See [[Forward proxy hides the client's identity by relaying requests to the destination server|forward proxy]] for the mirror-image pattern that protects the client instead of the server.

### Read more

- [[Forward proxy hides the client's identity by relaying requests to the destination server]]
- [[Firewall filters incoming connections by rule before they reach a server]]
- [[HTTP proxies operate in three modes for different traffic types]]
- [[Nginx buffers proxied responses by default and X-Accel-Buffering disables this for SSE]]
- [[Proxy object sits between caller and real object]]
