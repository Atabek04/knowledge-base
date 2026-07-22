---
aliases: [Keycloak clustering, Keycloak HA, Keycloak Infinispan]
tags: [keycloak, production, devops, infinispan]
created: 2026-06-23
---

Keycloak runs as a stateful service — active user sessions, login failures, and authentication state live in memory. To survive node failures and scale horizontally, Keycloak embeds <mark style="background: #FFF3A3A6;">Infinispan</mark>, a distributed in-memory data grid that replicates this state across every node in the cluster. No external cache server is required — Infinispan ships inside the Keycloak binary.

This note covers what each clustering component does, not exhaustive configuration. Understanding the model helps diagnose split-brain, latency, and failover issues in production.

---

### Embedded Infinispan: what it holds

Infinispan maintains several named caches, each owning a distinct category of runtime state:

- `sessions` / `clientSessions` — active SSO sessions and per-client token state
- `authenticationSessions` — in-flight login flows (OIDC code exchange, MFA steps)
- `offlineSessions` / `offlineClientSessions` — long-lived sessions backed by offline tokens
- `loginFailures` — brute-force tracking per user
- `actionTokens` — one-time tokens (email verification, password reset)
- `work` — cluster-wide invalidation signals (e.g. realm cache busts)

<mark style="background: #ADCCFFA6;">All of these are replicated across nodes</mark>, so there is no single point of failure for in-flight sessions. If node A dies mid-login, node B already has the session state — the user does not get logged out.

Persistent data (realms, users, clients, roles) always lives in the relational database, as explained in [[Keycloak requires a relational database to persist realms, users, and sessions across restarts|the DB persistence note]]. Infinispan is a fast read layer on top of that, not a replacement.

---

### Sticky sessions: optional but recommended

A load balancer can route each user's requests to the same Keycloak node for the duration of their session. This is called <mark style="background: #FFF3A3A6;">sticky sessions</mark> (or session affinity).

Without stickiness, every request may land on a different node. The node still finds the session via Infinispan, but that requires a <mark style="background: #ADCCFFA6;">cross-node network call</mark> for each lookup. With stickiness, the owning node serves the session from local memory — faster and cheaper.

Stickiness is a performance optimization, not a correctness requirement. Keycloak works correctly without it; it is just slower under load.

---

### Node discovery in Kubernetes

Before Infinispan can replicate, nodes must find each other. Keycloak supports two discovery mechanisms in Kubernetes deployments:

#### JDBC_PING

<mark style="background: #FFF3A3A6;">JDBC_PING</mark> uses the database as a coordination table. Each node inserts a row on startup and reads the table to discover peers. It works in any environment where the DB is reachable — no extra Kubernetes permissions needed. This is the default since Keycloak 26 (`KC_CACHE_STACK=jdbc-ping`).

One gotcha: the Keycloak DB user must have write access and DDL privileges so Infinispan can create the coordination table automatically on first boot.

#### KUBE_PING

<mark style="background: #BBFABBA6;">KUBE_PING</mark> queries the Kubernetes API to list pod IPs in the same namespace. It does not touch the database but requires RBAC — the pod's ServiceAccount needs `get` and `list` on `pods`. The Keycloak Operator configures this automatically when using the `kubernetes` cache stack.

---

### Node failure and session recovery

When a node dies, Infinispan's replication means the surviving nodes already hold copies of all distributed caches. <mark style="background: #ADCCFFA6;">Sessions that were active on the failed node remain available</mark> on the remaining nodes — users stay logged in.

Since Keycloak 26, <mark style="background: #FFF3A3A6;">persistent user sessions</mark> are enabled by default: active sessions are also written to the database. This means sessions survive a full cluster restart, not just single-node failures. The trade-off is that a database restore from backup will invalidate all sessions created after the backup point, logging out every active user — a new operational concern for RTO/RPO planning.

---

### Inter-node communication

Infinispan nodes communicate over <mark style="background: #FFF3A3A6;">TCP port 7800</mark> by default. In Kubernetes, this port must be open between pods (typically allowed by default within a namespace). Keycloak 26 secures inter-node traffic with TLS using auto-rotating self-signed certificates that renew every 30 days — no manual certificate management needed.

Keycloak sessions live at the user level and track token lifetimes — see [[Keycloak sessions track active logins and token lifetimes at the user and client level|Keycloak sessions]] for how session data maps to token expiry. In production, Keycloak almost always sits behind a reverse proxy; see [[Keycloak behind a reverse proxy needs KC_PROXY_HEADERS to trust forwarded request headers|reverse proxy config]] for how forwarded headers interact with a clustered setup.

---

### Read more

- [[Keycloak sessions track active logins and token lifetimes at the user and client level]]
- [[Keycloak requires a relational database to persist realms, users, and sessions across restarts]]
- [[Keycloak behind a reverse proxy needs KC_PROXY_HEADERS to trust forwarded request headers]]
