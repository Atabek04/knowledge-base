---
aliases: [Keycloak reverse proxy, KC_PROXY_HEADERS]
tags: [keycloak, production, devops]
created: 2026-06-23
---

When Keycloak sits behind a reverse proxy (Nginx, Traefik, AWS ALB), it must know the public URL the client actually used — not its internal hostname. Keycloak uses its own perceived URL to build <mark style="background: #FFF3A3A6;">redirect URIs</mark> and stamp the <mark style="background: #FFF3A3A6;">`iss` (issuer) claim</mark> in every JWT it issues. Without proxy header trust, those values reflect the internal hostname, and login breaks.

### Why the mismatch breaks login

A client registers `https://auth.example.com/realms/myrealm` as its redirect URI.
Keycloak, seeing only `http://keycloak:8080`, constructs redirect URIs and an issuer with that internal address.

The authorization server then rejects the callback because the registered URI (`https://auth.example.com/...`) does not match what Keycloak built (`http://keycloak:8080/...`).
Spring Security, similarly, will reject the token because the `iss` claim does not match the configured issuer URL.

---

### KC_PROXY_HEADERS — the correct setting (Keycloak 24+)

Set <mark style="background: #FFF3A3A6;">`KC_PROXY_HEADERS=xforwarded`</mark> to tell Keycloak to read and trust the standard forwarded headers injected by the proxy:

| Header | Purpose |
|---|---|
| `X-Forwarded-Proto` | Tells Keycloak the public scheme (`https`) |
| `X-Forwarded-Host` | Tells Keycloak the public hostname (`auth.example.com`) |
| `X-Forwarded-For` | Carries the real client IP |
| `X-Forwarded-Port` | Carries the public port (omit if 443/80) |

The proxy is responsible for setting all of these before the request reaches Keycloak.
Keycloak then uses them to construct correct redirect URIs and the issuer claim.

#### The other accepted value

`KC_PROXY_HEADERS=forwarded` trusts the RFC 7239 `Forwarded` header instead.
Use `xforwarded` unless your proxy specifically emits the RFC 7239 format — most do not.

---

### KC_PROXY=edge — deprecated migration trap

<mark style="background: #FF5582A6;">`KC_PROXY=edge` was deprecated in Keycloak 24 and removed in Keycloak 26.</mark>
Many Docker Compose examples, blog posts, and Helm chart values files still use it.

The critical danger: <mark style="background: #FF5582A6;">Keycloak 26 starts successfully with `KC_PROXY=edge` set and emits no warning or error.</mark>
Proxy headers are simply ignored.
The issuer URL in tokens becomes the internal hostname, redirect URI validation fails for all public clients, and HTTPS enforcement is silently broken.

Teams migrating from Keycloak 24 or older without updating this variable will see mysterious 403s and `invalid_token` errors with no obvious log signal.

**Migration:**
```
# Before (broken in Keycloak 26)
KC_PROXY=edge

# After
KC_PROXY_HEADERS=xforwarded
KC_HOSTNAME=https://auth.example.com
```

---

### Restricting which proxies are trusted

By default, `KC_PROXY_HEADERS=xforwarded` trusts forwarded headers from any source.
In Keycloak 26+, <mark style="background: #ADCCFFA6;">`KC_PROXY_TRUSTED_ADDRESSES`</mark> lets you restrict header trust to specific CIDR ranges — for example, only the load balancer subnet.
This prevents a malicious client from spoofing `X-Forwarded-For` directly against Keycloak's port.

---

### Read more

- [[Keycloak requires a relational database to persist realms, users, and sessions across restarts]]
- [[Keycloak clustering uses embedded Infinispan to replicate sessions across nodes]]
- [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration]]
