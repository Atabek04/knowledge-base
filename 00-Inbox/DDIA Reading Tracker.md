---
aliases: [DDIA Tracker, Designing Data-Intensive Applications Tracker]
tags: [tracker, book, reading]
---

Reading tracker for **Designing Data-Intensive Applications** by Martin Kleppmann (O'Reilly, 1st ed.).

Use this as the roadmap for setting reading goals and study plans. Every row carries both the **book page** (printed number, as cited everywhere) and the **PDF page** (what you type into the reader / the Read tool `pages` param).

PDF in vault: [[Designing Data-Intensive Applications - Martin Kleppmann.pdf]] (`Assets/Books/`).

---

### Page offset — book page vs PDF page

The printed page numbers and the PDF's physical page count do **not** match, because of cover + front-matter pages.

<mark style="background: #ADCCFFA6;">Body (Chapters 1–12, Glossary, Index): <b>PDF page = book page + 22</b></mark>

<mark style="background: #ADCCFFA6;">Front matter (roman numerals, e.g. Preface): <b>PDF page = roman number + 2</b></mark>

| To find… | Do this | Example |
|---|---|---|
| PDF page from a book page | add **22** | book p.199 → PDF 221 |
| Book page from a PDF page | subtract **22** | PDF 300 → book p.278 |
| A roman front-matter page | add **2** | Preface xiii → PDF 15 |

Verified anchors: Chapter 1 (book p.3) = PDF 25 · Chapter 6 (book p.199) = PDF 221 · Preface (book xiii) = PDF 15.

---

### Progress overview

Status legend: `[ ]` not started · `[/]` in progress · `[x]` done

| ✓ | Ch | Title | Book pp. | PDF pp. | Pages |
|---|----|-------|----------|---------|-------|
| | **Part I** | **Foundations of Data Systems** | 3–150 | 25–172 | |
| [ ] | 1 | Reliable, Scalable, and Maintainable Applications | 3–26 | 25–48 | 24 |
| [ ] | 2 | Data Models and Query Languages | 27–68 | 49–90 | 42 |
| [ ] | 3 | Storage and Retrieval | 69–110 | 91–132 | 42 |
| [ ] | 4 | Encoding and Evolution | 111–150 | 133–172 | 40 |
| | **Part II** | **Distributed Data** | 151–388 | 173–410 | |
| [ ] | 5 | Replication | 151–198 | 173–220 | 48 |
| [ ] | 6 | Partitioning | 199–220 | 221–242 | 22 |
| [ ] | 7 | Transactions | 221–272 | 243–294 | 52 |
| [ ] | 8 | The Trouble with Distributed Systems | 273–320 | 295–342 | 48 |
| [ ] | 9 | Consistency and Consensus | 321–388 | 343–410 | 68 |
| | **Part III** | **Derived Data** | 389–552 | 411–574 | |
| [ ] | 10 | Batch Processing | 389–438 | 411–460 | 50 |
| [ ] | 11 | Stream Processing | 439–488 | 461–510 | 50 |
| [ ] | 12 | The Future of Data Systems | 489–552 | 511–574 | 64 |
| | — | Glossary | 553–558 | 575–580 | 6 |
| | — | Index | 559– | 581– | |

Total body ≈ 550 book pages across 12 chapters.

---

## Part I — Foundations of Data Systems

### Ch 1 · Reliable, Scalable, and Maintainable Applications — book 3 / PDF 25

- [ ] Thinking About Data Systems — 4 / 26
- [ ] Reliability — 6 / 28 · Hardware Faults 7, Software Errors 8, Human Errors 9, How Important Is Reliability? 10
- [ ] Scalability — 10 / 32 · Describing Load 11, Describing Performance 13, Approaches for Coping with Load 17
- [ ] Maintainability — 18 / 40 · Operability 19, Simplicity 20, Evolvability 21
- [ ] Summary — 22 / 44

### Ch 2 · Data Models and Query Languages — book 27 / PDF 49

- [ ] Relational Model Versus Document Model — 28 / 50 · Birth of NoSQL 29, Object-Relational Mismatch 29, Many-to-One/Many-to-Many 33, Repeating History? 36, Relational vs Document Today 38
- [ ] Query Languages for Data — 42 / 64 · Declarative Queries on the Web 44, MapReduce Querying 46
- [ ] Graph-Like Data Models — 49 / 71 · Property Graphs 50, Cypher 52, Graph Queries in SQL 53, Triple-Stores and SPARQL 55, Datalog 60
- [ ] Summary — 63 / 85

### Ch 3 · Storage and Retrieval — book 69 / PDF 91

- [ ] Data Structures That Power Your Database — 70 / 92 · Hash Indexes 72, SSTables and LSM-Trees 76, B-Trees 79, Comparing B-Trees and LSM-Trees 83, Other Indexing Structures 85
- [ ] Transaction Processing or Analytics? — 90 / 112 · Data Warehousing 91, Stars and Snowflakes 93
- [ ] Column-Oriented Storage — 95 / 117 · Column Compression 97, Sort Order 99, Writing to Column Storage 101, Aggregation: Data Cubes and Materialized Views 101
- [ ] Summary — 103 / 125

### Ch 4 · Encoding and Evolution — book 111 / PDF 133

- [ ] Formats for Encoding Data — 112 / 134 · Language-Specific 113, JSON/XML/Binary 114, Thrift and Protocol Buffers 117, Avro 122, The Merits of Schemas 127
- [ ] Modes of Dataflow — 128 / 150 · Through Databases 129, Through Services: REST and RPC 131, Message-Passing Dataflow 136
- [ ] Summary — 139 / 161

---

## Part II — Distributed Data

### Ch 5 · Replication — book 151 / PDF 173

- [ ] Leaders and Followers — 152 / 174 · Sync vs Async 153, Setting Up New Followers 155, Handling Node Outages 156, Implementation of Replication Logs 158
- [ ] Problems with Replication Lag — 161 / 183 · Reading Your Own Writes 162, Monotonic Reads 164, Consistent Prefix Reads 165, Solutions 167
- [ ] Multi-Leader Replication — 168 / 190 · Use Cases 168, Handling Write Conflicts 171, Topologies 175
- [ ] Leaderless Replication — 177 / 199 · Writing When a Node Is Down 177, Quorum Consistency Limits 181, Sloppy Quorums and Hinted Handoff 183, Detecting Concurrent Writes 184
- [ ] Summary — 192 / 214

### Ch 6 · Partitioning — book 199 / PDF 221

- [ ] Partitioning and Replication — 200 / 222
- [ ] Partitioning of Key-Value Data — 201 / 223 · By Key Range 202, By Hash of Key 203, Skewed Workloads and Hot Spots 205
- [ ] Partitioning and Secondary Indexes — 206 / 228 · By Document 206, By Term 208
- [ ] Rebalancing Partitions — 209 / 231 · Strategies 210, Automatic or Manual 213
- [ ] Request Routing — 214 / 236 · Parallel Query Execution 216
- [ ] Summary — 216 / 238

### Ch 7 · Transactions — book 221 / PDF 243

- [ ] The Slippery Concept of a Transaction — 222 / 244 · Meaning of ACID 223, Single-Object and Multi-Object Operations 228
- [ ] Weak Isolation Levels — 233 / 255 · Read Committed 234, Snapshot Isolation and Repeatable Read 237, Preventing Lost Updates 242, Write Skew and Phantoms 246
- [ ] Serializability — 251 / 273 · Actual Serial Execution 252, Two-Phase Locking (2PL) 257, Serializable Snapshot Isolation (SSI) 261
- [ ] Summary — 266 / 288

### Ch 8 · The Trouble with Distributed Systems — book 273 / PDF 295

- [ ] Faults and Partial Failures — 274 / 296 · Cloud Computing and Supercomputing 275
- [ ] Unreliable Networks — 277 / 299 · Network Faults in Practice 279, Detecting Faults 280, Timeouts and Unbounded Delays 281, Sync vs Async Networks 284
- [ ] Unreliable Clocks — 287 / 309 · Monotonic vs Time-of-Day 288, Clock Sync and Accuracy 289, Relying on Synchronized Clocks 291, Process Pauses 295
- [ ] Knowledge, Truth, and Lies — 300 / 322 · Truth Defined by the Majority 300, Byzantine Faults 304, System Model and Reality 306
- [ ] Summary — 310 / 332

### Ch 9 · Consistency and Consensus — book 321 / PDF 343

- [ ] Consistency Guarantees — 322 / 344
- [ ] Linearizability — 324 / 346 · What Makes a System Linearizable? 325, Relying on Linearizability 330, Implementing 332, The Cost 335
- [ ] Ordering Guarantees — 339 / 361 · Ordering and Causality 339, Sequence Number Ordering 343, Total Order Broadcast 348
- [ ] Distributed Transactions and Consensus — 352 / 374 · Atomic Commit and 2PC 354, Distributed Transactions in Practice 360, Fault-Tolerant Consensus 364, Membership and Coordination Services 370
- [ ] Summary — 373 / 395

---

## Part III — Derived Data

### Ch 10 · Batch Processing — book 389 / PDF 411

- [ ] Batch Processing with Unix Tools — 391 / 413 · Simple Log Analysis 391, The Unix Philosophy 394
- [ ] MapReduce and Distributed Filesystems — 397 / 419 · MapReduce Job Execution 399, Reduce-Side Joins and Grouping 403, Map-Side Joins 408, The Output of Batch Workflows 411, Comparing Hadoop to Distributed Databases 414
- [ ] Beyond MapReduce — 419 / 441 · Materialization of Intermediate State 419, Graphs and Iterative Processing 424, High-Level APIs and Languages 426
- [ ] Summary — 429 / 451

### Ch 11 · Stream Processing — book 439 / PDF 461

- [ ] Transmitting Event Streams — 440 / 462 · Messaging Systems 441, Partitioned Logs 446
- [ ] Databases and Streams — 451 / 473 · Keeping Systems in Sync 452, Change Data Capture 454, Event Sourcing 457, State, Streams, and Immutability 459
- [ ] Processing Streams — 464 / 486 · Uses of Stream Processing 465, Reasoning About Time 468, Stream Joins 472, Fault Tolerance 476
- [ ] Summary — 479 / 501

### Ch 12 · The Future of Data Systems — book 489 / PDF 511

- [ ] Data Integration — 490 / 512 · Combining Specialized Tools by Deriving Data 490, Batch and Stream Processing 494
- [ ] Unbundling Databases — 499 / 521 · Composing Data Storage Technologies 499, Designing Applications Around Dataflow 504, Observing Derived State 509
- [ ] Aiming for Correctness — 515 / 537 · End-to-End Argument 516, Enforcing Constraints 521, Timeliness and Integrity 524, Trust but Verify 528
- [ ] Doing the Right Thing — 533 / 555 · Predictive Analytics 533, Privacy and Tracking 536
- [ ] Summary — 543 / 565

---

### Read more

- **Reading schedule:** `Ribaat/06-Planning/Topics/DDIA - August-September 2026 Reading Plan.md` — 8-week plan, 4 Aug → 30 Sep, ~13 pg/day.
- [[Technical Books - MOC]]
- [[DDIA - MOC]]
- [[Distributed Systems - MOC]]
- [[System Design - MOC]]
