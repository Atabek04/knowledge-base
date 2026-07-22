---
created: 2026-07-01
tags: [spring, scheduling, distributed-systems, locking, shedlock, backend]
aliases: [ShedLock, SchedulerLock, lockAtMostFor, lockAtLeastFor, distributed scheduler lock]
---

A [[Spring @Scheduled runs a method on a fixed interval or cron expression#Runs once per instance — not once per system|@Scheduled method fires inside every running instance]]. On one server that's correct; behind a load balancer with 3 pods it's a bug — at 02:00 all three schedulers fire `reconcileSlots()` at once, so the same night's slots get generated three times and every user gets three "hold expired" emails. Spring has no idea its siblings exist.

<mark style="background: #FFF3A3A6; font-weight: bold;">ShedLock</mark> fixes this. Before a task runs, it tries to acquire a **named lock in a store all pods share** (a Postgres row, a Redis key, a Mongo doc). Exactly one pod wins the lock and runs; the rest see it taken and <mark style="background: #FFB8EBA6;">skip their turn entirely</mark>. The job executes *at most once* per scheduled tick across the whole cluster.

The name says the scope: it *sheds* redundant *locks* — it sheds the duplicate executions.

---

### Skip, not block — the defining behavior

This is the one thing to remember. When a pod finds the lock already held, it does **not** queue up and wait its turn — it <mark style="background: #FFB8EBA6;">abandons this run and moves on</mark>. The losers do nothing at all; there is no second execution later.

That is the opposite of a [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race|blocking `FOR UPDATE`]], where a waiter *blocks* until the holder commits and then proceeds. ShedLock's goal is "one run total," so making the losers wait and then run would defeat the entire purpose.

---

### `@SchedulerLock` — the declarative form

Add the annotation next to `@Scheduled`. The three attributes that matter:

```kotlin
@Scheduled(cron = "0 0 2 * * *")
@SchedulerLock(name = "slotHorizonReconcile", lockAtMostFor = "30m", lockAtLeastFor = "1m")
fun generateNightly() = reconciliationService.reconcile()
```

- <mark style="background: #ABF7F7A6;">`name`</mark> — **the lock identity**. Same name across all pods = the same lock row = mutual exclusion. Two jobs with different names never block each other; two pods running the *same* name compete. This is the shared key, so it must be stable and unique per logical task.
- <mark style="background: #ABF7F7A6;">`lockAtMostFor`</mark> — the ceiling. Read it literally: *lock at most for* this long. It's a **safety net** — if the winning pod crashes or hangs mid-run and never releases, the lock auto-expires after this window so the job isn't frozen forever. **Set it comfortably longer than the worst-case run time**, or a slow run's lock expires while it's still working and a second pod starts a duplicate.
- <mark style="background: #ABF7F7A6;">`lockAtLeastFor`</mark> — the floor. *Lock at least for* this long, even if the task finishes in milliseconds. It guards against a task so fast that, with a little clock skew between nodes, another pod's tick could re-acquire and re-run it in the same window.

#### `lockAtLeastFor` also tames the restart stampede

A deploy restarts all pods at once, and every one fires an `ApplicationReadyEvent` startup job in the same second. The first pod grabs the lock and — because `lockAtLeastFor` pins it held for a minimum — the rest all find it taken and skip, instead of racing to run in the microsecond gap before the fast task releases.

---

### `LockingTaskExecutor` — the programmatic form

`@SchedulerLock` only decorates a method Spring already calls. For a trigger that isn't a plain `@Scheduled` — a startup `@EventListener`, a manual admin button — wrap the work yourself with the same lock:

```kotlin
lockingTaskExecutor.executeWithLock(
    Runnable { reconciliationService.reconcile() },
    LockConfiguration(Instant.now(), "slotHorizonReconcile", Duration.ofMinutes(30), Duration.ofSeconds(1)),
)
```

Same lock **name** as the annotated job, so the nightly cron and the startup run <mark style="background: #ABF7F7A6;">compete for one lock</mark> — they can never both reconcile at the same instant. The `LockConfiguration` args are `(createdAt, name, lockAtMostFor, lockAtLeastFor)` — the programmatic twins of the annotation attributes.

---

### It needs a shared store and a switch

ShedLock is only as distributed as its backing store. Wiring:

- `@EnableSchedulerLock(defaultLockAtMostFor = "10m")` on a config class turns it on and sets a fallback ceiling.
- A <mark style="background: #ABF7F7A6;">`LockProvider`</mark> bean picks the store — `JdbcTemplateLockProvider(dataSource)` uses your existing Postgres.
- The JDBC provider reads/writes one `shedlock` table: `name` (PRIMARY KEY), `lock_until`, `locked_at`, `locked_by`. Acquiring = conditionally inserting/updating that row; the pod whose write wins holds the lock, the others' writes fail and they skip.

---

### ShedLock vs a DB row lock — different layers, don't confuse them

Both use "if it's taken, skip it," but they coordinate different things and solve opposite goals:

- **ShedLock** locks a **task execution** — *only one node runs this job; everyone else does nothing.* It **deduplicates** work.
- [[SELECT FOR UPDATE SKIP LOCKED turns a table into a competing-consumers work queue|`FOR UPDATE SKIP LOCKED`]] locks **rows** — *many workers each grab a different row and all stay busy.* It **distributes** work.

So in the booking app you may need both: ShedLock so the nightly reconcile runs on one pod, and a [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race|row lock]] *inside* that run so two concurrent requests can't book the same seat. One guards the *scheduler*; the other guards the *data*.

---

### Read more

- [[Spring @Scheduled runs a method on a fixed interval or cron expression]]
- [[Cron runs commands on a schedule defined by a five-field time expression]]
- Contrast — data-level locking:
    - [[SELECT FOR UPDATE holds a row lock until the transaction ends, closing the read-then-write race]]
    - [[SELECT FOR UPDATE SKIP LOCKED turns a table into a competing-consumers work queue]]
    - [[Optimistic and pessimistic locking are two strategies for preventing lost updates]]
- [[Spring Ecosystem - MOC]]
