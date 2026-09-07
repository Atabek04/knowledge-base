TARGET DECK: Tech-KB::Architecture::Scalability & Performance
Tags: architecture scalability performance latency
**Chapter:** Scalability — describing load, measuring performance, coping with growth
**Related:** [[Architecture - MOC]]

START
Coding Questions
Why is "is this system scalable?" a meaningless question?
Back:
Because scalability is **not a one-dimensional label** you can attach to a system — it is a system's ability to cope with load increasing **in a particular direction**.
- 10× the users is a different problem from 10× the data per user
- Both differ from 10× the write rate on unchanged data
The answerable version: *"if the system grows in this specific way, what are our options for coping?"*
Tags: architecture scalability
<!--ID: 1788436392597-->
END

START
Coding Questions
What must you establish before proposing any scaling solution, and why is it the strong move in an interview?
Back:
**Which load parameter is growing.**
A **load parameter** is a number describing current load — requests/sec to a web server, read-to-write ratio, simultaneously active users, cache hit rate. Which numbers matter depends entirely on your architecture.
Without naming the growth direction there is nothing to answer, so asking *"which parameter is growing?"* before proposing anything shows you understand the problem is underspecified.
Tags: architecture scalability
<!--ID: 1788436392600-->
END

START
Coding Questions
Why should you expect to rethink an architecture repeatedly on a fast-growing service?
Back:
Because **an architecture appropriate for one level of load is unlikely to cope with ten times that load.**
Expect a rethink on **every order of magnitude** of growth — sometimes more often.
The consequence: a design is always a design for a *stated range*, never for all time.
Tags: architecture scalability
<!--ID: 1788436392602-->
END

START
Coding Questions
Twitter handled 4.6k tweets/sec and 300k home-timeline reads/sec. Why did they move the work to write time?
Back:
Because **the read rate was roughly two orders of magnitude higher than the write rate**, so moving work onto the rarer operation is a clear win.
- **Fan-out on read** → posting inserts one row; reading joins across everyone you follow. Cheap writes, expensive reads.
- **Fan-out on write** → posting inserts the tweet into every follower's timeline cache. Expensive writes, cheap reads.
The trade is always the same shape: **do the work at write time or at read time.** You choose which side pays, you don't avoid it.
Tags: architecture scalability fan-out
<!--ID: 1788436392604-->
END

START
Coding Questions
What does fan-out on write cost Twitter, and which part of that cost is hidden by the average?
Back:
At an average of **75 followers**, 4.6k tweets/sec becomes **345k writes/sec** into timeline caches. That's payable.
**The average hides the tail:** followers per user vary wildly, and a user with **30 million followers** means one tweet triggers 30 million writes — against a five-second delivery target.
Tags: architecture scalability fan-out
<!--ID: 1788436392606-->
END

START
Coding Questions
Twitter's key load parameter was not the tweet rate. What was it, and why?
Back:
**The distribution of followers per user**, weighted by how often those users tweet.
Because that distribution — not the tweet volume — determines the **fan-out load**, which is what the architecture actually has to survive. 12k writes/sec is unremarkable; 30 million writes from one of them is not.
Tags: architecture scalability fan-out
<!--ID: 1788436392608-->
END

START
Coding Questions
Twitter fans out most tweets on write but exempts celebrities. What is the general lesson beyond Twitter?
Back:
**When a distribution has a long tail, run the cheap strategy for the body and the other strategy for the tail** — rather than picking one design for everybody.
Twitter's hybrid: ordinary users' tweets are pushed into follower timelines at write time; celebrity tweets are fetched separately and merged at read time.
Tags: architecture scalability fan-out
<!--ID: 1788436392611-->
END

START
Coding Questions
What is the difference between response time and latency?
Back:
- **Response time** → what the client sees: the **service time** (actually processing the request) **plus** network delay **plus** queueing delay
- **Latency** → only the duration a request spends *waiting* to be handled, during which it is **latent**, awaiting service
The name is the mnemonic: something *latent* is dormant, present but not yet acted on. Latency is the dead time before the work starts, not the work.
Tags: architecture performance latency
<!--ID: 1788436392614-->
END

START
Coding Questions
Your p99 response time is bad. Why does it matter whether it's service time or queueing delay before you start fixing?
Back:
Because they point at **different fixes**, and picking wrong wastes months.
- **Large service time** → the code or query is slow. Profile, add an index, cache it.
- **Large queueing delay** → the server is saturated; requests wait behind others. Optimizing the handler barely moves the number, because the handler was never the problem. You need more capacity or less arriving work.
Tags: architecture performance latency
<!--ID: 1788436392616-->
END

