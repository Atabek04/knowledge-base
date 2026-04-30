---
created: 2026-04-27
tags: [cryptography/hash, security/attacks]
aliases: [collision attack, hash collision attack]
sr-due:
sr-interval:
sr-ease:
---

A collision attack finds two different inputs that produce the same hash output.

Real target: **digital signatures**.

Attack steps:
1. Attacker crafts `doc_good` and `doc_evil` with identical hashes
2. Gets victim to sign `doc_good`
3. Swaps it with `doc_evil` — signature still validates (same hash)

Cost: **2^(n/2)** operations — no specific target, any matching pair works.
Cheaper than preimage by the [[Birthday problem explains why collision resistance requires double the security bits|birthday bound]].

---

### Prevention

**Strong hash algorithm** — SHA-256+, Streebog (GOST R 34.11).
MD5 broken since 2004, SHA-1 broken since 2017 (Google SHAttered attack forged SSL certs).

**Algorithm enforcement** — CA/browsers reject signatures using weak algorithms outright.
No negotiation — if SHA-1 is used, certificate is rejected.

**Timestamp in signature** — CMS and ЭЦП embed signing time.
Makes it harder to reuse a forged signature across different documents.

---

### Collision does NOT require the private key

Public key lets anyone verify — not forge.
Forgery exploits the hash function weakness, not the asymmetric algorithm.
Two independent security layers — breaking one does not break the other.

---

### Read more

- [[Birthday problem explains why collision resistance requires double the security bits]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Signing hashes message then encrypts hash with private key]]
- [[Checksum verifies integrity but signature on checksum verifies authenticity]]
- [[Preimage attack reverses hash to recover input and is prevented by salting and slow KDFs]]
