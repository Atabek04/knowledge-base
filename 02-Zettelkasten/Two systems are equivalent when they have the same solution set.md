---
created: 2026-09-05
tags: [math, linear-algebra, solution-set, foundations]
aliases: [equivalent systems, equivalence]
---

Solving a linear system produces a trail of systems, each replacing the last, and the answer is read off the final one. <b>Equivalence</b> is the word for the relationship every pair in that trail must have, and without it the whole procedure would be unjustified.

---

### The definition

Two systems are <mark style="background: #FFF3A3A6;">equivalent when they have the same solution set</mark> — the same points satisfy both.

Note what is <i>not</i> required. They need not look alike, share coefficients, or even have the same number of equations. <mark style="background: #ABF7F7A6;">Only the answer has to match.</mark>

"Two systems" means two genuinely different collections of equations, not one system written twice.

---

### A worked example

Start with system <b>A</b>:

$$\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
x_1 &-& x_2 &=& 1
\end{array}$$

Replace the second equation with (second − first), giving system <b>B</b>:

$$\begin{array}{rrrrr}
x_1 &+&  x_2 &=&  3 \\
    & & -2x_2 &=& -2
\end{array}$$

Scale that second equation by $-\tfrac12$, giving system <b>C</b>:

$$\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
    & & x_2 &=& 1
\end{array}$$

Three systems. Apart from the first equation they share nothing, and B contains a coefficient ($-2$) appearing nowhere in A. They look like three different problems.

Substitute $(2, 1)$ into all three and every equation holds. Substitute anything else and all three fail. <mark style="background: #ABF7F7A6;">Same solution set, so all three are equivalent</mark> — and C is the one you can read the answer off, which is the entire point of having moved.

---

### What makes two systems equivalent in practice

Equivalence is a property to be <i>established</i>, not observed. Looking at A and C side by side tells you nothing; you would have to solve both to compare their solution sets, which defeats the purpose.

What supplies it is the route between them. A system reached by [[The three row operations are legal precisely because each one can be undone|the three row operations]] is equivalent to the one it came from, because [[A rewrite is safe exactly when the move that produced it can be undone|each of those moves can be undone]] — and a move that can be undone can neither lose nor gain a solution.

<mark style="background: #ADCCFFA6;">Establish equivalence from the moves you made, never from how the final system looks.</mark>

---

### Why this is the licence for the whole method

<mark style="background: #ABF7F7A6;">Because every legal move preserves the solution set, a chain of them does too.</mark> So you may keep [[Elimination replaces an equation, so solving a system means rewriting it|rewriting a system]] into simpler forms and read the answer off the final form knowing it is the answer to the original.

Equivalence is what makes the messy original and the clean final form the same question. Without it, solving would be a sequence of unjustified rewrites; with it, every intermediate system is a legitimate stand-in for the one you were asked about.

This is also why the answer never needs checking against the original system — the guarantee was established by the moves themselves, before any arithmetic happened.

---

### Read more

- [[A rewrite is safe exactly when the move that produced it can be undone]]
- [[The three row operations are legal precisely because each one can be undone]]
- [[Elimination replaces an equation, so solving a system means rewriting it]]
- [[Deriving an equation prevents losing a solution but not gaining one]]
- [[A linear system has zero, one, or infinitely many solutions and never any other count]]
- [[Math for ML MOC]]