START
Coding Questions
Why does the identical request return a different response time on every attempt?
Back:
Because many small, unrelated sources of delay interleave with it:
- a context switch to a background process
- a lost packet and TCP (Transmission Control Protocol) retransmission
- a garbage collection pause
- a page fault forcing a read from disk
- even mechanical vibration in the server rack
Which is why response time is a **distribution of values**, never a single number.
Tags: architecture performance latency
<!--ID: 1788436392618-->
END

START
Coding Questions
Beyond being dragged by outliers, what is the fundamental problem with reporting an average response time?
Back:
**It doesn't tell you how many users actually experienced that delay.**
"Average 200 ms" is equally consistent with:
- everyone getting 200 ms
- 90% getting 20 ms while 10% get 1.8 seconds
Those are different systems and one of them is on fire. Percentiles preserve that distinction; the mean discards it.
Tags: architecture performance latency
<!--ID: 1788436392620-->
END

START
Coding Questions
Your service reports a median (p50) response time of 200 ms. Why can a user's experience still routinely be worse than that?
Back:
Because **the median describes a single request**, and a user usually makes several — over a session, or because one page pulls several resources.
The probability that **at least one** of them is slower than the median is much greater than 50%.
A user's experience is the **worst** of their requests, not the median of them.
Tags: architecture performance latency
<!--ID: 1788436392622-->
END

START
Coding Questions
Why does Amazon specify internal services at the 99.9th percentile when that affects only 1 request in 1,000?
Back:
Because **the tail is not a random sample of users — it selects for your most valuable ones.**
The customers with the slowest requests usually have the most data on their accounts, because they have made the most purchases.
Measured stakes: a **100 ms** increase in response time cost about **1% of sales**, and a **1-second** slowdown moved a customer-satisfaction metric by **16%**.
Tags: architecture performance latency
<!--ID: 1788436392625-->
END

START
Coding Questions
Amazon optimizes p999 but deliberately does not optimize p9999. Why stop there?
Back:
Because response times at very high percentiles are **dominated by random events outside your control**, so effort stops converting into improvement.
The extreme tail eventually stops being your fault. Chasing it is a real trap — the returns diminish hard while the cost does not.
Tags: architecture performance latency
<!--ID: 1788436392627-->
END

START
Coding Questions
Why are service level agreements (SLAs) written in percentiles rather than averages?
Back:
Because **a mean makes no promise to any individual request**, so it cannot be enforced or refunded against.
A percentile is a concrete threshold: "median under 200 ms, p99 under 1 s, up 99.9% of the time" tells a client exactly what they are owed and makes a breach measurable.
Tags: architecture performance latency
<!--ID: 1788436392630-->
END

START
Coding Questions
You issue five backend calls in parallel to serve one user request. Why doesn't the parallelism protect your latency?
Back:
Because **you are waiting on a maximum, not a sum.** The request cannot finish until the slowest of the five returns.
One slow call makes the entire end-user request slow, no matter how fast the other four were.
Tags: architecture performance latency microservices
<!--ID: 1788436392632-->
END

START
Coding Questions
Why does adding one more service to a request path worsen the user-visible p99, even when that service is fast?
Back:
This is **tail latency amplification**.
Each backend has some chance of landing in its own tail. The more backends a request touches, the higher the odds that **at least one** does — so a larger proportion of end-user requests are slow than any single service's p99 suggests.
- It's a direct argument against gratuitous service decomposition
- Useful probe: *"after this split, how many backend calls will one user request make?"* That number is the multiplier on your tail.
Tags: architecture performance latency microservices
<!--ID: 1788436392634-->
END

START
Coding Questions
During a saturation incident, why can your server-side latency dashboard still show green?
Back:
Because **the server's timer starts when it picks the request up** — the waiting happened before that.
A request can sit 800 ms in the queue and then run in 5 ms. The server honestly reports 5 ms while the client experiences 805 ms.
Consequence: **response times must be measured client-side.** A server-side latency metric structurally cannot see its own queue.
Tags: architecture performance latency observability
<!--ID: 1788436392636-->
END

