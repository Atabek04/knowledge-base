---
created: 2026-09-05
tags: [math, linear-algebra, geometry, foundations]
aliases: [variables and dimensions, hyperplane, geometric view of equations]
---

A linear system can be read two ways at once: as algebra to be manipulated, and as shapes in space. The second reading is what makes results memorable rather than procedural, and it rests on one correspondence that is easy to state and easy to get backwards.

<mark style="background: #FF5582A6;">Variables and equations play completely different geometric roles, and swapping them is the single most common beginner error.</mark>

- <b>Variables</b> set the <b>dimension of the space</b> you are drawing in.
- <b>Equations</b> are the <b>shapes drawn inside it</b>.

Three equations in two unknowns is therefore three lines in one plane — not three planes, and not a 3-D picture.

---

### Each equation drops one dimension

| Variables | Space | One equation draws |
|---|---|---|
| 2 (`x₁, x₂`) | plane, 2-D | a <b>line</b> |
| 3 (`x₁, x₂, x₃`) | space, 3-D | a <b>plane</b> |
| n | n-D | a <b>hyperplane</b>, (n−1)-dimensional |

![[hyperplane_one_dimension_lower.svg|650]]

A <b>constraint</b> (ru: ограничение) is a restriction on what is allowed. <mark style="background: #FFF3A3A6;">An equation is a constraint because it does not describe every point in the space — it accepts the points that satisfy it and rejects the rest.</mark>

A <b>degree of freedom</b> (ru: степень свободы) is one choice you are still free to make. With three variables and nothing imposed on them, you have three: each coordinate can be whatever you like.

<mark style="background: #ABF7F7A6;">One equation is one constraint, and each constraint removes exactly one degree of freedom</mark> — after imposing it, one of the variables can no longer be chosen, because the equation already determines it from the others.

Fewer free choices means a smaller shape, and the loss is always exactly one.

#### Why exactly one dimension

Take three variables, so every point in the space is a triple $(x_1, x_2, x_3)$ — that triple *is* what "3-D" means here. All three coordinates are present at every point; none of them is the dimension count.

Now impose one equation:

$$x_1 + x_2 + x_3 = 6$$

Choose $x_1$ — anything at all, say $1$. Nothing stops you.

Choose $x_2$ — again anything, say $2$. Still nothing stops you.

Now try to choose $x_3$. <mark style="background: #FF5582A6;">You cannot: the equation already fixed it at $3$, because $1 + 2 + x_3 = 6$ has one answer.</mark> That is what "the equation forces $x_3$" means — not that $x_3$ disappeared, but that it is no longer yours to pick.

| $x_1$ | $x_2$ | $x_3$ forced to be | point on the shape |
|---|---|---|---|
| $1$ | $2$ | $3$ | $(1, 2, 3)$ |
| $0$ | $0$ | $6$ | $(0, 0, 6)$ |
| $5$ | $-1$ | $2$ | $(5, -1, 2)$ |

Three variables, but only <b>two</b> of them are free. Every free choice is one direction you can move in, so two free choices trace out a 2-dimensional sheet — a plane — sitting inside 3-D space.

<mark style="background: #ADCCFFA6;">The shape one equation draws always has one dimension fewer than the space, because one of the variables stops being a choice.</mark> It is always exactly minus one, and the lost degree of freedom is the reason.

#### Hyperplane

<mark style="background: #FFF3A3A6;">A hyperplane is the flat, (n−1)-dimensional slice that one linear equation carves out of n-dimensional space.</mark> In 2-D a hyperplane is an ordinary line; in 3-D it is an ordinary plane. The word exists only because "line" and "plane" run out at three dimensions.

The naming works the same way in each case — a <i>hyper</i>plane is the plane concept lifted past the dimensions we can draw.

![[intersecting_planes.svg|280]]

Both sheets above are hyperplanes of 3-D space: each is flat, each is 2-dimensional, and each is what a single equation in three unknowns draws. Two equations means two of them, and the points satisfying both lie on the line where they cross.

---

### Picturing four dimensions

<mark style="background: #FF9E9EA6;">Four dimensions and beyond cannot be visualised, and no amount of effort fixes that.</mark> This is not a gap in your intuition to be worked on; it is a limit of spatial imagination that everyone shares.

It is also the reason the algebra exists. Row reduction is mechanical and never consults a picture, so it keeps working unchanged at n = 500 where visual intuition stopped at 3.

<mark style="background: #ADCCFFA6;">Draw in 2-D to understand why a method works, then trust the algebra to carry it into dimensions you cannot see.</mark> The 2-D picture is a teaching aid, not the justification.

---

### Glossary

| Word | In this context |
|---|---|
| <b>Constraint</b> | One equation, seen as a restriction — it rules out every point that fails it |
| <b>Degree of freedom</b> | One variable you are still free to choose; each constraint removes one |
| <b>Line</b> | The shape one equation draws in 2-D |
| <b>Plane</b> | A flat 2-D sheet; the shape one equation draws in 3-D |
| <b>Hyperplane</b> | The same idea in n-D — the flat (n−1)-dimensional shape one equation draws |
| <b>Space</b> | The whole set of possible points, its dimension set by the variable count |

---

### Read more

- [[Subscript notation lets one formula describe any number of unknowns]]
- [[Solving a linear system means finding where the shapes its equations draw intersect]]
- [[A linear system has zero, one, or infinitely many solutions and never any other count]]
- [[Math for ML MOC]]
