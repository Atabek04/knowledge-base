TARGET DECK: Math::Linear Algebra
Tags: math linear-algebra
**Chapter:** Systems of Linear Equations (Lay §1.1)
**Related:** [[Math for ML MOC]]

---

START
Coding Questions
By linearity, what are the two types of equations?
Back:
- **Linear** — every variable appears alone, to the first power, multiplied only by a constant
- **Nonlinear** — everything else; the umbrella term for every equation that fails that test

There is no third category, and no second general word for nonlinear.
Tags: math linear-algebra linearity
<!--ID: 1788614163765-->
END

START
Coding Questions
You cannot picture 4 dimensions. Why is that not a problem for linear algebra?
Back: Because **row reduction never consults a picture.** It is mechanical, so it works unchanged at n = 500 where visual intuition stopped at 3.

**The working practice:** draw in 2-D to understand *why* a method works, then trust the algebra to carry it into dimensions you cannot see.

The 2-D picture is a teaching aid, never the justification.
Tags: math linear-algebra dimensions
<!--ID: 1788614163776-->
END

START
Coding Questions
What general form must an equation fit to be called linear?
Back: `a₁x₁ + a₂x₂ + ... + aₙxₙ = b`

where `a₁ … aₙ` and `b` are **constants**.

If ordinary algebra cannot force the equation into that shape, it is nonlinear.

**Name as mnemonic:** degree 1 in two variables draws a straight **line** — any other degree bends it.
Tags: math linear-algebra linearity
<!--ID: 1788608936981-->
END

START
Coding Questions
What is the single test that decides whether any equation is linear? List its criteria.
Back: An equation is **linear** when all four hold:

1. Every variable appears **alone** — never multiplied by another variable
2. Every variable is raised to the **first power** only
3. Every variable is multiplied only by a **constant**
4. The terms are only **added or subtracted**

Break any one of them and the equation is nonlinear.
Tags: math linear-algebra linearity
<!--ID: 1788608937004-->
END

START
Coding Questions
Name the six families of nonlinear equations.
Back:
- **Polynomial** (quadratic, cubic, …)
- **Bilinear / multiplicative**
- **Radical**
- **Exponential**
- **Trigonometric**
- **Rational**
Tags: math linear-algebra nonlinear-families
<!--ID: 1788608937026-->
END

START
Coding Questions
Nonlinear family — what is a **polynomial** equation, and what breaks linearity in it?
Back: An equation where a variable is raised to a power other than 1.

Example: `x² − 3x = 1`

**Breaks linearity:** variable raised to a power ≠ 1.
Tags: math linear-algebra nonlinear-families
<!--ID: 1788608937047-->
END

START
Coding Questions
Nonlinear family — what is a **bilinear (multiplicative)** equation, and what breaks linearity in it?
Back: An equation where two variables are multiplied by each other.

Example: `4x₁ − 6x₂ = x₁x₂`

**Breaks linearity:** variable × variable. Constant × variable (`3x₁`) is fine — only variables multiplying *each other* is forbidden.
Tags: math linear-algebra nonlinear-families
<!--ID: 1788608937069-->
END

START
Coding Questions
Nonlinear family — what is a **radical** equation, and what breaks linearity in it?
Back: An equation with a variable under a root.

Example: `x₂ = 2√x₁ − 7`

**Breaks linearity:** the variable sits under a root, i.e. raised to power ½.
Tags: math linear-algebra nonlinear-families
<!--ID: 1788608937092-->
END

START
Coding Questions
Nonlinear family — what is an **exponential** equation, and what breaks linearity in it?
Back: An equation where the variable sits in the exponent rather than the base.

Example: `2^x = 7`

**Breaks linearity:** variable in the exponent.
Tags: math linear-algebra nonlinear-families
<!--ID: 1788608937114-->
END

START
Coding Questions
Nonlinear family — what is a **trigonometric** equation, and what breaks linearity in it?
Back: An equation with a variable inside a trigonometric function.

Example: `sin x₁ + x₂ = 0`

**Breaks linearity:** variable inside a function.
Tags: math linear-algebra nonlinear-families
<!--ID: 1788608937136-->
END

START
Coding Questions
Nonlinear family — what is a **rational** equation, and what breaks linearity in it?
Back: An equation with a variable in a denominator.

Example: `1/x₁ + x₂ = 5`

**Breaks linearity:** variable in the denominator, i.e. raised to power −1.
Tags: math linear-algebra nonlinear-families
<!--ID: 1788608937157-->
END

START
Coding Questions
Is `x₂ = 2(√6 − x₁) + x₃` linear, and why is it a trap?
Back: **Linear.**

The root sits on **6** — a number, not a variable — so `2√6` is just a constant coefficient.

Rearranged: `2x₁ + x₂ − x₃ = 2√6`

**The rule:** judge a root, power or exponent by *what it sits on*. On a constant it is harmless arithmetic; on a variable it destroys linearity.
Tags: math linear-algebra linearity
<!--ID: 1788608937181-->
END

START
Coding Questions
Degree vs exponential — which position does the variable occupy in each?
Back:
- **Degree (power)** — variable in the **base**, number in the exponent: `x²`, `x³`
- **Exponential** — number in the **base**, variable in the **exponent**: `2^x`, `e^x`

**Key:** the distinguishing axis is which side of the exponent the variable is on. Both are nonlinear, but they grow very differently — the same O(n²) vs O(2ⁿ) split as in complexity analysis.
Tags: math linear-algebra nonlinear-families
<!--ID: 1788608937202-->
END

START
Coding Questions
List the five number systems with their symbols, from smallest to largest.
Back:
1. **ℕ** — naturals
2. **ℤ** — integers
3. **ℚ** — rationals
4. **ℝ** — reals
5. **ℂ** — complex

Each set **contains** all the ones above it.
Tags: math linear-algebra number-systems
<!--ID: 1788608937224-->
END

