---
type: fleeting
status: to-watch
source: https://youtu.be/G2B0YWuJUgI
tags: [fleeting, prompt-engineering, ai-engineering, agents]
created: 2026-05-23
---

### Prompting Playbook — Margot Vanlar

Video to watch, then extract atomic notes.

**Source:** https://youtu.be/G2B0YWuJUgI
**Speaker:** Margot Vanlar

---

### Where to file later

No AI Engineering / Prompt Engineering MOC exists yet → **create one** (`01-MOCs/AI-Engineering/Prompt Engineering - MOC.md` or similar) and map the atomic notes there.

Candidate MOC sections:
- Prompt maintenance & debugging
- Evals
- Prompt hygiene
- Output contracts
- Agentic systems / agentic loops
- Model selection trade-offs

---

### Topics to extract (from video outline)

**1. Introduction & Methodology (0:20–4:02)**
- Goal: apply core prompting principles to AI systems that plan, act, adapt
- Two scenarios: maintaining/migrating an existing prod prompt vs building a new agentic use case 0→1
- Evals are essential — need rigorous evals to know if a prompt change actually correlates to improvement

**2. Scenario 1 — Maintaining & Debugging a Prompt (4:02–23:34)**
- Eval suite should include: control case (unambiguous), edge cases (previously failed behaviors), capability tests (when to escalate or refuse)
- Prompt hygiene (7:02–11:34): remove redundant info, define clear roles, use XML tags to structure data / guidelines / policy
- Output contracts (11:34–13:21): XML tags or stop sequences in the API harness for consistent output format
- Pitfall — Overfitting (15:27–16:26): legacy "patches" no longer needed for newer, smarter models
- Pitfall — Capability vs Instruction (18:29–20:00): instructions can't compensate for missing capabilities → use tools instead of telling the model to "do mental math correctly"
- Trade-offs (21:56–22:50): when instructing on decisions (e.g. escalation costs), give both sides of the story

**3. Scenario 2 — Building an Agent from Scratch (23:34–33:04)**
- Use case: retail staff schedule with specific constraints
- Iterations:
  - Simple prompt + Sonnet 4.6 → failed
  - More powerful model (Opus 4.7) → fewer errors but still inconsistent
  - Adaptive thinking → accurate but expensive (high tokens/latency)
- Agentic loop (30:00–31:34): most effective = **Generate → Evaluate → Repair** loop. Split into 3 independent specialized prompts instead of one giant prompt → lower latency, higher reliability

**Conclusion (33:04–33:49)**
- Rigorously use evals for every change
- Apply prompt hygiene to reduce complexity
- Use agentic loops to decompose complex tasks

---

### Read more
- (link the AI Engineering / Prompt Engineering MOC once created)