START
Coding Questions
What is head-of-line blocking, and why does it fill the tail of your latency distribution?
Back:
A server processes only a small number of requests in parallel, bounded by something like its CPU core count.
So **a handful of slow requests hold up everything queued behind them** — the request at the head of the line blocks every request behind it, however cheap those are.
The blocked requests are **fast to process and slow to return**, which is exactly the profile that inflates high percentiles.
Tags: architecture performance latency
<!--ID: 1788436392638-->
END

START
Coding Questions
Your load generator waits for each response before sending the next request. Why does that make the test results a lie?
Back:
Because it **throttles itself in exact proportion to how slow the system is** — so the harder the system struggles, the gentler the test becomes.
Queues stay artificially shorter than production would ever make them, and the measured response times are correspondingly optimistic.
A load generator must keep sending **independently of response time**.
Tags: architecture performance testing
<!--ID: 1788436392640-->
END

START
Coding Questions
You have p99 latency from 10 servers and want one fleet-wide number. Why can't you average them?
Back:
Because **a p99 is a threshold on one distribution**, and the mean of two thresholds is a threshold on nothing — there is no distribution for which it is the 99th percentile.
Concretely: a server handling 10 requests reports p99 of 2 s, another handling 10,000 reports 50 ms. Their average (~1 s) describes neither the fleet nor any user.
The number isn't imprecise — it isn't a percentile at all.
Tags: architecture performance observability metrics
<!--ID: 1788436392642-->
END

START
Coding Questions
What is the correct way to aggregate response times across machines or across time?
Back:
**Add the histograms, then recompute the percentile from the combined data.**
A histogram keeps counts per bucket, so buckets from different machines or minutes sum cleanly and the percentile is read off the sum. This is why metrics systems store latency as histograms rather than pre-computed percentiles.
For cheap ongoing computation there are approximation algorithms: **forward decay**, **t-digest**, **HdrHistogram**.
Tags: architecture performance observability metrics
<!--ID: 1788436392644-->
END

START
Coding Questions
A system doing 100,000 requests/sec at 1 kB each and one doing 3 requests/minute at 2 GB each have identical data throughput. Why do they need completely different architectures?
Back:
Because **throughput is one number and the bottleneck is not.** The constraint could be read volume, write volume, stored data volume, data complexity, response-time requirements, access patterns — usually a mixture.
This is why there is **no generic, one-size-fits-all scalable architecture** (informally, no *magic scaling sauce*). Architecture at scale is highly specific to the application.
Tags: architecture scalability
<!--ID: 1788436392647-->
END

START
Coding Questions
An architecture that scales well is built around assumptions. Which ones, and what happens if they're wrong?
Back:
It's built around **which operations will be common and which will be rare** — the load parameters.
If those assumptions turn out wrong, the engineering effort is **at best wasted and at worst counterproductive**: you built a structure optimized for traffic that never arrived, and it now obstructs the traffic that did.
Hence in an early-stage startup or unproven product, iterating quickly on features usually beats scaling to hypothetical future load — you don't yet know the parameters to bet on.
Tags: architecture scalability
<!--ID: 1788436392649-->
END

START
Coding Questions
Why is scaling out straightforward for your application tier but hard for your database?
Back:
Because of the **stateless / stateful split**.
- **Stateless services** distribute across machines fairly easily — any instance can serve any request
- **Stateful data systems** going from one node to a distributed setup introduce a great deal of additional complexity
Hence the common wisdom: **scale the database up (vertically) until cost or high-availability requirements force you to distribute it.**
Tags: architecture scalability
<!--ID: 1788436392651-->
END

START
Coding Questions
Why is "scale up vs scale out" a false dichotomy in practice?
Back:
Because the cost curve and the complexity curve don't point the same way, so the optimum is usually neither extreme.
- A single machine is simpler, but high-end machines get very expensive
- **Several fairly powerful machines can be simpler *and* cheaper than a large number of small virtual machines**
Good architectures are a pragmatic mixture. ("Scale out" is also called **horizontal scaling** or a **shared-nothing** architecture.)
Tags: architecture scalability
<!--ID: 1788436392653-->
END

START
Coding Questions
When is manually scaled infrastructure the better choice over elastic auto-scaling?
Back:
When load is **reasonably predictable**.
- **Elastic** → adds resources automatically on detecting load increase. Useful when load is genuinely unpredictable.
- **Manual** → a human analyzes capacity and decides. **Simpler, with fewer operational surprises.**
Automation that reacts to load has its own failure modes — most notably that it is reactive, so it always trails the spike it is responding to.
Tags: architecture scalability
<!--ID: 1788436392655-->
END
