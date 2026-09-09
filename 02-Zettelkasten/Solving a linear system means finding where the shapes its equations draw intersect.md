---
created: 2026-09-05
tags: [math, linear-algebra, geometry, solution-set]
aliases: [solving as intersection, geometric meaning of solving]
---

A <mark style="background: #FFF3A3A6;">solution must satisfy every equation in the system <b>at once</b></mark> — that "at once" is the entire content of the word <i>system</i>. Satisfying one equation and failing another is not a partial success; it is not a solution.

Read geometrically, that requirement has an immediate meaning.

---

### Every equation is a shape, and the solution lies on all of them

Each equation draws a shape — [[The number of variables sets the dimension and each equation draws a shape one dimension lower|a line in 2-D, a plane in 3-D, a hyperplane in general]]. A point satisfies an equation exactly when it lies on that equation's shape.

So a point solving the whole system must lie on <b>every</b> shape simultaneously:

<mark style="background: #FFF3A3A6;">Solving a system = finding the intersection of all the shapes its equations draw.</mark>

There are only three ways shapes can meet:

1. At <b>one point</b> — one solution
2. Along a whole <b>line or plane</b> of points — infinitely many solutions
3. <b>Nowhere</b> — no solution

That is why [[A linear system has zero, one, or infinitely many solutions and never any other count|only three solution counts are possible]]. The geometry permits no fourth arrangement.

---

### Counting equations against unknowns

Because equations are constraints and variables are freedoms, the two counts predict the shape of the answer before any calculation.

#### Fewer equations than unknowns

Two equations in three unknowns is two planes in 3-D space. Two non-parallel planes meet in a whole <b>line</b> — infinitely many solutions.

<mark style="background: #ABF7F7A6;">Fewer equations than unknowns means not enough constraints to pin down a single point</mark>, and some freedom always survives. This is the underdetermined case, and it is the normal situation in machine learning, where a model has far more parameters than the data has constraints.

#### More equations than unknowns

Three equations in two unknowns is three lines in one plane. Two of them will generally cross somewhere, but the third has no reason to pass through that same point.

<mark style="background: #FF9E9EA6;">More equations than unknowns usually means an inconsistent, over-constrained system with no exact solution at all.</mark> Rather than give up, applied mathematics asks for the point that comes <i>closest</i> to all three, which is exactly what least-squares regression computes.

#### Equal counts guarantee nothing

Two equations in two unknowns still fails when the lines happen to be parallel, and still gives infinitely many when they coincide. <mark style="background: #FF5582A6;">Matching counts make a unique solution likely, never certain</mark> — only the algebra decides.

---

### Read more

- [[The number of variables sets the dimension and each equation draws a shape one dimension lower]]
- [[A linear system has zero, one, or infinitely many solutions and never any other count]]
- [[Two systems are equivalent when they have the same solution set]]
- [[Math for ML MOC]]
