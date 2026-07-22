---
aliases: [Keycloak database, Keycloak PostgreSQL]
tags: [keycloak, production, database]
created: 2026-06-23
---

Keycloak is stateful — every [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration|realm]], user, credential, and client registration must survive pod or process restarts. Without a database, all that state lives only in memory and is lost the moment the process exits. A relational database is therefore not optional in production — it is a hard dependency.

### What goes into the database

Keycloak persists everything that defines the authorization model and its participants:

- <mark style="background: #FFF3A3A6;">Realm configuration</mark> — login settings, token lifetimes, password policies, flows
- <mark style="background: #FFF3A3A6;">Users and credentials</mark> — user records, hashed passwords, OTP secrets, required actions
- Role assignments, group memberships, and client registrations
- Offline sessions — long-lived tokens issued with the `offline_access` scope that must outlive the server process

<mark style="background: #ADCCFFA6;">Active user sessions</mark> are a special case. In Keycloak 26+, persistent user sessions are enabled by default, so active sessions are also written to the database and survive node restarts. In earlier versions they lived only in Infinispan and were lost on restart. [[Keycloak clustering uses embedded Infinispan to replicate sessions across nodes|Infinispan]] still handles in-memory replication between nodes for performance, but the DB is now the source of truth for session durability.

---

### Supported databases in Keycloak 24+

<mark style="background: #FFF3A3A6;">PostgreSQL is the recommended choice</mark> for production. The full list of supported vendors:

- PostgreSQL
- MySQL
- MariaDB
- Microsoft SQL Server

<mark style="background: #FF5582A6;">H2 is an embedded database used only in dev mode.</mark> It requires no setup, but it stores data in a local file (or purely in memory) that is not suitable for production use. There is no migration path from H2 to a real database — you cannot export realm data and import it into PostgreSQL. Teams that run Keycloak in a container without a mounted external database end up on H2 by default and lose all realm configuration on every restart. This is the single most common production mistake when first deploying Keycloak.

---

### Configuring the database (Keycloak 17+ / Quarkus)

Keycloak switched from WildFly to a Quarkus-based distribution in version 17. Database configuration is done entirely through environment variables — no XML or properties files needed.

#### Core connection env vars

```
KC_DB=postgres
KC_DB_URL=jdbc:postgresql://host:5432/keycloak
KC_DB_USERNAME=keycloak
KC_DB_PASSWORD=secret
```

`KC_DB_URL` can be broken into parts if more convenient:

```
KC_DB_URL_HOST=host
KC_DB_URL_DATABASE=keycloak
```

#### Connection pool tuning

Keycloak uses <mark style="background: #FFF3A3A6;">Agroal</mark> as its connection pool — not HikariCP. Ops teams familiar with HikariCP must not map HikariCP property names directly to Keycloak env vars. The tuning surface is smaller and named differently:

| Env var | Purpose |
|---|---|
| `KC_DB_POOL_MAX_SIZE` | Max connections (default 100) |
| `KC_DB_POOL_MIN_SIZE` | Minimum connections held |
| `KC_DB_POOL_INITIAL_SIZE` | Connections created at startup |
| `KC_DB_POOL_CONNECTION_TIMEOUT` | Max wait for a connection |
| `KC_DB_POOL_IDLE_TIMEOUT` | Evict connections idle beyond this |

HikariCP's `maxLifetime` and `leakDetectionThreshold` have no direct equivalents here. Keycloak exposes `KC_DB_POOL_IDLE_TIMEOUT` for connection recycling instead.

---

### Persistent sessions and backup implications

Since Keycloak 26 stores active [[Keycloak sessions track active logins and token lifetimes at the user and client level|user sessions]] in the database by default, a database restore from backup will invalidate all sessions created after the backup point — logging out every active user. This is a new operational concern that did not exist before version 26. RTO/RPO planning must account for it.

---

### Read more

- [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration]]
- [[Keycloak clustering uses embedded Infinispan to replicate sessions across nodes]]
- [[Keycloak sessions track active logins and token lifetimes at the user and client level]]
