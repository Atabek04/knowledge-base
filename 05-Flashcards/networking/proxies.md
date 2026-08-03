TARGET DECK: Tech-KB::Networking::Proxies
Tags: networking proxy security

START
Coding Questions
What does a forward proxy do, and whose identity does it hide?
Back:
Sits **in front of the client**, relaying the client's requests to the destination server.

Hides the **client's** IP/location from the server — the server only ever sees the proxy.
Tags: networking proxy
END

START
Coding Questions
What does a reverse proxy do, and whose identity does it hide?
Back:
Sits **in front of the server**, relaying client requests to the real origin (or serving them from cache).

Hides the **origin server's** IP from the client — the client only ever sees the proxy (e.g. Cloudflare).
Tags: networking proxy
END

START
Coding Questions
Forward proxy vs reverse proxy — what's the one-line distinguishing question to ask?
Back:
**Which side does it act on behalf of?**

- Forward proxy → acts as the **client**
- Reverse proxy → acts as the **server**

Same relaying mechanic, opposite side of the connection.
Tags: networking proxy
END

START
Coding Questions
Why can't hiding the origin server's IP behind a reverse proxy fully stop a DDoS attack?
Back:
Hiding only works while the real IP stays secret.

If it leaks (stale DNS record, misconfigured subdomain), an attacker can bypass the reverse proxy and hit the origin directly.

Real defense: origin's **firewall** accepts connections only from the reverse proxy's known IP ranges — a leaked IP alone isn't enough to get through.
Tags: networking proxy security
END

START
Coding Questions
How does a reverse proxy decide whether its cached copy of a response is still fresh?
Back:
The origin server attaches freshness metadata to its response:

- `Cache-Control: max-age=...` — treat as fresh for N seconds
- `ETag` / `Last-Modified` — a fingerprint the proxy can send back later to ask "changed since X?"

While fresh → serve the cached copy directly, no origin contact.
Once stale → re-fetch, or revalidate via `ETag` (cheaper than a full re-download).
Tags: networking proxy caching
END

START
Coding Questions
What is a firewall, and how is it different from a proxy?
Back:
Inspects incoming (or outgoing) connections against rules — **IP ranges, ports, protocols** — and allows or blocks each one.

Key difference: a firewall never forwards or transforms traffic like a proxy does — it only decides **yes or no**.
Tags: networking security
END

START
Coding Questions
Is a VPN a forward proxy or a reverse proxy — and what does it add on top?
Back:
A **forward proxy** — it acts on behalf of the client toward the internet.

Adds two things a plain forward proxy doesn't guarantee:
- **System-wide tunneling** — routes all of the device's traffic, not just one app's
- **Encryption** — traffic between client and VPN server is encrypted, hiding it from the local ISP/network
Tags: networking proxy security
END
