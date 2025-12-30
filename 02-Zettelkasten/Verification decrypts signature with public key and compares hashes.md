---
created: 2025-12-24
tags: [signatures/digital]
sr-due:
sr-interval:
sr-ease:
---

Signature verification reverses the signing process to confirm authenticity and integrity.
Anyone with the public key can verify signatures without needing the private key.

**Step 1: Hash the received message** using the same hash algorithm the signer used.
This produces a fresh hash value representing the current state of the data.

**Step 2: Decrypt the signature** with the signer's public key.
For RSA, this uses modular exponentiation with the public exponent.
For elliptic curve algorithms, this involves point operations on the curve.

**Step 3: Compare the two hash values**.
If the hash from the signature matches the hash of the received message, the signature is valid.

A match proves two things simultaneously:
The message hasn't been modified (integrity), and it was signed by the private key holder (authenticity).

Verification **does not** require knowledge of the private key.
This is the asymmetric property that makes digital signatures practical for public use.

The public key must be trusted to belong to the claimed signer.
Certificates from trusted CAs establish this trust relationship.

Verification fails if:
- The message was modified after signing
- The signature was created with a different private key
- The wrong public key is used for verification
- The hash algorithm doesn't match what was used for signing

**Certificate chain validation** often accompanies signature verification.
The verifier checks that the signing certificate is valid, not revoked, and chains to a trusted root.

Time is an important verification factor.
The signature must have been created while the certificate was valid (between notBefore and notAfter).

## Links
- [[Digital signature proves who signed and ensures message integrity]]
- [[Signing hashes message then encrypts hash with private key]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Certificate binds public key to verified identity]]
- [[Certificate chain includes end certificate plus all intermediates]]
- [[Public key encrypts while private key decrypts in asymmetric systems]]
- [[Digital Signatures MOC]]
