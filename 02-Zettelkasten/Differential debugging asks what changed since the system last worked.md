---
created: 2026-06-24
tags: [debugging/method]
aliases: [differential debugging, what changed]
---

"It worked yesterday." That sentence is a gift, not a complaint — it tells you the code, config, and environment were once correct, so something *changed* between then and now. Differential debugging makes that change the prime suspect instead of treating the whole system as equally guilty.

The core question: <mark style="background: #FFF3A3A6; font-weight: bold;">what is different between the last-known-good state and now?</mark>

---

### The diff is your suspect list

Between "working" and "broken," look at everything that could have moved:

- **Deploys** — new code shipped
- **Config / env vars** — a flag flipped, a value changed
- **Dependencies** — a library or base image bumped a version
- **Data** — a new row, a null where there wasn't one, a volume spike
- **Infrastructure** — a cert expired, disk filled, a node replaced
- **Traffic** — load, a new client, a different request shape

The fault is almost certainly downstream of one of these, which is a far smaller space than "the entire codebase."

---

#### Check the boring changes first

The dramatic explanation (a deep concurrency bug) is rarely the cause when something *suddenly* breaks. <mark style="background: #FF5582A6; font-weight: bold;">Suspect the boring, recent change first</mark> — yesterday's deploy, an expired certificate, a dependency that auto-updated, a config edit. These cause most "it worked yesterday" failures.

---

### How it pairs with the other methods

Differential debugging finds *what* changed; the [[The Five Whys traces a symptom to its root cause by asking why repeatedly|Five Whys]] then asks *why that change broke things and slipped through*. And once you suspect a range of commits, [[Bisection isolates a fault by repeatedly halving the search space|bisection]] (via `git bisect`) pinpoints <mark style="background: #ADCCFFA6;">the exact change</mark> in log time.

---

### Read more
- [[The Five Whys traces a symptom to its root cause by asking why repeatedly]]
- [[Bisection isolates a fault by repeatedly halving the search space]]
- [[Debugging & Troubleshooting - MOC]]
