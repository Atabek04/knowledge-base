---
aliases: [Keycloak realm, realm]
tags: [keycloak, security, identity, multitenant]
created: 2026-06-23
---

A <mark style="background: #FFF3A3A6;">realm</mark> is the top-level isolation boundary in Keycloak — every user, client, role, group, and policy lives inside exactly one realm. Think of it as a <mark style="background: #ADCCFFA6;">kingdom</mark>: its own subjects (users), its own laws (auth flows), and its own royal seal (token signing keys). A user in realm A literally does not exist in realm B — not filtered out, genuinely absent — and a token issued by realm A is completely invalid in realm B.

When Keycloak starts for the first time it creates the <mark style="background: #FF5582A6;">master realm</mark> automatically. The master realm is admin-only — its sole purpose is to create and manage other realms. Never put application users or clients inside master.

---

### What a realm owns

Everything that defines an identity domain lives at realm scope:

- **Users and credentials** — the user store (local or federated via LDAP/IdP)
- **Clients** — registered applications that delegate auth to this realm (see [[A Keycloak client represents an application registered in a realm to delegate authentication|clients]])
- **Roles and groups** — see [[Keycloak roles represent named permissions assigned to users, groups, or clients|roles]]
- **Identity providers** — social login or external OIDC/SAML federation
- **Authentication flows** — the ordered steps users must pass (MFA, password policy, etc.)
- **Session settings** — SSO session idle/max, access token lifetime, refresh token lifetime (see [[Keycloak sessions track active logins and token lifetimes at the user and client level|session settings]])
- **Theme and email** — login page appearance, email sender config
- **Token signing keys** — each realm holds its own RSA/ECDSA key pair; resource servers verify tokens against the realm's public key without a network call

---

### Multi-tenant pattern

The standard Keycloak multi-tenancy approach is <mark style="background: #FFF3A3A6;">one realm per tenant</mark>. Each tenant gets full isolation: separate users, separate roles, separate SSO sessions, separate password policies. There is no cross-realm user lookup by default.

The trade-off: every realm is a separate administrative unit. At scale (hundreds of tenants) this demands automation — realm creation, client registration, and role seeding must be scripted via the Admin REST API or Terraform, not done by hand.

#### Why this beats a discriminator column

The hand-rolled alternative is a <mark style="background: #FFF3A3A6;">discriminator column</mark> — one shared `users` table with a `tenant_id`, isolated by a `WHERE tenant_id = ?` on every query. Isolation then depends on <mark style="background: #FF5582A6;">never forgetting that clause</mark>; one missing `WHERE` leaks one tenant's data into another.

Realm-per-tenant removes that failure mode entirely. There is no shared table to filter — tenant B's users are a separate store, and tenant B's tokens are signed with a separate key. Isolation is enforced by <mark style="background: #ADCCFFA6;">crypto and separate storage, not by a query predicate a developer can fumble</mark>.

---

### Tokens are realm-scoped

<mark style="background: #ADCCFFA6;">A resource server configured with realm A's `issuer-uri` rejects any token whose `iss` claim points at realm B</mark> — even when both realms run on the same Keycloak instance. The `iss` (issuer) claim names the realm, and verification uses that realm's public key, so a realm-B token fails realm-A validation on both issuer mismatch and signature.

---

### Master realm — the one exception

<mark style="background: #FF5582A6;">Never use the master realm for application users or clients.</mark> It exists only so Keycloak admins can log in and manage other realms via the Admin Console or Admin REST API. Mixing application users into master breaks the isolation model and creates a security risk — a compromised master-realm credential can affect all other realms.

Create a dedicated realm for every application or tenant group instead.

---

### Database persistence

Realm configuration, users, clients, and roles are all persisted to a relational database. Keycloak requires a DB from day one — there is no in-memory-only production mode. See [[Keycloak requires a relational database to persist realms, users, and sessions across restarts|DB persistence]] for what gets stored and why in-memory mode is development-only.

---

### Read more

- [[A Keycloak client represents an application registered in a realm to delegate authentication]]
- [[Keycloak roles represent named permissions assigned to users, groups, or clients]]
- [[Keycloak sessions track active logins and token lifetimes at the user and client level]]
- [[Keycloak requires a relational database to persist realms, users, and sessions across restarts]]
