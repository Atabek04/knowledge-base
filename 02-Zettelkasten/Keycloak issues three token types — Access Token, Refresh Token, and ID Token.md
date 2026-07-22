---
aliases: [Keycloak token types]
tags: [keycloak, security, tokens, jwt]
created: 2026-06-23
---

Every successful Keycloak login returns up to three tokens, each with a different audience and lifetime.
Knowing which token goes where — and which one to never send to your API — prevents a class of security mistakes that are surprisingly common.

### Access Token

The <mark style="background: #FFF3A3A6;">Access Token</mark> is what your Spring resource server reads on every request.
It is a <mark style="background: #ADCCFFA6;">signed [[A JWT is a self-contained signed token that carries claims verifiable without a server round-trip|JWT]]</mark> that the API validates locally against Keycloak's public key — no round-trip needed.

Default lifetime is <mark style="background: #FFF3A3A6;">5 minutes</mark>.
Keep it short: if a token leaks, the blast radius is limited to its remaining validity window.

#### What it contains

The payload carries the user's identity and permissions:

- `sub` — the user's stable UUID inside the realm
- `iss` — the realm URL (`https://keycloak.example.com/realms/myrealm`)
- `exp` / `iat` — expiry and issue time
- `realm_access.roles` — realm-level roles (e.g. `["admin", "user"]`)
- `resource_access.{clientId}.roles` — client-scoped roles
- `azp` — the client that requested the token
- `scope` — space-separated [[OAuth 2.0 scopes limit the set of resources an access token is permitted to access|OAuth scopes]] granted

The [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access|role claim structure]] is Keycloak-specific; your Spring `JwtAuthenticationConverter` must know to look in `realm_access.roles`, not a generic `roles` field.

---

### ID Token

The <mark style="background: #FFF3A3A6;">ID Token</mark> is an [[OpenID Connect adds an identity layer on top of OAuth 2.0 via the ID token|OIDC]] concept — it proves *who* the user is, not *what* they are allowed to do.

It is meant for the <mark style="background: #FFF3A3A6;">client application only</mark> (the browser SPA, mobile app, or BFF).
The client reads it to display a name or avatar; it is never forwarded to a backend API.

#### Common mistake

<mark style="background: #FF5582A6;">Never send the ID Token as a Bearer token to your resource server.</mark>
It is not intended as an authorization credential.
A backend that accepts it is relying on a token whose audience is the front-end client, not the API — this violates the OIDC spec and breaks when Keycloak changes what claims it emits in ID tokens.

#### What it contains

User profile claims:

- `name`, `given_name`, `family_name`
- `preferred_username` — display name, but not guaranteed unique across realms
- `email`, `email_verified`
- `nonce` — replay protection value echoed from the authorization request (present in ID tokens, removed from access tokens in Keycloak 25)
- `sid` — session ID (replaced `session_state` in Keycloak 25)

---

### Refresh Token

The <mark style="background: #FFF3A3A6;">Refresh Token</mark> is a longer-lived credential used exclusively at Keycloak's token endpoint.
It never leaves the client — it is never sent to your API.

Default lifetime is tied to the SSO session idle timeout (<mark style="background: #FFF3A3A6;">30 minutes idle</mark>, up to the session max of 10 hours by default).
When the access token expires, the client exchanges the refresh token for a new access token without requiring the user to log in again.

#### How the exchange works

```bash
POST /realms/{realm}/protocol/openid-connect/token
Content-Type: application/x-www-form-urlencoded

grant_type=refresh_token
&refresh_token=<the_refresh_token>
&client_id=my-app
&client_secret=my-secret
```

Keycloak responds with a fresh `access_token`, a new `refresh_token` (when rotation is enabled), and their updated expiry times.

#### Refresh token rotation

<mark style="background: #ADCCFFA6;">Refresh token rotation</mark> invalidates the old token on each use and issues a new one.
This limits the damage from a stolen refresh token: using the old token after rotation triggers detection and Keycloak can revoke the entire session.

<mark style="background: #FF5582A6;">Note: the Client Credentials grant (machine-to-machine) does not issue a refresh token</mark> — the client simply re-authenticates with its credentials when the access token expires.

---

### Token type summary

| Token | Format | Audience | Lifetime | Purpose |
|---|---|---|---|---|
| Access Token | JWT | Resource servers (your API) | ~5 min | Authorize API calls |
| ID Token | JWT | Client app only | Same as access | Prove user identity (OIDC) |
| Refresh Token | Opaque or JWT | Keycloak token endpoint only | ~30 min idle | Obtain new access tokens |

---

### Read more

- [[A JWT is a self-contained signed token that carries claims verifiable without a server round-trip]]
- [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access]]
- [[Token introspection validates a token by querying the authorization server instead of verifying locally]]
- [[OpenID Connect adds an identity layer on top of OAuth 2.0 via the ID token]]
- [[OAuth 2.0 scopes limit the set of resources an access token is permitted to access]]
