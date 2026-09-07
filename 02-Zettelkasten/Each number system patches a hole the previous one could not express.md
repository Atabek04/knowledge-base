---
created: 2026-09-05
tags: [math, foundations, number-systems, notation]
aliases: [number systems, number sets]
---

Mathematics does not have one kind of number. It has five nested collections, and they were not invented all at once — each one appeared because an ordinary operation produced an answer the existing numbers could not name.

Read the sequence as a repair history rather than a list.

---

### The five systems

| Symbol | Name | Contents | What broke → what it fixes | Example |
| --- | --- | --- | --- | --- |
| ℕ | naturals | 1, 2, 3, … | the starting point — things you can count | `7` |
| ℤ | integers | … −2, −1, 0, 1, 2 … | `3 − 5` has no answer in ℕ → <b>negatives</b> | `−12` |
| ℚ | rationals | any fraction `p/q`, q ≠ 0 | `3 ÷ 4` has no answer in ℤ → <b>fractions</b> | `3/4` |
| ℝ | reals | every point on the number line | `x² = 2` has no answer in ℚ → <b>irrationals</b> | `√2`, `π` |
| ℂ | complex | `a + bi` where `i² = −1` | `x² = −1` has no answer in ℝ → <b>imaginary</b> | `3 + 2i` |

<mark style="background: #ABF7F7A6;">The pattern is one sentence: an operation escapes the set, so new numbers are invented to catch it.</mark> Recall which equation broke and the fix follows — far easier than memorising five definitions.

#### Why the letters look arbitrary

Two of them are not English at all, which is why they resist memorisation until you see the source:

- <b>ℤ</b> — from German <i>Zahlen</i>, "numbers".
- <b>ℚ</b> — from <i>quotient</i>, since a rational is one number divided by another.

`ℝ` and `ℂ` are simply <i>real</i> and <i>complex</i>. "Real" is a historical label, coined only to contrast with the numbers its inventors distrusted enough to call "imaginary".

---

### Containment

<mark style="background: #FFF3A3A6;">Each set sits entirely inside the next</mark> — ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ

<div style="text-align:center; padding:14px; border:2px solid #888; border-radius:12px;">ℂ complex
<div style="padding:12px; margin-top:6px; border:2px solid #888; border-radius:12px;">ℝ reals
<div style="padding:12px; margin-top:6px; border:2px solid #888; border-radius:12px;">ℚ rationals
<div style="padding:12px; margin-top:6px; border:2px solid #888; border-radius:12px;">ℤ integers
<div style="padding:12px; margin-top:6px; border:2px solid #888; border-radius:12px;">ℕ naturals</div></div></div></div></div>

<mark style="background: #FF9E9EA6;">The containment never reverses.</mark> `5` is a perfectly good rational (`5/1`) and a perfectly good complex number (`5 + 0i`), but `3/4` is not an integer.

The boundaries are easier to hold by what each set <b>excludes</b>:

| Set | In | Not in |
|---|---|---|
| ℕ | `1`, `7`, `500` | `−3`, `0.5`, `√2` |
| ℤ | `−12`, `0`, `48` | `3/4`, `π` |
| ℚ | `3/4`, `−7/2`, `0.25`, `5` | `√2`, `π` |
| ℝ | `√2`, `π`, `e` | `√(−1)` |
| ℂ | `3 + 2i`, `−i`, `5` | nothing — every polynomial is solvable here |

Where ℕ starts is itself a matter of convention rather than fact — see [[Whether zero is a natural number depends on the convention in use|whether zero counts as natural]].

---

### Membership notation

Belonging to a set is written with `∈`, read "is an element of":

```
x ∈ ℝ        x is a real number
n ∈ ℤ        n is an integer
```

This is how a textbook states the <b>type</b> of a quantity before using it, the same way a signature declares a parameter's type in code. When a linear algebra text opens with "let `a ∈ ℝ`", it is fixing which numbers the coefficients are allowed to be.

---

### Which system a linear algebra course lives in

Introductory linear algebra works almost entirely in <b>ℝ</b> — coefficients, variables and solutions are all real numbers.

ℂ appears only later, when a real matrix turns out to have complex eigenvalues. The reason is geometric: a rotation leaves no direction unmoved, so it has no real eigenvector, and the numbers that describe it have to come from outside ℝ.

---

### Read more

- [[Whether zero is a natural number depends on the convention in use]]
- [[The numerator counts the parts taken and the denominator names the size of each part]]
- [[Math Foundations MOC]]
