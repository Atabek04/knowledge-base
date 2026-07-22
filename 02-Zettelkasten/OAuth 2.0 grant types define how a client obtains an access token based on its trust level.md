---
aliases: [OAuth grant types, grant types]
tags: [security, oauth, keycloak]
created: 2026-06-23
---

Every OAuth 2.0 flow starts with one question: <mark style="background: #FFF3A3A6;">how much can the authorization server trust this client?</mark> The answer determines which grant type the client is allowed to use. A grant type is not just a protocol step — it is the trust model encoded as a flow.

Think of it like Spring Security's authentication providers: each one handles a different credential type. Grant types do the same for OAuth clients.

### Authorization Code + PKCE

<mark style="background: #FFF3A3A6;">Authorization Code</mark> is the standard flow for any app that acts on behalf of a user — web apps, SPAs, and mobile clients. The user authenticates directly with the authorization server (e.g., Keycloak), which returns a short-lived `code` to the client. The client then exchanges that code for an access token via a back-channel call.

The critical add-on for public clients is <mark style="background: #FFF3A3A6;">PKCE (Proof Key for Code Exchange, RFC 7636)</mark>. A public client — a SPA or mobile app — cannot safely store a client secret. Without PKCE, an attacker who intercepts the authorization code (e.g., via a malicious redirect) can exchange it for a token. PKCE closes that gap.

#### How PKCE works

Before the redirect, the client generates a `code_verifier` — a cryptographically random string using a CSPRNG, with at least 256 bits of entropy in practice (RFC 7636 says "sufficient entropy" without naming a specific bit count). The character set is `[A-Za-z0-9\-._~]`, 43–128 characters; if you base64url-encode a 32-byte random buffer, strip the = padding.

The client sends a `code_challenge` with the authorization request:

```
code_challenge = BASE64URL(SHA256(ASCII(code_verifier)))   ← RFC 7636 §4.2
```

When exchanging the code for a token, the client sends the original `code_verifier`. The authorization server recomputes the hash and verifies they match. An intercepted code is useless without the verifier.

<mark style="background: #FF5582A6;">Always use `S256` as the challenge method. `plain` SHOULD NOT be used — it provides no security benefit over sending the verifier directly.</mark>

For confidential clients (server-side apps that can keep a secret), Authorization Code without PKCE is still valid under RFC 6749. Once OAuth 2.1 is finalized as an RFC, PKCE will be mandatory for all clients — plan for it now.

---

### Client Credentials

<mark style="background: #FFF3A3A6;">Client Credentials</mark> is for machine-to-machine communication where no user is involved. Service A presents its `client_id` and `client_secret` directly to the authorization server and receives an access token. There is no user login step, no redirect, no browser.

This is the right grant for a backend microservice calling another microservice — for example, a `report-service` calling `core-service`. The client is trusted because it holds a secret that only it and the authorization server know.

<mark style="background: #ADCCFFA6;">In Keycloak, the client must have "Service Accounts Enabled" turned on. The service account user is created automatically and is where you assign realm or client roles for that service.</mark>

---

### Device Authorization Flow

<mark style="background: #FFF3A3A6;">Device Authorization (RFC 8628)</mark> covers devices that have no browser or have constrained input — IoT devices, smart TVs, CLI tools. The device requests a `device_code` and a short URL (e.g., `https://example.com/activate`) from the authorization server, displays both to the user, and then polls until the user completes login on a separate browser. The grant type value is `urn:ietf:params:oauth:grant-type:device_code`.

---

### Deprecated: Resource Owner Password Credentials

<mark style="background: #FF5582A6;">ROPC (Resource Owner Password Credentials) MUST NOT be used — RFC 9700 §2.4.</mark> The client collects the user's username and password directly and sends them to the authorization server. This breaks the core OAuth promise: the user's credentials are exposed to the client application, not just to the authorization server. Any client storing or logging those credentials becomes a liability.

ROPC is omitted entirely from the OAuth 2.1 draft. In Keycloak, it is still available via the "Direct Access Grants" toggle — but enabling it is a deliberate step backward in security posture.

The <mark style="background: #FF5582A6;">Implicit grant (RFC 9700 §2.1.2) SHOULD NOT be used either</mark> — it returned tokens directly in the URL fragment, exposing them to browser history and referrer headers. Authorization Code + PKCE replaces it for all public clients.

---

### The pattern

| Grant type | Who is the client? | User involved? |
|---|---|---|
| Authorization Code + PKCE | Public or confidential app acting for a user | Yes |
| Client Credentials | Confidential service-to-service | No |
| Device Authorization | Browserless device acting for a user | Yes (on another device) |
| ~~ROPC~~ | ~~Any~~ | ~~Yes~~ — avoid |

<mark style="background: #ADCCFFA6;">The pattern to remember: grant type = trust model. The more the client can prove about itself (secret, PKCE verifier, device code round-trip), the simpler and more direct the flow. The less it can prove, the more the authorization server must verify through redirects and user interaction.</mark>

---

### Read more

- [[OAuth 2.0 delegates authorization by issuing scoped access tokens without exposing credentials]]
- [[A Keycloak client represents an application registered in a realm to delegate authentication]]
- [[OpenID Connect adds an identity layer on top of OAuth 2.0 via the ID token]]
