---
created: 2026-04-27
tags: [cryptography/hash]
aliases: [birthday problem, birthday bound, birthday attack]
sr-due:
sr-interval:
sr-ease:
---

The birthday problem is a probability insight:
in a group of 23 people, there's a ~50% chance two share a birthday.

Why so few? Because you're not asking "does someone share *my* birthday?"
You're asking "does *any pair* share a birthday?" — every pair is a candidate.
365 days, but only 23 people needed. The search space collapses.

---

### Two different attack goals

**Preimage attack** — you have a specific hash, find an input that produces it.

> Attacker sees `hash(contract.pdf)` and wants to forge a doc matching that exact hash.
> Must hit one specific target → cost: **2ⁿ**

**Collision attack** — find *any two inputs* that produce the same hash. No specific target.

> Attacker prepares `contract_good.pdf` and `contract_evil.pdf` with identical hashes.
> Gets you to sign the good one, swaps it. Any match counts → cost: **2^(n/2)**

Birthday analogy applied:
- Preimage = "find someone who shares *your* birthday" → need ~183 people
- Collision = "find *any two* people who share a birthday" → need only 23 people

Same principle. Collision is exponentially cheaper because no specific target.

---

### Why this forces double the bits

To achieve 128-bit security (attacker needs 2¹²⁸ operations):
- Preimage resistance → 128-bit hash is enough (cost = 2¹²⁸)
- Collision resistance → need 256-bit hash (birthday bound halves it: 2²⁵⁶ / 2 = 2¹²⁸)

**128-bit security always requires 256-bit hash output.**

---

### Why MD5 broke

MD5 = 128-bit output → collision resistance = 2⁶⁴.

2⁶⁴ sounds large, but it's reachable with modern hardware.
In 2004, researchers found real MD5 collisions using differential cryptanalysis — not random guessing, but mathematical exploitation of MD5's internal structure.
By 2008, forged SSL certificates using MD5 collisions were demonstrated in practice.

---

### Read more

- [[Hashing produces fixed-length fingerprint that cannot be reversed]]
- [[Signing hashes message then encrypts hash with private key]]
- [[Checksum verifies integrity but signature on checksum verifies authenticity]]
- [[Collision attack forges signatures by finding two inputs with the same hash]]
- [[Preimage attack reverses hash to recover input and is prevented by salting and slow KDFs]]
