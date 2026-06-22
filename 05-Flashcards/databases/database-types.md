TARGET DECK: Tech-KB::Databases::Database Types
Tags: database nosql data-modeling
**Chapter:** Database Types & Selection
**Related:** [[Databases - MOC]]

---

START
Coding Questions
What is the core trade-off between relational and NoSQL databases?
Back:
**Relational** enforces a **fixed schema + ACID**; **NoSQL** relaxes one or both for **scale and flexibility**.

- Relational: schema-on-write, joins, strong consistency → integrity-critical data (payments, orders)
- NoSQL: schema-on-read, horizontal scale, often eventual consistency → huge volume / flexible shape
- It's a trade, not a ranking
Tags: database relational nosql
<!--ID: 1782128729757-->
END

START
Coding Questions
When should a relational database be your default choice?
Back:
When you need **multi-record transactions** or **strong integrity**, and relationships/joins are central.

- Schema-on-write rejects bad data at insert
- ACID makes multi-table changes atomic
- Default until a specific NFR forces you off it
Tags: database relational
<!--ID: 1782128729761-->
END

START
Coding Questions
What is a document database, and what makes it different from a relational row?
Back:
Stores **self-describing documents** (JSON/BSON) queried by their **nested content** (MongoDB, Couchbase).

- A document can **nest** arrays/sub-objects — the whole aggregate in one place, no join
- Flexible schema; great locality
- Cost: duplication across documents, weak cross-document joins
Tags: database nosql document
<!--ID: 1782128729763-->
END

START
Coding Questions
What is a key-value store, and what is the one query it supports?
Back:
A distributed **hash map**: unique key → **opaque value** (Redis, DynamoDB).

- Only query is **by key** — the store never inspects values
- Therefore O(1) lookup, trivially shardable
- Best for caching, sessions, counters — when you always know the exact key
Tags: database nosql key-value caching
<!--ID: 1782128729766-->
END

START
Coding Questions
What workload is a column-family (wide-column) store built for, and how does it differ from a columnar OLAP store?
Back:
**Wide-column** (Cassandra, HBase): rows with **different sparse columns**, append-optimized for **massive write throughput** (time-series, IoT, logs).

⚠️ Different from columnar **OLAP** (ClickHouse): both store by column, but OLAP targets **analytical scans**, wide-column targets high-volume OLTP-style writes.
Tags: database nosql column-family
<!--ID: 1782128729769-->
END

START
Coding Questions
What problem does a graph database solve that relational databases struggle with?
Back:
**Deep relationship traversal.** "Friends of friends of friends" is a 3× self-join in SQL (cost explodes); a graph DB follows **edge pointers**, so multi-hop stays cheap.

- Nodes = entities, edges = typed relationships carrying data
- Best for social graphs, recommendations, fraud rings, permissions
Tags: database nosql graph
<!--ID: 1782128729771-->
END

START
Coding Questions
How do you choose a database for a system?
Back:
Match the store's **model + guarantees** to your **non-functional requirements**, walking NFRs in priority order:

- Transactions/integrity → relational
- Flexible shape → document; key lookups → key-value
- Write throughput → column-family; traversal → graph; analytics → columnar OLAP

Model around **access patterns**; polyglot persistence is normal; don't add a store until an NFR forces it.
Tags: database selection nfr
<!--ID: 1782128729774-->
END