START
Coding Questions
Number system **ℕ** — name, contents, and what it adds?
Back:
- **Name:** naturals
- **Contents:** 1, 2, 3, … (sometimes from 0)
- **Fixes:** nothing — it is the starting point, the numbers you count with

**Examples:** `1`, `7`, `500`
**Not in ℕ:** `−3`, `0.5`, `√2`
Tags: math linear-algebra number-systems
<!--ID: 1788608937246-->
END

START
Coding Questions
Number system **ℤ** — name, contents, and what it adds?
Back:
- **Name:** integers
- **Contents:** … −2, −1, 0, 1, 2 …
- **Fixes:** `3 − 5` has no answer in ℕ → adds **negatives**

**Examples:** `−12`, `0`, `48`
**Not in ℤ:** `3/4`, `π`

**Why the letter Z:** from German *Zahlen*, "numbers".
Tags: math linear-algebra number-systems
<!--ID: 1788608937268-->
END

START
Coding Questions
Number system **ℚ** — name, contents, and what it adds?
Back:
- **Name:** rationals
- **Contents:** any fraction `p/q`, with q ≠ 0
- **Fixes:** `3 ÷ 4` has no answer in ℤ → adds **fractions**

**Examples:** `3/4`, `−7/2`, `0.25`, and every integer (`5 = 5/1`)
**Not in ℚ:** `√2`, `π` — no fraction can hit them

**Why the letter Q:** from *quotient*.
Tags: math linear-algebra number-systems
<!--ID: 1788608937291-->
END

START
Coding Questions
Number system **ℝ** — name, contents, and what it adds?
Back:
- **Name:** reals
- **Contents:** every point on the number line, with no gaps
- **Fixes:** `x² = 2` has no answer in ℚ → adds **irrationals**

**Examples:** `√2`, `π`, `e`, plus every rational
**Not in ℝ:** `√(−1)`

"Real" is a historical label, coined to contrast with the "imaginary" ones.
Tags: math linear-algebra number-systems
<!--ID: 1788608937314-->
END

START
Coding Questions
Number system **ℂ** — name, contents, and what it adds?
Back:
- **Name:** complex
- **Contents:** `a + bi`, where `i² = −1` — a real part plus an imaginary part
- **Fixes:** `x² = −1` has no answer in ℝ → adds **imaginary** numbers

**Examples:** `3 + 2i`, `−i`, and every real (`5 = 5 + 0i`)

**Why they exist:** defining `i = √(−1)` patches that one hole, and that single patch makes *every* polynomial solvable.
Tags: math linear-algebra number-systems
<!--ID: 1788608937335-->
END

START
Coding Questions
Is `0` a natural number (ℕ) and is it an integer (ℤ)?
Back:
- **Integer — yes, always.** `0 ∈ ℤ` is never disputed.
- **Natural — depends on the convention.**
    - **ISO 80000-2, set theory, computer science:** ℕ starts at 0
    - **US K–12 and many school texts:** ℕ starts at 1, and 0 is a *whole number*

**In practice:** check what your book uses. To be unambiguous, write **ℕ₀** for the set including 0.
Tags: math number-systems zero-convention
<!--ID: 1788608937363-->
END

START
Coding Questions
For each number system, what broken equation forced it into existence?
Back: Each set patches a hole in the set before it.

- **ℕ** naturals — the starting point: things you can count
- **ℤ** integers — `3 − 5` has no answer in ℕ → **negatives**
- **ℚ** rationals — `3 ÷ 4` has no answer in ℤ → **fractions**
- **ℝ** reals — `x² = 2` has no answer in ℚ → **irrationals**
- **ℂ** complex — `x² = −1` has no answer in ℝ → **imaginary**

**Pattern:** an operation escapes the set → invent the numbers that catch it.
Tags: math linear-algebra number-systems
<!--ID: 1788608937386-->
END

START
Coding Questions
Draw or describe the containment of the five number systems.
Back: Each set sits **inside** the next — ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ

<div style="text-align:center; padding:14px; border:2px solid #888; border-radius:12px;">ℂ complex
<div style="padding:12px; margin-top:6px; border:2px solid #888; border-radius:12px;">ℝ reals
<div style="padding:12px; margin-top:6px; border:2px solid #888; border-radius:12px;">ℚ rationals
<div style="padding:12px; margin-top:6px; border:2px solid #888; border-radius:12px;">ℤ integers
<div style="padding:12px; margin-top:6px; border:2px solid #888; border-radius:12px;">ℕ naturals</div></div></div></div></div>

Every natural number is also an integer, a rational, a real and a complex number — the containment never reverses.
Tags: math linear-algebra number-systems
<!--ID: 1788608937410-->
END

START
Coding Questions
How do you write "x is a real number" in set notation, and what is the symbol called?
Back: `x ∈ ℝ`

`∈` is the **membership** symbol — read as "is an element of" / "belongs to".
Tags: math linear-algebra number-systems
<!--ID: 1788608937432-->
END

START
Coding Questions
In the fraction `3/4`, what are the top number, the bottom number, and the line called?
Back:
- **Numerator** — the top (3). It *numbers* how many parts you take.
- **Denominator** — the bottom (4). It *denominates* — names how many equal parts the whole was cut into. **D for down.**
- **Fraction bar** (formally *vinculum*) — the line, which means division.
Tags: math fractions fraction-parts
<!--ID: 1788608937456-->
END

START
Coding Questions
Name the four types of fractions.
Back:
1. **Proper**
2. **Improper**
3. **Mixed number**
4. **Unit fraction**
Tags: math fractions fraction-types
<!--ID: 1788608937479-->
END

START
Coding Questions
Fractions — what is a **proper** fraction vs an **improper** fraction?
Back:
- **Proper** — numerator < denominator, so the value is less than 1. Example: `3/4`
- **Improper** — numerator ≥ denominator, so the value is 1 or more. Example: `7/4`

**Key:** the distinguishing axis is which of the two numbers is bigger.
Tags: math fractions fraction-types
<!--ID: 1788608937488-->
END

