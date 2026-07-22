---
created: 2026-07-22
tags: [database/concurrency, transactions, spring, locking]
aliases: [external call in transaction, HTTP inside transactional, lock held during HTTP]
---

A `@Transactional` method holds its database connection — and any row locks it took — from the moment the transaction opens until the method returns. Usually that window is a few milliseconds of local writes. But the instant you put an **external HTTP call** inside that window, the lock duration becomes *your DB work + someone else's network latency*, which you don't control.

This is why a common system-wide invariant is: <mark style="background: #FFF3A3A6; font-weight: bold;">read and call external services *before* opening the write transaction — never make an outbound HTTP call inside `@Transactional`.</mark> The transaction wraps only the local writes; everything slow and foreign stays outside it.

---

### The problem

You gate a booking on an external eligibility service, then save. The repository method takes a pessimistic lock so two concurrent requests can't both confirm the same booking:

```kotlin
interface BookingRepository : JpaRepository<Booking, UUID> {

    // @Lock adds FOR UPDATE to the SELECT — the row is locked, not just read
    @Lock(LockModeType.PESSIMISTIC_WRITE)
    @Query("select b from Booking b where b.iin = :iin")
    fun findByIinForUpdate(iin: String): Booking?
}
```

```kotlin
@Service
class BookingService(
    private val webClient: WebClient,
    private val bookingRepository: BookingRepository,
) {

    @Transactional  // ❌ transaction open across the HTTP call
    fun createBooking(iin: String): Booking {
        val booking = bookingRepository.findByIinForUpdate(iin)  // SELECT ... FOR UPDATE → row locked
            ?: throw BookingNotFoundException(iin)

        // transaction is STILL open here — connection + row lock held
        val eligible = webClient.get()
            .uri("/licenses/{iin}", iin)
            .retrieve()
            .bodyToMono<EligibilityResponse>()
            .block()!!  // blocks 100ms? 5s? until timeout?

        booking.status = if (eligible.isValid) CONFIRMED else REJECTED
        return bookingRepository.save(booking)
    }
}
```

While `.block()` waits on the other service, this transaction keeps its DB connection checked out of the pool **and** holds the [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race|FOR UPDATE row lock]] the whole time. If the external service is slow — or hangs to its timeout — every other request that needs that row queues behind you, and every request that needs *a connection at all* competes for a pool that's draining.

<mark style="background: #FF9E9EA6; font-weight: bold;">Under load this is how one slow dependency freezes the whole service: locks pile up, connections stay checked out, and the pool empties</mark> — the same [[A connection storm from new instances can exhaust the database connection limit|connection exhaustion]] failure, this time caused by holding connections too long instead of opening too many.

---

### The fix

Do the read and the external call with **no transaction open**, then open a short transaction that only writes:

```kotlin
@Service
class BookingService(
    private val webClient: WebClient,
    private val bookingRepository: BookingRepository,
) {

    // NO @Transactional — nothing here holds a lock
    fun createBooking(iin: String): Booking {
        val eligible = webClient.get()
            .uri("/licenses/{iin}", iin)
            .retrieve()
            .bodyToMono<EligibilityResponse>()
            .block()!!

        return confirmBooking(iin, eligible.isValid)
    }

    @Transactional  // ✅ tx wraps ONLY local writes — opens and commits in ms
    fun confirmBooking(iin: String, isValid: Boolean): Booking {
        val booking = bookingRepository.findByIinForUpdate(iin)  // lock now held for ms, not the HTTP round-trip
            ?: throw BookingNotFoundException(iin)
        booking.status = if (isValid) CONFIRMED else REJECTED
        return bookingRepository.save(booking)
    }
}
```

Now the lock lives for microseconds of write time, not for the round-trip to a foreign server. The external latency happens on your own thread with **zero DB resources held**.

---

#### Gotcha: self-invocation bypasses the proxy

`this.confirmBooking(...)` above only works because Spring's `@Transactional` is applied by a **proxy** wrapping the bean. A call through `this` skips the proxy, so the annotation is silently ignored and no transaction starts. To keep the pattern honest, either split the two methods into **separate beans** (the reading orchestrator calls the writing service as an injected dependency), or run the write block through a `TransactionTemplate` instead of the annotation.

---

### Read more

- [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race]]
- [[A JPA @Lock pessimistic lock releases automatically at transaction end, never by a separate query]]
- [[A connection storm from new instances can exhaust the database connection limit]]
- [[Spring @Transactional defaults to READ COMMITTED which does not prevent lost updates]]
- [[Connection pooling reuses connections at application level to reduce overhead]]
- [[Database Transactions & Concurrency - MOC]]
