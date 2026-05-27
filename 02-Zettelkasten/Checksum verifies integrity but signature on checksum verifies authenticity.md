---
created: 2026-04-27
tags: [cryptography/hash, signatures/digital]
aliases: [checksum trust chain, checksum vs signature]
sr-due:
sr-interval:
sr-ease:
---

A checksum (hash) proves a file wasn't corrupted in transit.
It does not prove the file came from a legitimate source.

If an attacker compromises the server, they can replace both the file and its checksum.
Checksum alone cannot detect this — it only detects accidental corruption.

---

### Full trust chain

Authenticity requires a signature on top of the checksum:

1. Developer hashes the file → checksum
2. Developer signs the checksum with their private key
3. You verify the signature using the developer's public key (trusted separately)
4. You compare the checksum against your downloaded file

| What it proves | Mechanism |
|---|---|
| File not corrupted | Checksum matches |
| File came from real author | Signature on checksum is valid |

---

### How trust is established in practice

- **HTTPS download page** — TLS cert proves you're on the real site; checksum published there is trustworthy
- **GPG-signed release** — developer's public key published independently; signature verifiable offline
- **Package managers** (apt, Maven, npm) — repository has its own signing key, verified automatically

---

### Read more

- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Digital signature proves who signed and ensures message integrity]]
- [[Signing hashes message then encrypts hash with private key]]
