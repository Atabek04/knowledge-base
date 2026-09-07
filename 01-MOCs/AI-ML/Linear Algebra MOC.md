---
created: 2026-09-04
tags: [moc, linear-algebra]
---

The roadmap for Block 1 of the mathematics track, worked from Lay, Lay & McDonald,
*Linear Algebra and Its Applications*, 5th edition. Taught by the `math-professor` skill,
one section at a time, at 30 minutes a day through September 2026 and an hour a day from
October.

Chapter order is the reading path. Dependency is carried by the links inside each note, not
by this file. A checkbox becomes a link once the note exists, and never before.

**A section is done when its exercises are worked, not when it was read.** The four exit
conditions are in the skill: teach it back in two minutes, four of five fresh exercises
correct closed-book, one problem of a different surface form, and the note written.

---

## Chapter 1 — Linear Equations in Linear Algebra

- [ ] §1.1 Systems of Linear Equations
- [ ] §1.2 Row Reduction and Echelon Forms
- [ ] §1.3 Vector Equations
- [ ] §1.4 The Matrix Equation Ax = b
- [ ] §1.5 Solution Sets of Linear Systems
- [ ] §1.7 Linear Independence
- [ ] §1.8 Introduction to Linear Transformations
- [ ] §1.9 The Matrix of a Linear Transformation

## Chapter 2 — Matrix Algebra

- [ ] §2.1 Matrix Operations
- [ ] §2.2 The Inverse of a Matrix
- [ ] §2.3 Characterizations of Invertible Matrices
- [ ] §2.8 Subspaces of R^n
- [ ] §2.9 Dimension and Rank

## Chapter 3 — Determinants

Trimmed to properties only. Enough for the characteristic polynomial, no more.

- [ ] §3.1 Introduction to Determinants
- [ ] §3.2 Properties of Determinants

## Chapter 5 — Eigenvalues and Eigenvectors

- [ ] §5.1 Eigenvectors and Eigenvalues
- [ ] §5.2 The Characteristic Equation
- [ ] §5.3 Diagonalization

## Chapter 6 — Orthogonality and Least Squares

- [ ] §6.1 Inner Product, Length, and Orthogonality
- [ ] §6.2 Orthogonal Sets
- [ ] §6.3 Orthogonal Projections
- [ ] §6.4 The Gram-Schmidt Process
- [ ] §6.5 Least-Squares Problems

## Chapter 7 — Symmetric Matrices and the SVD

Lay titles §7.5 "Applications to Image Processing and Statistics". It is PCA.

- [ ] §7.1 Diagonalization of Symmetric Matrices
- [ ] §7.4 The Singular Value Decomposition
- [ ] §7.5 Applications to Image Processing and Statistics

---

## Counterexamples and boundaries

The objects that fix the edge of a theorem. A counterexample note always records **which
hypothesis it forces in**, not just the odd object.

- [ ] Determinant one does not mean rotation
- [ ] Independence is not pairwise
- [ ] A line missing the origin is not a subspace
- [ ] A matrix with a repeated eigenvalue need not be diagonalizable

## ML payoffs

Where each piece of Chapter 1 to 7 shows up in a real model. Full map with citations lives
in the skill's `references/math-to-ml-map.md`.

- [ ] Rank and the low-rank update behind LoRA
- [ ] Orthogonal projection and why LayerNorm is one
- [ ] Least squares and the linear probe
- [ ] The SVD and how PCA is actually computed

---

## Skipped, deliberately

Lay Chapter 4 is skipped entirely. Abstract vector spaces are not load-bearing for machine
learning, and §2.8 and §2.9 already supply subspaces, dimension and rank in R^n. Chapter 3 is
trimmed to §3.1 and §3.2. Sections 1.6, 1.10, 2.4 through 2.7, 5.4 through 5.8, 6.6 through
6.8 and 7.2 through 7.3 are off the path for this block.

---

## Teaching Progress

- **Last taught:** nothing yet. Track opened 2026-09-04
- **Next:** placement probe, twelve minutes, then §1.1 Systems of Linear Equations
- **Blocked on:** nothing
- **Open loop:** none

---

## Parking lot

Tangents raised mid-session and deliberately deferred. Each entry names the section that
triggers picking it back up.

- *(empty)*

---

### Read more

- [[Math for ML MOC]]
- [[Machine Learning MOC]]
