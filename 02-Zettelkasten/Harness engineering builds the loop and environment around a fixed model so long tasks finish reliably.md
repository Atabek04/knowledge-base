---
aliases: [harness engineering, agent harness, harness]
created: 2026-09-20
---

Context engineering answered "what goes in the window on this call". It did not answer what happens when a task is too long for any single window. An agent given a feature to implement would work well for an hour, hit the window limit, compact its history into a summary, and continue from that summary. <mark style="background: #FF5582A6;">Compaction loses exactly the details a later step needs, so long tasks ended in code that was incomplete or subtly broken, however well each individual call was engineered.</mark>

<mark style="background: #FFF3A3A6;">A harness is everything around the model that turns it into an agent: the loop that decides when to call it again, the tools it can run, the state that persists between calls, the checks that verify its output, and the rules for stopping.</mark> Agent = model + harness. Harness engineering, named as a discipline in early 2026, is the work of designing that environment rather than the prompt or the window.

---

### Loops replace one long window

The defining move: <mark style="background: #ABF7F7A6;">instead of one elastic context that degrades as it grows, the harness runs the model in iterations, and each iteration starts from a fresh window loaded with the same instructions plus the current state read from disk.</mark> Memory lives outside the model, in files and git history, not in the conversation. A fresh window every iteration means the tenth step is as sharp as the first.

The harness owns the start and finish rules: what state each iteration reads, what counts as one unit of work, what signal ends the loop. The model owns only the step in between.

---

### What a harness is made of

- **Loop and orchestration**: iteration, sub-agents, hand-offs, when to stop
- **State on disk**: a task list with pass/fail, a progress log, commits
- **Tools and skills**: filesystem, shell, MCP servers, instruction files loaded on demand
- **Verification in the loop**: tests, typecheck, lint, hooks, so the model gets ground truth instead of self-judgement
- **Guardrails**: permissions, sandboxes, what the harness refuses regardless of the model's request
- **Observability**: logs and traces, since the model cannot report on its own failures

Prompt engineering and context engineering are not replaced; <mark style="background: #ADCCFFA6;">the harness treats prompt and context as components it assembles per iteration, so leverage moves from wording one call to designing the system of calls.</mark> Same model, different harness, very different agent.

---

### Read more

- [[Context engineering curates everything in the window and not the wording of one message]]
- [[Ralph runs a coding agent in a bash loop with a fresh context each pass and a PRD on disk as the only memory]]
- [[Tool calling lets a model fetch what it needs during a task instead of being handed everything upfront]]
- [[AI Engineering MOC]]
- [[Agentic Engineering MOC]]
- Sources: [Addy Osmani, Agent Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/), [awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering)