START
Coding Questions
What is the term for a whole number written **before** a fraction, e.g. `1¾`?
Back: A **mixed number** — a whole number mixed with a proper fraction.

Read aloud as "one and three quarters".

It is the same value as the improper fraction `7/4`.
Tags: math fractions fraction-types
<!--ID: 1788608937514-->
END

START
Coding Questions
Fractions — what is a **unit fraction**?
Back: A fraction whose **numerator is 1**. Example: `1/5`

The name says it: it is one single part of the whole.
Tags: math fractions fraction-types
<!--ID: 1788608937538-->
END

START
Coding Questions
Fractions — what is the **reciprocal** of a fraction?
Back: The fraction **flipped** — numerator and denominator swapped.

The reciprocal of `3/4` is `4/3`.

Any number times its reciprocal equals **1**.
Tags: math fractions fraction-parts
<!--ID: 1788608937563-->
END

START
Coding Questions
Why does linear algebra write `x₁, x₂, x₃` instead of `x, y, z`?
Back: Same meaning — it is only a renaming. Two reasons for the switch:

- **The alphabet runs out.** With 500 unknowns there is no letter scheme; `x₁ … x₅₀₀` is trivial.
- **Letters cannot be generalised.** `xᵢ` means "the i-th variable", and `x₁, …, xₙ` means the whole family for any n.

**Why it matters:** the general linear equation `a₁x₁ + ... + aₙxₙ = b` cannot be written in `x, y, z` at all. The notation is a prerequisite for talking about n dimensions.
Tags: math linear-algebra notation
<!--ID: 1788609610700-->
END

START
Coding Questions
In `aᵢⱼ`, what do the two subscripts refer to, and in what order?
Back: **Row `i` first, column `j` second** — the coefficient at row i, column j.

Same two-index addressing as `grid[i][j]` in code.

**Careful:** the order is fixed. Swapping it silently produces the transposed matrix.
Tags: math linear-algebra notation
<!--ID: 1788609610703-->
END

START
Coding Questions
In the geometry of a linear system, what role do **variables** play and what role do **equations** play?
Back: They are completely different roles:

- **Variables** set the **dimension of the space** you draw in
- **Equations** are the **shapes drawn inside it**

**Example:** 3 equations in 2 unknowns = three **lines in one plane** — not three planes, and not a 3-D picture.

**Key:** swapping these two is the most common beginner error.
Tags: math linear-algebra dimensions
<!--ID: 1788609610704-->
END

START
Coding Questions
What shape does a single linear equation draw in 2-D, in 3-D, and in n dimensions?
Back:
- **2 variables** → a **line** in the plane
- **3 variables** → a **plane** in space
- **n variables** → a **hyperplane**, of dimension (n−1)

**Why one dimension is always lost:** one equation is one constraint. In 3-D you pick `x₁` and `x₂` freely, and the equation then forces `x₃` — two free choices trace a surface.
Tags: math linear-algebra dimensions
<!--ID: 1788609610705-->
END

START
Coding Questions
What is a **hyperplane**?
Back: The flat, **(n−1)-dimensional** slice that one linear equation carves out of n-dimensional space.

- In 2-D a hyperplane is an ordinary **line**
- In 3-D it is an ordinary **plane**

**Name as mnemonic:** it is the "plane" idea lifted past the dimensions we can draw. The word exists only because *line* and *plane* run out at three dimensions.
Tags: math linear-algebra dimensions
<!--ID: 1788609610706-->
END

START
Coding Questions
How many solutions can a linear system have?
Back: Exactly three possibilities — **zero, one, or infinitely many.**

Never two, never seventeen. This is a theorem, not a simplification.

**Why it matters:** "how many solutions?" has only three answers to check.
Tags: math linear-algebra solution-counts
<!--ID: 1788609610715-->
END

START
Coding Questions
Two lines in a plane — what are the three ways they can sit, and how many solutions does each give?
Back:
- **Cross once** → exactly **one** solution
- **Parallel and distinct** → **no** solution
- **The same line** → **infinitely many** solutions

These are the three solution counts, seen geometrically.
Tags: math linear-algebra solution-counts
<!--ID: 1788609610716-->
END

START
Coding Questions
Give a system with **no solution** and explain why it has none.
Back:
<div>
\[\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
x_1 &+& x_2 &=& 5
\end{array}\]
</div>

The same quantity cannot equal two different numbers — the constraints **contradict** each other.

**Geometrically:** the lines are parallel and never meet.
Tags: math linear-algebra solution-counts
<!--ID: 1788609610717-->
END

START
Coding Questions
Give a system with **infinitely many solutions** and explain why.
Back:
<div>
\[\begin{array}{rrrrr}
 x_1 &+&  x_2 &=& 3 \\
2x_1 &+& 2x_2 &=& 6
\end{array}\]
</div>

The second equation is the first one **doubled** — it draws the same line and adds no information.

Two equations were written, but only **one constraint** exists, so every point on that line satisfies both.

**Lesson:** counting equations is not the same as counting constraints.
Tags: math linear-algebra solution-counts
<!--ID: 1788609610718-->
END

START
Coding Questions
What do **consistent** and **inconsistent** mean for a linear system?
Back:
- **Consistent** — has **at least one** solution (so: one *or* infinitely many)
- **Inconsistent** — has **no** solution

**Key:** the axis is "any solution at all?", not "exactly one?". An infinitely-many system is fully consistent.

**Name as mnemonic:** an inconsistent system is one whose equations contradict each other.
Tags: math linear-algebra solution-counts
<!--ID: 1788609610719-->
END

START
Coding Questions
What is the difference between a **solution** and a **solution set**?
Back:
- **Solution** — one single point, written as an ordered list `(s₁, s₂, …, sₙ)`
    - Order carries meaning: `(5, 6.5, 3)` means `x₁ = 5`, `x₂ = 6.5`, `x₃ = 3`
- **Solution set** — the collection of **every** such point

