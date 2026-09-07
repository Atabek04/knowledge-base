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
