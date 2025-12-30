---
created: 2025-12-24
tags: [pki/ca]
sr-due:
sr-interval:
sr-ease:
---

A Root CA is the top-level Certificate Authority in a PKI hierarchy whose certificate is self-signed.
It signs its own certificate since there's no higher authority to sign it — it's the ultimate trust anchor.

The root certificate is pre-installed in operating systems, browsers, and devices during manufacturing or OS installation.
Your computer ships with around 150 root certificates from trusted CAs worldwide.

The root's private key is kept offline in maximum security — typically in an HSM within a vault.
Physical access controls, multiple authentication requirements, and audit logging protect this critical key.

Root CAs rarely issue end-entity certificates directly.
Instead, they sign intermediate CA certificates, which do the day-to-day certificate signing work.

This isolation protects the root private key.
If it's only used occasionally to sign intermediates, there's less exposure to potential attacks.

If a root private key is compromised, it's catastrophic.
All certificates signed by that root (and its intermediates) become untrustworthy.
The root must be removed from all trust stores globally — a massive, expensive operation.

Root certificates have very long validity periods, often 20-30 years.
This stability is important since changing roots requires updating billions of devices.

The self-signed nature doesn't make roots less trustworthy.
Trust comes from the rigorous vetting process before a root is included in OS/browser trust stores.

## Links
- [[Intermediate CA performs daily certificate signing operations]]
- [[Trust chain transfers trust from pre-installed root to end certificate]]
- [[Root certificate is pre-installed in operating system trust store]]
- [[Compromised root CA requires global trust store updates]]
- [[HSM protects private keys with tamper-resistant hardware]]
- [[PKI MOC]]
