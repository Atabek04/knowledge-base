---
created: 2026-10-18
tags: [education, ai-in-education, its]
aliases: [step-based tutor, answer-based tutor, tutoring granularity]
---

Tutoring systems differ in how small a piece of the student's work they respond to. VanLehn (2011) used that size to sort every kind of tutor, human or software, into one scale.

### Glossary

- **Granularity**: <mark style="background: #FFF3A3A6;">the size of the unit of student work a tutor responds to: the whole answer, each step, or parts of a step</mark>.
- **Answer-based tutor**: a tutor that gives feedback only on the final answer.
- **Step-based tutor**: a tutor that gives feedback on each step of the solution as the student enters it.
- **Substep-based tutor**: a tutor that breaks a step further, usually through dialogue about the reasoning behind it.

---

### Why an answer cannot say which step broke

Two students write the accusative ending (fatha) where the genitive (kasra) belongs after a preposition. One misread which word is the preposition. The other knew the preposition but forgot that it takes the genitive.

Their final answers are identical, so an answer-based tutor gives both the same feedback. <mark style="background: #ABF7F7A6;">A final answer is the output of every step at once, so a wrong answer shows that some step failed but not which one.</mark>

---

### How a step-based tutor locates the error

A step-based tutor makes the steps visible by asking for them: first "which word is the preposition?", then "which case does it take?", then the ending.

The first student fails the first step, the second student fails the second. Each gets feedback on their own error, and the **learner model** records two different weaknesses instead of one vague "case endings wrong".

<mark style="background: #FF5582A6;">Step-based feedback only works if the interface makes the student enter the steps; a free-text box that receives only the final answer stays answer-based however smart the model behind it.</mark>

---

### Source

- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist*, 46(4), 197–221. https://doi.org/10.1080/00461520.2011.611369

### Read more

- [[AI in Education MOC]]
- [[An intelligent tutoring system has four parts, and the learner model is what lets it remember a student]]
