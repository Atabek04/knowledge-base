---
aliases: [Primary Key, PK, surrogate key, natural key]
tags: [database, sql, relational-model, fundamentals]
created: 2026-05-26
---

### Why the problem exists

A table without a reliable row identifier is unusable at scale.
Imagine a `users` table with 10 million rows — how do you update *one specific user* without accidentally touching others with the same name or email?

You can't. That's the problem a primary key solves.

---

### What a primary key does

A primary key (PK) is a column (or set of columns) that the database engine guarantees to be:

- **NOT NULL** — every row must have a value
- **UNIQUE** — no two rows share the same PK value

These two constraints together mean: every row has exactly one identity, and no two rows share it.

---

### Four reasons PKs are non-negotiable

**1. Row identity**
Without a PK, there is no stable, unambiguous way to refer to a single row.
`UPDATE users SET email = '...' WHERE name = 'John'` fails if two Johns exist.
`UPDATE users SET email = '...' WHERE id = 42` always works.

**2. Referential integrity via foreign keys**
Other tables reference rows using the PK.
A `orders.user_id` column is a <mark style="background: #93d4d4">foreign key</mark> pointing to `users.id`.
The DB engine enforces that every `user_id` in `orders` must exist in `users.id` — this is referential integrity.
Without a PK, foreign keys cannot exist, and the relational model breaks down.

**3. Automatic index → fast lookups**
Every PK automatically creates a unique index.
`SELECT * FROM users WHERE id = 42` hits the index and reads one page — O(log n), not a full scan.
This is why PKs are always the cheapest lookup path.

**4. JOIN anchor**
JOINs work by matching FK values to PK values.
The PK is the anchor that makes multi-table queries coherent and fast.

---

### Natural key vs surrogate key

| Type | Example | When to use |
|------|---------|-------------|
| **Natural key** | `passport_number`, `email` | When the domain guarantees global uniqueness and the value never changes |
| **Surrogate key** | `BIGINT` auto-increment, `UUID` | Default choice — decouples identity from business data |

**Rule of thumb:** prefer surrogate keys.
Natural keys look stable but change (emails get updated, passport numbers get reissued).
Changing a PK cascades to every FK reference — expensive and risky.

---

### Surrogate key types: BIGINT vs UUID

| | `BIGINT` (auto-increment) | `UUID v4` |
|--|--|--|
| **Size** | 8 bytes | 16 bytes |
| **Insert pattern** | Sequential → no index fragmentation | Random → B-tree page splits, fragmentation |
| **Distributed safe** | No — single sequence, not mergeable | Yes — generated independently on any node |
| **Readability** | Easy to debug | Opaque |

<mark style="background: #f9a8d4">Warning:</mark> UUID v4 as a PK in PostgreSQL causes write amplification due to random inserts into the B-tree index.
Use `UUID v7` (time-ordered) or `BIGINT` for high-write tables.

---

### Composite primary key

A PK can span multiple columns: `PRIMARY KEY (order_id, product_id)`.

Use it for pure join tables (many-to-many mapping).
Avoid it for entity tables — composite PKs make FK references verbose and JOINs harder to read.

---

### What happens without a PK

- No FK references → no relational integrity
- No unique index → full scans on every lookup
- Duplicate rows become possible → data corruption
- ORM frameworks (JPA/Hibernate) require `@Id` — they refuse to map entities without a PK

---

Read more:
- [[PostgreSQL transactions wrap multiple operations in an atomic unit with automatic rollback on failure]]
- [[Databases - MOC]]
