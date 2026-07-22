---
aliases: [Keycloak, Identity Management, IAM]
tags: [moc, keycloak, security, oauth, oidc, spring]
created: 2026-06-23
---

> Keycloak as an identity and access management platform — from core concepts (realms, clients, roles, tokens) through OAuth 2.0 / OIDC protocols, Spring Boot integration, and production deployment.

---

## Core Concepts

- [[A Keycloak realm is an isolated tenant that owns its own users, clients, roles, and configuration|Realm — isolated tenant owning users, clients, and config]]
- [[A Keycloak client represents an application registered in a realm to delegate authentication|Client — app registered in a realm to delegate auth]]
- [[A Keycloak user is a human account in a realm, distinct from a client application|User — human account, distinct from a client app]]
- [[Keycloak roles represent named permissions assigned to users, groups, or clients|Roles — named permissions assigned to users or groups]]
- [[Keycloak sessions track active logins and token lifetimes at the user and client level|Sessions — track active logins and token lifetimes]]
- [[Keycloak issues three token types — Access Token, Refresh Token, and ID Token|Token types — Access, Refresh, and ID Token]]

---

## Protocols

- [[OAuth 2.0 delegates authorization by issuing scoped access tokens without exposing credentials|OAuth 2.0 — delegates auth via scoped tokens, not credentials]]
- [[OpenID Connect adds an identity layer on top of OAuth 2.0 via the ID token|OIDC — adds identity layer on top of OAuth 2.0]]
- [[OAuth 2.0 grant types define how a client obtains an access token based on its trust level|Grant types — how a client obtains a token by trust level]]
- [[OAuth 2.0 scopes limit the set of resources an access token is permitted to access|Scopes — limit what resources an access token can reach]]

---

## Authentication Flows

- [[Keycloak Authentication Flows define the ordered steps a user must complete to authenticate|Auth Flows — ordered steps required to authenticate]]
- [[A Keycloak client's redirect URI allowlist restricts where the authorization code is sent after login|Redirect URIs — per-client allowlist of post-login return URLs]]
- [[Keycloak Identity Providers enable social login by federating external auth into a local realm|Identity Providers — federate external auth into a realm]]
- [[Keycloak MFA adds a second authentication factor via OTP or WebAuthn|MFA — second factor via OTP or WebAuthn]]

---

## Authorization

- [[RBAC in Keycloak grants access by mapping roles to users or groups inside a realm|RBAC — grants access by mapping roles to users or groups]]
- [[Keycloak Authorization Services enable ABAC through fine-grained policies and permissions|Authorization Services — ABAC via fine-grained policies]]

---

## JWT and Tokens

- [[A JWT is a self-contained signed token that carries claims verifiable without a server round-trip|JWT — self-contained signed token, no server round-trip]]
- [[Keycloak encodes realm and client roles inside the JWT under realm_access and resource_access|Keycloak JWT claims — roles under realm_access and resource_access]]
- [[A Keycloak protocol mapper writes a single claim into a token from user, role, or client data|Protocol mapper — one rule that injects one claim into a token]]
- [[A Keycloak client scope is a reusable bundle of mappers and roles shared across clients|Client scope — reusable mapper bundle shared across clients]]
- [[Token introspection validates a token by querying the authorization server instead of verifying locally|Token introspection — validates token via authorization server]]

---

## Spring Boot Integration

- [[Spring Security OAuth2 Resource Server validates JWTs issued by Keycloak without legacy adapters|Resource Server — validates Keycloak JWTs, no legacy adapters]]
- [[JwtAuthenticationConverter maps Keycloak JWT role claims to Spring Security GrantedAuthority objects|JwtAuthenticationConverter — maps JWT roles to GrantedAuthority]]
- [[Spring @PreAuthorize enforces method-level access control using Security Expression Language|@PreAuthorize — method-level access control via SpEL]]
- [[Testcontainers Keycloak extension spins up a real Keycloak instance for integration tests|Testcontainers Keycloak — real instance for integration tests]]

---

## Production

- [[Keycloak requires a relational database to persist realms, users, and sessions across restarts|DB backend — persists realms, users, and sessions]]
- [[Keycloak behind a reverse proxy needs KC_PROXY_HEADERS to trust forwarded request headers|Reverse proxy — KC_PROXY_HEADERS to trust forwarded headers]]
- [[Keycloak clustering uses embedded Infinispan to replicate sessions across nodes|Clustering — Infinispan replicates sessions across nodes]]

---

## Related

- [[Security - MOC]]
- [[Spring Ecosystem - MOC]]
