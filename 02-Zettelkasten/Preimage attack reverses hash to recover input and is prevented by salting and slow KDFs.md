---
created: 2026-04-27
tags: [cryptography/hash, security/attacks]
aliases: [preimage attack, hash reversal attack]
sr-due:
sr-interval:
sr-ease:
---

A preimage attack tries to find an input that produces a specific hash output.

Real target: **password hashes stored in a database**.
Server stores `hash(password)`, never the password itself.
Attacker steals the DB → tries to reverse hashes → recovers passwords.

Cost: **2ⁿ** operations — must hit one specific target value.

---

### Prevention

**Strong algorithm** — SHA-256, bcrypt, Argon2. Never MD5 or SHA-1 for passwords.

**Salting** — add a random value before hashing: `hash(salt + password)`.
- Each password gets a unique salt stored alongside the hash
- Identical passwords produce different hashes
- Precomputed rainbow tables become useless — attacker must recompute per-entry

**Slow KDF** (bcrypt, Argon2, scrypt) — intentionally expensive to compute.
- Legitimate login: ~100ms, acceptable
- Attacker brute-forcing 1 billion guesses: years instead of seconds

---

### What preimage does NOT threaten

File checksums — the hash is public by design, not secret.
Digital signatures — attacker needs a *collision*, not a preimage (different attack).

---

### Read more

- [[Birthday problem explains why collision resistance requires double the security bits]]
- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Checksum verifies integrity but signature on checksum verifies authenticity]]
- [[KDF turns shared point into uniform cryptographic keys]]
