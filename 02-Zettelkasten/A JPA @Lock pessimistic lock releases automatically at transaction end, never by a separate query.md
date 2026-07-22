---
created: 2026-07-22
tags: [database/concurrency, spring, jpa, locking]
aliases: [Lock releases at transaction end, pessimistic lock release, when does FOR UPDATE release]
---

When you put `@Lock(LockModeType.PESSIMISTIC_WRITE)` on a Spring Data repository method, a natural question is: how do you *let go* of the lock afterward? Is there an unlock call, a second query?

No. <mark style="background: #FFF3A3A6; font-weight: bold;">The lock releases automatically when the transaction ends — at `COMMIT` or `ROLLBACK` — and there is no separate query, no unlock statement.</mark> The lock's lifetime *is* the transaction's lifetime.

---

### What @Lock actually changes

`@Lock` only affects the **`SELECT` that Hibernate generates** — it appends `FOR UPDATE` to it. That is the whole mechanism.

```kotlin
@Lock(LockModeType.PESSIMISTIC_WRITE)
@Query("select b from Booking b where b.iin = :iin")
fun findByIinForUpdate(iin: String): Booking?
// → SELECT ... FROM booking WHERE iin = ? FOR UPDATE
```

Releasing isn't a second SQL statement you issue — it's the [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race|FOR UPDATE row lock]] being dropped by the database the moment the surrounding transaction commits or rolls back.

---

#### It does nothing without an open transaction

Because the release point *is* the transaction boundary, <mark style="background: #FF9E9EA6; font-weight: bold;">`@Lock` is meaningless without an open `@Transactional`</mark> — there's no transaction for the lock to live inside. Call the method with no active transaction and the pessimistic lock has nothing to hold to (Hibernate throws, or the `FOR UPDATE` is applied to an auto-commit statement that releases instantly — either way you get no protection).

This is also why <mark style="background: #ADCCFFA6; font-weight: bold;">a long `@Transactional` = a long-held lock.</mark> You don't control the release with a call; you control it by how long the transaction stays open — which is exactly why you keep slow work (like [[External HTTP calls inside a transaction hold the row lock while you wait on another service|external HTTP calls]]) *out* of the transaction.

---

### Read more

- [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race]]
- [[External HTTP calls inside a transaction hold the row lock while you wait on another service]]
- [[Optimistic and pessimistic locking are two strategies for preventing lost updates]]
- [[Database Transactions & Concurrency - MOC]]
