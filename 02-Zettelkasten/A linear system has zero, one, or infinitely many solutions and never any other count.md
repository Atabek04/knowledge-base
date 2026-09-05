---
created: 2026-09-05
tags: [math, linear-algebra, solution-set, foundations]
aliases: [solution set, consistent system, inconsistent system]
---

School algebra trains one expectation: a system of equations has <i>an</i> answer, and solving means finding it. That expectation is a special case, and holding onto it makes the general theory look like a series of exceptions.

The textbook phrase is <b>solution set</b>, plural — and the plural is deliberate.

---

### Only three outcomes are possible

<mark style="background: #FF5582A6;">A linear system has zero, exactly one, or infinitely many solutions. No other count can occur.</mark>

There is never a system with exactly two solutions, or seventeen. That is a genuine theorem, not a simplification, and it is one of the strongest facts in the subject — it means "how many solutions?" has only three answers to check.

Seen as two lines in a plane, the three cases are exactly the three ways two lines can sit:

| Geometry | Solutions | Name |
|---|---|---|
| They cross once | exactly one | <b>consistent</b> |
| Parallel and distinct | none | <b>inconsistent</b> |
| The same line | infinitely many | <b>consistent</b> |

#### No solution — contradictory constraints

$$\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
x_1 &+& x_2 &=& 5
\end{array}$$

The same quantity cannot equal two different numbers. The lines are parallel and never meet, and no assignment of `x₁` and `x₂` can satisfy both.

#### Infinitely many — a redundant constraint

$$\begin{array}{rrrrr}
 x_1 &+&  x_2 &=& 3 \\
2x_1 &+& 2x_2 &=& 6
\end{array}$$

The second equation is the first one doubled. It draws the same line and <mark style="background: #FFF3A3A6;">adds no information</mark>, so every point on that line satisfies both equations.

Two equations were written, but only one constraint exists. This is why counting equations is not the same as counting constraints.

---

### Consistent is the word to keep

<mark style="background: #FFF3A3A6;">A system is <b>consistent</b> when it has at least one solution</mark> — one or infinitely many — and <b>inconsistent</b> when it has none.

The name is apt: an inconsistent system is one whose equations contradict each other. Consistency is a question about the equations agreeing, asked before any question about what the answer is.

---

### A solution is one point, a solution set is all of them

These two are separate objects and the words are not interchangeable.

- A <mark style="background: #FFF3A3A6;">solution</mark> is a single assignment, written as an ordered list `(s₁, s₂, …, sₙ)`. Order carries meaning — position says which variable — so `(5, 6.5, 3)` means `x₁ = 5`, `x₂ = 6.5`, `x₃ = 3` and nothing else.
- The <mark style="background: #FFF3A3A6;">solution set</mark> is the collection of every such point.

<mark style="background: #ABF7F7A6;">The solution set is the real answer to a system</mark>, and it may be empty, a single point, or an infinite family. "Solve the system" means describe that set, not produce one number.

---

### Read more

- [[Two systems are equivalent when they have the same solution set]]
- [[Solving a linear system means finding where the shapes its equations draw intersect]]
- [[The number of variables sets the dimension and each equation draws a shape one dimension lower]]
- [[Math for ML MOC]]
