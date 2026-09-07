---
created: 2026-07-06
tags: [system-design/scaling, system-design/caching]
aliases: [thundering herd, cache stampede, cold cache, dogpile]
---

A cache exists to shield the database: most reads hit the cache, only misses fall through. That protection depends on the cache being **warm** — full of the data people are asking for. When the cache is empty or its entries all expire at once, that shield vanishes.

<mark style="background: #FFF3A3A6;">A cold cache means every request misses and falls straight through to the database at the same time — a thundering herd that can crush the very database the cache was meant to protect.</mark>

The name is the picture: a **herd** of requests all **thundering** at the database in one instant.

---

#### The two ways a cache goes cold

- **New instance** — a freshly scaled server starts with an empty local cache, so its first burst of requests all miss. Part of [[A newly launched instance needs warm-up before it can serve traffic|instance warm-up]].
- **Synchronized expiry** — many keys were cached at the same time (e.g. right after a deploy) with the same TTL, so they all expire together. One instant later, every read for those keys misses at once.

---

#### Why it's a feedback loop, not a blip

The herd overloads the database → queries slow down → the cache takes longer to repopulate → the cache stays cold longer → more requests miss. <mark style="background: #FF9E9EA6;">The stampede feeds itself; without intervention it doesn't self-heal, it collapses.</mark> This is the same [[Server capacity is bounded by whichever resource saturates first, not just RAM|saturation feedback loop]] seen in most "server crashed" stories.

---

#### The standard defenses

- **TTL jitter** — add a random offset to each key's expiry so they don't all expire on the same tick. Breaks synchronized expiry.
- **Request coalescing (single-flight)** — on a miss, let *one* request fetch from the DB and repopulate; make the rest wait for that result instead of all querying.
- **Cache warming** — pre-load hot keys before an instance takes traffic, so it never starts cold.
- **Stale-while-revalidate** — serve the old value while one background request refreshes it.

---

### Read more
- [[A newly launched instance needs warm-up before it can serve traffic]]
- [[The database is the hardest tier to scale because every app server shares one writer]]
- [[Server capacity is bounded by whichever resource saturates first, not just RAM]]
- [[Pre-warming and spare headroom absorb bursts that reactive scaling cannot]]
- [[System Design - MOC]]