**Key:** "solve the system" means describe the *set*, which may be empty, a single point, or an infinite family — not produce one number.
Tags: math linear-algebra solution-counts
<!--ID: 1788609610720-->
END

START
Coding Questions
When are two linear systems called **equivalent**?
Back: When they have the **same solution set**.

They need **not** look alike, share coefficients, or even have the same number of equations. Only the answer has to match.

"Two systems" means two genuinely **different collections of equations** — not the same one rewritten cosmetically.

**Example** — all three are equivalent, solution `(2, 1)`:

<div>
\[
\underset{\textbf{A}}{\begin{array}{rrrrr} x_1 &+& x_2 &=& 3 \\ x_1 &-& x_2 &=& 1 \end{array}}
\qquad
\underset{\textbf{B}}{\begin{array}{rrrrr} x_1 &+& x_2 &=& 3 \\ & & -2x_2 &=& -2 \end{array}}
\qquad
\underset{\textbf{C}}{\begin{array}{rrrrr} x_1 &+& x_2 &=& 3 \\ & & x_2 &=& 1 \end{array}}
\]
</div>

Different coefficients, same solution set. **C** is the one you can read the answer off — which is why you moved.
Tags: math linear-algebra equivalence
<!--ID: 1788609610721-->
END

START
Coding Questions
What are the three operations that turn a system into an **equivalent** one, and how is each undone?
Back:
1. **Swap** two equations → swap them back
2. **Scale** an equation by a nonzero `c` → scale by `1/c`
3. **Add** `c` times one equation to another → subtract `c` times it

**Why they are safe:** each is **reversible**, so the old system implies the new one *and* the new implies the old — nothing lost, nothing gained.
Tags: math linear-algebra row-operations
<!--ID: 1788610928863-->
END

START
Coding Questions
School elimination — "cancel a variable" — is really doing what?
Back: **Replacing one equation with another**, i.e. rewriting the system.

<div>
\[\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
x_1 &-& x_2 &=& 1
\end{array}
\;\longrightarrow\;
\begin{array}{rrrrr}
x_1 &+& x_2 &=& 3 \\
    & & 2x_2 &=& 2
\end{array}\]
</div>

`x₁ − x₂ = 1` is **gone** — everything after this solves its replacement.

**Elimination is rewriting.** It is safe only because the move preserves the solution set.
Tags: math linear-algebra elimination-rewriting
<!--ID: 1788610928840-->
END

START
Coding Questions
A rewrite can go wrong in two opposite ways. What are they, and which one does "it was derived from the original" rule out?
Back:
- **Losing** a solution — the new system misses an answer the old one had
- **Gaining** a solution — the new system accepts an answer the old one rejected

**"Derived from" rules out losing only.** Any point satisfying the old equations satisfies a combination of them.

Nothing in "derived from" prevents *gaining* — which is why derivation alone is not a guarantee.
Tags: math linear-algebra losing-gaining
<!--ID: 1788610928845-->
END

START
Coding Questions
Give a step that **loses** a solution, and say what went wrong.
Back: Cancelling a variable:

<div>\[ x^2 = 2x \quad\longrightarrow\quad x = 2 \qquad(\text{divide by } x) \]</div>

- `x² = 2x` is solved by **{0, 2}**
- `x = 2` is solved by **{2}**

**`x = 0` vanished.** Dividing by `x` quietly assumed `x ≠ 0` — and threw away the solution that assumption excluded.

**Rule:** never divide by something that might be zero.
Tags: math linear-algebra losing-gaining
<!--ID: 1788611823663-->
END

START
Coding Questions
Give a step that **gains** a solution, and say what went wrong.
Back: Squaring both sides:

<div>\[ x = 2 \quad\longrightarrow\quad x^2 = 4 \]</div>

- `x = 2` is solved by **{2}**
- `x² = 4` is solved by **{2, −2}**

**`x = −2` appeared from nowhere**, with no algebraic mistake made.

**Why:** the step is not reversible — from `x² = 4` you recover `x = ±2`, never `x = 2`.

The invented answer is called an **extraneous solution**.
Tags: math linear-algebra losing-gaining
<!--ID: 1788611823668-->
END

START
Coding Questions
An answer read off the final system — when does it need checking against the original?
Back: **Never**, provided every move was reversible.

The guarantee is established by the **moves**, before any arithmetic happens — not by inspecting the answer afterwards.

Likewise, equivalence is established from the route between two systems, never from how the final one looks.
Tags: math linear-algebra reversibility
<!--ID: 1788615795361-->
END

START
Coding Questions
Why is dividing an equation by a **variable** absent from the three legal moves?
Back: A variable may be **zero**, so the move has no guaranteed undo — and an irreversible move can change the solution set.

Dividing by a **nonzero constant** is fine: that is just scaling by `1/c`, which is move 2.

**Mirror image:** scaling by zero gains solutions; dividing by a variable loses them.
Tags: math linear-algebra row-operations
<!--ID: 1788615795373-->
END

START
Coding Questions
What are the three row operations called when performed on a matrix?
Back: The **elementary row operations**.

Nothing changes but the notation — a **row** is an equation with the variable names stripped out, and the three moves are the same three moves, legal for the same reason.
Tags: math linear-algebra row-operations
<!--ID: 1788615795375-->
END

START
Coding Questions
What is the test for whether a rewritten system can be trusted?
Back: **Can the move be undone?**

- **Reversible** → trust it. The implication runs both ways, so the solution set is unchanged.
- **Not reversible** → distrust it. It can have gained solutions.

**Not** the test: "does it look similar", or "was it derived from the original" — derivation alone only prevents *losing*.
Tags: math linear-algebra reversibility
<!--ID: 1788611658081-->
END

START
Coding Questions
Why must the constant be **nonzero** when scaling an equation?
Back: Multiplying by 0 turns the equation into `0 = 0`, which is true for **every** point.

The constraint is destroyed and the solution set **grows** — that is a different problem, not a simplification.

