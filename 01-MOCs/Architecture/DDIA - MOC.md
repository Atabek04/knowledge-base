> Reading index for *Designing Data-Intensive Applications* (Kleppmann, 1st ed.) — chapter map, note budget, and routing targets.

Paper source. This MOC tracks reading progress only; finished atomic notes live in the topic MOCs listed per chapter, and are repeated here as links once written.

---

## Workflow

- **While reading** — margin symbols only: `?` (don't get it), `!` (counterintuitive / trade-off), `→X` (links to something I already know). No prose in margins.
- **End of session** — write **questions only** into `00-Inbox/DDIA Ch{N} — {title}.md`, with page refs. No summary, no recall prose: the book and the notes repo already state it better than I would.
- **End of chapter — the interview.** Hand the questions file to the agent. It answers them first, then quizzes me on the chapter **closed book, before I open the notes repo or re-read**. An interview run after re-reading measures recognition, not memory.
- **Cards from the interview misses only** — never a card pass over the whole chapter.
- **Atomize what held up**, within the chapter's note budget, routed to its topic MOC.
- **Delete the inbox file** once atomized — no parallel truth.

> The `/teach` skill runs the interview — Socratic, one concept at a time, persisting each concept before advancing.
> Cross-check afterwards against [ps06756/Designing-Data-Intensive-Applications](https://github.com/ps06756/Designing-Data-Intensive-Applications) — after the interview, never before.

---

## Reading order

Not front-to-back. Priority for backend / interview readiness:

- **Core** — Ch3, Ch5, Ch6, Ch7, Ch8, Ch9, Ch11
- **Medium** — Ch2, Ch4
- **Light** — Ch1, Ch10, Ch12
- Part III (Ch10–12) only after Part II is atomized — it assumes replication + partitioning cold.

---

## Part I — Foundations of Data Systems

### Ch1 — Reliable, Scalable, and Maintainable Applications

- Fault vs failure; fault tolerance covers hardware faults, software bugs, human error
- Scalability: load parameters, Twitter fan-out on write vs read as the worked example
- Response time is a distribution — measure p95/p99, never the mean; tail latency amplification
- Throughput vs response time; queueing delay dominates at high utilization
- Maintainability: operability, simplicity, evolvability

Notes: 1–2 · Route: [[Architecture - MOC]] · Framing chapter — skip the summary prose.

### Ch2 — Data Models and Query Languages

- Object-relational impedance mismatch; why the document model appeared
- Document model: schema-on-read, storage locality, weak join support — fits one-to-many trees
- Relational model: joins and many-to-many are its whole point
- Graph models: property graphs vs triple stores; Cypher, SPARQL, Datalog
- Declarative (SQL) vs imperative query languages — declarative frees the optimizer and parallelizes

Notes: 4–6 · Route: [[Databases - MOC]]

### Ch3 — Storage and Retrieval

- Log-structured storage: memtable → SSTable → compaction (LSM-tree); Bloom filters for absent keys
- B-trees: fixed-size pages, in-place update, WAL/redo log for crash safety
- LSM vs B-tree trade-off: write throughput and write amplification vs read latency and compaction stalls
- Secondary indexes; clustered vs non-clustered; covering indexes; multi-column and fuzzy indexes
- OLTP vs OLAP split; data warehouse and star schema
- Column-oriented storage: column compression (bitmap + run-length), sort orders, materialized views and cubes

Notes: 6–8 · Route: [[PostgreSQL - MOC]], [[Databases - MOC]], [[ClickHouse - MOC]] · Highest-yield chapter.

### Ch4 — Encoding and Evolution

- Language-specific serialization is a trap (security, versioning, cross-language)
- JSON/XML/CSV limits: number precision, no binary, ambiguous schema
- Binary formats: Thrift/Protobuf field tags, Avro writer's vs reader's schema, no tag numbers
- Backward vs forward compatibility — rolling upgrades need both directions at once
- Dataflow modes: through a database, via REST/RPC, via async message brokers

Notes: 3–4 · Route: [[API Design - MOC]], [[Distributed Systems - MOC]] · One comparison note for the formats, not one per format.

---

## Part II — Distributed Data

### Ch5 — Replication

- Leader-based replication; sync vs async followers; semi-synchronous as the practical middle
- Failover hazards: lost writes on async promotion, split brain, wrong timeout tuning
- Replication log formats: statement-based, WAL shipping, logical (row-based), trigger-based
- Replication-lag anomalies: read-your-writes, monotonic reads, consistent prefix reads
- Multi-leader: multi-datacenter, offline clients, collaborative editing — write conflicts are the price
- Conflict resolution: last-write-wins (lossy), version vectors, CRDTs
- Leaderless (Dynamo-style): quorums `w + r > n`, read repair, anti-entropy, sloppy quorum + hinted handoff

Notes: 8–10 · Route: [[Distributed Systems - MOC]], [[PostgreSQL - MOC]] · Biggest chapter of the book.

### Ch6 — Partitioning

- Key-range partitioning vs hash partitioning; skew and hot spots
- Secondary indexes: local/document-partitioned (scatter-gather reads) vs global/term-partitioned (slower writes)
- Rebalancing strategies: fixed number of partitions, dynamic partitioning, proportional to nodes — never `hash mod N`
- Automatic vs manual rebalancing; the runaway-failover risk
- Request routing: coordination service (ZooKeeper), gossip, routing tier

Notes: 4–6 · Route: [[Distributed Systems - MOC]] · Pairs with Kafka partitions — link, don't rewrite.

### Ch7 — Transactions

- What ACID actually guarantees; atomicity means abortability; "BASE" is defined by what it isn't
- Single-object vs multi-object operations; why multi-object atomicity is the hard part
- Weak isolation levels: read committed, snapshot isolation / MVCC
- Race conditions: dirty reads/writes, read skew, lost update, write skew, phantoms
- Preventing lost update: atomic write ops, explicit locking (`FOR UPDATE`), compare-and-set, conflict detection
- Serializability: actual serial execution (stored procedures), two-phase locking + predicate/index-range locks, serializable snapshot isolation (optimistic)

Notes: 6–8 · Route: [[Database Transactions & Concurrency - MOC]], [[PostgreSQL - MOC]] · Heavy overlap with existing notes — link into them, only write what's genuinely new.

### Ch8 — The Trouble with Distributed Systems

- Partial failure and why it has no analogue in single-machine software
- Unreliable networks: unbounded delay, timeouts are always a guess
- Unreliable clocks: time-of-day vs monotonic clocks, NTP skew, clock as a confidence interval (Spanner TrueTime)
- Why last-write-wins over physical timestamps silently drops writes
- Process pauses: GC stop-the-world, VM suspend — no code has timing guarantees
- Truth by majority: a node's own belief is not truth; fencing tokens stop zombie leaders
- System models: crash-stop, crash-recovery, byzantine; safety vs liveness

Notes: 5–7 · Route: [[Distributed Systems - MOC]]

### Ch9 — Consistency and Consensus

- Linearizability: a recency guarantee, the illusion of a single copy — and its cost
- Linearizability vs serializability — different guarantees, often confused
- CAP restated precisely; what it does and does not say
- Ordering and causality: causality is a partial order, linearizability a total one; Lamport timestamps aren't enough
- Total order broadcast and its equivalence to consensus
- Distributed transactions: two-phase commit, the in-doubt window, coordinator failure, XA
- Consensus algorithms (Raft, Paxos, Zab, VSR): epochs plus quorum voting; FLP impossibility
- Coordination services: ZooKeeper/etcd for leader election, membership, service discovery, fencing

Notes: 6–8 · Route: [[Distributed Systems - MOC]]

---

## Part III — Derived Data

### Ch10 — Batch Processing

- Unix philosophy: uniform interface, composition via pipes, immutable inputs
- MapReduce and distributed filesystems (HDFS); mapper/reducer, the sort-merge shuffle
- Reduce-side joins: sort-merge join; skew handling
- Map-side joins: broadcast hash join, partitioned hash join, map-side merge join
- Dataflow engines (Spark, Tez, Flink) — avoid materializing every intermediate state
- Outputs: build search indexes and read-only key-value stores; retry is safe because inputs are immutable

Notes: 3–5 · Route: [[Distributed Systems - MOC]] · Lowest interview relevance — read fast.

### Ch11 — Stream Processing

- Event streams; producers/consumers; message brokers vs log-based brokers
- AMQP/JMS-style (delete on ack, per-message fanout) vs log-based (Kafka: offsets, replay, ordered per partition)
- Change data capture and event sourcing; log compaction as durable state
- Event time vs processing time; straggler events; windows (tumbling, hopping, sliding, session)
- Stream joins: stream-stream, stream-table, table-table; slowly changing dimensions
- Fault tolerance: microbatching, checkpointing, idempotent writes, "exactly-once" as effectively-once

Notes: 5–7 · Route: [[Distributed Systems - MOC]] · Highest day-job relevance — Kafka.

### Ch12 — The Future of Data Systems

- Data integration: systems of record vs derived data; every derived system is a materialized view
- Unbundling the database; lambda architecture and its critique
- End-to-end argument: correctness cannot be delegated to any single layer
- Idempotence and constraints without coordination; integrity vs timeliness
- Auditability of dataflow
- Ethics of predictive analytics, privacy, surveillance

Notes: 1–3 · Route: [[Architecture - MOC]] · Mostly essay — capture the end-to-end argument and skip the rest.

---

## Failure modes

- Margins fill with prose → reading stalls. Symbols only.
- Inbox file survives atomizing → parallel truth, vault decoheres. Delete it.
- Notes paraphrase Kleppmann's sentences instead of stating the trade-off → nothing recalls later. Every title names a tension.
- Notes never reach a MOC → orphans. A note is not done until it's linked.
- Flashcards ask "what is X" instead of "when does X break" → recognition, not retrieval.

---

## Do NOT

- Don't take notes on Ch1 framing or any chapter's Summary section.
- Don't atomize the Ch4 format catalog into five notes — one comparison note.
- Don't duplicate what the vault already owns (MVCC, isolation levels, locking, Kafka delivery semantics) — link into those notes.
- Don't start Part III before Part II is atomized.
- Don't skip resolving the `?` list — an unresolved question becomes a wrong flashcard.

---

## Related
- [[Distributed Systems - MOC]]
- [[Databases - MOC]]
- [[Database Transactions & Concurrency - MOC]]
- [[PostgreSQL - MOC]]
- [[Architecture - MOC]]
- [[API Design - MOC]]
