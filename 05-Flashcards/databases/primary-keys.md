TARGET DECK: Tech-KB::Databases::SQL Fundamentals
Tags: database sql relational-model
**Chapter:** SQL Fundamentals
**Related:** [[Databases - MOC]]

---

START
Coding Questions
What two constraints does a database engine enforce on a primary key column?
Back:
- **NOT NULL** — every row must have a value
- **UNIQUE** — no two rows share the same PK value

Together: every row has exactly one identity, and no two rows share it.
Tags: database sql relational-model fundamentals
END

START
Coding Questions
What are the four reasons a primary key is non-negotiable in a relational table?
Back:
1. **Row identity** — stable, unambiguous reference to a single row; `WHERE id = 42` always targets exactly one row
2. **Referential integrity** — foreign keys can only reference a PK; without it, cross-table relationships cannot be enforced
3. **Automatic index** — PK auto-creates a unique index → O(log n) lookup instead of full scan
4. **JOIN anchor** — JOINs match FK values to PK values; PK makes multi-table queries coherent and fast
Tags: database sql relational-model fundamentals
END

START
Coding Questions
How does a primary key enable referential integrity?
Back:
**Referential integrity** = guarantee that a FK value always points to an existing row.

- FK column (e.g. `orders.user_id`) references the PK of another table (`users.id`)
- DB engine enforces: every `user_id` in `orders` must exist in `users.id`
- Without a PK, FK constraints cannot be defined → relational model breaks down
Tags: database sql relational-model foreign-key
END

START
Coding Questions
Why does a primary key speed up row lookups?
Back:
Every PK **automatically creates a unique index** on that column.

`SELECT * FROM users WHERE id = 42` → hits the B-tree index → reads one page → **O(log n)**, not a full table scan.

This is why the PK is always the cheapest lookup path in any query.
Tags: database sql index performance
END

START
Coding Questions
What is the difference between a natural key and a surrogate key? When should you prefer each?
Back:
| Type | Example | When to use |
|------|---------|-------------|
| **Natural key** | `passport_number`, `email` | Domain guarantees global uniqueness AND value never changes |
| **Surrogate key** | `BIGINT` auto-increment, `UUID` | Default choice — decouples identity from business data |

**Rule:** prefer surrogate keys.
Natural keys appear stable but change (emails get updated, passports reissued).
Changing a PK cascades to every FK reference — expensive and risky.
Tags: database sql relational-model surrogate-key natural-key
END

START
Coding Questions
What are the tradeoffs between BIGINT and UUID v4 as a surrogate primary key?
Back:
| | `BIGINT` (auto-increment) | `UUID v4` |
|--|--|--|
| **Size** | 8 bytes | 16 bytes |
| **Insert pattern** | Sequential → no B-tree fragmentation | Random → page splits, write amplification |
| **Distributed safe** | No — single sequence | Yes — generated on any node independently |
| **Readability** | Easy to debug | Opaque |

Use `BIGINT` for single-node high-write tables.
Use `UUID v7` (time-ordered) for distributed systems — avoids fragmentation.
Tags: database sql surrogate-key uuid bigint performance
END

START
Coding Questions
Why is UUID v4 problematic as a primary key in PostgreSQL on high-write tables?
Back:
UUID v4 values are **random** → inserts land at random positions in the B-tree index.

This causes:
- **Page splits** — new pages allocated constantly
- **Index fragmentation** — pages fill unevenly, wasted space
- **Write amplification** — more I/O per insert than sequential keys

Fix: use **UUID v7** (time-ordered) or `BIGINT` auto-increment for high-write tables.
Tags: database postgresql uuid performance index
END

START
Coding Questions
When should you use a composite primary key, and when should you avoid it?
Back:
**Use composite PK when:**
- Pure join/mapping table (many-to-many): `PRIMARY KEY (order_id, product_id)`
- The combination is the identity — no other natural surrogate needed

**Avoid composite PK for entity tables:**
- FK references become verbose (must include all PK columns)
- JOINs get harder to read and maintain
- ORM mapping is more complex
Tags: database sql composite-key design
END

START
Coding Questions
What happens to a table that has no primary key?
Back:
- No FK references possible → **no referential integrity** across tables
- No unique index → every lookup requires a **full table scan**
- **Duplicate rows** become possible → silent data corruption
- ORM frameworks (JPA/Hibernate) require `@Id` → **refuse to map the entity**
Tags: database sql relational-model fundamentals
END
