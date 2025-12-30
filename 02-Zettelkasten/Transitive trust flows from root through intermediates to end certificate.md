---
created: 2025-12-24
tags: [pki/trust]
sr-due:
sr-interval:
sr-ease:
---

Transitive trust is the principle that trust can flow through a chain of signed certificates.
If you trust A, and A vouches for B (by signing B's certificate), then you trust B.

This enables scalable PKI without requiring every end certificate to be individually trusted.
You only need to trust a small number of root CAs, not millions of end-entity certificates.

The flow works through cryptographic signatures at each level.
Root CA signs intermediate → your trust in root transfers to intermediate.
Intermediate signs end certificate → your trust in intermediate transfers to end certificate.

Each signature proves the signer vouches for the signed certificate.
The root says "I trust this intermediate," the intermediate says "I trust this server."

Verification confirms each link in the trust chain.
Check intermediate's signature using root's public key, check end certificate's signature using intermediate's public key.

If any link breaks — invalid signature, expired certificate, revoked certificate — the entire chain fails.
Trust is all-or-nothing; partial chains don't work.

This model mirrors real-world trust relationships.
You trust your friend, your friend trusts their colleague, so you give some trust to the colleague.

The system assumes CAs are careful about what they sign.
If a CA signs certificates carelessly, they're vouching for untrustworthy entities, breaking the trust model.

## Links
- [[Trust chain transfers trust from pre-installed root to end certificate]]
- [[Root CA is ultimate trust anchor with self-signed certificate]]
- [[Intermediate CA performs daily certificate signing operations]]
- [[Browser builds chain from server certificate to trusted root]]
- [[PKI MOC]]
