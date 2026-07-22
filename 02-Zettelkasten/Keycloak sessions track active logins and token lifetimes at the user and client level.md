---
aliases: [Keycloak sessions]
tags: [keycloak, security, sso]
created: 2026-06-23
---

When a user logs in, Keycloak creates two distinct session objects: a <mark style="background: #FFF3A3A6;">user session</mark> (also called an SSO session) and a <mark style="background: #FFF3A3A6;">client session</mark> for each application involved. Understanding the difference between them explains how SSO works, how tokens are scoped, and what happens on logout.

### User session (SSO session)

The user session is created the moment the user successfully authenticates against the realm. It spans all applications in that realm — this is the SSO guarantee. Once the session exists, any other client in the same realm can get tokens for that user without prompting for credentials again.

Two timeouts govern how long a user session lives:

- <mark style="background: #FFF3A3A6;">SSO Session Idle Timeout</mark> — the session expires if no token activity occurs within this window. Each new token request resets the clock.
- <mark style="background: #FFF3A3A6;">SSO Session Max Lifetime</mark> — a hard ceiling, regardless of activity. Once reached, the user must re-authenticate.

These are configured at the [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration|realm]] level under Realm Settings → Sessions.

---

### Client session

Every time a specific client (application) participates in a user's SSO session, Keycloak creates a <mark style="background: #FFF3A3A6;">client session</mark> tied to both the user session and that [[A Keycloak client represents an application registered in a realm to delegate authentication|client]]. The client session tracks which tokens were issued to that application and when they expire.

Token lifetimes are bounded by the client session, which is in turn bounded by the user session. An access token cannot outlive its refresh token, and neither can outlive the user session's max lifetime. The hierarchy is:

```
User Session Max Lifetime
  └── Client Session Max (per client, must not exceed realm max)
        └── Access Token Lifetime (default 5 minutes)
        └── Refresh Token Lifetime
```

Client-level lifetime overrides must not exceed the realm-level settings — this is enforced at save time in the Admin UI and API.

---

### SSO: one login, all apps

<mark style="background: #ADCCFFA6;">Single Sign-On means the user authenticates once and all clients in the same realm trust that session.</mark> When a second app redirects the user to Keycloak, Keycloak detects the active user session via the SSO cookie and issues tokens immediately — no login form appears.

The SSO cookie is scoped to the Keycloak domain, not to individual applications. Client apps never see this cookie; they only receive the tokens Keycloak issues.

---

### Session storage: Infinispan

Keycloak stores active sessions in <mark style="background: #FFF3A3A6;">Infinispan</mark>, an in-memory distributed cache. This is why sessions survive node restarts only when clustering is configured — a single-node deployment loses all sessions on restart (pre-Keycloak 26 behavior).

Since Keycloak 26, online sessions are persisted to the database by default, so they survive restarts even without an external Infinispan cluster. Before 26, only offline sessions (backed by the `offline_access` scope) were stored in the database; regular online sessions lived in Infinispan only.

For clustered deployments, Infinispan replicates session data across nodes. See [[Keycloak clustering uses embedded Infinispan to replicate sessions across nodes|Keycloak clustering]] for how this works.

---

### Logout and back-channel notification

When a user logs out, Keycloak invalidates the user session, which cascades to all client sessions beneath it. <mark style="background: #ADCCFFA6;">Back-channel logout</mark> is the mechanism Keycloak uses to actively notify registered clients that their session is gone.

Each client can register a back-channel logout URL. When logout occurs, Keycloak sends a signed `logout_token` (a JWT defined by the OIDC Back-Channel Logout spec) to each registered URL. The client application must then invalidate its local session.

<mark style="background: #FF5582A6;">Without back-channel logout configured, a client app may continue to accept requests using a locally cached token until it expires — the user is "logged out" of Keycloak but not out of the application.</mark> This is the window where a short access token lifetime matters most.

Front-channel logout is also supported (browser-based redirects), but it is less reliable because it depends on the browser making each redirect successfully. Back-channel is preferred for server-side applications.

---

### Read more

- [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration]]
- [[Keycloak issues three token types — Access Token, Refresh Token, and ID Token]]
- [[Keycloak clustering uses embedded Infinispan to replicate sessions across nodes]]
- [[A Keycloak client represents an application registered in a realm to delegate authentication]]
