---
created: 2026-09-05
tags: [math, linear-algebra, equations, foundations]
aliases: [linear equation, linearity test]
---

Linear algebra is named after the objects it studies, so the first thing worth being exact about is which equations qualify. The test is mechanical and takes a few seconds to run, which matters: you will be classifying equations at a glance for the rest of the subject.

---

### The general form

<mark style="background: #FFF3A3A6;">An equation is linear when it can be written as a sum of constants times single variables, equal to a constant.</mark> Formally:

$$a_1x_1 + a_2x_2 + \cdots + a_nx_n = b$$

where `a₁ … aₙ` (the <b>coefficients</b>) and `b` are <b>constants</b>, and `x₁ … xₙ` are the variables. The subscripts are doing real work here — see [[Subscript notation lets one formula describe any number of unknowns|why variables are numbered rather than lettered]].

<mark style="background: #ADCCFFA6;">If ordinary algebra cannot force the equation into that shape, it is nonlinear.</mark>

---

### The four criteria

Written as a checklist you can actually run:

1. Every variable appears <b>alone</b> — never multiplied by another variable
2. Every variable is raised to the <b>first power</b> only
3. Every variable is multiplied only by a <b>constant</b>
4. The terms are only <b>added or subtracted</b>

Break any single one and the equation is nonlinear. Each family of nonlinear equation corresponds to exactly one broken criterion — that mapping is the subject of [[Each family of nonlinear equation breaks exactly one criterion of linearity|the nonlinear taxonomy]].

#### Name as mnemonic

The word carries the definition: <b>degree 1 in two variables draws a straight line</b>. Any other degree bends it. "Linear" is not jargon layered on top of the idea, it is a description of the picture.

---

### Judge a power by what it sits on

The most common misreading is treating any root or exponent as disqualifying. Consider:

$$x_2 = 2(\sqrt{6} - x_1) + x_3$$

This looks nonlinear, and it is not. The root sits on <b>6</b> — a number, not a variable — so $2\sqrt{6}$ is just an awkward-looking constant. Rearranged:

$$2x_1 + x_2 - x_3 = 2\sqrt{6}$$

Every variable stands alone, to the first power, times a constant. Linear.

<mark style="background: #ADCCFFA6;">Judge a root, power or exponent by what it sits on.</mark> On a constant it is harmless arithmetic that changes nothing; on a variable it destroys linearity.

---

### Constant times variable is fine — variable times variable is not

Criterion 1 is often compressed to "no multiplication", which is too strong and leads to rejecting perfectly linear equations.

Multiplication is allowed whenever one side of it is a constant. `3x₁` is linear. What is forbidden is two <b>variables</b> multiplying each other:

- `x₁x₂` — two different variables
- `x₁²` — which is `x₁ · x₁`, the same violation
- `x₁/x₂` — division by a variable is multiplication by its reciprocal

<mark style="background: #ADCCFFA6;">Constant × variable is allowed; variable × variable is not.</mark> Note that `x₁x₂` also has total degree 2, so criteria 1 and 2 are the same restriction seen from two angles.

---

### Read more

- [[Each family of nonlinear equation breaks exactly one criterion of linearity]]
- [[Subscript notation lets one formula describe any number of unknowns]]
- [[The number of variables sets the dimension and each equation draws a shape one dimension lower]]
- [[Math for ML MOC]]
