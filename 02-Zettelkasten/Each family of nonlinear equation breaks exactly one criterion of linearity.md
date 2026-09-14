---
created: 2026-09-05
tags: [math, linear-algebra, equations, foundations]
aliases: [nonlinear equations, nonlinear families]
---

<mark style="background: #FFF3A3A6;">"Nonlinear" is the only umbrella term — everything that fails the linearity test falls under it, and mathematics offers no second general word.</mark> But the families underneath the umbrella have names worth knowing, because a textbook will name them without defining them.

The useful way to hold the list is not as six separate definitions. Each family is one criterion of [[An equation is linear when every variable stands alone to the first power and is multiplied only by a constant|the linearity test]] being broken. <mark style="background: #ABF7F7A6;">The taxonomy of nonlinear families and the linearity test are the same knowledge seen from two directions.</mark>

---

### The six families

| Family | Example | What breaks linearity |
|---|---|---|
| <b>Polynomial</b> (quadratic, cubic, …) | `x² − 3x = 1` | variable raised to a power ≠ 1 |
| <b>Bilinear / multiplicative</b> | `4x₁ − 6x₂ = x₁x₂` | two variables multiplied together |
| <b>Radical</b> | `x₂ = 2√x₁ − 7` | variable under a root, i.e. power ½ |
| <b>Exponential</b> | `2^x = 7` | variable sitting in the exponent |
| <b>Trigonometric</b> | `sin x₁ + x₂ = 0` | variable inside a function |
| <b>Rational</b> | `1/x₁ + x₂ = 5` | variable in a denominator, i.e. power −1 |

A root is a fractional power and a denominator is a negative power, so <mark style="background: #ABF7F7A6;">polynomial, radical and rational are one violation — power ≠ 1 — wearing three faces.</mark> Seeing that cuts the list you have to hold from six to four.

---

### Degree versus exponential

These two get conflated constantly, and the distinction is simply <b>which position the variable occupies</b>.

- <b>Degree</b> (a <i>power</i>) — the variable is in the <b>base</b>, a number in the exponent: `x²`, `x³`
- <b>Exponential</b> — a number is in the <b>base</b>, the variable in the <b>exponent</b>: `2^x`, `e^x`

Both are nonlinear, and they are not interchangeable descriptions of the same growth. At `x = 10`, `x²` is 100 while `2^x` is 1024, and the gap widens without limit from there.

<mark style="background: #ABF7F7A6;">This is the same split as O(n²) versus O(2ⁿ) in algorithmic complexity</mark> — literally the same two functions, and the same reason a quadratic algorithm is tolerable while an exponential one is not.

---

### Why the boundary matters

Nonlinear equations are not harder versions of linear ones; they are a different problem with no general solution method. Linear systems have a procedure that always terminates with a complete answer.

<mark style="background: #ABF7F7A6;">The whole leverage of linear algebra comes from staying on the linear side of this line.</mark> That is also why so much of applied mathematics is spent approximating a nonlinear problem with a linear one.

---

### Read more

- [[An equation is linear when every variable stands alone to the first power and is multiplied only by a constant]]
- [[Math for ML MOC]]
