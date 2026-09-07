---
aliases: [fan-out, fan-out on write, fan-out on read, timeline fanout, write fanout]
created: 2026-09-03
tags: [scalability, system-design, architecture, ddia]
---

Twitter's scaling problem was never tweet volume — 12k writes/sec at peak is unremarkable. It was **fan-out**: each user follows many people and is followed by many people, so one write has to reach many readers.

The term is borrowed from electronics, where fan-out is the number of gate inputs driven by one output. Here it's the number of downstream places one incoming request must touch.

---

### The two designs

**Fan-out on read.** Posting a tweet just inserts one row into a global collection. Reading a home timeline looks up everyone you follow, gathers their tweets, and merges them by time — a join at read time.

Writes are trivial. Reads are expensive, and there are 300k timeline reads/sec against 4.6k posts/sec.

**Fan-out on write.** Each user gets a home-timeline cache, like a mailbox. Posting a tweet looks up all your followers and inserts the tweet into every one of their caches. Reading is then just a cache read, because the answer was computed in advance.

<mark style="background: #FFF3A3A6;">The trade is always the same shape: <b>do the work at write time, or do it at read time.</b></mark> You cannot avoid it, only choose which side pays.

Twitter started with read-side and switched to write-side, because <mark style="background: #ABF7F7A6;">the read rate was roughly two orders of magnitude higher than the write rate</mark> — so moving work to the rarer operation was a clear win.

---

### What the write side costs

At an average of 75 followers, 4.6k tweets/sec becomes **345k writes/sec** into timeline caches. That's the price of cheap reads, and it's payable.

The average is the trap. <mark style="background: #FF5582A6;">Followers per user vary wildly, and a user with 30 million followers means one tweet triggers 30 million writes</mark> — with a five-second delivery target.

So the load parameter that actually determines the design is not the tweet rate but the **distribution of followers per user**, weighted by how often those users tweet.

#### The hybrid resolution

Twitter now does both. Most users' tweets are fanned out on write; celebrities are exempted and their tweets are fetched separately and merged at read time.

The general lesson is worth more than the Twitter detail: <mark style="background: #ADCCFFA6;">when a distribution has a long tail, the right answer is often to run the cheap strategy for the body and the other strategy for the tail</mark>, rather than picking one design for everybody.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[Scalability is not a property of a system but a question about a specific direction of growth]]
- [[Denormalization trades write integrity for read performance by reintroducing redundancy]]
- [[A cold cache sends every request to the database, causing a thundering herd]]
