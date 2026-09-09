---
created: 2026-09-06
tags: [math, linear-algebra, notation, foundations]
aliases: [matrix, matrix notation, augmented matrix, coefficient matrix, matrix size]
---

Writing a system out in full means writing `x₁`, `x₂`, `x₃` on every line, and none of those symbols ever changes. Only the numbers do. Matrix notation drops the names and keeps the numbers, which is what makes the mechanical solving methods possible to write down at all.

---

### A matrix is a rectangular array of numbers

<mark style="background: #FFF3A3A6;">A <b>matrix</b> is a rectangular array of numbers.</mark> Nothing more is required of it — no meaning is built into the definition.

The meaning comes from how a system is loaded into it. Take this system, with the coefficients of each variable aligned in columns:

$$\begin{array}{rrrrrrr}
 x_1 &-& 2x_2 &+&  x_3 &=& 0 \\
     & &  2x_2 &-& 8x_3 &=& 8 \\
5x_1 & &       &-& 5x_3 &=& 10
\end{array}$$

Each row of the matrix will be one equation, and each column one variable.

<mark style="background: #ABF7F7A6;">Position is what replaces the variable names: a number's column says which variable it multiplies, so the name is no longer needed to say it.</mark>

That is also why the alignment above matters. A gap in the written system — the missing $x_2$ term in the third equation — becomes a $0$ in the matrix, and a missing gap becomes a number in the wrong column.

---

### Coefficient matrix and augmented matrix

Two matrices come out of one system, and they differ by exactly one column.

#### Coefficient matrix — the left-hand sides only

$$\begin{bmatrix} 1 & -2 & 1 \\ 0 & 2 & -8 \\ 5 & 0 & -5 \end{bmatrix}$$

<mark style="background: #FFF3A3A6;">The <b>coefficient matrix</b> (also <i>matrix of coefficients</i>) holds the coefficients of the variables and nothing else.</mark>

The second row opens with $0$ because the second equation carries no $x_1$ term — written in full it is $0 \cdot x_1 + 2x_2 - 8x_3 = 8$. <mark style="background: #FF5582A6;">A variable absent from an equation is not a missing entry; it is a coefficient of zero, and it must be written.</mark> Leaving the position empty shifts every later number into the wrong column.

#### Augmented matrix — with the constants attached

$$\left[\begin{array}{ccc|c} 1 & -2 & 1 & 0 \\ 0 & 2 & -8 & 8 \\ 5 & 0 & -5 & 10 \end{array}\right]$$

<mark style="background: #FFF3A3A6;">The <b>augmented matrix</b> is the coefficient matrix with one added column holding the constants from the right-hand sides.</mark>

The name says what happened: the coefficient matrix was <i>augmented</i> — enlarged by one column. The vertical bar is a reading aid marking where the equals signs used to be; it is not part of the matrix.

<mark style="background: #ADCCFFA6;">Solve with the augmented matrix, because the coefficient matrix alone has thrown away the right-hand sides and no longer describes the system.</mark>

---

### Size is written m × n, rows first

<mark style="background: #FFF3A3A6;">The <b>size</b> of a matrix is its number of rows and columns, written $m \times n$ for $m$ rows and $n$ columns.</mark>

The augmented matrix above has 3 rows and 4 columns, so it is a $3 \times 4$ matrix — read aloud as "three by four". The coefficient matrix is $3 \times 3$.

<mark style="background: #FF5582A6;">The number of rows always comes first, and reversing the pair names a different matrix.</mark> A $3 \times 4$ and a $4 \times 3$ matrix are not the same shape.

The same row-then-column order governs [[Subscript notation lets one formula describe any number of unknowns|the double subscript $a_{ij}$]], which addresses the entry in row $i$, column $j$.

---

### What the numbers mean once the names are gone

A row is an equation; a column is a variable. That correspondence is the whole content of the notation, and it is what lets [[The three row operations are legal precisely because each one can be undone|the three row operations]] be performed on rows of numbers rather than on written-out equations — under the name <b>elementary row operations</b>, doing the same thing for the same reason.

Two matrices reachable from each other that way are called [[Row equivalent matrices are linked by the route between them, since a matrix has no solution set to compare|row equivalent]], which is how one matrix is certified to describe the same system as another.

---

### Glossary

| Word | In this context |
|---|---|
| <b>Matrix</b> | A rectangular array of numbers |
| <b>Entry</b> | One number in the array, addressed by row then column |
| <b>Coefficient matrix</b> | The coefficients of the variables, left-hand sides only |
| <b>Augmented matrix</b> | The coefficient matrix plus a column of the constants |
| <b>Augmented</b> | Enlarged — here, by exactly one column |
| <b>Size</b> | $m \times n$: $m$ rows by $n$ columns, rows first |

---

### Read more

- [[Subscript notation lets one formula describe any number of unknowns]]
- [[The three row operations are legal precisely because each one can be undone]]
- [[Elimination replaces an equation, so solving a system means rewriting it]]
- [[An equation is linear when every variable stands alone to the first power and is multiplied only by a constant]]
- [[Math for ML MOC]]
