---
aliases: [response time, latency, service time, response time vs latency]
created: 2026-09-03
tags: [performance, latency, architecture, ddia]
---

These two words are used interchangeably in almost every performance conversation, and they name different quantities. Keeping them apart changes which fix you reach for.

---

### The split

<mark style="background: #FFF3A3A6;"><b>Response time</b> is what the client sees: the <b>service time</b> (actually processing the request), plus network delay, plus queueing delay.</mark>

<mark style="background: #FFF3A3A6;"><b>Latency</b> is only the duration a request spends waiting to be handled — during which it is <b>latent</b>, awaiting service.</mark>

The name is its own mnemonic. Something *latent* is dormant, present but not yet acted on. Latency is the dead time before the work starts, not the work.

---

### Why the distinction pays

They point at different fixes, and reaching for the wrong one wastes weeks.

**Large service time** means your code or your query is slow. Profile it, add an index, cache the result.

**Large queueing delay** means the server is saturated — requests are sitting in line behind others. Optimizing the handler barely moves the number, because the handler was never the problem. You need more capacity, or less work arriving.

<mark style="background: #FFB8EBA6;">A response time that is mostly queueing will not respond to code optimization, and teams routinely spend a quarter discovering that.</mark>

Network delay is the third component, and it has its own trap — [[High bandwidth does not guarantee low latency|adding bandwidth does not reduce it]].

---

### Read more

- [[DDIA - MOC]]
- [[Architecture - MOC]]
- [[Response time is a distribution so percentiles describe it and the mean does not]]
- [[Queueing delay is invisible to server-side metrics and to closed-loop load generators]]
- [[High bandwidth does not guarantee low latency]]
