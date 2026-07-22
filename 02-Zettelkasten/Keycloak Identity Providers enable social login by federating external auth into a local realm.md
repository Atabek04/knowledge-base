---
aliases: [Keycloak social login, Keycloak Identity Providers, identity brokering]
tags: [keycloak, security, authentication, federation]
created: 2026-06-23
---

<mark style="background: #FFF3A3A6;">Identity brokering</mark> is Keycloak's mechanism for acting as a middleman between your application and external identity providers like Google, GitHub, or any OIDC/SAML-compliant service. Your app never speaks directly to those providers — it only ever talks to Keycloak, which handles all the external communication on its behalf.

This means you ship one integration (your app → Keycloak) instead of N integrations (your app → Google, GitHub, Facebook, ...). Keycloak absorbs the complexity of each provider's SDK, token format, and redirect dance.

---

### How the brokering flow works

When a user clicks "Login with Google", Keycloak takes over completely:

1. Keycloak redirects the browser to Google's authorization endpoint.
2. Google authenticates the user and returns an <mark style="background: #FFF3A3A6;">ID token</mark> (OIDC) or an assertion (SAML) back to Keycloak's callback URL.
3. Keycloak validates the external token, then either finds or creates a local user in the [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration|realm]].
4. Keycloak issues its own Access Token, Refresh Token, and ID Token to your app — in the exact same shape as a local login.

Your app receives standard Keycloak tokens regardless of how the user authenticated. The external IdP is invisible to your application code.

---

### Account linking and first-login flow

#### Account linking

When a social user logs in for the first time, Keycloak needs to decide what to do with them. If a local account already exists with the same email address, Keycloak can <mark style="background: #FFF3A3A6;">link</mark> the social identity to it — so the user can log in with either their password or their Google account, and they land in the same local account.

If no match exists, Keycloak creates a new local user and stores the external identity as a federated credential tied to that user.

#### First-login flow

The <mark style="background: #FFF3A3A6;">First Login Flow</mark> is a configurable [[Keycloak Authentication Flows define the ordered steps a user must complete to authenticate|authentication flow]] that runs only when a social identity is seen for the first time. The default steps are:

- **Review Profile** — prompt the user to confirm or fill in missing profile fields (name, email) that the IdP may not have provided.
- **Account Linking** — if an existing local user matches by email, prompt the user to confirm they want to link the accounts.
- **Email Verification** — optionally verify the email the IdP returned before creating the local account.

You can customize or replace this flow entirely in the realm's Identity Provider settings.

---

### Configuring an Identity Provider

In the Keycloak Admin Console, go to **Identity Providers** in the realm sidebar. Keycloak ships built-in templates for:

- Google, GitHub, Facebook, Microsoft, Twitter — preconfigured OIDC/OAuth2 flows
- Generic OIDC provider — for any standards-compliant IdP
- SAML 2.0 provider — for enterprise federation (Active Directory, Okta, etc.)

Each provider needs at minimum a **Client ID** and **Client Secret** issued by the external service. Keycloak generates a **Redirect URI** you paste into the external provider's app settings.

#### IDP Mappers

After authentication, Keycloak runs <mark style="background: #BBFABBA6;">IDP mappers</mark> to translate claims from the external token into local user attributes or roles. For example, you can map the `email` claim from Google's ID token to the Keycloak user's email field, or map a GitHub organization membership to a Keycloak realm role. Mappers are configured per-provider in the **Mappers** tab.

---

### Account linking for existing users

A user who already has a local Keycloak account can link a social identity to it later via the <mark style="background: #ADCCFFA6;">Account Console</mark> (`/realms/{realm}/account`). Under **Linked Accounts**, they click "Link" next to any configured Identity Provider. Keycloak redirects them through the external IdP's login, then attaches the returned identity to their existing local account.

---

### Why this matters

Without Keycloak acting as a broker, your app would need to integrate each external IdP independently — each with its own SDK, token validation logic, and session handling. <mark style="background: #ADCCFFA6;">Keycloak abstracts all of that behind a single OIDC endpoint</mark>, so adding a new social login provider is a configuration change in the Admin Console, not a code change in your application.

The trade-off is that Keycloak becomes a critical dependency in your auth path. Its availability directly determines whether social logins work.

---

### Read more

- [[Keycloak Authentication Flows define the ordered steps a user must complete to authenticate]]
- [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration]]
- [[OpenID Connect adds an identity layer on top of OAuth 2.0 via the ID token]]
- [[A Keycloak client represents an application registered in a realm to delegate authentication]]
