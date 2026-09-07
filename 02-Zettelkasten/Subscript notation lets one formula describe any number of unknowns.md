---
created: 2026-09-05
tags: [math, linear-algebra, notation, foundations]
aliases: [subscript notation, indexed variables]
---

School algebra names its unknowns `x`, `y`, `z`. Linear algebra abruptly switches to `x₁, x₂, x₃` and never switches back. The change looks like formality for its own sake, and it is not — it is what makes the entire subject expressible.

<mark style="background: #FFF3A3A6;">`x₁, x₂, x₃` means exactly what `x, y, z` means.</mark> Same variables, same equations, different naming scheme.

---

### Why the alphabet had to go

The alphabet runs out. With three unknowns `x, y, z` is comfortable; with five hundred there is no letter scheme that works, while `x₁ … x₅₀₀` is trivial.

More importantly, letters cannot be <b>generalised</b>. Subscripts can:

- `xᵢ` — the i-th variable, whichever one that is
- `x₁, …, xₙ` — the whole family, for any n

<mark style="background: #ABF7F7A6;">One formula can now describe a system with any number of unknowns at once</mark>, which is precisely why linear algebra can state results about n dimensions instead of proving the 2-D case, then the 3-D case, then giving up.

You cannot write the general linear equation `a₁x₁ + a₂x₂ + ... + aₙxₙ = b` in `x, y, z` at all. The notation is a prerequisite for the idea.

---

### Two subscripts address a grid

Coefficients carry two indices: <mark style="background: #FFF3A3A6;">`aᵢⱼ` is the coefficient in row `i`, column `j`</mark>. Row first, column second — the order is fixed and worth committing, since transposing it silently produces the wrong matrix.

This is the same two-index addressing as `grid[i][j]` in code, and the mental model transfers directly: a matrix is a 2-D array, and `aᵢⱼ` is an element access.

---

### Read more

- [[The number of variables sets the dimension and each equation draws a shape one dimension lower]]
- [[An equation is linear when every variable stands alone to the first power and is multiplied only by a constant]]
- [[Math for ML MOC]]
