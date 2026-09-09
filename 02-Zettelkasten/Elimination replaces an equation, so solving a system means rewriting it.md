---
created: 2026-09-05
tags: [math, linear-algebra, solution-set, foundations]
aliases: [elimination is rewriting, solving as rewriting]
---

Textbooks say that solving a linear system means "rewriting it into a simpler equivalent form". To anyone who learned elimination at school that sounds like a new technique, with nothing to attach it to.

It is not new. It is a name for what elimination has been doing all along, watched one step at a time.

---

### Watch a single elimination step

Take the familiar pair:

$$\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
x_1 &-& x_2 &=& 1
\end{array}$$

Subtract the second equation from the first to eliminate $x_1$:

$$(x_1 + x_2) - (x_1 - x_2) = 3 - 1 \quad\Longrightarrow\quad 2x_2 = 2$$

Now look at what is actually on the page:

$$\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
    & & 2x_2 &=& 2
\end{array}$$

The second equation, $x_1 - x_2 = 1$, is no longer there. <mark style="background: #ABF7F7A6;">Elimination replaces an equation, and every step from that point on solves the replacement rather than the original.</mark>

Dividing by 2 gives $x_2 = 1$, substituting back gives $x_1 = 2$ — and the equation that was dropped is never consulted again.

---

### Why the word "rewriting" is the right one

Solving is not a single transformation applied to one fixed system. It is a <b>sequence of systems</b>, each replacing the last, ending at one whose answer can be read off directly:

$$\{e_1,\ e_2\} \;\longrightarrow\; \{e_1,\ e_3\} \;\longrightarrow\; \cdots \;\longrightarrow\; \text{answer readable}$$

Every arrow discards a system and keeps going. That is what "rewriting, repeatedly" means, and it is why the vocabulary of <b>equivalent systems</b> exists at all — there would be nothing to name if solving never produced a second system.

The same procedure appears later performed on rows of [[A matrix records a linear system's numbers, with column position replacing the variable names|a matrix]] rather than on written-out equations. The rows are the equations, and the moves are these moves.

Which rewrite to perform first, and when to stop, is [[Elimination clears one variable per column going down, then clears back up until each row names one variable|the algorithm]].

---

### Which raises a question the method has to answer

The answer $(2, 1)$ came out of a system that is <b>not</b> the one that was asked. <mark style="background: #FF9E9EA6;">Reading an answer off equations you were never given is only safe if something guarantees the two systems have the same answers.</mark>

That guarantee is the subject of [[Two systems are equivalent when they have the same solution set|equivalence]], and the property that supplies it is [[A rewrite is safe exactly when the move that produced it can be undone|reversibility]].

---

### Read more

- [[Two systems are equivalent when they have the same solution set]]
- [[A rewrite is safe exactly when the move that produced it can be undone]]
- [[Elimination clears one variable per column going down, then clears back up until each row names one variable]]
- [[A matrix records a linear system's numbers, with column position replacing the variable names]]
- [[Math for ML MOC]]
