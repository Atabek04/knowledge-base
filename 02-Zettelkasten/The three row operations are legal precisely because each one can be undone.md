---
created: 2026-09-05
tags: [math, linear-algebra, solution-set, foundations]
aliases: [three legal moves, row operations, elementary row operations]
---

Only three operations may be performed on a system of linear equations. The list looks arbitrary until you notice what the three have in common, and why a fourth obvious-looking candidate is missing.

The organising principle is [[A rewrite is safe exactly when the move that produced it can be undone|reversibility]]: an operation is permitted exactly when it can be walked backwards.

---

### The three, each with its undo

| Move | How to undo it |
|---|---|
| <b>Swap</b> two equations | swap them back |
| <b>Scale</b> an equation by a nonzero $c$ | scale it by $1/c$ |
| <b>Add</b> $c$ times one equation to another | subtract $c$ times that equation |

<mark style="background: #FFF3A3A6;">Each move has an inverse that is itself one of the three, so any sequence of them can be run backwards step by step.</mark>

That closure is what lets a whole chain of rewrites inherit the guarantee: undo the last move, then the one before it, and you arrive back at the system you were given.

#### Swap — exchange two whole equations

<mark style="background: #FFF3A3A6;">Swap moves entire equations up or down the list; it never moves terms across the equals sign.</mark> The equations themselves are untouched — only their order on the page changes.

$$\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
2x_1 &+& 5x_2 &=& 9
\end{array}
\qquad\longrightarrow\qquad
\begin{array}{rrrrr}
2x_1 &+& 5x_2 &=& 9 \\
x_1 &+& x_2 &=& 3
\end{array}$$

Undo: swap them back.

<mark style="background: #FF5582A6;">Moving a term from one side of an equals sign to the other is not a row operation at all.</mark> It rewrites a single equation internally, which the three moves never do.

#### Scale — multiply one equation by a nonzero number

Every term on both sides is multiplied by the same $c$. Row 1 below is scaled by $3$:

$$\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3
\end{array}
\qquad\longrightarrow\qquad
\begin{array}{rrrrr}
3x_1 &+& 3x_2 &=& 9
\end{array}$$

Undo: scale by $1/3$ — which is division, and division is just scaling by a reciprocal. That is why the list names only one of the two.

#### Add — add a multiple of one equation to another

The equation being used as the source stays exactly as it was; only the target row changes. Here $-2 \times R_1$ is added to $R_2$:

$$\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
2x_1 &+& 5x_2 &=& 9
\end{array}
\qquad\longrightarrow\qquad
\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
 & & 3x_2 &=& 3
\end{array}$$

Undo: add $+2 \times R_1$ back to $R_2$.

<mark style="background: #ABF7F7A6;">This is the only move that eliminates a variable, and it is the engine of every solution method built on these three.</mark>

---

### Why "nonzero" is doing real work

<mark style="background: #FF5582A6;">Scaling by zero has no undo, because there is no $1/0$ to scale back by.</mark>

The damage is visible immediately. Multiplying an equation by $0$ turns it into `0 = 0`, which is true at every point — the constraint is destroyed and the solution set grows.

$$\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
x_1 &-& x_2 &=& 1
\end{array}
\qquad\longrightarrow\qquad
\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
   0 & &     &=& 0
\end{array}$$

One solution has become infinitely many. The word "nonzero" in the second move is not a technicality — it is the entire difference between a legal move and a broken one.

---

### Why division is absent from the list

Dividing an equation by a nonzero constant is already covered: it is scaling by $1/c$.

What is <i>not</i> on the list is dividing by a <b>variable</b>, and its absence is deliberate. A variable may be zero, so the move has no guaranteed undo and [[Deriving an equation prevents losing a solution but not gaining one|silently discards solutions]] — the mirror-image failure to scaling by zero.

<mark style="background: #ADCCFFA6;">Every restriction in the list exists to keep the move reversible.</mark>

---

### The same three moves on a matrix

Performed on the rows of a [[A matrix records a linear system's numbers, with column position replacing the variable names|matrix]] rather than on written-out equations, these are called the <b>elementary row operations</b>. Nothing changes but the notation: a row is an equation with the variable names stripped out, and the three moves are these three moves, legal for the same reason.

Two matrices connected by a sequence of them are [[Row equivalent matrices are linked by the route between them, since a matrix has no solution set to compare|row equivalent]]. Applied in a fixed order rather than ad hoc, the same three moves become [[Elimination clears one variable per column going down, then clears back up until each row names one variable|the elimination algorithm]].

---

### Read more

- [[A rewrite is safe exactly when the move that produced it can be undone]]
- [[Two systems are equivalent when they have the same solution set]]
- [[Deriving an equation prevents losing a solution but not gaining one]]
- [[A matrix records a linear system's numbers, with column position replacing the variable names]]
- [[Row equivalent matrices are linked by the route between them, since a matrix has no solution set to compare]]
- [[Elimination clears one variable per column going down, then clears back up until each row names one variable]]
- [[Math for ML MOC]]
