---
aliases: [GPT Tutor study, Bastani study, AI tutor guardrails, hint-only AI tutor]
---

Giving students a chatbot during practice looks like a pure win: their practice scores go up immediately.

A field experiment in high-school maths showed what happens when the chatbot is taken away, and that the design of the tool decides whether students learn or lean.

---

### The experiment

Bastani and colleagues (PNAS, 2025) gave nearly 1,000 high-school maths students one of three conditions during practice sessions:

- no AI (control)
- **GPT Base**: a standard ChatGPT-style interface on GPT-4
- **GPT Tutor**: the same model, prompted with teacher-written hints and instructed not to hand over the full solution

Afterwards, every student sat an exam without any AI.

---

### Practice gains, exam losses

During practice, GPT Base raised grades by 48% and GPT Tutor by 127%.

On the exam, the GPT Base students scored 17% lower than the control group, who had never had AI at all. Students had used it as a crutch, asking for answers and copying them.

GPT Tutor students landed at roughly the control group's level: the loss was avoided.

#### Practice scores measure the pair, not the student

<mark style="background: #ABF7F7A6;">A practice score taken with AI measures what the student and the tool can do together, while the exam measures what the student can do alone.</mark> The two can move in opposite directions.

<mark style="background: #FF5582A6;">A jump in scores while the AI is available is not evidence that any learning happened.</mark>

---

### What the guardrail changed

The tutor withheld the one thing a crutch needs: the finished answer. Students still got unstuck, but they had to take the last step themselves, which kept the [[Desirable difficulties make learning harder in ways that improve long-term retention over short-term fluency|generation effect]] in play.

<mark style="background: #ADCCFFA6;">When the goal is learning, configure the AI to give hints and withhold full solutions.</mark> Claude's Learning mode and ChatGPT's Study mode are built-in versions of the same guardrail.

The guardrail prevented harm; it did not produce a measurable exam gain over learning without AI.

---

### Read more
- [[Using AI to bypass work causes skill atrophy while using it for inquiry builds skill]]
- [[Desirable difficulties make learning harder in ways that improve long-term retention over short-term fluency]]
- [[Ten minutes of AI help makes people give up sooner on problems they then face alone]]
- [[Effective AI learning removes friction from busywork and adds friction to thinking]]
- [[Agentic Engineering MOC]]

### External Resources
- [Bastani et al. (2025), PNAS: Generative AI without guardrails can harm learning](https://www.pnas.org/doi/10.1073/pnas.2422633122)
- [Knowledge at Wharton: Without Guardrails, Generative AI Can Harm Education](https://knowledge.wharton.upenn.edu/article/without-guardrails-generative-ai-can-harm-education/)
