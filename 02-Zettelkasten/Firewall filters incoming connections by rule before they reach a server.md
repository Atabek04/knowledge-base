---
created: 2026-07-05
tags: [networking/security]
aliases: [firewall]
sr-due:
sr-interval:
sr-ease:
---

A firewall inspects incoming (and sometimes outgoing) network connections against a set of rules — IP ranges, ports, protocols — and allows or blocks each one. It's a gatekeeper, not a proxy: it never forwards or transforms traffic, it only decides yes or no.

### Rule example

<mark style="background: #FFF3A3A6; font-weight: bold;">"Only allow traffic from these IP ranges"</mark> or "block port 22 from outside" are typical firewall rules.

#### Where it fits with a reverse proxy

A [[Reverse proxy hides the origin server's IP by relaying client requests to backend servers|reverse proxy]] hides the origin server's real IP, but hiding isn't blocking — if the IP ever leaks, an attacker can still connect directly unless the origin's firewall is configured to accept connections **only** from the reverse proxy's known IP ranges. The firewall is what makes a leaked IP useless on its own.

---

### Read more

- [[Reverse proxy hides the origin server's IP by relaying client requests to backend servers]]
