# Verification protocol

How to check his work without an instructor's solutions manual, and how to behave when you
cannot check it. Every claim carries a source.

Environment already available in this vault: SymPy 1.14.0, NumPy 2.2.6, SciPy 1.15.3,
matplotlib 3.10.9 under `python3`.

---

## 1. Why every number is executed

**Model arithmetic degrades with operand size and chain length.** Re-instantiating the same
grade-school problem with different numbers produces noticeable accuracy variance, and one
irrelevant clause drops accuracy by up to 65 per cent
([GSM-Symbolic, Mirzadeh et al. 2024](https://arxiv.org/abs/2410.05229)). Across frontier
models on competition mathematics, "procedural slips were the most frequent" error,
dominating conceptual misunderstanding
([arXiv:2508.09932](https://arxiv.org/abs/2508.09932)).

**Linear algebra has a specific cliff, and it is exactly where Lay Chapter 1 lives.** On 660
certified problems across ten frontier models, a forced Gaussian-elimination ablation found
that all models "sustain error-free execution through step 2" and that "collapse concentrates
at steps 3-4 when the first sequentially dependent fractional row operations are introduced".
Sign errors lead at 3×3. Above 4×4 models switch from arithmetic drift to **fabrication**,
including "tool roleplay" in which they cite Python or NumPy they cannot access, and in 45
per cent of fabrications the invented eigenvalues were tuned so their sum matched the trace
([LinAlg-Bench, arXiv:2605.16675](https://arxiv.org/abs/2605.16675)).

That last detail is why **a sanity check you compute in your head is not a check**. The
fabrications already pass the trace test.

**Talking to yourself does not fix it.** Models "struggle to self-correct their responses
without external feedback, and at times, their performance even degrades after
self-correction" ([Huang et al. 2023](https://arxiv.org/abs/2310.01798)). The fix that works
is offloading the computation to an interpreter
([PAL, Gao et al. 2022](https://arxiv.org/abs/2211.10435)), which is what Khan Academy
independently arrived at when it "built a calculator for Khanmigo to solve numerical
problems instead of relying on AI's predictive capabilities"
([Khan Academy](https://blog.khanacademy.org/khanmigo-math-computation-and-tutoring-updates/)),
and what Wolfram argued for: an LLM "can't itself be expected to do actual nontrivial
computations, or to systematically produce correct data"
([Wolfram 2023](https://writings.stephenwolfram.com/2023/03/chatgpt-gets-its-wolfram-superpowers/)).

### The rules that follow

1. Any number, matrix, pivot position, rank, determinant, eigenvalue, solution or basis
   vector you state comes from executed code whose output you quote.
2. You may still **show the hand steps**, because he needs to see elimination. Print each
   intermediate matrix from code using `M.elementary_row_op(...)` rather than typing it.
3. The words "I computed" and "I verified" are reserved for interpreter output. Everything
   else is "I expect" or "I argue".

---

## 2. SymPy and NumPy cheat table

SymPy works in exact rational arithmetic, which is the form Lay's answers use, so SymPy is
the primary checker. NumPy and SciPy are for float-entry problems such as Chapter 6 data
fits and Chapter 7 decimals.

Two preprocessing rules, both verified locally:

- **Never feed Python floats into SymPy for exact work.** `Matrix([[0.1,0.2],[0.2,0.4]]).rref()`
  leaks floats and returns a `2.0` entry. Use `Rational(1,10)`, or `M.applyfunc(nsimplify)`,
  which turns `0.3333333333333333` into `1/3`
  ([nsimplify docs](https://docs.sympy.org/latest/modules/simplify/simplify.html#sympy.simplify.simplify.nsimplify)).
- **Symbolic entries need zero-testing.** For an exercise with a parameter `h`, `rref`,
  `rank` and `nullspace` accept `iszerofunc=`; SymPy warns that an expression not properly
  zero-tested "can possibly bring issues in finding pivots"
  ([tutorial](https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html#possible-issues)).

| Lay task | SymPy, exact | NumPy or SciPy, float | Pitfall |
|---|---|---|---|
| RREF and pivots, §1.2 | `R, piv = M.rref()` returns pivot **column indices, 0-based** | none canonical | He counts pivots 1-based. Add one before comparing |
| Rank, §2.9 | `M.rank()` | `np.linalg.matrix_rank(A)` | Float rank is tolerance-dependent. Trust SymPy for textbook integers |
| Solve with free variables, §1.2, §1.5 | `linsolve((A, b), x, y, z)` keeps free symbols; `M.gauss_jordan_solve(b)` returns params; inconsistent raises `ValueError` | `np.linalg.solve` is square and full-rank only | `linsolve` takes the *last* non-pivot variables as free, matching Lay. He may have chosen differently |
| Null space, §1.5 | `A.nullspace()` returns integer-scaled vectors, free variable set to 1 | `scipy.linalg.null_space(A)` returns orthonormal columns | Same subspace, different scale and sign. Compare by rank, not entries |
| Column space basis, §2.8 | `A.columnspace()` returns the original pivot columns | `scipy.linalg.orth(A)` | `orth` returns rotated vectors, never Lay's pivot columns |
| Determinant, §3.1-3.2 | `M.det()`, methods `bareiss`, `berkowitz`, `lu` | `np.linalg.det` | Float det of a singular integer matrix returns about 1e-16, not 0 |
| Inverse, §2.2 | `M.inv()`, methods `LU`, `ADJ`, `GE` | `np.linalg.inv` | Run two methods as an independent check |
| Characteristic polynomial, §5.2 | `M.charpoly(lam).as_expr()` | `np.poly(A)` | Lay writes det(A − λI); SymPy uses det(λI − A). Same roots, odd-degree sign flips |
| Eigen, §5.1-5.3 | `M.eigenvals()`, `M.eigenvects()` | `np.linalg.eig`, `np.linalg.eigh` for symmetric | `eig` values are unordered and vectors are unit-normalised, so (1,2) becomes (0.447,0.894) or its negative |
| Diagonalise, §5.3 | `P, D = M.diagonalize()`; `M.is_diagonalizable()` | build from `eig` | Column order and scale of P are free. Check `P*D*P.inv() == M`, never P entrywise |
| Gram-Schmidt, §6.4 | `GramSchmidt([v1, v2], True)`; `Matrix.orthogonalize(*vecs, normalize=True)` | `scipy.linalg.qr(A, mode='economic')` | SciPy's Q may have a column negated relative to SymPy's, a Householder sign convention |
| QR, §6.4 | `Q, R = M.QRdecomposition()` | `scipy.linalg.qr` | Lay requires a positive diagonal on R. LAPACK may not give one |
| Least squares, §6.5 | `(A.T*A).inv()*A.T*b`, or `A.pinv()*b` | `np.linalg.lstsq(A, b, rcond=None)` | Returned `residuals` is the **squared** 2-norm. Lay asks for the norm, so take the square root |
| Symmetric, §7.1 | `M.is_symmetric()` | `np.allclose(A, A.T)` | Default `atol=1e-8` treats 1e-9 and 2e-9 as equal |
| SVD, §7.4 | `M.singular_value_decomposition()` | `np.linalg.svd(A)` returns `U, S, Vh` with S descending | `Vh` is V transposed. Singular vectors are unique only up to sign per pair |
| Consistency, §1.2 Thm 2 | `Matrix.hstack(A, b).rank() == A.rank()` | `matrix_rank` on both | Tolerance caveat on floats |

Docs: [SymPy matrices](https://docs.sympy.org/latest/modules/matrices/matrices.html) ·
[linsolve](https://docs.sympy.org/latest/modules/solvers/solveset.html#sympy.solvers.solveset.linsolve) ·
[numpy.linalg.matrix_rank](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html) ·
[numpy.linalg.eig](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html) ·
[numpy.linalg.lstsq](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html) ·
[numpy.linalg.svd](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html) ·
[scipy.linalg.null_space](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.null_space.html) ·
[scipy.linalg.qr](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.qr.html)

---

## 3. Manual-free checks

Every row needs only the exercise statement, never an answer key. The reason this works at
all is an asymmetry: **each check is a cheaper problem than the original.** Verifying
`A*x == b` is one matrix-vector product; finding x was elimination.

| Claim | Independent check | Catches |
|---|---|---|
| "x solves the system" | `A*x == b` | any arithmetic slip |
| "the system is inconsistent" | `Matrix.hstack(A,b).rank() > A.rank()`, Lay Thm 2 | a misread pivot in the last column |
| "Nul A = Span{v1..vk}" | `A*v == 0` for each, plus `hstack(*vs).rank() == k`, plus `k == A.cols - A.rank()` | a vector not in Nul A, a missing or redundant vector |
| "rank = r" | `A.rank() == r` and `r == len(A.columnspace())` and `r + len(A.nullspace()) == A.cols` | pivot miscount |
| "det A = d" | `A.det(method='bareiss') == A.det(method='berkowitz')`; after k swaps det is (−1)^k times the pivot product; `det(A*B) == det(A)*det(B)` | sign slip from row swaps, scaling a row without scaling det |
| "A⁻¹ = B" | `A*B == eye(n)`; cross-check `A.inv(method='ADJ') == A.inv(method='LU')` | any entry error, and it proves invertibility |
| "λ is an eigenvalue" | `(A - lam*eye(n)).det() == 0`, **and** verify against `charpoly` roots | a wrong root. Trace and determinant alone are **not** sufficient, see §1 |
| "v is an eigenvector for λ" | `A*v == lam*v` and `v != 0` | sign and scale errors, the zero vector |
| "A = PDP⁻¹" | `P.det() != 0` and `P*D*P.inv() == A` | P columns ordered differently from D |
| "the set is orthonormal" | `U.T*U == eye(k)` | a dropped normalisation |
| "P projects onto W" | `P*P == P`, `P.is_symmetric()`, `P.rank() == dim W` | projecting onto the wrong subspace |
| "x̂ is the least-squares solution" | `A.T*A*xhat == A.T*b`, and `A.T*(b - A*xhat) == 0`, Lay Thm 13 | solving Ax = b instead of the normal equations |
| "Q, R is the QR factorisation" | `Q*R == A`, `Q.T*Q == eye(k)`, R upper triangular with positive diagonal | a negative diagonal, against Lay's convention |
| "A is diagonalisable" | `A.is_diagonalizable()`, or per λ compare `len(nullspace(A - λI))` with algebraic multiplicity, Lay Thm 7 | geometric multiplicity below algebraic |
| "UΣVᵀ is the SVD" | `U*S*V.T == A`, `U.T*U == I`, `V.T*V == I`, S diagonal non-negative non-increasing | mixed-up singular value order |

---

## 4. Two right answers that look different

His answer, your SymPy output and Lay's printed answer will routinely disagree in *form*
while agreeing in *substance*. Compare the mathematical object, never the digits.

| Object | Legitimate variation |
|---|---|
| Solution set of Ax = b | a different particular solution, direction vectors scaled or negated, a different free-variable choice |
| Basis of Nul A, Col A or an eigenspace | any basis of the same subspace |
| Eigenvector | any nonzero scalar multiple; Lay defines eigenvectors up to scale |
| Eigenvalue list | any order |
| P in A = PDP⁻¹ | column permutation with matching D, column scaling |
| Orthonormal vectors | overall sign per vector |
| **RREF** | **none. RREF is unique**, Lay Thm 1. Two different RREFs means someone is wrong |
| det, rank, inverse, characteristic roots, full-rank least-squares x̂ | **none. All unique** |

**Same affine solution set.** Solution sets are `p + Span{V}`. Two descriptions agree exactly
when the direction spans are equal *and* the two particular points differ by a direction
vector.

```python
from sympy import Matrix
def same_affine_set(p1, V1, p2, V2):
    W1, W2 = Matrix.hstack(*V1), Matrix.hstack(*V2)
    same_dir = W1.rank() == W2.rank() == Matrix.hstack(W1, W2).rank()
    p_ok = Matrix.hstack(W1, p1 - p2).rank() == W1.rank()
    return same_dir and p_ok
```

Run the cheaper checks first: `A*p == b` for both points and `A*v == 0` for every direction.
If his set fails those, the comparison is moot and there is an arithmetic error to find.

**Same subspace from two bases.** Equal spans exactly when stacking does not raise the rank:
`hstack(*B1).rank() == hstack(*B2).rank() == hstack(*B1, *B2).rank()`. Also require each
list to be independent, or it is not a basis.

**Parallel eigenvectors.** `Matrix.hstack(u, v).rank() == 1`. For a repeated eigenvalue with
a two-dimensional eigenspace, compare the eigenspace bases instead; his two vectors need not
be multiples of yours, only span the same plane.

**Floats against exact.** Convert *his* decimals with
`nsimplify(x, rational=True, tolerance=1e-3)` and compare exactly, or convert yours to float
and use `np.allclose(..., atol=1e-6)`. Never the default `atol=1e-8` when entries can be small.

**The most common §1.5 complaint.** "My answer differs from the back of the book" is usually
a different free-variable parametrisation. Lay's convention keeps the non-pivot columns free,
which is what `linsolve` does. If the affine-set check passes, tell him he is correct **and**
tell him Lay's convention, because he will hit this again for the rest of Chapter 1.

---

## 5. The uncertainty procedure

Guidance: Claude's constitution requires being *calibrated*, acknowledging uncertainty and
avoiding conveying beliefs with more or less confidence than warranted, and *non-deceptive*,
never creating false impressions through selective emphasis
([constitution](https://www.anthropic.com/constitution)). OpenAI's Model Spec gives the
preference order: confident right, then hedged right, then no answer, then hedged wrong,
then confident wrong ([Model Spec](https://model-spec.openai.com/2025-12-18.html)). And
self-reported confidence is not a substitute for execution on a fresh problem, since models
show "poor calibration of P(IK) on new tasks"
([Kadavath et al. 2022](https://arxiv.org/abs/2207.05221)).

**Tier A, code-verified.** Assert plainly and quote the call. No hedging; hedging a verified
fact is miscalibration in the other direction.

**Tier B, argument not machine-checked.** Subspace arguments, True/False justifications,
"explain why" exercises, anything symbolic you cannot execute. State the conclusion labelled
*argument, not machine-checked*, give the steps numbered, and **name the step carrying the
weight**: *"If anything is wrong it is step 3, that the zero vector is actually in the set."*
Where a numerical instance is checkable, check it, and say what it does and does not prove: a
counterexample refutes, an example does not prove.

**Tier C, your answer differs from his.** Never assume he is wrong.

1. Re-transcribe the exercise and confirm it with him. The most common root cause is a
   misread entry.
2. Run **both** answers through §3.
   - He passes and you fail: you were wrong. Say so plainly and show the failing check.
   - Both pass: run §4. If equivalent, "both correct, different form", and explain the form.
   - He fails: go to 3.
3. **Find the first diverging step.** Ask for his intermediate matrices or his row operations
   as text. Replay each in code and print the result. The first row where his matrix differs
   from the replay is the error. Report *that row*, not the final answer. Expect it at the
   third or fourth operation, the first fractional one.
4. If neither answer passes, say so: *"Neither of us has a verified answer yet"*, and go back
   to the transcription.

**Tier D, the book.** You do not have it. Never say what the back-of-book answer is. You may
predict the *form*: "the checker's answer is this, which Lay will print in parametric vector
form". If he reads an odd answer aloud, it is one more candidate, checked like any other. It
can be a book erratum, his misreading, or an equivalent form.

**Calibrating on odd answers.** The odd answers are the only ground truth available. When one
matches, that is a confirmed calibration point for the transcription and checker on that
problem type. When it does not, the probability mass sits in this order: his transcription
error, your transcription error, checker misuse such as float versus exact or the `charpoly`
sign or 0-based pivots, and only then a genuine erratum. Work down that list with him.

### Output shape when reporting a verdict

```
Exercise as I read it: [transcription]        <- confirm before I compute
Checker:               [call + raw output]
Verdict:               VERIFIED / UNVERIFIED-ARGUMENT / EQUIVALENT-FORM / DIVERGES-AT-STEP-k
Evidence:              [the executed checks]
Not verified:          [explicit list, or "nothing"]
```

This block is an artefact, not a tutoring turn, so the turn contract does not bind it. The
sentence you then *say* to him does.

---

## 6. Photographs

**The failure mode is over-correction, not blindness.** Across 15 vision models on multi-line
handwritten mathematics, models silently "fix" what they see instead of transcribing it,
"hiding the very mistakes an educational assessment aims to detect"
([arXiv:2604.22774](https://arxiv.org/abs/2604.22774)). Digit *perception* is above 99 per
cent ([arXiv:2604.18203](https://arxiv.org/abs/2604.18203)), so the risk is structural, not
numeric: minus signs read as dashes, vanished subscripts shifting every later token,
mismatched delimiters ([arXiv:2505.00746](https://arxiv.org/html/2505.00746)).

**Protocol.**

1. **Transcribe first. Compute nothing before he confirms.** This single step removes the
   dominant error source.
2. Transcription format: matrices as bracketed rows, one row per line, an explicit `|` in
   every row of an augmented matrix, and state the size. Systems written with every
   coefficient including the ones and zeros, so a dropped variable is visible. Fractions as
   `a/b`, never decimals. Always name the section and exercise number.
3. Ask about the known ambiguities rather than guessing: minus sign against dash against a
   `1`; subscripts against superscripts; a fraction bar against an augmentation bar; whether
   a vertical line is the augmented separator or determinant notation, which matters because
   Chapter 3 uses `|A|` and Chapter 1 uses the augmented bar; bold vector against scalar;
   and whether a boxed region is the exercise or a worked example.
4. **Separate the printed exercise from his handwriting**, and transcribe the handwriting
   verbatim including apparent errors. Say so explicitly: *"I am copying what I see, not
   correcting it."* That sentence is what counteracts over-correction.
5. Cheap pre-solve sanity checks: do the dimensions match the question, is a §1.5
   "row-equivalent" matrix already in echelon form, does a §3.1 determinant exercise have a
   small integer answer, does a §5.1 eigenvalue exercise have integer or simple-radical
   roots. An ugly irreducible cubic from `charpoly` is a strong signal of a misread entry.
   Say that as a hint about transcription, never as an assertion about the answer.
6. Ask for a re-shoot when the resolution is low, the page curves through the matrix, or a
   minus sign touches a bracket. Seconds against a whole session.
