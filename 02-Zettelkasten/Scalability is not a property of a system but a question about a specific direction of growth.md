---
aliases: [scalability, load parameters, describing load]
created: 2026-09-03
tags: [scalability, architecture, system-design, ddia]
---

"Is it scalable?" is asked constantly and answers nothing. <mark style="background: #FFB8EBA6;">It is meaningless to say <b>X is scalable</b> or <b>Y doesn't scale</b></mark> — scalability is not a one-dimensional label you can attach to a system.

---

### The question that replaces it

Scalability is a system's ability to cope with **increased load**, and load increases in a specific direction. So the useful questions are:

- *If the system grows in this particular way, what are our options for coping?*
- *How can we add computing resources to handle that additional load?*

<mark style="background: #FFF3A3A6;">Both require naming the growth direction first. Without it there's nothing to answer.</mark>

Ten times the users is a different problem from ten times the data per user, which is different again from ten times the write rate on unchanged data.

---

### Load parameters

To describe growth you first describe the present, using a few numbers called **load parameters**. Which numbers depends entirely on your architecture:

- requests per second to a web server
- ratio of reads to writes in a database
- simultaneously active users in a chat room
- hit rate on a cache

Sometimes the average is what matters. Sometimes your bottleneck is dominated by a small number of extreme cases — and then the average is actively misleading, and the right load parameter is the shape of the distribution rather than its centre. Twitter's is [[Fan-out on write trades expensive writes for cheap reads and fan-out on read does the reverse|the distribution of followers per user]], not the tweet rate.

---

### Why this matters in an interview

<mark style="background: #ABF7F7A6;">Asked "how would you make this scale", the strong move is to ask which load parameter is growing before proposing anything.</mark>

An architecture appropriate for one level of load is unlikely to cope with ten times that load. On a fast-growing service you can expect to rethink the architecture on **every order of magnitude** — so a design is always a design for a stated range, not for all time.

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[Fan-out on write trades expensive writes for cheap reads and fan-out on read does the reverse]]
- [[Response time is a distribution so percentiles describe it and the mean does not]]
- [[Auto-scaling is reactive so it always trails a sudden traffic spike]]
