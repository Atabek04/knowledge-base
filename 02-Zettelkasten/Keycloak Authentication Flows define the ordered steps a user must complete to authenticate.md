---
aliases: [Keycloak authentication flows, authentication flows]
tags: [keycloak, security, authentication]
created: 2026-06-23
---

An <mark style="background: #FFF3A3A6;">authentication flow</mark> is a configurable pipeline of ordered steps Keycloak executes when a user tries to log in. Think of it like a Spring Security filter chain — each step either passes, fails, or delegates to the next, and the overall result decides whether login succeeds. What makes flows powerful is that they are fully pluggable: you can insert MFA, CAPTCHA, or custom business checks without touching application code.

---

### Built-in flows

Keycloak ships with several ready-made flows, each targeting a different login scenario:

- **Browser** — the standard login page flow. Handles cookie-based SSO, identity provider redirects, and the username/password form with optional 2FA. This is what runs when a user opens your app in a browser.
- **Direct Grant** — username and password submitted directly via the token endpoint (`/protocol/openid-connect/token`). Used by CLI tools and service integrations where there is no browser. Corresponds to the OAuth 2.0 Resource Owner Password Credentials grant.
- **Registration** — runs when a user self-registers. Can include profile collection, email verification, and CAPTCHA.
- **Reset Credentials** — the forgot-password flow. Verifies identity via email link before allowing a password change.
- **Client Authentication** — authenticates the client application itself (not the user), using client secrets or signed JWTs.

---

### Step requirement types

Each authenticator in a flow carries one of four requirement labels that control when it runs:

- <mark style="background: #FFF3A3A6;">**Required**</mark> — must succeed; failure stops the flow entirely.
- <mark style="background: #FFF3A3A6;">**Alternative**</mark> — one of several options the user can satisfy; if any Alternative in the group passes, the group passes.
- <mark style="background: #FFF3A3A6;">**Conditional**</mark> — the sub-flow runs only if attached condition authenticators evaluate to true (e.g., "user has OTP configured"). This is the modern replacement for the old Optional type.
- **Disabled** — step is skipped unconditionally; useful for temporarily removing an authenticator without deleting it.

<mark style="background: #FF5582A6;">Avoid the legacy **Optional** requirement</mark> — it was standard before Keycloak 19 but the Conditional sub-flow pattern is now the recommended approach. Optional remains in the UI for backward compatibility but should not be used in new flows.

---

### How the Browser flow is structured

The default Browser flow illustrates how sub-flows compose:

```
Browser flow
  ├── Cookie               (Alternative)  — pass if session cookie is valid
  ├── Identity Provider Redirector (Alternative)  — redirect if kc_idp_hint present
  └── Forms sub-flow       (Alternative)
        ├── Username Password Form  (Required)
        └── Conditional 2FA sub-flow  (Conditional)
              ├── Condition - User Configured  (Required)  — only run if OTP enrolled
              └── OTP Form  (Required)
```

<mark style="background: #ADCCFFA6;">The Cookie step is what enables SSO</mark> — if a valid session cookie exists for the realm, the user skips the login form entirely and lands straight in the app.

---

### Conditional OTP sub-flow evaluation

The Conditional 2FA sub-flow is the canonical way to make OTP optional per user. The evaluation order matters:

1. Keycloak checks the condition authenticators inside the sub-flow (e.g., `Condition - User Configured`).
2. If the condition fails (user has no OTP device enrolled), the entire sub-flow is skipped.
3. If the condition passes, all Required steps inside the sub-flow must complete.

<mark style="background: #FF5582A6;">When using IP-range-based OTP bypass (force vs skip headers), note that the force-OTP header match takes precedence over the skip-OTP header match</mark> — a request matching both is treated as forced OTP. Getting this backwards means a trusted-network header cannot silently bypass OTP when a force header is also matched.

---

### Customizing a flow

You never edit built-in flows directly — Keycloak marks them read-only. The customization pattern is:

1. Go to **Authentication → Flows**, find the built-in flow you want to extend.
2. Click **Duplicate** to create a copy in the same realm.
3. Add, remove, or reorder authenticators in the copy.
4. Change requirement labels as needed.
5. Bind the custom flow: for login flows, go to **Authentication → Bindings** and set "Browser Flow" (or whichever slot) to your copy.

<mark style="background: #BBFABBA6;">Example: adding WebAuthn as a second factor</mark> means duplicating Browser, expanding the Conditional 2FA sub-flow, and replacing (or adding alongside) the OTP Form with the WebAuthn Authenticator. The `Condition - User Configured` step automatically detects which credential type the user has enrolled, so users with OTP see the OTP form and users with a security key see the WebAuthn prompt — no code change in the application.

---

### Flow pluggability via SPIs

Flows are what make Keycloak extensible. Every box in the flow diagram is an `Authenticator` SPI implementation. <mark style="background: #ADCCFFA6;">Writing a custom authenticator means implementing the `Authenticator` and `AuthenticatorFactory` interfaces</mark>, packaging as a JAR, dropping it in Keycloak's provider directory, and then it appears in the flow editor as a selectable step. This is how teams inject CAPTCHA, risk scoring, or corporate SSO checks without forking Keycloak itself.

---

### Read more

- [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration]]
- [[A Keycloak client represents an application registered in a realm to delegate authentication]]
- [[Keycloak Identity Providers enable social login by federating external auth into a local realm]]
- [[Keycloak MFA adds a second authentication factor via OTP or WebAuthn]]