Reversibility is the reason: there is no `1/0` to scale back by.
Tags: math linear-algebra row-operations
<!--ID: 1788609610723-->
END

START
Coding Questions
Geometrically, what does it mean to **solve** a linear system?
Back: **Find the intersection of all the shapes its equations draw.**

A solution must satisfy every equation at once, so the point must lie on every shape simultaneously.

The three solution counts fall straight out of this: the shapes meet at one point, in a whole line or plane of points, or nowhere.
Tags: math linear-algebra intersection
<!--ID: 1788609610725-->
END

START
Coding Questions
A system has **fewer equations than unknowns**. What does that predict, and why?
Back: Usually **infinitely many** solutions — the *underdetermined* case.

Equations are constraints, variables are freedoms, so too few constraints leave some freedom alive.

**Example:** 2 equations in 3 unknowns = two planes in 3-D, meeting in a whole **line** of solutions.

**Where it shows up:** machine learning, where a model has far more parameters than the data has constraints.
Tags: math linear-algebra intersection
<!--ID: 1788609610726-->
END

START
Coding Questions
A system has **more equations than unknowns**. What does that predict, and what is done about it?
Back: Usually **no** solution — the *over-constrained* case.

**Example:** 3 equations in 2 unknowns = three lines in a plane. Two will cross somewhere, but the third has no reason to pass through that point.

**What is done:** rather than give up, ask for the point that comes *closest* to satisfying all of them — which is exactly what least-squares regression computes.
Tags: math linear-algebra intersection
<!--ID: 1788609610727-->
END

START
Coding Questions
A system has **exactly as many equations as unknowns**. Is a unique solution guaranteed?
Back: **No.** Matching counts make a unique solution *likely*, never certain.

Two equations in two unknowns still gives:
- **no** solution if the lines are parallel
- **infinitely many** if they coincide

Only the algebra decides.
Tags: math linear-algebra intersection
<!--ID: 1788609610728-->
END

START
Coding Questions
Row operation **Swap** — what exactly moves, and what is the trap?
Back: Two **whole equations** exchange places in the list. The equations themselves are untouched — only their order on the page changes.

<div>
\[\begin{array}{rrrrr} x_1 &+& x_2 &=& 3 \\ 2x_1 &+& 5x_2 &=& 9 \end{array}
\;\longrightarrow\;
\begin{array}{rrrrr} 2x_1 &+& 5x_2 &=& 9 \\ x_1 &+& x_2 &=& 3 \end{array}\]
</div>

**Trap:** moving a term across the equals sign is **not** swap, and not a row operation at all — it rewrites one equation internally, which none of the three moves do.
Tags: math linear-algebra row-operations
<!--ID: 1788672525052-->
END

START
Coding Questions
Row operation **Add** — when `c` times R₁ is added to R₂, which row changes?
Back: **Only R₂.** The source row R₁ is used, not consumed, and stays exactly as it was.

<div>
\[\begin{array}{rrrrr} x_1 &+& x_2 &=& 3 \\ 2x_1 &+& 5x_2 &=& 9 \end{array}
\;\xrightarrow{\;R_2 - 2R_1\;}\;
\begin{array}{rrrrr} x_1 &+& x_2 &=& 3 \\ & & 3x_2 &=& 3 \end{array}\]
</div>

Undo: add `+2R₁` back to R₂.

**Why it matters:** this is the only move that eliminates a variable — the engine of every method built on the three.
Tags: math linear-algebra row-operations
<!--ID: 1788672525059-->
END

START
Coding Questions
Why is **division** not a fourth row operation?
Back: Dividing by a nonzero constant `c` **is** scaling — by `1/c`. It is move 2 under another name, so the list names only one of the pair.

Dividing by a **variable** is a different matter: it is excluded, because a variable may be zero.
Tags: math linear-algebra row-operations
<!--ID: 1788672525063-->
END

START
Coding Questions
Three variables, one equation `x₁ + x₂ + x₃ = 6`. How many of the three are you free to choose, and why?
Back: **Two.** Pick `x₁ = 1` freely, pick `x₂ = 2` freely — then `x₃` is **forced to 3**, because `1 + 2 + x₃ = 6` has exactly one answer.

`x₃` has not disappeared; it is simply no longer yours to pick.

| x₁ | x₂ | x₃ forced | point |
|---|---|---|---|
| 1 | 2 | 3 | (1, 2, 3) |
| 0 | 0 | 6 | (0, 0, 6) |
| 5 | −1 | 2 | (5, −1, 2) |

Two free choices = two directions to move = a **2-D plane** inside 3-D space.
Tags: math linear-algebra dimensions
<!--ID: 1788673581565-->
END

START
Coding Questions
What is a **degree of freedom**, and what does one equation do to the count?
Back: A **degree of freedom** is one variable you are still free to choose.

One equation is one **constraint**, and each constraint **removes exactly one** degree of freedom.

n variables minus 1 constraint = n−1 free choices, which trace out an (n−1)-dimensional shape. That is why the shape an equation draws is always exactly one dimension below the space it sits in.
Tags: math linear-algebra dimensions
<!--ID: 1788673581584-->
END

START
Coding Questions
Why is an equation called a **constraint** (ru: ограничение)?
Back: Because it does **not** describe every point in the space — it **accepts** the points that satisfy it and **rejects** the rest.

A constraint is a restriction on what is allowed, and that is exactly what an equation does to a space of points.

**Consequence:** one equation = one constraint = one **degree of freedom** removed.
Tags: math linear-algebra dimensions
<!--ID: 1788674001696-->
END

START
Coding Questions
What is a **matrix**, and what replaces the variable names in it?
Back: A **rectangular array of numbers** — nothing more is required by the definition.

**Position** replaces the names: a number's **column** says which variable it multiplies, so `x₁, x₂, x₃` need not be written.

- Each **row** = one equation
- Each **column** = one variable
Tags: math linear-algebra matrix-notation
<!--ID: 1788676022287-->
END

