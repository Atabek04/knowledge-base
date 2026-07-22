---
aliases: [redirect URI allowlist, Keycloak redirect URI, valid redirect URIs]
tags: [keycloak, security, oauth, oidc]
created: 2026-06-30
---

In any login flow that redirects the user's browser (the Authorization Code Flow), Keycloak authenticates the user and then has to send the resulting authorization code *somewhere* — back to the app that started the login. The <mark style="background: #FFF3A3A6;">redirect URI allowlist</mark> is how a [[A Keycloak client represents an application registered in a realm to delegate authentication|client]] declares the exact URLs Keycloak is permitted to send that code to.

It is configured **per client**, at registration time — one of the core properties that defines a client alongside its `client_id` and type.

---

### Exact-match allowlist

After the user authenticates, Keycloak returns the authorization code only to a URI that <mark style="background: #FFF3A3A6;">exactly matches an entry in the client's list</mark>. A request asking to be redirected anywhere else is rejected before any code is issued.

During development `http://localhost:3000/*` is common. In production only the real, exact application URLs belong in the list.

---

### Why it is a security control

Without the allowlist, an attacker could start a login against your client but ask Keycloak to send the authorization code to <mark style="background: #FF5582A6;">a server they control</mark>. They'd capture a valid code for your client and exchange it for tokens — an *authorization code interception* attack.

The allowlist closes that hole: the code can only ever land on a URL you pre-approved, so an attacker-controlled return address is refused.

#### Wildcards in production are a misconfiguration

<mark style="background: #FF5582A6;">A wildcard URI (`*`, or a broad `https://*.example.com/*`) in production defeats the control</mark> — it re-opens redirects to any path or subdomain an attacker can reach. Keep wildcards to local development only; list exact URLs in production.

---

### Read more

- [[A Keycloak client represents an application registered in a realm to delegate authentication]]
- [[OAuth 2.0 grant types define how a client obtains an access token based on its trust level]]
- [[Keycloak Authentication Flows define the ordered steps a user must complete to authenticate]]
