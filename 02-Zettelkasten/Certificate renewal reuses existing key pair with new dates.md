---
created: 2025-12-24
tags: [pki/lifecycle]
sr-due:
sr-interval:
sr-ease:
---

Certificate renewal creates a new certificate for the same public key with updated validity dates.
You keep using your existing private-public key pair and just get a fresh certificate.

The process is simpler than initial issuance since verification may be streamlined.
Some CAs fast-track renewals for existing customers or require less documentation.

You generate a new CSR using the same public key as the expiring certificate.
The CSR signature proves you still control the corresponding private key.

After verification, the CA issues a new certificate with fresh validity dates.
The serial number changes, but the public key remains identical.

Renewal is faster and more convenient than re-keying.
No need to update the private key on servers, redeploy applications, or update configurations.

However, security best practice recommends periodic re-keying (generating new key pairs).
Using the same key indefinitely increases exposure if the key is eventually compromised.

Many organizations renew 2-3 times with the same key, then re-key.
This balances operational simplicity with security.

Automated renewal systems like certbot default to renewal with the same key.
Manual intervention is required if you want to generate new keys.

Renewal should start well before expiration — typically 30 days prior.
This provides a buffer for any verification issues or technical problems.

## Links
- [[Certificate expiration automatically invalidates after validity period]]
- [[Certificate re-issuance generates fresh key pair for security]]
- [[Certificate issuance begins with key pair generation]]
- [[PKI MOC]]
