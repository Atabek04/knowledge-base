---
created: 2026-06-12
tags: [postgresql, database, concurrency, transactions, locking]
aliases: [optimistic locking, pessimistic locking, optimistic vs pessimistic locking]
---

Once you know a [[A lost update occurs when two transactions read a row then both write and the second write erases the first|lost update]] can happen, there are two opposite philosophies for stopping it. They differ in *when* they deal with the conflict — up front, or at the last moment. Their names tell you which.

---

### Pessimistic — assume conflict, lock first

**Pessimistic** locking *expects* a clash, so it takes a lock **before** touching the data and makes everyone else wait. No two writers ever overlap, so a lost update is impossible by construction.

In PostgreSQL this is a [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race|locking read with `FOR UPDATE`]] (Spring Data JPA's `@Lock(PESSIMISTIC_WRITE)`). The name fits: you're <mark style="background: #FFF3A3A6;">pessimistic</mark> — you presume a collision and pay the locking cost to prevent it.

Best when contention is **high** — conflicts are likely, so blocking up front is cheaper than constantly retrying.

---

### Optimistic — assume no conflict, check at write

**Optimistic** locking *bets* there's no clash, so it takes **no lock**. Everyone reads freely; at write time you verify nothing changed underneath you — usually by comparing a **version number** or timestamp. If it moved, your write is rejected and you retry.

This is what [[ETag header enables optimistic concurrency by rejecting updates based on stale resource versions|the ETag version-compare]] does on the web, and what a JPA `@Version` column does in the database. The name fits: you're <mark style="background: #FFF3A3A6;">optimistic</mark> — you assume success and only pay if the rare conflict actually happens.

Best when contention is **low** — conflicts are rare, so skipping the lock and occasionally retrying beats locking everyone.

---

### The core trade-off

<mark style="background: #ABF7F7A6;">Pessimistic pays a guaranteed cost (locking, waiting) to avoid conflict. Optimistic pays nothing up front but a retry cost when conflict strikes.</mark> Pick by how often writers actually collide.

---

### Read more

- [[A lost update occurs when two transactions read a row then both write and the second write erases the first]]
- [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race]]
- [[ETag header enables optimistic concurrency by rejecting updates based on stale resource versions]]
