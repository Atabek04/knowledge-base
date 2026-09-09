---
created: 2026-09-05
tags: [math, linear-algebra, solution-set, foundations]
aliases: [reversibility, reversible move, the reversibility test]
---

Solving a system means [[Elimination replaces an equation, so solving a system means rewriting it|replacing it with a different system]], then answering that one instead. The obvious defence — "the new equations were derived from the old" — [[Deriving an equation prevents losing a solution but not gaining one|only prevents losing a solution, not gaining one]].

So a stronger test is needed. It is a single question, and it is not the one most people reach for.

---

### The test

<mark style="background: #FFF3A3A6;">Trust a rewritten system when the move that produced it can be undone. Distrust it when it cannot.</mark>

Not "does it look similar", not "was it derived" — <b>is it reversible?</b>

Applied to the failures and the success side by side:

| Step | Can you undo it? | Result |
|---|---|---|
| $x^2 = 2x \rightarrow x = 2$ (divide by $x$) | No — multiplying back needs the $x=0$ case you discarded | <b>lost</b> a solution |
| $x = 2 \rightarrow x^2 = 4$ (square) | No — undoing gives $x = \pm 2$, not $x = 2$ | <b>gained</b> a solution |
| Multiply an equation by $0$ | No — nothing recovers the original from `0 = 0` | <b>gained</b> solutions |
| Replace $e_2$ with $e_1 - e_2$ | <b>Yes</b> | solution set unchanged |

Every step that went wrong is a step you cannot walk backwards.

---

### Working the last row explicitly

<b>Name every equation, including the new one.</b> The third name matters: the equation the move produces is not a version of $e_2$, it is a different equation.

$$\begin{array}{ll}
e_1: & x_1 + x_2 = 3 \\
e_2: & x_1 - x_2 = 1 \\
e_3: & 2x_2 = 2 \qquad \text{(the new one, } e_3 = e_1 - e_2\text{)}
\end{array}$$

<b>The forward move</b> computes $e_3$ and puts it where $e_2$ was:

$$e_3 \;=\; e_1 - e_2 \;=\; (x_1 + x_2) - (x_1 - x_2) \;=\; 3 - 1 \quad\Longrightarrow\quad 2x_2 = 2$$

The page now holds $\{e_1,\ e_3\}$, and $e_2$ <b>is gone</b>. Can it be recovered from what remains?

#### Finding the undo

You do not have to guess it. The forward move left behind a relation between the three equations:

$$e_1 - e_2 = e_3$$

The lost equation sits inside that relation, so <b>solve it for $e_2$</b> exactly as you would for a number:

$$\begin{array}{rll}
e_1 - e_2 &= e_3 & \text{the relation the move created} \\[4pt]
e_1 &= e_3 + e_2 & \text{add } e_2 \text{ to both sides} \\[4pt]
e_1 - e_3 &= e_2 & \text{subtract } e_3 \text{ from both sides}
\end{array}$$

So the undo is $e_1 - e_3$. It was derivable, not invented.

#### Carrying it out

On the equations still on the page:

$$\begin{array}{rl}
e_1 - e_3 &= (x_1 + x_2) - 2x_2 \\[4pt]
&= 3 - 2 \\[4pt]
&\Longrightarrow\; x_1 - x_2 = 1
\end{array}$$

That is $e_2$, back exactly as it was.

<mark style="background: #ABF7F7A6;">Nothing was destroyed by the forward move — the discarded equation is still reachable from the equations that replaced it.</mark>

---

### Why undoing it settles the question

If the move can be undone, the implication runs <b>both directions</b>:

- <b>old ⇒ new</b> — every solution of the original survives, so <b>nothing is lost</b>
- <b>new ⇒ old</b> — every solution of the new system also solves the original, so <b>nothing is gained</b>

The second bullet is exactly what derivation alone could not supply, and running the step backwards is what supplies it: the reverse move is itself a derivation, in the opposite direction.

<mark style="background: #ABF7F7A6;">Two systems that each imply the other must accept exactly the same points.</mark>

#### The consequence for practice

An answer read off the final system never needs checking against the original. <mark style="background: #ADCCFFA6;">Verify that each move was reversible, and the answer is guaranteed before any arithmetic is done.</mark>

In the running example, $(2, 1)$ can be trusted against the original pair because every step from $\{e_1, e_2\}$ down to $x_2 = 1$ was reversible, so the chain runs backwards as well as forwards.

---

### Read more

- [[Deriving an equation prevents losing a solution but not gaining one]]
- [[The three row operations are legal precisely because each one can be undone]]
- [[Two systems are equivalent when they have the same solution set]]
- [[Elimination replaces an equation, so solving a system means rewriting it]]
- [[Row equivalent matrices are linked by the route between them, since a matrix has no solution set to compare]]
- [[Math for ML MOC]]
