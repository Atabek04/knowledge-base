---
created: 2026-09-06
tags: [math, linear-algebra, elimination, algorithm, foundations]
aliases: [elimination algorithm, solving a system step by step, forward elimination, back substitution]
---

The three legal moves say what you are <i>allowed</i> to do to a system. They do not say what to do first. Left unordered they are a pile of options; the procedure below is the order that turns them into an algorithm, and it is the same order whether the work is written as equations or as rows of a matrix.

The system worked here is Lay's Example 1:

$$\begin{array}{rrrrrrr}
 x_1 &-& 2x_2 &+&  x_3 &=& 0 \\
     & &  2x_2 &-& 8x_3 &=& 8 \\
5x_1 & &       &-& 5x_3 &=& 10
\end{array}
\qquad
\left[\begin{array}{ccc|c} 1 & -2 & 1 & 0 \\ 0 & 2 & -8 & 8 \\ 5 & 0 & -5 & 10 \end{array}\right]$$

Every step below is one of [[The three row operations are legal precisely because each one can be undone|the three row operations]], so every system it produces is [[Two systems are equivalent when they have the same solution set|equivalent to the one before it]]. The matrix on the right is the [[A matrix records a linear system's numbers, with column position replacing the variable names|augmented matrix]], carried alongside to show that the two notations do the same work.

---

### Where elimination stops

Read a row from left to right and stop at the first coefficient that is not zero. <mark style="background: #FFF3A3A6;">That number is the row's <b>leading coefficient</b>, and the variable it multiplies is the row's <b>leading variable</b>.</mark>

$$\begin{array}{rcl}
0x_1 + 2x_2 - 8x_3 = 8 & \quad & \text{leads with } x_2 \\
0x_1 + 0x_2 + x_3 = -1 & \quad & \text{leads with } x_3
\end{array}$$

Zeros before the first nonzero entry are skipped — a variable absent from a row can never be that row's leading variable.

#### Distinct leading variables

<mark style="background: #ADCCFFA6;">The goal of elimination is to reach a system where each row leads with a different variable, and the leading variable moves further right as you go down.</mark>

$$\begin{array}{rrrrrrrl}
 x_1 &-& 2x_2 &+&  x_3 &=& 0 & \quad \text{leads with } x_1 \\
     & &  x_2 &-& 4x_3 &=& 4 & \quad \text{leads with } x_2 \\
     & &      & &  x_3 &=& -1 & \quad \text{leads with } x_3
\end{array}$$

A row is still allowed to <i>contain</i> other variables — the first row above holds all three. The restriction is only on which variable each row <b>leads</b> with.

<mark style="background: #ABF7F7A6;">Two rows leading with the same variable means work is still owed: a multiple of one can be subtracted from the other to remove that variable, which is precisely the step the algorithm performs.</mark>

Each row therefore ends up carrying a variable no other row is competing for, and the bottom row — leading with the last variable and holding nothing else — is solved outright.

---

### Going down the columns

<mark style="background: #ADCCFFA6;">Work column by column from the left: keep the leading variable in one equation, and use it to remove that variable from every equation below.</mark>

#### Clearing column 1

Add $-5$ times equation 1 to equation 3:

$$\begin{array}{rrrrrrr}
 x_1 &-& 2x_2 &+&  x_3 &=& 0 \\
     & &  2x_2 &-& 8x_3 &=& 8 \\
     & & 10x_2 &-& 10x_3 &=& 10
\end{array}
\qquad
\left[\begin{array}{ccc|c} 1 & -2 & 1 & 0 \\ 0 & 2 & -8 & 8 \\ 0 & 10 & -10 & 10 \end{array}\right]$$

Equation 2 needed nothing — it already had no $x_1$ term.

#### Swapping past a zero

The system above happened to open with an $x_1$ term. One that does not has nothing to eliminate with:

$$\begin{array}{rrrrrrr}
     & &  x_2 &-& 4x_3 &=& 8 \\
2x_1 &-& 3x_2 &+& 2x_3 &=& 1 \\
4x_1 &-& 8x_2 &+& 12x_3 &=& 1
\end{array}$$

Equation 1 cannot clear $x_1$ from anything, because it has no $x_1$.

<mark style="background: #ADCCFFA6;">Interchange it with a row below that does — the swap costs nothing and is what the operation exists for.</mark> Exchanging equations 1 and 2 puts a usable $2x_1$ on top and the column can then be cleared as usual.

This is the only place the algorithm needs the swap, and it is why a list of two operations would not be enough.

#### Scaling the leading coefficient

Multiply equation 2 by $\tfrac12$:

$$\begin{array}{rrrrrrr}
 x_1 &-& 2x_2 &+&  x_3 &=& 0 \\
     & &   x_2 &-& 4x_3 &=& 4 \\
     & & 10x_2 &-& 10x_3 &=& 10
\end{array}
\qquad
\left[\begin{array}{ccc|c} 1 & -2 & 1 & 0 \\ 0 & 1 & -4 & 4 \\ 0 & 10 & -10 & 10 \end{array}\right]$$

<mark style="background: #ABF7F7A6;">Scaling to a leading 1 is optional for correctness and worth doing anyway, because a coefficient of 1 makes every later multiplier a whole number instead of a fraction.</mark>

#### Clearing column 2

Add $-10$ times equation 2 to equation 3, then scale the result by $\tfrac{1}{30}$:

$$\begin{array}{rrrrrrr}
 x_1 &-& 2x_2 &+&  x_3 &=& 0 \\
     & &   x_2 &-& 4x_3 &=& 4 \\
     & &       & &  x_3 &=& -1
\end{array}
\qquad
\left[\begin{array}{ccc|c} 1 & -2 & 1 & 0 \\ 0 & 1 & -4 & 4 \\ 0 & 0 & 1 & -1 \end{array}\right]$$

<mark style="background: #FFF3A3A6;">A system whose zeros form a staircase below the diagonal is in <b>triangular</b> form: each equation involves one variable fewer than the one above it.</mark>

The bottom row now reads $x_3 = -1$ outright, and the downward pass is finished.

At this halfway point [[Existence and uniqueness are the only two questions a linear system has to answer|both fundamental questions are already answered]] — each row leaves one variable forced, so a solution exists and is unique — even though no value has been computed yet.

<mark style="background: #FF5582A6;"><i>Triangular</i> is an informal term, replaced by a precise one — echelon form — once the general shape is defined.</mark> It describes the picture, not the rule.

---

### Going back up the columns

The system could be finished from here by substituting $x_3 = -1$ into the row above, then both values into the row above that. Continuing with row operations instead keeps the work mechanical, and mechanical is what survives at 500 variables.

<mark style="background: #ADCCFFA6;">Work from the bottom row upward, using each solved variable to clear its column above.</mark>

#### Clearing column 3 upward

Add $4$ times equation 3 to equation 2, and $-1$ times equation 3 to equation 1:

$$\begin{array}{rrrrrrr}
 x_1 &-& 2x_2 & & &=& 1 \\
     & &   x_2 & & &=& 0 \\
     & &       & &  x_3 &=& -1
\end{array}
\qquad
\left[\begin{array}{ccc|c} 1 & -2 & 0 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & -1 \end{array}\right]$$

#### Clearing column 2 upward

Add $2$ times equation 2 to equation 1:

$$\begin{array}{rrrrrrr}
 x_1 & & & & &=& 1 \\
     & &   x_2 & & &=& 0 \\
     & &       & &  x_3 &=& -1
\end{array}
\qquad
\left[\begin{array}{ccc|c} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & -1 \end{array}\right]$$

<mark style="background: #ABF7F7A6;">The algorithm stops when every row names exactly one variable, because at that point no arithmetic is left: each row states its variable's value outright.</mark>

The solution is $(1, 0, -1)$.

#### Why not go upward first

Clearing $x_3$ from the upper rows first is cheaper than clearing $x_2$ first, because once the $x_3$ column is clean no later step has any $x_3$ arithmetic left to carry. Ordering the passes this way is not required for correctness, only for effort.

---

### What checking actually verifies

Substituting $(1, 0, -1)$ into the <i>original</i> system:

$$\begin{array}{rcl}
1(1) - 2(0) + 1(-1) &=& 0 \\
2(0) - 8(-1) &=& 8 \\
5(1) - 5(-1) &=& 10
\end{array}$$

All three match the original right-hand sides.

<mark style="background: #FF5582A6;">This check catches slips in the arithmetic, never a flaw in the procedure.</mark> The procedure needed no checking: every step was a reversible move, so the final system was guaranteed to have the original's solution set before a single number was substituted.

Worth doing anyway — the number of hand calculations in a long elimination is exactly where mistakes live.

---

### Glossary

| Word                       | In this context                                                                             |
| -------------------------- | ------------------------------------------------------------------------------------------- |
| <b>Elimination</b>         | Removing a variable from an equation by adding a multiple of another equation to it         |
| <b>Leading coefficient</b> | The first nonzero number in a row, reading left to right                                    |
| <b>Leading variable</b>    | The variable that leading coefficient multiplies; every row must lead with a different one  |
| <b>Triangular form</b>     | Zeros in a staircase below the diagonal; each row has one variable fewer than the row above |
| <b>Forward pass</b>        | Going down the columns, clearing below the diagonal, ending in triangular form              |
| <b>Backward pass</b>       | Going up from the bottom row, clearing above the diagonal, ending with one variable per row |

---

### Read more

- [[The three row operations are legal precisely because each one can be undone]]
- [[Two systems are equivalent when they have the same solution set]]
- [[A matrix records a linear system's numbers, with column position replacing the variable names]]
- [[Elimination replaces an equation, so solving a system means rewriting it]]
- [[A rewrite is safe exactly when the move that produced it can be undone]]
- [[Solving a linear system means finding where the shapes its equations draw intersect]]
- [[Existence and uniqueness are the only two questions a linear system has to answer]]
- [[A row reading zero equals a nonzero number proves the system is inconsistent]]
- [[Elimination runs in floating point on a computer, so every stored number is an approximation]]
- [[Math for ML MOC]]
