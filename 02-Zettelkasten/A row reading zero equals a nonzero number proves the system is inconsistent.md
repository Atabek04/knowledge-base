---
created: 2026-09-09
tags: [math, linear-algebra, solution-set, elimination]
aliases: [inconsistent row, zero equals nonzero, contradictory row, no solution signature]
---

Elimination sometimes produces a row that looks like a mistake — every coefficient zero, but the constant on the right is not. That row is not a mistake, and it is the fastest answer a system ever gives.

$$\left[\begin{array}{ccc|c} 2 & -3 & 2 & 1 \\ 0 & 1 & -4 & 8 \\ 0 & 0 & 0 & 15 \end{array}\right]$$

Read the bottom row back as an equation and it says $0x_1 + 0x_2 + 0x_3 = 15$, which is $0 = 15$.

> [!theorem] The inconsistent row
> If elimination produces a row whose coefficients are all zero and whose constant is not, the system has no solution.

<mark style="background: #FFF3A3A6;">No assignment of the variables can make that row true, and a solution must satisfy every row at once, so no solution exists.</mark>

---

### The verdict transfers back

The contradiction appeared in a system nobody was asked about — it was produced by several row operations.

It still settles the original, because [[Row equivalent matrices are linked by the route between them, since a matrix has no solution set to compare|row equivalent matrices describe systems with the same solution set]]. An empty solution set at the end means an empty solution set at the start.

<mark style="background: #ADCCFFA6;">Stop the moment such a row appears — the remaining work would compute values for a system that has none.</mark>

---

### The all-zero row

A row of zeros with a zero constant, $0 = 0$, is harmless. It is true at every point.

| Bottom row | Reads as | Meaning |
|---|---|---|
| $[\,0\ 0\ 0\ \mid 15\,]$ | $0 = 15$ | contradiction — no solution |
| $[\,0\ 0\ 0\ \mid 0\,]$ | $0 = 0$ | redundant equation — no information |

<mark style="background: #FF5582A6;">The two rows look nearly identical and mean opposite things: the constant column is the entire difference.</mark>

A $0 = 0$ row means one equation was a combination of the others and contributed nothing — the system had [[A linear system has zero, one, or infinitely many solutions and never any other count|fewer real constraints than it had equations]], which points toward infinitely many solutions rather than none.

---

### Existence answered, uniqueness not

Finding this row settles [[Existence and uniqueness are the only two questions a linear system has to answer|the existence question]] with a "no", at which point uniqueness stops being a question — there is nothing to be unique.

<mark style="background: #ABF7F7A6;">Inconsistency is detectable long before a system is solved, and detecting it is the only outcome that makes finishing the solve pointless.</mark>

---

### Glossary

| Word | In this context |
|---|---|
| <b>Inconsistent</b> | Has no solution |
| <b>Inconsistent row</b> | All coefficients zero, constant nonzero — reads $0 = b$ with $b \neq 0$ |
| <b>Redundant row</b> | All entries zero including the constant — reads $0 = 0$, always true |

---

### Read more

- [[A linear system has zero, one, or infinitely many solutions and never any other count]]
- [[Existence and uniqueness are the only two questions a linear system has to answer]]
- [[Row equivalent matrices are linked by the route between them, since a matrix has no solution set to compare]]
- [[Elimination clears one variable per column going down, then clears back up until each row names one variable]]
- [[A matrix records a linear system's numbers, with column position replacing the variable names]]
- [[Math for ML MOC]]
