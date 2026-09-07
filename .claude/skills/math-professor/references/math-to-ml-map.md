# Math to ML map

The answer to "where does this show up in an LLM?", for every Block-1 topic, with the exact
equation or code line and a citation. Nothing here is asserted from memory.

Use it in state 7 of the loop, one sentence per session. Do not deliver the whole entry.
The payoff is content, not motivation; his *own* weekly utility-value writing is the
motivation and you never supply that.

---

## The table

| Lay § | Topic | ML payoff | LLM instance | Citation |
|---|---|---|---|---|
| 1.1-1.2 | Systems, row reduction | Normal equations; LU with pivoting inside every dense solver | You never row-reduce, but rank and pivots explain a singular XᵀX in a probe | [torch.linalg.lu_factor](https://docs.pytorch.org/docs/stable/generated/torch.linalg.lu_factor.html) |
| 1.3-1.5 | Vector equations, span, Ax = b | Embeddings as vectors; representability is "is it in the span"; underdetermined means many weights fit | Linear representation hypothesis: concepts are directions | [arXiv:2311.03658](https://arxiv.org/abs/2311.03658) |
| 1.7 | Linear independence | Multicollinearity; rank-deficient design matrices | Dimensional collapse: embeddings span a strict subspace | [arXiv:2110.09348](https://arxiv.org/abs/2110.09348) |
| 1.8-1.9 | Linear transformations | Every `nn.Linear`; composition is a matrix product, so nonlinearity is mandatory | Q, K, V are three learned linear maps; pure attention collapses to rank 1 | [arXiv:2103.03404](https://arxiv.org/abs/2103.03404) |
| 2.1-2.3 | Matrix algebra, inverse | (XᵀX)⁻¹ in theory, `solve` and `lstsq` in practice; invertible means information-preserving | Preconditioners avoid inverses; flows require invertibility | [arXiv:1505.05770](https://arxiv.org/abs/1505.05770) |
| 2.8-2.9 | Subspaces, rank, null space | Low-rank structure is the organising idea of efficient adaptation | LoRA: ΔW = BA, up to 10,000× fewer trainable parameters on GPT-3 175B | [arXiv:2106.09685](https://arxiv.org/abs/2106.09685) |
| 3.1-3.2 | Determinants | Volume scaling; log det Σ in the Gaussian likelihood; log-det via Cholesky | Log-det Jacobian in flows. LLMs dodge it by autoregressive factorisation | [arXiv:1605.08803](https://arxiv.org/abs/1605.08803) |
| 5.1-5.3 | Eigenvectors, diagonalisation | PCA; power iteration; κ = λmax/λmin sets gradient-descent convergence | The Hessian spectrum explains why normalisation makes deep training work | [arXiv:1901.10159](https://arxiv.org/abs/1901.10159) |
| 6.1-6.3 | Inner product, projection | Cosine similarity; least squares *is* orthogonal projection | LayerNorm projects onto the hyperplane orthogonal to the all-ones vector | [ACL Findings 2023](https://aclanthology.org/2023.findings-acl.895/) |
| 6.4 | Gram-Schmidt, QR | QR is the production least-squares algorithm | Muon orthogonalises momentum by Newton-Schulz | [Jordan 2024](https://kellerjordan.github.io/posts/muon/) |
| 6.5 | Least squares | Closed-form regression; ridge is regularised normal equations | Frozen features plus one linear layer is the linear probe | [arXiv:1610.01644](https://arxiv.org/abs/1610.01644) |
| 7.1, 7.4-7.5 | Spectral theorem, SVD, PCA | Eckart-Young: truncated SVD is the provably best rank-k approximation | PiSSA initialises LoRA from principal singular vectors; SVD-LLM compresses | [arXiv:2404.02948](https://arxiv.org/abs/2404.02948) |

---

## 1. Systems and row reduction, §1.1-1.2

**Payoff.** The normal equations `XᵀX w = Xᵀy` are a square linear system, which is what
`sklearn.linear_model.LinearRegression` solves. Gaussian elimination lives inside every dense
solver: `torch.linalg.solve` is documented as `lu_factor()` followed by `lu_solve()`, and LU
*is* row reduction with the multipliers saved. Consistency and pivot positions are the
definition of rank, which carries all the way to LoRA.

**The line.** `w = torch.linalg.solve(X.T @ X, X.T @ y)`.

**What breaks.** Without pivoting, elimination divides by a zero or tiny pivot and the answer
is garbage. Without the pivot theory you cannot say why XᵀX goes singular under collinear
features, which scikit-learn states plainly: "the design matrix becomes close to singular and
as a result, the least-squares estimate becomes highly sensitive to random errors"
([sklearn](https://scikit-learn.org/stable/modules/linear_model.html)).

**The honest framing for an engineer.** Row reduction is the algorithm you never call and the
theory you use constantly.

## 2. Vector equations, span, Ax = b, §1.3-1.5

**Payoff.** A token embedding is a vector in R^d and the embedding matrix is a list of V of
them, so lookup is a one-hot times a matrix: `E[token_id] == one_hot(token_id) @ E`. "Is b in
Span{a1..an}" is the representability question: can this read-out express the target at all.
Underdetermined systems, solution equals particular plus null space, are the geometry of
over-parameterised networks where many weight settings fit equally well.

**The line.** `nn.Linear` computes `y = xAᵀ + b`
([PyTorch](https://docs.pytorch.org/docs/stable/generated/torch.nn.Linear.html)). Solution set
`x = x_p + x_h` with `x_h ∈ Nul A`.

**What breaks.** If the target direction is not in the span of the read-out's columns, no
amount of training finds it and the residual is a hard floor. And without `x_p + Nul A`, "many
different weight vectors fit" reads as a bug rather than the defining property of the regime.

**LLM instance.** The linear representation hypothesis: high-level concepts are represented as
*directions* in activation space
([Park, Choe & Veitch](https://arxiv.org/abs/2311.03658)), which is what linear probes test
([Alain & Bengio](https://arxiv.org/abs/1610.01644)).

## 3. Linear independence, §1.7

**Payoff.** Multicollinearity, redundant features, rank-deficient design matrices where the
OLS solution is not unique, and dimensional collapse in representation learning.

**The line.** Columns of X dependent means `Nul X != {0}` means `rank X < n` means XᵀX
singular. Diagnose with `np.linalg.matrix_rank(X)` against `X.shape[1]`, or count near-zero
singular values in `np.linalg.svd(X)[1]`.

**What breaks.** Ridge exists to fix exactly this: `min ‖Xw − y‖² + α‖w‖²` makes "the
coefficients more robust to collinearity"
([sklearn](https://scikit-learn.org/stable/modules/linear_model.html)).

**LLM instance.** Contrastive self-supervised embeddings "only span a lower-dimensional
subspace" instead of the full space, diagnosed through the singular-value spectrum of the
embedding covariance ([Jing, Vincent, LeCun & Tian](https://arxiv.org/abs/2110.09348)). The
LLM cousin is anisotropy, item 12.

## 4. Linear transformations, §1.8-1.9

**Payoff.** Every `nn.Linear` is the matrix of a linear transformation, standard-basis columns
and all. Attention's Q, K and V projections are three learned linear maps on the same input.
Composition of layers is a matrix product.

**The line.** `Q = X W^Q`, `K = X W^K`, `V = X W^V`, then
`Attention(Q,K,V) = softmax(QKᵀ/√d_k) V`, equation 1 of
[Vaswani et al.](https://arxiv.org/abs/1706.03762).

**What breaks.** `W₂(W₁x) = (W₂W₁)x`. A stack of L linear layers with no nonlinearity
collapses to a single matrix, so depth buys literally nothing in expressivity. That one fact,
a direct consequence of §1.9, is the entire justification for ReLU, GELU and SwiGLU.

**LLM instance.** Without skip connections and MLPs, pure self-attention output "converges
doubly exponentially to a rank-1 matrix"
([Dong, Cordonnier & Loukas](https://arxiv.org/abs/2103.03404)). That is §1.9 composition plus
§2.9 rank, stated as a theorem about GPT-shaped models.

## 5. Matrix operations and the inverse, §2.1-2.3

**Payoff.** The textbook OLS formula uses (XᵀX)⁻¹, and the engineering rule is that you never
form it. Invertible means information-preserving, which is the defining requirement of
normalizing flows. The Invertible Matrix Theorem is the single statement tying rank, null
space, determinant and eigenvalue zero together, and every later topic is a corollary.

**The line.** Not `np.linalg.inv(X.T @ X) @ X.T @ y`. Instead
`w, res, rank, sv = np.linalg.lstsq(X, y, rcond=None)`, which minimises the residual via SVD
and hands back the rank and singular values so conditioning is visible
([NumPy](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html)).

**What breaks.** Explicit inversion is slower and numerically worse than a solve, and it
explodes silently when XᵀX is near-singular. For flows, a non-invertible transform makes the
density undefined.

## 6. Subspaces, column space, null space, rank, §2.8-2.9

**This is the highest-leverage section in Block 1 for LLM work.**

**Payoff.** LoRA constrains fine-tuning updates to a rank-r subspace. Intrinsic dimensionality
measures how many parameters a task actually needs. Head size caps the rank of the attention
matrix. Rank collapses with depth.

**The line.** LoRA freezes W₀ and learns `ΔW = BA` with B in R^{d×r}, A in R^{r×k}, r much
smaller than min(d,k), so `h = W₀x + BAx` and `rank(ΔW) ≤ r`. Reported: up to 10,000 times
fewer trainable parameters than full fine-tuning of GPT-3 175B with Adam, and three times less
GPU memory, at on-par or better quality ([Hu et al.](https://arxiv.org/abs/2106.09685)).

**What breaks.** Without knowing that `rank(BA) ≤ r`, LoRA's premise is an unfalsifiable
slogan. Without knowing that column-space dimension caps expressivity, the attention
bottleneck is invisible: the standard scaling between head count and head size "gives rise to
a low-rank bottleneck in attention heads"
([Bhojanapalli et al.](https://arxiv.org/abs/2002.07028)).

**LLM instances.** Tuning about 200 randomly-projected parameters recovers 90 per cent of full
fine-tuning on MRPC, and larger models have *lower* intrinsic dimension
([Aghajanyan, Zettlemoyer & Gupta](https://arxiv.org/abs/2012.13255)). Rank-nullity,
`rank A + dim Nul A = n`, is what makes "rank at most r" mean "the update can only move within
an r-dimensional column space".

## 7. Determinants, §3.1-3.2

**Payoff.** |det A| is the volume scaling factor, which is why it appears in change of
variables. The log-det Jacobian is a term in every flow likelihood. `log det Σ` appears in the
multivariate Gaussian log-likelihood, computed through Cholesky rather than cofactors.

**The line.** `log p(x) = log π(z) − log |det J_f(z)|`
([Rezende & Mohamed](https://arxiv.org/abs/1505.05770)). With `Σ = LLᵀ`,
`logdet = 2 * torch.log(torch.diag(L)).sum()`, because the determinant of a triangular matrix
is the product of its diagonal.

**What breaks.** A naive determinant costs O(D³) per step. RealNVP's coupling layers make the
Jacobian triangular so the log-det is a sum of diagonal entries and costs nothing
([Dinh, Sohl-Dickstein & Bengio](https://arxiv.org/abs/1605.08803)). Without the log-det term
you are not maximising a likelihood; the model cheats by shrinking volume.

**Be honest here.** Determinants are peripheral to transformer LLMs, which are not density
models in the flow sense. Say so rather than inventing a link. The real connection is that
log-det is how any exact-likelihood generative model pays for the volume it moves, and the LLM
answer is a *different* trick for the same problem: the autoregressive factorisation
`log p(x) = Σ log p(xᵢ | x_<i)` avoids the Jacobian entirely.

## 8. Eigenvectors and diagonalisation, §5.1-5.3

**Payoff.** PCA is the eigendecomposition of the covariance. Power iteration is repeated
multiplication converging to the dominant eigenvector, which is PageRank and also spectral
normalisation. The Hessian spectrum diagnoses what optimisation is doing. The condition number
governs convergence.

**The line.** `Σ = (1/n)XᵀX`, then `Σv = λv`. Gradient descent on a quadratic with optimal
step satisfies `‖x_k − x*‖ ≤ ((κ−1)/(κ+1))^k ‖x₀ − x*‖` with `κ = λmax/λmin`
([CMU 10-725](https://www.stat.cmu.edu/~ryantibs/convexopt/lectures/grad-descent.pdf)).

**What breaks.** Large κ means a long thin valley and gradient descent zig-zags, with progress
per step approaching zero. In recurrent networks, when eigenvalues of the recurrent matrix
"deviate from absolute value 1, optimization becomes difficult due to vanishing and exploding
gradients" ([Arjovsky, Shah & Bengio](https://arxiv.org/abs/1511.06464); analysis and gradient
clipping in [Pascanu, Mikolov & Bengio](https://arxiv.org/abs/1211.5063)).

**LLM instance.** Measuring the full Hessian eigenvalue density during training shows "the
rapid appearance of large isolated eigenvalues in the spectrum along with a surprising
concentration of the gradient in the corresponding eigenspaces" in non-normalised networks,
and normalisation largely removes both
([Ghorbani, Krishnan & Xiao](https://arxiv.org/abs/1901.10159)). That is the mechanistic reason
LayerNorm makes deep transformers trainable: it conditions the optimisation problem.

## 9. Inner product, orthogonal sets, projection, §6.1-6.3

**Payoff.** Cosine similarity is the retrieval metric of every vector database. Dot-product
attention is an inner product between every query and every key. Orthogonal projection is the
geometry of least squares. LayerNorm is literally a projection. Gram matrices carry kernel
methods.

**The line.** `cos(u,v) = ⟨u,v⟩ / (‖u‖‖v‖)`. Attention scores `S = QKᵀ/√d_k`. Projection onto
an orthonormal basis: `ŷ = Σ ⟨y,uᵢ⟩ uᵢ`, with `y − ŷ` orthogonal to W.

**What breaks, twice.** *Scale*: Vaswani's own footnote assumes components of q and k are
independent with mean 0 and variance 1, so `q·k` has variance `d_k`; for large `d_k` "the dot
products grow large in magnitude, pushing the softmax function into regions where it has
extremely small gradients", hence `1/√d_k`
([Vaswani et al.](https://arxiv.org/abs/1706.03762)). Drop it and attention saturates.
*Geometry*: without orthogonality, cosine similarity in an anisotropic space is dominated by a
shared mean direction and everything looks similar to everything.

**LLM instance, the cleanest bridge in the whole block.** LayerNorm decomposes into exactly
two geometric operations: "(a) projection of the input vectors to a d−1 space that is
orthogonal to the [1,1,…,1] vector, and (b) scaling of all vectors to the same norm of √d",
and the projection is what lets attention form a query attending to all keys equally
([Brody, Alon & Yahav, Findings of ACL 2023](https://aclanthology.org/2023.findings-acl.895/)).
RMSNorm drops the re-centring half on the hypothesis that "re-centering invariance in
LayerNorm is dispensable" ([Zhang & Sennrich](https://arxiv.org/abs/1910.07467)), which is why
Llama-family models use it. Original: [Ba, Kiros & Hinton](https://arxiv.org/abs/1607.06450).

## 10. Gram-Schmidt and QR, §6.4

**Payoff.** QR is the production least-squares algorithm; LAPACK's `dgels` "solves
overdetermined or underdetermined real linear systems using a QR or LQ factorization".
Orthogonalisation appears inside modern optimisers. Krylov methods are Gram-Schmidt applied
to `{b, Ab, A²b, …}`.

**The line.** `A = QR`, so least squares becomes the triangular solve `Rx = Qᵀb` and XᵀX is
never formed. In PyTorch, `torch.linalg.lstsq(A, B, driver='gels')` selects the QR-based
driver.

**What breaks.** Classical Gram-Schmidt loses orthogonality catastrophically in floating
point, hence modified Gram-Schmidt and Householder QR. And forming the normal equations
instead of QR squares the condition number: `κ(XᵀX) = κ(X)²`.

**LLM instance.** Muon, "MomentUm Orthogonalized by Newton-Schulz", replaces the momentum
matrix with its nearest orthogonal matrix in Frobenius norm, setting all singular values to 1
while keeping the singular directions, approximated by a cheap Newton-Schulz iteration rather
than an exact SVD or QR. It applies only to 2D parameters; embeddings, the head and all
scalars stay on AdamW ([Jordan 2024](https://kellerjordan.github.io/posts/muon/)). Scaled to
LLM training in [arXiv:2502.16982](https://arxiv.org/pdf/2502.16982).

## 11. Least squares, §6.5

**Payoff.** The closed form of linear regression, what `sklearn.LinearRegression` wraps, the
linear probe, and ridge as regularised normal equations.

**The line.** `XᵀXŵ = Xᵀy`; ridge `ŵ = (XᵀX + αI)⁻¹Xᵀy`. The geometry:
`ŷ = proj_{Col X} y` and `y − ŷ ⊥ Col X`, which *is* the normal equations, since
`Xᵀ(y − Xŵ) = 0`.

**What breaks.** With collinear columns the coefficients swing wildly under tiny target noise.
The `αI` in ridge lifts every eigenvalue of XᵀX by α, bounding the condition number. That is
*why* ridge stabilises, and it is a §5 eigenvalue argument wearing a §6.5 costume.

**LLM instance.** Frozen features plus a last layer is the entire linear-probing methodology
for asking what a model knows at layer ℓ. Probes trained "entirely independently of the model
itself" show linear separability rising monotonically with depth
([Alain & Bengio](https://arxiv.org/abs/1610.01644)).

## 12. Spectral theorem, SVD, PCA, §7.1, §7.4-7.5

**This is the payoff section.**

**Payoff.** Eckart-Young says truncated SVD is the *provably best* rank-k approximation, which
licenses every low-rank compression. The pseudo-inverse `A⁺ = VΣ⁺Uᵀ` is how `lstsq` solves
rank-deficient systems. Whitening, latent semantic analysis, spectral norm as a layer's
Lipschitz constant, and embedding anisotropy all live here.

**The line.** `A = UΣVᵀ`, truncated to `A_k = U_k Σ_k V_kᵀ`. Spectral theorem: a symmetric A
is orthogonally diagonalisable, `A = PDPᵀ` with P orthogonal, which is exactly why PCA on the
symmetric covariance has real eigenvalues and orthogonal principal directions. Spectral
normalisation divides each weight by its largest singular value, estimated by power iteration
([Miyato et al.](https://arxiv.org/abs/1802.05957)).

**What breaks.** Without Eckart-Young there is no reason to believe truncating small singular
values is the *right* compression rather than one heuristic among many. Without the
pseudo-inverse, rank-deficient least squares has no canonical answer.

**LLM instances, four live ones.** PiSSA initialises LoRA's A and B from the *principal*
singular vectors of W and reports faster convergence and better accuracy at identical setup
([Meng et al.](https://arxiv.org/abs/2404.02948)). SVD-LLM does post-training compression with
"truncation-aware data whitening to ensure a direct mapping between singular values and
compression loss" ([Wang et al.](https://arxiv.org/abs/2403.07378)). Contextual
representations are "highly anisotropic, confined to a narrow cone" in every layer
([Ethayarajh](https://arxiv.org/abs/1909.00512)), and the classic fix, All-but-the-Top,
removes the common mean vector and the top principal directions
([Mu, Bhat & Viswanath](https://arxiv.org/abs/1702.01417)). That postprocessing is PCA used as
a subtraction, and it is why retrieval pipelines often centre embeddings before cosine.

---

## 13. Cross-cutting stories

**Attention is a chain of matrix products.** `softmax(QKᵀ/√d_k)V`. `QKᵀ` is an all-pairs inner
product from §6.1, the softmax is the only nonlinearity, and multiplying by V produces a
convex combination of value vectors, so the output lies in the **column space of V**, §2.8.
The `√d_k` is a variance argument you can derive on a napkin.

**Embeddings have linear structure.** "Each relationship is characterized by a
relation-specific vector offset", giving king minus man plus woman approximately queen
([Mikolov, Yih & Zweig](https://aclanthology.org/N13-1090/)). That is §1.3 vector arithmetic
making an empirical claim about meaning.

**Gradient descent geometry.** The gradient is steepest ascent **with respect to the Euclidean
inner product**. Change the inner product to `⟨u,v⟩_P = uᵀPv` and steepest descent becomes
`P⁻¹∇f`, which is exactly what preconditioning is, and why Adam with a diagonal P, Shampoo and
Muon are the same algorithm in different geometries. Note the §6.7 idea underneath: choosing a
different inner product changes all the geometry, and Park, Choe and Veitch identify a *causal
inner product* under which cosine similarity becomes meaningful for concepts
([arXiv:2311.03658](https://arxiv.org/abs/2311.03658)).

**Weight tying.** The output projection is itself a valid word embedding, so tie it to the
input embedding: `logits = h Eᵀ` reuses the matrix from §1.4. Tying reduces model size and
improves perplexity ([Press & Wolf](https://arxiv.org/abs/1608.05859)).

**RoPE is rotations, and rotations are orthogonal matrices.** RoPE "encodes the absolute
position with a rotation matrix and meanwhile incorporates the explicit relative position
dependency in self-attention formulation", partitioning the head dimension into d/2
two-dimensional subspaces and applying a position-dependent 2×2 rotation to each
([Su et al.](https://arxiv.org/abs/2104.09864)). Because rotations preserve norms and inner
products, `⟨R_m q, R_n k⟩` depends only on m − n, which gives relative position for free. That
is §6.2 orthogonality doing load-bearing work in a model he uses daily.
