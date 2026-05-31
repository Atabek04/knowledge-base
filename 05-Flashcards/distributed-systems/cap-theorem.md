TARGET DECK: Tech-KB::Distributed Systems::CAP Theorem
Tags: distributed-systems consistency database
**Chapter:** CAP Theorem & Consistency
**Related:** [[Distributed Systems - MOC]]

---

START
Coding Questions
What do the three letters in the CAP theorem stand for?
Back:
- **C — Consistency**: every read sees the most recent write (one agreed value)
- **A — Availability**: every request gets a non-error response
- **P — Partition tolerance**: the system keeps working when the network drops messages between nodes
Tags: distributed-systems cap
END

START
Coding Questions
Why is "pick any 2 of 3" a misleading framing of CAP?
Back:
In a real distributed system, **network partitions will happen** → P is **not optional**.

So the actual choice is narrower: **when a partition occurs, sacrifice C or A?**
- Keep C → reject/block on the cut-off side (**CP**)
- Keep A → answer with possibly-stale data (**AP**)
Tags: distributed-systems cap
END

START
Coding Questions
How do CP and AP systems behave under a partition? Give an example of each.
Back:
- **CP** (sacrifice availability): refuse/block to avoid stale data — a bank ledger, etcd, ZooKeeper
- **AP** (sacrifice consistency): answer anyway, reconcile later — a shopping cart, DNS, Cassandra

Neither is "better": payments must be CP; a catalog can be AP.
Tags: distributed-systems cap cp ap
END

START
Coding Questions
What does the PACELC extension add to CAP?
Back:
PACELC: *if **P**artition then **C** or **A**, **E**lse **L**atency or **C**onsistency.*

It captures that even with **no partition**, a system still trades **latency vs consistency** — CAP only describes the partition case.
Tags: distributed-systems cap pacelc
END

START
Coding Questions
What is eventual consistency, and which CAP choice leads to it?
Back:
**Eventual consistency**: if no new writes arrive, all replicas **eventually converge** to the same value — but interim reads may be **stale**.

It's the model an **AP** system adopts after choosing availability under partition. Replicas accept writes locally, then propagate and resolve conflicts (LWW, vector clocks, CRDTs).
Tags: distributed-systems eventual-consistency cap
END

START
Coding Questions
When is eventual consistency acceptable, and when is it wrong?
Back:
**Acceptable** when a brief stale read causes no harm — view counts, social feeds, caches, DNS.

**Wrong** when staleness corrupts a decision — payments, inventory reservations, balances (use strong consistency).
Tags: distributed-systems eventual-consistency
END
