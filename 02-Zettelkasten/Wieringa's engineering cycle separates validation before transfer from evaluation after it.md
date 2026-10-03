---
aliases: [engineering cycle, design cycle, treatment validation, validation vs evaluation, Wieringa cycle]
---

Once a thesis is [[Design science builds an artifact to test an idea and the knowledge from evaluating it is the contribution|design science]], the next question is which part of the engineer's work is research and which is practice. Wieringa (*Design Science Methodology for Information Systems and Software Engineering*, 2014, ch 3) answers with the **engineering cycle**: the loop an engineer runs on a real problem, and the line inside it where research stops.

---

### The five tasks

1. **Problem investigation**: who has the problem, what causes it, what would count as improvement.
2. **Treatment design**: specify the artifact that should produce that improvement.
3. **Treatment validation**: predict, in a setting the researcher controls, whether the design *would* produce the effect once implemented.
4. **Treatment implementation**: transfer the artifact into the real context.
5. **Implementation evaluation**: study what happened in the real context after transfer.

The first three tasks form the **design cycle**, and that is the whole of what a research project does. <mark style="background: #FFF3A3A6;">Research runs the design cycle, problem investigation through validation; implementation and evaluation belong to practice, after the researcher has handed the artifact over.</mark>

---

### Validation and evaluation are two words on purpose

Wieringa uses *validation* and *evaluation* for different things, and the difference is not whether the artifact has been released. <mark style="background: #ABF7F7A6;">Validation happens in a context the researcher controls, before transfer; evaluation happens in the real context, after transfer, where nobody assigns anything.</mark>

| | Validation | Evaluation |
|---|---|---|
| When | before transfer to practice | after transfer |
| Context | artificial: recruited sample, assigned conditions, fixed protocol | real: users adopt on their own |
| Question | would it work if implemented? | what happened once it was? |
| Buys | causal isolation: which mechanism did what | realism |
| Costs | realism | control and a counterfactual |

A recruited within-subjects study with assigned conditions and a fixed schedule is validation even if the same app is publicly available that day. The researcher's control over the context is what makes it artificial. Observing whoever installs the app after release, with no assignment, is evaluation.

---

### Two confusions the word invites

<mark style="background: #FF5582A6;">Startup "idea validation", asking whether people have the problem, is Wieringa's problem investigation, not validation; validation asks whether the treatment produces the effect, and assumes the problem is already established.</mark>

The second confusion is treating a launched product as evaluation. Launch is implementation; evaluation is the later study of real use. A thesis can validate a treatment that is already in production, provided the study itself controls the context.

### Read more

- [[Design science builds an artifact to test an idea and the knowledge from evaluating it is the contribution]]
- [[A dissertation's type is fixed by what its contribution is, not by what the student did]]
- [[Research Craft - MOC]]
