---
created: 2026-07-05
tags: [networking/proxy, networking/security]
aliases: [VPN, virtual private network]
sr-due:
sr-interval:
sr-ease:
---

A VPN routes all of a device's traffic through a remote server before it reaches the internet, encrypting it along the way. Choosing a country in a VPN app picks *where that remote server is located* — the client calls the VPN server, and the VPN server calls the real destination on the client's behalf.

### A VPN is a forward proxy, plus encryption

<mark style="background: #FFF3A3A6; font-weight: bold;">The relaying mechanic is exactly a [[Forward proxy hides the client's identity by relaying requests to the destination server|forward proxy]]</mark> — it acts on behalf of the client toward the internet. A VPN adds two things a plain forward proxy doesn't guarantee:

#### System-wide tunneling

All traffic from the device is routed through the VPN, not just one app's requests (unlike a browser-level proxy setting).

#### Encryption

Traffic between the client and the VPN server is encrypted, so the client's own ISP or local network can't inspect it — only the VPN server sees the plaintext request before forwarding it onward.

---

### Read more

- [[Forward proxy hides the client's identity by relaying requests to the destination server]]
- [[Reverse proxy hides the origin server's IP by relaying client requests to backend servers]]
