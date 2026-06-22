---
aliases: [AI slop, false vulnerability reports, hallucinated CVEs, slop security reports]
---

The clearest real-world proof that AI produces confident, plausible, *wrong* technical claims at scale is the wave of AI-generated security reports that flooded open-source projects in 2024–2026. The reports look like real vulnerability disclosures. Almost none describe a real bug.

The maintainers coined a name for it: <mark style="background: yellow;">**AI slop**</mark> — output that has the shape of expertise with none of the substance.

---

### What the fake reports look like

They are not obvious spam. A slop report cites function names, includes exploit narratives, even fabricates GDB sessions and register dumps — for code paths that <mark style="background: pink;">do not exist in the project</mark>.

Seth Larson, the Python Software Foundation's Security Developer-in-Residence, wrote the first systematic warning (Dec 2024) and named the root cause: <mark style="background: yellow;">"these systems today cannot understand code."</mark>

His example: urllib3 was reported as vulnerable because a tool flagged its use of `SSLv2` as insecure — when the code's actual purpose was to *disable* SSLv2. The AI inverted the meaning of the very line it flagged.

---

### The curl numbers

Daniel Stenberg (curl maintainer) documented the escalation precisely:

- By mid-2025, <mark style="background: green;">~20% of all security submissions were AI slop</mark>, and the valid-report rate **collapsed from a historical >15% to below 5%**.
- Each report still <mark style="background: pink;">engages 3–4 people for 30 minutes to several hours</mark> to triage — real labor spent disproving fiction.
- Stenberg's framing: <mark style="background: cyan;">"We are effectively being DDoSed,"</mark> and curl began instantly banning anyone submitting slop.

In January 2026 curl **ended its bug-bounty program entirely** — 87 confirmed vulns and \$100k+ paid over its life — to remove the incentive for made-up reports.

---

### Why this is the load-bearing example

It isolates the danger cleanly. The AI is not malicious and not lazy; it is <mark style="background: yellow;">fluently, specifically, and confidently wrong</mark> about whether a bug exists.

The only thing standing between the fiction and a wasted response is a human expert who can read the actual code and say "this function isn't real." That judgment is the whole defense — which is exactly why [[Telling an LLM to reason harder can rationalize a wrong answer instead of correcting it|prompting the model to "analyze harder" does not fix it]] and why [[You cannot review what you cannot understand so AI oversight collapses into rubber-stamping|a reviewer who can't read the code just forwards the slop]].

---

### Read more
- [[Telling an LLM to reason harder can rationalize a wrong answer instead of correcting it]]
- [[You cannot review what you cannot understand so AI oversight collapses into rubber-stamping]]
- [[Verification becomes the scarce engineering skill as AI makes generating code cheap]]
- [[Agentic Engineering MOC]]

### External Resources
- [Seth Larson (2024) — New era of slop security reports for open source](https://sethmlarson.dev/slop-security-reports)
- [Stenberg (2025) — Death by a thousand slops](https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/)
- [Stenberg (2026) — The end of the curl bug-bounty](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/)
