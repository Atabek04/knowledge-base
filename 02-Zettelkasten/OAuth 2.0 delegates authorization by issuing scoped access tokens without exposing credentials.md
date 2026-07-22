---
aliases: [OAuth 2.0, OAuth2]
tags: [security, oauth, authorization, keycloak]
created: 2026-06-23
---

<mark style="background: #FFF3A3A6;">OAuth 2.0 is an authorization framework</mark> (RFC 6749, updated by security BCP RFC 9700) that lets a third party act on your behalf without ever seeing your password. The core insight is simple: instead of handing over your credentials, you issue a limited-access token — like giving a valet a card that only opens the parking garage, not your hotel room.

It solves the <mark style="background: #FFF3A3A6;">delegated authorization</mark> problem. Before OAuth, if you wanted app A to read your emails on service B, you had to give A your password for B. OAuth replaces that with a negotiated token whose permissions are explicit and revocable.

---

### The four roles

OAuth 2.0 defines four actors (RFC 6749 §1.1):

- **Resource Owner** — the user who owns the data (you)
- **Resource Server** — the API that holds the data (Google Drive, GitHub API)
- **Client** — the application requesting access (a third-party app)
- **Authorization Server** — the authority that issues tokens (Keycloak, Google, GitHub OAuth)

The Client never touches the Resource Owner's credentials. It negotiates with the Authorization Server, receives a token, and presents that token to the Resource Server.

---

### What an access token is

An <mark style="background: #FFF3A3A6;">access token</mark> is a credential that represents a specific authorization grant. It encodes:

- **Who** authorized it (the resource owner)
- **For whom** it was issued (the client)
- **What** it permits (scopes)
- **Until when** it is valid (expiry)

Tokens are intentionally short-lived. When they expire, the client uses a refresh token to get a new one — without bothering the user again.

The Resource Server validates the token and serves the request. It does not need to call the Authorization Server for every request if the token is a [[A JWT is a self-contained signed token that carries claims verifiable without a server round-trip|self-contained JWT]].

---

### OAuth 2.0 does NOT prove identity

This is the most important boundary to understand: <mark style="background: #FF5582A6;">OAuth 2.0 is about authorization — who can do what. It says nothing about who the user is.</mark>

An access token tells the Resource Server "this client is allowed to read your contacts." It does not tell the client "the person who authorized this is Alice, born 1990, email alice@example.com."

Identity is the job of [[OpenID Connect adds an identity layer on top of OAuth 2.0 via the ID token|OIDC]], which adds an ID token on top of OAuth 2.0 for that purpose. Mixing these up is a classic security mistake — do not use the access token to derive user identity.

---

### Scopes constrain what the token permits

<mark style="background: #FFF3A3A6;">Scopes</mark> are the mechanism for expressing "what." The client requests a set of scopes when initiating a flow; the Authorization Server may grant all, some, or none. The issued token carries only the granted scopes.

This principle of least privilege means a token for `read:contacts` cannot be used to delete contacts even if the user has that permission. See [[OAuth 2.0 scopes limit the set of resources an access token is permitted to access|scopes]] for the full picture.

---

### How a token is obtained — the grant

The exact sequence for obtaining a token depends on the client type and context. This is called a <mark style="background: #FFF3A3A6;">grant type</mark>. The most important is the Authorization Code flow (with PKCE for public clients): the user logs in at the Authorization Server, which redirects back to the client with a short-lived code; the client exchanges the code for tokens server-to-server.

Different trust levels require different grants. See [[OAuth 2.0 grant types define how a client obtains an access token based on its trust level|grant types]] for all flows including Device, Client Credentials, and the deprecated Implicit and ROPC grants.

---

### What OAuth 2.0 does not cover

OAuth 2.0 defines the *framework*, not the wire details. It does not specify:

- <mark style="background: #ADCCFFA6;">Token format</mark> — JWT is common but not mandated by RFC 6749
- <mark style="background: #ADCCFFA6;">How the Resource Server validates a token</mark> — introspection endpoint, local JWT verification, or both
- <mark style="background: #ADCCFFA6;">User identity</mark> — that is OIDC's extension

This separation keeps the protocol composable: OIDC layers identity on top, RFC 7662 adds introspection, RFC 7636 adds PKCE, all as extensions.

---

### Read more

- [[OpenID Connect adds an identity layer on top of OAuth 2.0 via the ID token]]
- [[OAuth 2.0 grant types define how a client obtains an access token based on its trust level]]
- [[OAuth 2.0 scopes limit the set of resources an access token is permitted to access]]
- [[A JWT is a self-contained signed token that carries claims verifiable without a server round-trip]]
