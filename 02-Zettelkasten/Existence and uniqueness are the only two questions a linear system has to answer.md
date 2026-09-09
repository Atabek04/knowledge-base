---
created: 2026-09-09
tags: [math, linear-algebra, solution-set, foundations]
aliases: [existence and uniqueness, two fundamental questions, is the system consistent]
---

"Solve the system" sounds like one task, but almost every question asked about a system in practice is one of two, and neither of them requires producing the answer.

> [!definition] The two fundamental questions
> 1. <b>Existence</b> — is the system consistent; that is, does at least one solution exist?
> 2. <b>Uniqueness</b> — if a solution exists, is it the only one?

<mark style="background: #ABF7F7A6;">Between them the two questions pin down the solution set completely, because a linear system has only three possible outcomes and these two yes/no answers separate all three.</mark>

| Existence | Uniqueness | Outcome |
|---|---|---|
| no | — | no solution |
| yes | yes | exactly one solution |
| yes | no | infinitely many |

The first question splits [[A linear system has zero, one, or infinitely many solutions and never any other count|the three solution counts]] into "none" against "some"; the second splits "some" into one against infinitely many. There is no third question to ask, because there is no fourth outcome to distinguish.

---

### Answering them is cheaper than solving

<mark style="background: #ADCCFFA6;">Both questions can be answered from a partly solved system, before any value has been computed.</mark>

Take the triangular form reached halfway through [[Elimination clears one variable per column going down, then clears back up until each row names one variable|the elimination algorithm]]:

$$\begin{array}{rrrrrrr}
 x_1 &-& 2x_2 &+&  x_3 &=& 0 \\
     & &  x_2 &-& 4x_3 &=& 4 \\
     & &      & &  x_3 &=& -1
\end{array}
\qquad
\left[\begin{array}{ccc|c} 1 & -2 & 1 & 0 \\ 0 & 1 & -4 & 4 \\ 0 & 0 & 1 & -1 \end{array}\right]$$

The bottom row fixes $x_3$. Substituting it into row 2 would force $x_2$, and both into row 1 would force $x_1$.

<mark style="background: #ABF7F7A6;">Each row leaves exactly one variable to determine and no freedom in what it becomes, so a solution exists and it is unique.</mark> Both questions are answered, and not one of the three values has been computed.

<mark style="background: #FF5582A6;">Knowing the answer exists is not the same as knowing it.</mark> Existence and uniqueness are questions about the <i>shape</i> of the solution set; producing the point is separate work, and often not the work you were asked for.

---

### Why the pair keeps returning

The same two questions reappear throughout linear algebra in different vocabulary — spanning and linear independence, injective and surjective maps, invertibility — because they are the two things that can go wrong with any equation-like object.

<mark style="background: #FFF3A3A6;">Existence asks whether the target is reachable at all; uniqueness asks whether it is reachable in more than one way.</mark> Recognising a new theorem as one of these two in disguise is most of what makes the subject cohere rather than accumulate.

---

### Glossary

| Word | In this context |
|---|---|
| <b>Existence</b> | Whether at least one solution exists — the system is consistent |
| <b>Uniqueness</b> | Whether that solution is the only one |
| <b>Consistent</b> | Has at least one solution; the answer to question 1 being yes |

---

### Read more

- [[A linear system has zero, one, or infinitely many solutions and never any other count]]
- [[Elimination clears one variable per column going down, then clears back up until each row names one variable]]
- [[A row reading zero equals a nonzero number proves the system is inconsistent]]
- [[Solving a linear system means finding where the shapes its equations draw intersect]]
- [[Math for ML MOC]]
