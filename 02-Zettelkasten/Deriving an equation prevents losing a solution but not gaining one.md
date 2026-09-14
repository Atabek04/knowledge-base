---
created: 2026-09-05
tags: [math, linear-algebra, solution-set, foundations]
aliases: [losing and gaining solutions, extraneous solutions]
---

When a step in solving produces a new equation, the natural reassurance is: <i>it was derived from the ones I had, so it must be trustworthy.</i>

That reassurance is half right, and the missing half is where wrong answers come from.

---

### Two ways a rewrite fails

<mark style="background: #FFF3A3A6;">A rewrite can go wrong in two opposite directions: losing a solution the original had, or gaining one it rejected.</mark>

- <b>Losing</b>: the new equation misses an answer the old one had
- <b>Gaining</b>: the new equation accepts an answer the old one rejected

These are independent. A step can be safe against one and fail the other, which is exactly what makes "it was derived" misleading.

---

### Why derivation cannot lose a solution

If a point satisfies every original equation, it satisfies anything assembled from them. Take:

$$x_1 + x_2 = 3 \qquad\text{and}\qquad x_1 - x_2 = 1$$

Subtracting one from the other means putting the two left sides on one side and the two right sides on the other:

$$\underbrace{(x_1 + x_2) - (x_1 - x_2)}_{\text{the two left sides}} \;=\; \underbrace{3 - 1}_{\text{the two right sides}} \quad\Longrightarrow\quad 2x_2 = 2$$

The point $(2, 1)$ satisfies it, since $2(1) = 2$, and could not have failed to. The step is licensed by the rule that [[Two true equations can be added or subtracted side by side and stay true|equals combined with equals give equals]], which says a combination of true equations is itself true.

#### The set-inclusion guarantee

The argument runs for every solution, not just $(2, 1)$:

$$\text{solutions of the original} \;\subseteq\; \text{solutions of the new system}$$

<mark style="background: #FFF3A3A6;">The new solution set is at least as big as the old one</mark>, never smaller, so nothing that was an answer stops being one.

#### Steps that do lose a solution

Losing needs a step that is <i>not</i> a plain derivation. Cancelling a variable is the classic one:

$$x^2 = 2x \quad\xrightarrow{\ \text{divide both sides by } x\ }\quad x = 2$$

| Equation | Solution set |
|---|---|
| $x^2 = 2x$ | $\{0,\ 2\}$ |
| $x = 2$ | $\{2\}$ |

One of the two solutions has vanished. <mark style="background: #FF5582A6;">Dividing by a variable quietly assumes it is not zero, and that assumption throws away the very solution it excluded.</mark>

Note how silent the failure is: no error appears, the arithmetic is clean, and the answer handed in is simply missing a case.

<mark style="background: #ADCCFFA6;">Dividing both sides by a variable is never a legal move on a system, because you cannot divide by something that might be zero.</mark>

---

### Why derivation can still gain a solution

Here is an honestly derived step that invents a solution out of nothing:

$$x = 2 \quad\xrightarrow{\ \text{square both sides}\ }\quad x^2 = 4$$

Squaring is legal algebra and $x^2 = 4$ genuinely follows. But look at what each accepts:

| Equation | Solution set |
|---|---|
| $x = 2$ | $\{2\}$ |
| $x^2 = 4$ | $\{2,\ -2\}$ |

A solution appeared that was never there. Anyone reporting "$x = -2$" would be wrong about the original problem, having made no algebraic mistake at all. Such an invented answer is called an <b>extraneous solution</b>.

#### Gaining inside a linear system

No squaring is required. Multiply the second equation by $0$:

$$\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
x_1 &-& x_2 &=& 1
\end{array}
\qquad\longrightarrow\qquad
\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
   0 & &     &=& 0
\end{array}$$

`0 = 0` is perfectly true and perfectly derived. But the new system is satisfied by <i>every</i> point on the line $x_1 + x_2 = 3$, so one solution has become infinitely many.

---

### The two tests compared

Squaring <b>passes</b> the losing test, since $x = 2$ survives into $x^2 = 4$ intact. The two steps differ only in the second column:

| Step | Loses a solution? | Gains a solution? |
|---|---|---|
| Subtracting two equations of a linear system | no | no |
| $x = 2 \rightarrow x^2 = 4$ | no | <b>yes</b> |

<mark style="background: #FF5582A6;">Both steps pass the losing test; only one passes the gaining test.</mark> That is the precise sense in which "it was derived from the original" is half a guarantee: it fills the first column and leaves the second blank.

Gaining solutions is one careless multiplication away, so a stronger test than derivation is needed. That stronger test is [[A rewrite is safe exactly when the move that produced it can be undone|reversibility]].

---

### Read more

- [[Two true equations can be added or subtracted side by side and stay true]]
- [[A rewrite is safe exactly when the move that produced it can be undone]]
- [[Two systems are equivalent when they have the same solution set]]
- [[Elimination replaces an equation, so solving a system means rewriting it]]
- [[Math for ML MOC]]