START
Coding Questions
**Coefficient matrix** vs **augmented matrix** — what is the difference?
Back: They differ by **exactly one column**.

- **Coefficient matrix** — the coefficients of the variables, left-hand sides only
- **Augmented matrix** — the same, *augmented* by one column holding the constants from the right-hand sides

<div>
\[ \begin{bmatrix} 1 & -2 & 1 \\ 0 & 2 & -8 \\ 5 & 0 & -5 \end{bmatrix} \qquad \left[\begin{array}{ccc|c} 1 & -2 & 1 & 0 \\ 0 & 2 & -8 & 8 \\ 5 & 0 & -5 & 10 \end{array}\right] \]
</div>

**Solve with the augmented one** — the coefficient matrix has thrown away the right-hand sides and no longer describes the system.

The vertical bar is a reading aid marking the old equals signs, not part of the matrix.
Tags: math linear-algebra matrix-notation
<!--ID: 1788676022297-->
END

START
Coding Questions
An equation has no `x₁` term. What goes in that column of the matrix, and why does it matter?
Back: A **0** — and it must be written.

`2x₂ − 8x₃ = 8` is really `0·x₁ + 2x₂ − 8x₃ = 8`, so its row starts with 0.

**Why it matters:** a variable absent from an equation is not a missing entry, it is a coefficient of zero. Leaving the position empty shifts every later number into the **wrong column**.
Tags: math linear-algebra matrix-notation
<!--ID: 1788676022312-->
END

START
Coding Questions
How is the **size** of a matrix written, and which number comes first?
Back: **m × n** — **m rows** by **n columns**. The number of **rows always comes first**.

A 3-row, 4-column matrix is a **3 × 4** matrix, read "three by four".

**Trap:** 3 × 4 and 4 × 3 are different shapes, not the same matrix described two ways.

Same row-then-column order as the double subscript `aᵢⱼ` — row i, column j.
Tags: math linear-algebra matrix-notation
<!--ID: 1788676022320-->
END

START
Coding Questions
What is a **matrix**, and what do its rows and columns mean for a linear system?
Back: A **matrix** is a rectangular array of numbers — nothing more is built into the definition.

Loaded from a system:
- **Row** = one equation
- **Column** = one variable

**Why it works:** position replaces the variable names. A number's column says which variable it multiplies, so `x₁, x₂, x₃` never need to be written.
Tags: math linear-algebra matrix-notation
<!--ID: 1788676022323-->
END

START
Coding Questions
**Coefficient matrix** vs **augmented matrix** — what is the difference?
Back: **Exactly one column.** The augmented matrix is the coefficient matrix plus a column holding the constants from the right-hand sides.

<div>
\[\underset{\textbf{coefficient } (3\times3)}{\begin{bmatrix} 1 & -2 & 1 \\ 0 & 2 & -8 \\ 5 & 0 & -5 \end{bmatrix}}
\qquad
\underset{\textbf{augmented } (3\times4)}{\left[\begin{array}{ccc|c} 1 & -2 & 1 & 0 \\ 0 & 2 & -8 & 8 \\ 5 & 0 & -5 & 10 \end{array}\right]}\]
</div>

**Name as mnemonic:** *augmented* = enlarged, by one column.

The vertical bar marks where the equals signs were — a reading aid, not part of the matrix.
Tags: math linear-algebra matrix-notation
<!--ID: 1788676022368-->
END

START
Coding Questions
Which of the two matrices do you actually solve with, and why not the other?
Back: The **augmented** matrix.

The coefficient matrix has thrown away the right-hand sides, so it no longer describes the system — the same coefficients with different constants are a different problem.
Tags: math linear-algebra matrix-notation
<!--ID: 1788676022332-->
END

START
Coding Questions
The equation `2x₂ − 8x₃ = 8` becomes the row `0  2  −8 | 8`. Why the leading zero?
Back: Because `x₁` is **absent**, and absent means **coefficient zero** — written in full the equation is `0·x₁ + 2x₂ − 8x₃ = 8`.

**Trap:** a missing variable is not a missing entry. Leaving the position empty shifts every later number into the wrong column, and the column is the only thing saying which variable a number belongs to.
Tags: math linear-algebra matrix-notation
<!--ID: 1788676022335-->
END

START
Coding Questions
How is the **size** of a matrix written, and which number comes first?
Back: `m × n` — **m rows, n columns. Rows always first.**

Read aloud "m by n". The augmented matrix of a 3-equation, 3-unknown system is **3 × 4**: 3 rows, 4 columns.

**Trap:** the order is not a convention you can flip. A 3 × 4 and a 4 × 3 matrix are different shapes.

Same row-then-column order as the subscript `aᵢⱼ` and as `grid[i][j]` in code.
Tags: math linear-algebra matrix-notation
<!--ID: 1788676022394-->
END

START
Coding Questions
Elimination has two passes. What does each one do, and in which direction?
Back:
- **Forward pass — going down.** Column by column from the left: keep the leading variable in one equation, use it to clear that variable from every equation **below**. Ends in **triangular** form.
- **Backward pass — going up.** From the bottom row upward, use each solved variable to clear its column **above**. Ends with one variable per row.

**Stop condition:** every row names exactly one variable — the answer is then **read off**, not computed.
Tags: math linear-algebra elimination-algorithm
<!--ID: 1788676831850-->
END

START
Coding Questions
What is **triangular** form, and why is the word only a placeholder?
Back: Zeros form a **staircase below the diagonal** — each equation involves one variable fewer than the one above it.

<div>
\[\left[\begin{array}{ccc|c} 1 & -2 & 1 & 0 \\ 0 & 1 & -4 & 4 \\ 0 & 0 & 1 & -1 \end{array}\right]\]
</div>

**Placeholder:** *triangular* describes the picture, not the rule. It is replaced by the precise term **echelon form** once the general shape is defined.
Tags: math linear-algebra elimination-algorithm
<!--ID: 1788676831860-->
END

