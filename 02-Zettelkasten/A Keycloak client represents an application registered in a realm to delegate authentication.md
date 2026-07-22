---
aliases: [Keycloak client]
tags: [keycloak, security, oauth]
created: 2026-06-23
---

A <mark style="background: #FFF3A3A6;">Keycloak client</mark> is an application registered inside a [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration|realm]] that is allowed to participate in authentication and authorization flows. Think of it as a record that says: "this application exists, here is how it authenticates, and here is what it is permitted to do."

A client is <mark style="background: #ADCCFFA6;">not only a browser app facing end users</mark>. Any application that needs Keycloak registers as a client — a frontend SPA, a backend service, a mobile app, a CLI tool. Some act *on behalf of a logged-in user*; others, like a backend service, act *as themselves* with no user involved. Every one must be a registered client before Keycloak will issue it a token.

> **Client vs user.** A client is an *application*; a [[A Keycloak user is a human account in a realm, distinct from a client application|user]] is a *person*. The person logs *into* the app. That is why the Admin console has two separate pages — **Clients** for apps, **Users** for people.

---

### Public vs confidential clients

The defining property of a client is whether it can <mark style="background: #FFF3A3A6;">keep a secret</mark>. That single fact decides how the app proves its identity — and it splits every client into one of two types.

#### Public client — cannot keep a secret

The application runs where its code is exposed to the user. A browser SPA ships all its JavaScript to the user's machine; a mobile app can be decompiled. Any `client_secret` baked in is readable by anyone, so it is no secret at all.

A public client therefore identifies with only a `client_id` and protects its login with <mark style="background: #ADCCFFA6;">PKCE</mark> instead of a secret.

> **Example — a React SPA.** Client authentication `OFF`, redirect URIs like `https://app.example.com/*`, no `client_secret`. It uses the Authorization Code Flow + PKCE and obtains an [[Keycloak issues three token types — Access Token, Refresh Token, and ID Token|access token]] on behalf of the logged-in user.

#### Confidential client — can keep a secret

The application runs server-side, where credentials stay private. A backend service stores its secret in an environment variable or a secret manager (e.g. a Kubernetes Secret), never shipping it to a user. It authenticates with both `client_id` and `client_secret`.

> **Example — a backend service.** Client authentication `ON`, secret stored in config/env. It can use the [[OAuth 2.0 grant types define how a client obtains an access token based on its trust level|Client Credentials Grant]] to call downstream services *as itself*, with no user session.

In the Keycloak Admin UI (19+) this is the <mark style="background: #FFF3A3A6;">"Client authentication"</mark> toggle: `ON` = confidential, `OFF` = public.

---

### Client credentials

Every client has a `client_id` — a human-readable string chosen at registration time (e.g. `my-react-app`, `order-service`). It is always required and appears in every token request.

Confidential clients also get a `client_secret` — a credential Keycloak generates and the application stores in its config (an env var or secret manager). It is sent alongside `client_id` when calling the token endpoint:

```bash
curl -X POST https://keycloak/realms/myrealm/protocol/openid-connect/token \
  -d grant_type=client_credentials \
  -d client_id=order-service \
  -d client_secret=40cc097b-2a57-4c17-b36a-8fdf3fc2d578
```

<mark style="background: #FF5582A6;">Never embed a `client_secret` in frontend code.</mark> If a secret leaks, rotate it in the Keycloak Admin console — rotation does not invalidate existing tokens, it only changes what future token requests must send.

---

### Other client properties

Beyond identity and type, a client carries further registration settings — each its own concept:

- <mark style="background: #ADCCFFA6;">Redirect URIs</mark> — the [[A Keycloak client's redirect URI allowlist restricts where the authorization code is sent after login|allowlist of URLs Keycloak may return the user to]] after login.
- **Roles** — client-scoped permissions, covered under [[Keycloak roles represent named permissions assigned to users, groups, or clients|roles]].
- **Token claims** — *which* claims this client's token carries are shaped by its assigned [[A Keycloak client scope is a reusable bundle of mappers and roles shared across clients|client scopes]] and their [[A Keycloak protocol mapper writes a single claim into a token from user, role, or client data|protocol mappers]]. The same user can get different claims in different clients' tokens.

---

### Read more

- [[A Keycloak user is a human account in a realm, distinct from a client application]]
- [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration]]
- [[A Keycloak client's redirect URI allowlist restricts where the authorization code is sent after login]]
- [[Keycloak roles represent named permissions assigned to users, groups, or clients]]
- [[A Keycloak client scope is a reusable bundle of mappers and roles shared across clients]]
- [[A Keycloak protocol mapper writes a single claim into a token from user, role, or client data]]
- [[OAuth 2.0 grant types define how a client obtains an access token based on its trust level]]
- [[Keycloak issues three token types — Access Token, Refresh Token, and ID Token]]
