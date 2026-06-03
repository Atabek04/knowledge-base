> Application and API security for backend services

---

## Progress

- [ ] Authentication & authorization
- [ ] Token-based auth (OAuth2, OIDC, JWT)
- [ ] Application security (OWASP)
- [ ] Secret management

---

## Topics

### Authentication & Authorization
- [ ] Authentication vs authorization
- [ ] Session management — stateful vs stateless
- [ ] RBAC vs ABAC
- [ ] Method-level authorization

### OAuth2 & OIDC
- [ ] OAuth2 flows — authorization code, client credentials, device flow
- [ ] OIDC — ID token, UserInfo endpoint
- [ ] Resource server vs authorization server
- [ ] Token introspection

### JWT
- [ ] Structure — header, payload, signature
- [ ] Validation — signature, claims, expiry
- [ ] Refresh token rotation
- [ ] Storage and revocation trade-offs

### Application Security (OWASP)
- [ ] OWASP Top 10 — injection, broken auth, XSS, IDOR, SSRF
- [ ] Input validation and sanitization
- [ ] SQL injection prevention — parameterized queries
- [ ] CSRF and CORS protection
- [ ] Security headers (CSP, HSTS)

### Secret Management
- [ ] Never store secrets in code or plain env vars in prod
- [ ] HashiCorp Vault — secret engines, dynamic secrets
- [ ] Cloud secret stores (AWS Secrets Manager, Parameter Store)
- [ ] Secret rotation

### Transport Security
- [ ] TLS / HTTPS
- [ ] mTLS for service-to-service auth

---

## Books

| Book | Priority | Status |
|------|----------|--------|
| **Spring Security in Action** — Manning | Important | ⏳ |

---

## Related
- [[Spring Ecosystem - MOC]] — Spring Security implementation
- [[API Design - MOC]] — API authentication & CORS
- [[AWS - MOC]] — IAM, KMS, Secrets Manager