START
Coding Questions
Why scale a row so its leading coefficient is **1**, when correctness does not require it?
Back: Because a leading coefficient of **1** makes every later multiplier a **whole number** instead of a fraction.

It is an arithmetic convenience, not a legality requirement — scaling by a nonzero constant is legal either way.
Tags: math linear-algebra elimination-algorithm
<!--ID: 1788676831863-->
END

START
Coding Questions
You substitute the answer back into the **original** system and it checks out. What has that proved — and what had you already proved without it?
Back: **The check proves only that the arithmetic was right.**

**Already guaranteed, before substituting anything:** every step was a **reversible** move, so the final system has the original's solution set. The *method* never needed checking.

Still worth doing — a long elimination is many hand calculations, and that is where slips live.
Tags: math linear-algebra elimination-algorithm
<!--ID: 1788676831866-->
END

START
Coding Questions
On the backward pass, why clear the `x₃` column before the `x₂` column?
Back: **Effort, not correctness.** Once the `x₃` column is clean, no later step carries any `x₃` arithmetic.

Doing `x₂` first would leave `x₃` terms to drag through every remaining operation. Both orders reach the same answer.
Tags: math linear-algebra elimination-algorithm
<!--ID: 1788676831870-->
END

START
Coding Questions
In a row, what is the **leading coefficient** and the **leading variable**?
Back: Read the row left to right and stop at the **first nonzero** number.

- That number is the **leading coefficient**
- The variable it multiplies is the **leading variable**

<div>
\[\begin{array}{rcl}
0x_1 + 2x_2 - 8x_3 = 8 & \quad & \text{leads with } x_2 \\
0x_1 + 0x_2 + x_3 = -1 & \quad & \text{leads with } x_3
\end{array}\]
</div>

Leading zeros are skipped — a variable **absent** from a row can never lead it.
Tags: math linear-algebra elimination-algorithm
<!--ID: 1788677353494-->
END

START
Coding Questions
What does a finished elimination look like, stated in terms of **leading variables**?
Back: **Every row leads with a different variable, and the leading variable moves further right going down.**

A row may still **contain** other variables — the top row can hold all three. The restriction is only on what each row **leads** with.

**Two rows leading with the same variable = work still owed:** subtract a multiple of one from the other to remove it. That is exactly the step the algorithm performs.
Tags: math linear-algebra elimination-algorithm
<!--ID: 1788677353509-->
END

START
Coding Questions
When are two matrices **row equivalent**?
Back: When some **sequence of elementary row operations** transforms one into the other.

**Defined by the route, never by anything visible in the matrices.** Two matrices that look alike need not be row equivalent; two that look nothing alike may be.
Tags: math linear-algebra row-equivalence
<!--ID: 1788677877673-->
END

START
Coding Questions
Why is row equivalence defined by **operations**, while system equivalence is defined by **solution sets**?
Back: Because a **matrix has no solution set**. It is a rectangular array of numbers and may not have come from a system at all — so "same answer" is not available as a test.

The route is the only thing left to compare.

**Upside:** row operations apply to *any* matrix, so row equivalence is a relation on all matrices, not only on augmented ones.
Tags: math linear-algebra row-equivalence
<!--ID: 1788677877680-->
END

START
Coding Questions
Row equivalence is **symmetric**. Why, and why does that matter?
Back: **Why:** row operations are reversible. If operations take A to B, undoing them in reverse order takes B back to A.

**Why it matters:** a one-way relation would be a mere *derivation*, which only prevents **losing** a solution, not **gaining** one. Symmetry is what makes the word *equivalent* honest.
Tags: math linear-algebra row-equivalence
<!--ID: 1788677877688-->
END

START
Coding Questions
State the theorem connecting row equivalence to solution sets.
Back: **If the augmented matrices of two linear systems are row equivalent, then the two systems have the same solution set.**

Both directions, from reversibility:
- Every solution of the original satisfies the new system — each row operation is a legal move
- Every solution of the new satisfies the original — the operations run backwards to rebuild it

**Practical rule:** establish that two systems agree by pointing at the operations performed, never by comparing how the matrices look.
Tags: math linear-algebra row-equivalence
<!--ID: 1788677877696-->
END

START
Coding Questions
The name *row equivalent* misleads twice. How?
Back:
1. **It compares two whole matrices, not two rows.** *Row* names the kind of operation used, not the thing being compared.
2. **It asks only whether a sequence exists**, not whether anyone performed one. Two matrices with no shared history can still be row equivalent.

Also: neither matrix is the "starting" one — the relation is symmetric.
Tags: math linear-algebra row-equivalence
<!--ID: 1788678340456-->
END

START
Coding Questions
**Equivalent systems** vs **row equivalent matrices** — put them side by side.
Back:
| | Equivalent systems | Row equivalent matrices |
|---|---|---|
| Holds between | two **systems** | two **matrices** |
| Defined by | the **outcome** — same solution set | the **route** — a sequence of row operations |
| Silent about | how either was obtained | what either one solves |
| Needs a system? | yes | no |

**Bridge:** row equivalent augmented matrices ⟹ same solution set.
Tags: math linear-algebra row-equivalence
<!--ID: 1788678659822-->
END

START
Coding Questions
Row equivalent ⟹ same solution set. Does the **converse** hold?
Back: **No.** Two systems can share a solution set with no route between their augmented matrices.

**Counterexample — different sizes:** `x₁ + x₂ = 1` alone, versus that plus its double `2x₁ + 2x₂ = 2`. Same solution set; matrices are 1×3 and 2×3, and **no row operation adds or removes a row**.

**Counterexample — same size:** `{x₁ = 0, x₁ = 1}` and `{x₁ + x₂ = 0, x₁ + x₂ = 1}`. Both inconsistent, so both solution sets are empty. The first has an all-zero `x₂` column, and **a column of zeros stays a column of zeros** under every row operation.

Nothing is lost — the theorem is only ever used forwards.
Tags: math linear-algebra row-equivalence
<!--ID: 1788678659830-->
END

