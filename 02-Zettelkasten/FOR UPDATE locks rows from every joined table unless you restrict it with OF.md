---
created: 2026-06-12
tags: [database, sql, postgresql, concurrency, locking]
aliases: [FOR UPDATE OF, lock specific table]
---

A [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race|locking read]] on a single table is obvious — it locks that table's matching rows. On a **join** it is not: a bare `FOR UPDATE` locks rows from *every* table that contributed to the result, not just the one you care about.

That silent over-locking is a classic source of contention you never meant to create.

---

### Default — every contributing table is locked

```sql
SELECT s.slot_id
FROM slot s JOIN resource r ON r.id = s.resource_id
WHERE s.status = 'OPEN'
FOR UPDATE;            -- locks matching rows in BOTH slot AND resource
```

You wanted to claim a `slot`. But <mark style="background: #FFB8EBA6;">the `resource` rows that joined in are locked too</mark>. Anyone else reading those resources `FOR UPDATE` — even for unrelated work — now blocks on you.

---

### OF names which tables to lock

Append `OF <table>` to restrict the lock to specific tables; the rest are read normally:

```sql
SELECT s.slot_id
FROM slot s JOIN resource r ON r.id = s.resource_id
WHERE s.status = 'OPEN'
FOR UPDATE OF s;       -- lock only slot rows; resource is just read
```

The name is the mnemonic: lock the rows <mark style="background: #FFF3A3A6; font-weight: bold;">**OF** these named tables</mark>, leave the others untouched.

<mark style="background: #ABF7F7A6;">Rule of thumb: on any `FOR UPDATE` that joins, always add `OF` for the table you actually intend to claim</mark> — otherwise you lock more than you think.

---

### Read more

- [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race]]
- [[FOR UPDATE locks rows beneath LIMIT and OFFSET in the query plan]]
- [[A locking read wait policy decides whether it blocks errors or skips a row another transaction locked]]
