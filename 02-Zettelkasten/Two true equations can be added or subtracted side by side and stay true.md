---
created: 2026-09-09
tags: [math, linear-algebra, foundations]
aliases: [subtracting equals from equals, adding equals to equals, combining two equations]
---

Every elimination step in a linear system takes two equations and combines them into one: subtract this row from that one, add twice this row to another. The step feels obviously allowed, but what licenses it is a rule old enough to be one of Euclid's common notions, and it is worth stating on its own.

---

### Adding and subtracting two equations

> [!theorem] Equals combined with equals give equals
> If $a = b$ and $c = d$, then $a - c = b - d$ and $a + c = b + d$.

Two separate true statements go in; a third true statement comes out. Nothing about the individual letters is assumed, only that each pair was equal to begin with.

#### Why it holds

Picture a balanced scale holding $a$ against $b$, and a second balanced scale holding $c$ against $d$. Take the contents of the second scale off the first, left pan from left pan and right pan from right pan. The two amounts removed were equal to each other, so <mark style="background: #ABF7F7A6;">removing equal amounts from both sides of a balanced scale leaves it balanced.</mark>

![[subtracting_equals_from_equals_balance_scale.jpg|620]]

The same picture read backwards gives the addition case: hanging equal weights on both pans tips nothing.

---

### Scaling by a constant

Multiplying one equation through by a constant $k$ is the same move, with $c$ and $d$ chosen to be $k$ copies of the two sides:

$$\text{if } a = b, \text{ then } ka = kb \text{ for any constant } k$$

<mark style="background: #ADCCFFA6;">The factor must be a genuine number, never a variable whose value is still unknown.</mark> A variable might be zero, and multiplying by zero flattens the equation into $0 = 0$, which is still true but true of everything.

---

### Use in elimination

An elimination step is this rule applied to two rows of a system. Subtracting the second equation from the first:

$$\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
x_1 &-& x_2 &=& 1
\end{array}
\qquad\longrightarrow\qquad
2x_2 = 2$$

Any point satisfying both originals satisfies the result, because the rule says so. <mark style="background: #FF5582A6;">That guarantee runs one way only: the new equation keeps every old solution, but it may also accept points the originals rejected.</mark> Which is why combining equations is safe against [[Deriving an equation prevents losing a solution but not gaining one|losing a solution but not against gaining one]].

---

### Read more

- [[Deriving an equation prevents losing a solution but not gaining one]]
- [[Elimination replaces an equation, so solving a system means rewriting it]]
- [[A rewrite is safe exactly when the move that produced it can be undone]]
- [[Math for ML MOC]]