START
Coding Questions
What counts as a **proof** that two matrices are row equivalent?
Back: **Exhibiting one legal sequence** of elementary row operations taking one to the other. That is the whole proof.

**No solution set is needed** — it need not be known, and need not exist. The two matrices may describe systems nobody has solved, or no system at all.
Tags: math linear-algebra row-equivalence
<!--ID: 1788678776790-->
END

START
Coding Questions
A system and its augmented matrix are the same data. So how do *equivalent* and *row equivalent* differ at all?
Back: **Not by the objects — by the test**, applied to the same pair.

- **Equivalent:** compare the solution sets (the outcome)
- **Row equivalent:** find a sequence of row operations between them (the route)

**Row equivalent is the stricter test.** Passing it grants equivalence free; the reverse fails.

The only place the objects differ: a matrix need not come from a system, and then only row equivalence is even askable.
Tags: math linear-algebra row-equivalence
<!--ID: 1788678979429-->
END

START
Coding Questions
What are the **two fundamental questions** about a linear system?
Back:
1. **Existence** — is the system **consistent**; does at least one solution exist?
2. **Uniqueness** — if one exists, is it the **only** one?

**Why exactly two:** they separate all three possible outcomes.

| Existence | Uniqueness | Outcome |
|---|---|---|
| no | — | no solution |
| yes | yes | exactly one |
| yes | no | infinitely many |

No third question exists, because there is no fourth outcome.
Tags: math linear-algebra existence-uniqueness
<!--ID: 1788930941332-->
END

START
Coding Questions
Why can existence and uniqueness be answered **before** the system is solved?
Back: Because they are questions about the **shape** of the solution set, not its contents.

From triangular form:

<div>
\[\left[\begin{array}{ccc|c} 1 & -2 & 1 & 0 \\ 0 & 1 & -4 & 4 \\ 0 & 0 & 1 & -1 \end{array}\right]\]
</div>

Each row leaves exactly one variable to determine, with no freedom in what it becomes → **exists, and unique**. Not one of the three values has been computed.

**Trap:** knowing the answer exists is not knowing the answer.
Tags: math linear-algebra existence-uniqueness
<!--ID: 1788930941336-->
END

START
Coding Questions
Elimination produces the row `[0 0 0 | 15]`. What does it prove, and what should you do?
Back: Read back, it says `0x₁ + 0x₂ + 0x₃ = 15`, i.e. **0 = 15** — never true.

A solution must satisfy **every** row, so **no solution exists**: the system is **inconsistent**.

**Stop immediately.** Further work computes values for a system that has none.

**Transfers to the original** — the matrices are row equivalent, so an empty solution set at the end means an empty one at the start.
Tags: math linear-algebra existence-uniqueness
<!--ID: 1788930941337-->
END

START
Coding Questions
`[0 0 0 | 15]` vs `[0 0 0 | 0]` — nearly identical rows. What does each mean?
Back:
| Row | Reads as | Meaning |
|---|---|---|
| `[0 0 0 | 15]` | 0 = 15 | **contradiction** — no solution |
| `[0 0 0 | 0]` | 0 = 0 | **redundant** equation — no information |

**The constant column is the entire difference.** A `0 = 0` row means one equation was a combination of the others — fewer real constraints than equations, pointing toward *infinitely many* solutions rather than none.
Tags: math linear-algebra existence-uniqueness
<!--ID: 1788930941338-->
END

START
Coding Questions
In elimination, when is the **swap** operation actually needed?
Back: When the leading position holds a **zero** — the top row has no term in the variable you are trying to clear, so it cannot eliminate anything.

<div>
\[\begin{array}{rrrrrrr}
 & & x_2 &-& 4x_3 &=& 8 \\
2x_1 &-& 3x_2 &+& 2x_3 &=& 1
\end{array}\]
</div>

Interchange with a row below that does have the term. **This is the only place the algorithm needs swap** — which is why two operations would not be enough.
Tags: math linear-algebra elimination-algorithm
<!--ID: 1788930941339-->
END

START
Coding Questions
Computers solve systems in **floating point**. What two distinct errors does that introduce?
Back: A number is stored as `±.d₁…d_p × 10ʳ` — a **fixed budget of significant digits**.

1. **Representation error** — `1/3` has no finite decimal form, so the stored value is wrong *before* any arithmetic.
2. **Roundoff error** — each operation's result is squeezed back into `p` digits, so every step adds more.

**Why elimination shows it:** a long chain of multiply-and-subtract, where nothing resets and errors compound.

**What it changes about the theory:** *nothing*. Reversibility, equivalence and the three solution counts are statements about exact arithmetic. Floating point is a property of the machine, not the algorithm.
Tags: math linear-algebra floating-point
<!--ID: 1788930941340-->
END

START
Coding Questions
What rule licenses combining two equations of a system into a new one, and what exactly does it claim?
Back: **Equals combined with equals give equals.**

<div>\[ \text{if } a = b \text{ and } c = d, \text{ then } a - c = b - d \text{ and } a + c = b + d \]</div>

Two separate *true* statements go in, a third true statement comes out. Nothing is assumed about the letters, only that each pair was equal to start with.

**The picture:** two balanced scales. Take the contents of the second off the first, pan for pan. Equal amounts left both sides, so the balance holds.

**Scaling is the same rule:** if `a = b` then `ka = kb`, for a constant `k`.
Tags: math linear-algebra equals-combined
<!--ID: 1788936498373-->
END

START
Coding Questions
When you scale an equation by a factor `k`, why must `k` be a constant and never a variable?
Back: **A variable might be zero.**

Multiplying through by a variable that turns out to be `0` flattens the equation to `0 = 0`, which is still true but true of *everything*, so the system now accepts every point on the remaining line.

That is **gaining** solutions, and it needs no squaring or exotic algebra: one careless multiplication does it inside a plain linear system.
Tags: math linear-algebra equals-combined
<!--ID: 1788936498417-->
END
