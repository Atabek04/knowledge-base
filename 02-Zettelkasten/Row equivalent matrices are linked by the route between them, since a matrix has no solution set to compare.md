---
created: 2026-09-06
tags: [math, linear-algebra, matrices, equivalence, foundations]
aliases: [row equivalent, row equivalence, row equivalent matrices]
---

Two systems are called equivalent when they have the same solution set. Matrices need a relation of their own, because a matrix is a rectangular array of numbers and nothing in it answers "what is the solution?" — it may not have come from a system at all.

> [!definition] Row equivalent
> Two matrices are <b>row equivalent</b> if some sequence of elementary row operations transforms one into the other.

<mark style="background: #FFF3A3A6;">Row equivalence is defined by the route between two matrices, never by anything visible in the matrices themselves.</mark>

<mark style="background: #ABF7F7A6;">Exhibiting one legal sequence is a complete proof of row equivalence — no solution set has to be known, or to exist.</mark> The two matrices could describe systems nobody has solved, or no system at all.

<mark style="background: #FF5582A6;">The phrase <i>row equivalent</i> misleads twice: the relation compares two whole matrices rather than two rows, and it asks only whether a sequence of operations <i>exists</i>, not whether anyone performed one.</mark>

<i>Row</i> names the kind of operation, not the thing being compared. And two matrices with no shared history can still be row equivalent — the usual case, where the second was built from the first, just answers the question for free.

---

### The two relations side by side

A system and its augmented matrix are the same data in two notations, so the two relations are not asking about different objects. <mark style="background: #ABF7F7A6;">They are two different tests applied to the same pair, and one is strictly stricter than the other.</mark>

| | Equivalent systems | Row equivalent matrices |
|---|---|---|
| The test | compare the <b>solution sets</b> | find a <b>sequence of row operations</b> between them |
| Defined by | the <b>outcome</b> | the <b>route</b> |
| Says nothing about | how either was obtained | what either one solves |
| Strength | the weaker demand | the stricter one — passing it grants the other free |
| Askable without a system? | no, there is nothing to solve | yes, any two matrices qualify |

<mark style="background: #ABF7F7A6;">A bare matrix has no solution set, so "same answer" is unavailable as a definition and the route is the only thing left to compare.</mark>

The upside of defining it that way is reach: [[The three row operations are legal precisely because each one can be undone|the three row operations]] apply to any matrix whatever, so row equivalence is a relation on all matrices — not only on the ones that happen to be [[A matrix records a linear system's numbers, with column position replacing the variable names|augmented matrices of systems]].

The full outcome-side story is [[Two systems are equivalent when they have the same solution set|equivalence of systems]].

---

### The relation runs both ways

If a sequence of operations takes $A$ to $B$, undoing each operation in reverse order takes $B$ back to $A$. <mark style="background: #ABF7F7A6;">Row equivalence is therefore symmetric — there is no "direction" to it, and saying $A$ is row equivalent to $B$ says exactly the same thing as the reverse.</mark>

That symmetry is what makes the word <i>equivalent</i> honest rather than decorative. A one-way relation would be a derivation, and [[Deriving an equation prevents losing a solution but not gaining one|derivation alone is a weaker guarantee]].

---

### The bridge back to systems

> [!theorem] Row equivalence preserves the solution set
> If the augmented matrices of two linear systems are row equivalent, then the two systems have the same solution set.

The argument is the one already made for systems, restated one level down in the notation:

- Every solution of the original satisfies the new system, because each row operation is a legal move.
- Every solution of the new system satisfies the original, because the operations can be run backwards to rebuild it.

<mark style="background: #ADCCFFA6;">Establish that two systems agree by pointing at the operations performed, never by comparing how their matrices look.</mark>

This is what licenses the whole method: a solution read off the final matrix is a solution of the original system, because row equivalence carried the solution set through every step unchanged.

#### The implication runs one way only

<mark style="background: #FF5582A6;">Row equivalent ⟹ same solution set. The converse fails: two systems can share a solution set without their augmented matrices being row equivalent.</mark>

Nothing is lost by that. The theorem is used in the direction that matters — you perform operations and want the answer to survive — and never in reverse.

#### Same solution set, no route

Both of these are satisfied by exactly the points on the line $x_1 + x_2 = 1$:

$$\begin{array}{rrrrr}
x_1 &+& x_2 &=& 1
\end{array}
\qquad\qquad
\begin{array}{rrrrr}
 x_1 &+&  x_2 &=& 1 \\
2x_1 &+& 2x_2 &=& 2
\end{array}$$

$$\left[\begin{array}{cc|c} 1 & 1 & 1 \end{array}\right]
\qquad\qquad
\left[\begin{array}{cc|c} 1 & 1 & 1 \\ 2 & 2 & 2 \end{array}\right]$$

Equivalent systems, and their matrices are not row equivalent: one is $1 \times 3$ and the other $2 \times 3$, and <mark style="background: #ABF7F7A6;">no row operation ever adds or removes a row, so a matrix can never reach one of a different size.</mark>

Matching sizes do not rescue the converse either. Both systems below are inconsistent, so both solution sets are empty and the systems are equivalent:

$$\begin{array}{rrrrr}
x_1 &=& 0 \\
x_1 &=& 1
\end{array}
\qquad\qquad
\begin{array}{rrrrr}
x_1 &+& x_2 &=& 0 \\
x_1 &+& x_2 &=& 1
\end{array}$$

$$\left[\begin{array}{cc|c} 1 & 0 & 0 \\ 1 & 0 & 1 \end{array}\right]
\qquad\qquad
\left[\begin{array}{cc|c} 1 & 1 & 0 \\ 1 & 1 & 1 \end{array}\right]$$

The first matrix has an all-zero $x_2$ column, and every row operation combines, swaps or scales entries within rows — a column of zeros stays a column of zeros. The second can therefore never be reached from the first.

---

### Glossary

| Word | In this context |
|---|---|
| <b>Row equivalent</b> | Two matrices, one reachable from the other by elementary row operations |
| <b>Equivalent systems</b> | Two systems with the same solution set |
| <b>Symmetric</b> | The relation holds in both directions; order of the two matrices is irrelevant |
| <b>Converse</b> | The implication read backwards — here, false |

---

### Read more

- [[Two systems are equivalent when they have the same solution set]]
- [[The three row operations are legal precisely because each one can be undone]]
- [[A matrix records a linear system's numbers, with column position replacing the variable names]]
- [[A rewrite is safe exactly when the move that produced it can be undone]]
- [[Deriving an equation prevents losing a solution but not gaining one]]
- [[Math for ML MOC]]
