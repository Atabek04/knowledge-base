---
created: 2026-04-27
tags: [cryptography/asymmetric, cryptography/symmetric]
aliases: [encryption size limits, why encryption uses chunks]
sr-due:
sr-interval:
sr-ease:
---

Both asymmetric and symmetric algorithms have size constraints — but for completely different reasons.

---

### Asymmetric — hard mathematical limit

RSA works by: `message^e mod n`

The message must be a number **smaller than n** (the key modulus).
RSA-2048 → n is 2048 bits → max input ~256 bytes.

This is not an engineering choice — it is the math itself.
No mode of operation can work around it — the constraint is in the formula, not the implementation.

<mark style="background: #FF5582A6;">**Asymmetric is never used to encrypt data directly.**</mark>
It encrypts only small things: a session key, a hash, a short token.

Symmetric solves the large-data problem via block chaining modes (CBC, CTR, GCM).
Asymmetric has no equivalent — instead of solving the size problem, the design avoids it entirely by delegating bulk encryption to symmetric.

---

### Symmetric — engineering choice

AES was designed to operate on fixed **128-bit (16-byte) blocks**.
Matches CPU register sizes and hardware acceleration circuits (AES-NI).

No fundamental mathematical constraint — it is a deliberate design for speed and simplicity.
Modes of operation (CBC, CTR, GCM) chain blocks to handle arbitrary-length data.

---

### Why this forces hybrid encryption

| Algorithm | Max input | Used for |
|---|---|---|
| RSA / GOST | ~256 bytes | encrypting session keys, signing hashes |
| AES / symmetric | unlimited (via modes) | encrypting actual data |

Hybrid encryption exists because of these limits:
asymmetric handles key exchange, symmetric handles bulk data.

---

### Read more

- [[Block cipher processes fixed-size data chunks]]
- [[Hybrid encryption uses asymmetric to exchange key then symmetric to encrypt data]]
- [[Asymmetric cryptography uses public-private key pairs]]
- [[Hashing before signing is required because asymmetric algorithms cannot process arbitrary-length data]]
- [[Mode of operation defines how block cipher processes long messages]]
