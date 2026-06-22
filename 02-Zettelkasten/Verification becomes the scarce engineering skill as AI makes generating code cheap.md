---
aliases: [verification is the moat, judgment is the bottleneck, generation outpaces review]
---

This is the direct answer to "will AI replace engineers?" AI collapses the cost of *generating* code to near zero. It does not collapse the cost of knowing whether that code is *correct*. So value migrates from the part AI does cheaply to the part it can't be trusted with — and the engineers who own that part become more valuable, not less.

The asymmetry is the whole argument: <mark style="background: yellow;">generation is cheap, verification is hard, and they don't scale together</mark>.

---

### You can't outsource the verdict

Simon Willison states the irreducible part bluntly: <mark style="background: yellow;">"the one thing you absolutely cannot outsource to the machine is testing that the code actually works... If you haven't seen it run, it's not a working system."</mark>

The model can write it. It cannot be the one accountable for it working. That accountability requires someone who can tell — which is exactly the capacity a [[You cannot review what you cannot understand so AI oversight collapses into rubber-stamping|rubber-stamping reviewer lacks]].

---

### The bottleneck moved, it didn't vanish

Machine-speed generation pours into human-speed review. The constraint didn't disappear — it relocated to verification.

- Faros AI (10,000+ developers): <mark style="background: green;">PR volume up ~98%, PR review time up ~91%</mark>.
- Cursor's CEO: code review is taking a growing share of developer time as time spent writing code shrinks.

When AI generates far more code, <mark style="background: cyan;">someone still has to read it — and that someone becomes the bottleneck</mark>.

---

### The job rebalances toward judgment

Steve Yegge's framing: the work becomes "agent babysitting," and the skill to build is <mark style="background: green;">"validation and verification"</mark>.

Birgitta Böckeler (Thoughtworks), after successful agentic sessions: <mark style="background: pink;">"I intervened, corrected and steered all the time... my 20+ years of programming experience mattered the most."</mark>

This is why human work isn't simply automated away: it survives where it stays accountable for correctness — a craft parallel to the economic point that [[Humans keep their edge in physical, strategic, and social work|humans keep their edge where AI can't be trusted to act alone]], and that [[Jobs survive automation when they aren't worth the compute, not because humans are better|jobs survive where the alternative isn't worth the compute]].

---

### Read more
- [[The 70 percent problem means AI delivers the first 70 percent fast but the last 30 percent needs expertise]]
- [[The software engineer's role is shifting from writing code to specifying reviewing and orchestrating it]]
- [[The Expert Generalist gains value as AI writes more code because fundamentals decomposition and judgment compound]]
- [[Humans keep their edge in physical, strategic, and social work]]
- [[Agentic Engineering MOC]]

### External Resources
- [Simon Willison (2025) — Here's how I use LLMs to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)
- [Steve Yegge (2025) — Revenge of the Junior Developer](https://sourcegraph.com/blog/revenge-of-the-junior-developer)
- [Birgitta Böckeler (2025) — The role of developer skills in agentic coding](https://martinfowler.com/articles/exploring-gen-ai/13-role-of-developer-skills.html)
