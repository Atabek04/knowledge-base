---
created: 2026-09-09
tags: [math, linear-algebra, numerical-methods, floating-point]
aliases: [floating point, roundoff error, numerical stability]
---

Every system worked by hand uses exact arithmetic: $\tfrac13$ stays $\tfrac13$. Real systems are solved by computers, which cannot store $\tfrac13$ at all, and the gap between those two facts is where numerical linear algebra begins.

A computer holds a number as a decimal of fixed length — $\pm .d_1 \ldots d_p \times 10^r$, with $p$ usually between 8 and 16 digits. <mark style="background: #FFF3A3A6;">That is <b>floating point</b>: a fixed budget of significant digits, with the decimal point's position stored separately.</mark>

<mark style="background: #FF5582A6;">Two different things go wrong, and both are unavoidable.</mark>

- <b>Representation error</b> — $\tfrac13$ has no finite decimal form, so the stored value is already wrong before any arithmetic happens.
- <b>Roundoff error</b> — each operation's exact result must be squeezed back into $p$ digits, so every step adds a little more.

---

### Why elimination is where it shows

<mark style="background: #ABF7F7A6;">[[Elimination clears one variable per column going down, then clears back up until each row names one variable|Elimination]] is a long chain of multiplications and subtractions, and each link inherits the error of the ones before it.</mark> Nothing resets; the errors compound.

Production solvers therefore run the same algorithm with modifications for accuracy rather than for speed — most importantly choosing which row to use as the pivot, instead of taking whichever one is there.

<mark style="background: #FF5582A6;">Compounding error does not make computed answers untrustworthy — for the overwhelming majority of problems it stays far below anything that matters.</mark> It becomes visible only in badly conditioned systems, where a tiny change in the input moves the answer a long way.

---

### What it changes about the theory

Nothing. <mark style="background: #ADCCFFA6;">Every guarantee in the subject — reversibility, equivalence, the three solution counts — is a statement about exact arithmetic and stays exactly true.</mark>

Floating point is a property of the <i>machine performing</i> the algorithm, not of the algorithm. Keeping those two apart is what stops "the computer said so" from being mistaken for a proof, and stops a rounding artefact from being mistaken for a mathematical result.

---

### Read more

- [[Elimination clears one variable per column going down, then clears back up until each row names one variable]]
- [[A rewrite is safe exactly when the move that produced it can be undone]]
- [[A linear system has zero, one, or infinitely many solutions and never any other count]]
- [[Math for ML MOC]]
