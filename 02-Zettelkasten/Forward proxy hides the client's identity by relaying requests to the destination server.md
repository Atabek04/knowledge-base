---
created: 2026-07-05
tags: [networking/proxy]
aliases: [forward proxy, client proxy]
sr-due:
sr-interval:
sr-ease:
---

A forward proxy sits **in front of the client**, between the client and the wider internet. The client sends its request to the proxy; the proxy then makes the actual request to the destination server on the client's behalf.

### Acts on behalf of the client

<mark style="background: #FFF3A3A6;">A forward proxy represents the client to the outside world</mark> — the destination server sees the proxy's identity (IP address), not the client's.

#### What it hides

- Client's real IP address
- Client's network location / country

This is why forward proxies are used to bypass geo-blocking, browse anonymously, or filter outbound traffic on a corporate network.

### VPN is a forward proxy with encryption

A VPN is a specific implementation of this pattern: it tunnels traffic to a proxy server (often in a chosen country) and encrypts it end-to-end, in addition to relaying it. See [[VPN encrypts and tunnels traffic through a forward proxy to hide the client's IP and location|VPN]] for the encryption + tunneling layer on top.

---

### Contrast with reverse proxy

A forward proxy protects the **client** from the server's view. The mirror-image pattern, [[Reverse proxy hides the origin server's IP by relaying client requests to backend servers|reverse proxy]], protects the **server** from the client's view — same relaying mechanic, opposite side of the connection.

| | Acts as | Faces | Example |
|---|---|---|---|
| **Forward proxy** | a client | the internet | VPN, corporate web proxy |
| **Reverse proxy** | a server | the internet | Cloudflare, Nginx |

### Read more

- [[Reverse proxy hides the origin server's IP by relaying client requests to backend servers]]
- [[VPN encrypts and tunnels traffic through a forward proxy to hide the client's IP and location]]
- [[HTTP proxies operate in three modes for different traffic types]]
- [[Proxy object sits between caller and real object]]
