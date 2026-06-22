---
aliases: [rubber-stamping AI, vibe coding risk, oversight theater, the verifier problem]
---

"Keep a human in the loop" is the standard reassurance about AI-written code. It only works if that human can actually evaluate the output. When they can't, the loop still exists on paper — but the human becomes a rubber stamp, approving whatever looks plausible.

This is the precise answer to "won't a careful person catch the mistakes?": <mark style="background: yellow;">only if they have the expertise to recognize a mistake when they see one</mark>.

---

### Vibe coding names the failure

Andrej Karpathy coined **vibe coding** (Feb 2025): "you fully give in to the vibes... and forget that the code even exists," including "I 'Accept All' always, I don't read the diffs anymore."

Simon Willison drew the line that separates it from engineering: <mark style="background: green;">"I won't commit any code to my repository if I couldn't explain exactly what it does to somebody else."</mark>

The vibe coder violates exactly that rule — approving code they could not explain, and therefore could not verify.

---

### Why prompting for rigor doesn't rescue them

The user in the prompt asked the model to do deep analysis, chain of thought, pros and cons. But [[Telling an LLM to reason harder can rationalize a wrong answer instead of correcting it|asking the model to reason harder can just rationalize a wrong answer]] — and a reviewer who can't independently judge correctness has <mark style="background: pink;">no way to tell good reasoning from a confident rationalization</mark>.

So the safeguard collapses: the unskilled reviewer approves the [[AI confidently reports software vulnerabilities that do not exist burying maintainers in slop|fabricated bug report]] or the subtly-broken code, because to them it reads exactly like the correct version.

---

### This is automation bias under the worst conditions

The mechanism is not new — it is [[Automation bias makes people accept a machine's recommendation without verifying it|automation bias]], the documented tendency to accept a machine's recommendation without checking it.

AI code stacks every aggravating factor at once: <mark style="background: cyan;">high verification complexity, fluent plausible output, and a reviewer who lacks the schema to verify</mark>. That is the exact regime where the bias is strongest.

#### The asymmetry that decides who is safe

A senior reviews AI output *against* their own model of correct; the vibe coder reviews it against *nothing*. Same tool, opposite outcome — the protection was never the loop, it was the expertise inside it.

---

### Read more
- [[Automation bias makes people accept a machine's recommendation without verifying it]]
- [[Telling an LLM to reason harder can rationalize a wrong answer instead of correcting it]]
- [[Over-relying on AI coding tools without reading output erodes genuine programming confidence]]
- [[AI-generated code is harder to review because it looks clean even when the logic is wrong]]
- [[Agentic Engineering MOC]]

### External Resources
- [Karpathy (2025) — the original vibe-coding post](https://x.com/karpathy/status/1886192184808149383)
- [Simon Willison (2025) — Not all AI-assisted programming is vibe coding](https://simonwillison.net/2025/Mar/19/vibe-coding/)
