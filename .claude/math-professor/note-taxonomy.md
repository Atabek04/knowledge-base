# Note taxonomy

Seven note types for mathematics, each with a template and a filled example. All obey
`CLAUDE.md`: statement titles, no `#` heading, only `###` and `####` inside, short
paragraphs, highlights before a note is done, `### Read more` with full titles, two or more
links, no fake links.

Notes are written **when a section closes**, not when a chunk closes. At 30 minutes a day the
write-before-advance gate consumes the session.

---

## 1. Principles

**A note is a claim, not a topic.** Evergreen notes should be atomic, concept-oriented and
densely linked, where atomic means "notes which are only about one thing, but which, as much
as possible, capture the entirety of that thing"
([Matuschak](https://notes.andymatuschak.org/zNUaiGAXp21eorsER1Jm9yU)). His other note,
*evergreen note titles are like APIs*, is why this vault demands statement titles: a title is
the interface other notes call. A label like "orthogonal projection" tells a caller nothing.

**Concept-orientation, not source-orientation.** Factor by concept "rather than by author,
book, event, project, topic"
([Matuschak](https://notes.andymatuschak.org/z2hQEhqWkdRLL9JUwfawZZx)). For a textbook-driven
learner this is the hardest discipline, because the temptation is one note per Lay section.
Resist it. Lay §6.2 alone contains at least four separable claims.

**Write for a reader who has lost the context.** Ahrens: write each note "as if you were
writing for someone else". Luhmann's framing is stronger: the slip-box is a communication
partner, and "one of the most basic presuppositions of communication is that the partners can
mutually surprise each other"
([Luhmann](https://luhmann.surge.sh/communicating-with-slip-boxes)). A note that only parses
with today's working memory loaded cannot surprise him in 2028.

**The forcing question is the title.** Nielsen's method for seeing through a piece of
mathematics ends at a single question of the form *"in one sentence, what is the core reason
X holds?"*, and that one-sentence answer **is** the note title
([Nielsen](https://cognitivemedium.com/srs-mathematics);
[Matuschak's gloss](https://notes.andymatuschak.org/zJGFwgcC4YLRt6K2vVDFEvR)). If he cannot
write the forcing-question answer, there is no note yet, only a transcription.

**One note per idea, not one note per theorem.** This is where every published mathematics
zettelkasten converged
([Holmes](https://mildobsessions.com/thoughts-on-using-the-zettelkasten-method-for-mathematics-notes/);
[Obsidian forum](https://forum.obsidian.md/t/how-use-obsidian-with-mathematics-at-the-university-zettelkasten-and-or-anything-else/90472);
[Murari](https://mathonelist.substack.com/p/how-i-take-math-notes-in-obsidian)). A theorem
that restates a definition earns no note. A theorem carrying three separable insights earns
three. Proofs are compressed to a few sentences, with links carrying the supporting steps.

**Halmos, for exposition.** Say something, speak to someone, organise, and **write in
spirals**: write one, write two, rewrite one, rewrite two
([*How to Write Mathematics*](https://sites.math.washington.edu/~lind/Resources/Halmos.pdf)).
"Saying a lot about nothing is worse than having nothing to say." The spiral rule is the
licence to deepen an existing note when a later chapter revisits a concept, rather than
creating a near-duplicate.

**Two rules govern every type below.**

- If you cannot write the title as a sentence you would defend, the thing is not understood well enough to note. That is Halmos's "say something" applied to filenames.
- A theorem note and a concept note never carry the same explanation. Gloss and link.

---

## 2. The taxonomy

| Type | What it holds | Title pattern | Create when | Example from Lay Ch 1-7 |
|---|---|---|---|---|
| **Concept** | One definition, plus why it is worded that way and what it buys | `<Object> is <defining property> so <what it buys>` | The term recurs across chapters and other notes will lean on it | *A subspace is a subset closed under addition and scaling so linear algebra still works inside it* |
| **Theorem** | One claim, its hypotheses, a compressed proof *idea* | `<Hypothesis> implies <conclusion>` | The result is used elsewhere, or its idea is reusable | *An n by n matrix is invertible exactly when its columns are linearly independent* |
| **Worked technique** | A procedure, its invariant, when it applies, its failure mode | `<Technique> <does what> by <mechanism>` | He could be asked to *execute* it, not just state it | *Gram-Schmidt builds an orthogonal basis by subtracting each vector's projection onto the span so far* |
| **Formula** | A symbolic identity that encodes an idea | `<Formula in words> means <what it computes>` | Not re-derivable in ten seconds, and the symbols carry meaning | *The normal equations turn least squares into a solvable square system by projecting b onto the column space* |
| **Counterexample** | One object refuting a tempting generalisation | `<Object> shows that <tempting claim> is false` | He, or the book, almost believed the false claim | *A shear matrix shows that determinant one does not mean the transformation is a rotation* |
| **Intuition** | The geometric story in words, plus a figure | `<Concept> is <the picture>` | The formal note is correct but he cannot see it | *Matrix multiplication is composing two transformations so the columns record where the basis vectors land* |
| **Math to ML** | The payoff in one sentence, naming the exact algorithm | `<Math object> is what makes <ML thing> work because <mechanism>` | A math note has a named downstream use | *The singular value decomposition is what makes PCA work because its right singular vectors diagonalize the covariance matrix* |

**Formula notes are the type to be strict about.** `(AB)ᵀ = BᵀAᵀ` earns no note; it is
re-derivable in seconds and its whole content is "order reverses". The normal equations do
earn one. The governing rule inside a formula note: **state what each symbol *does*, not just
what it is.** "A is the design matrix" is a label. "A's columns span every prediction the
model can produce" is a job description.

**Counterexample notes are the highest-value type.** Refuting "every member of A is a member
of B" needs a *single object*, and that asymmetry is the value
([Gelbaum & Olmsted](https://faculty.ksu.edu.sa/sites/default/files/_olmsted_1.pdf)). Always
record **which hypothesis the counterexample forces into the theorem**; that is Lakatos's
lemma-incorporation done in the vault
([*Proofs and Refutations*](https://classes.matthewjbrown.net/teaching-files/hps/lakatos.pdf)).

---

## 3. Templates

### Concept

```markdown
---
aliases: [subspace, linear subspace]
tags: [linear-algebra, concept, lay-ch2]
---

Linear algebra keeps asking whether a set of vectors is closed enough that the
usual operations stay inside it. A subspace is the name for that guarantee.

### The definition and why it is worded this way

<mark style="background: #FFF3A3A6;">A subspace $H$ of a vector space $V$ is a subset that contains the zero
vector and is closed under addition and scalar multiplication.</mark>

Only two closure conditions appear because those are the two operations a
vector space has. Closing under both means every linear combination of vectors
in $H$ stays in $H$, so $H$ is itself a vector space, for free.

#### Why zero is listed separately

The empty set is closed under both operations vacuously. Requiring
$\mathbf{0} \in H$ rules it out, and it is the cheapest non-emptiness test.

---

### What the definition buys

Every theorem proved about vector spaces applies verbatim inside a subspace.
Verify two closure properties, inherit a theory.

### The common mistake

<mark style="background: #FF5582A6;">A subspace must pass through the origin.</mark> A line in $\mathbb{R}^2$
missing the origin is closed under nothing.

### Read more

- [[Full title of the null-space and column-space note]]
- [[Full title of the affine-line counterexample note]]
- [[Linear Algebra MOC]]
```

### Theorem

```markdown
---
aliases: [invertible matrix theorem, IMT]
tags: [linear-algebra, theorem, lay-ch2]
---

Lay accumulates a long list of conditions that all turn out to be one condition.
This note keeps the single idea that collapses the list.

### The claim

<mark style="background: #FFF3A3A6;">For a square $n \times n$ matrix $A$, invertibility, linear independence of
the columns, and a pivot in all $n$ columns are the same statement.</mark>

$$A \text{ invertible} \iff A\mathbf{x} = \mathbf{0} \text{ has only } \mathbf{x} = \mathbf{0}$$

---

### The one-sentence reason

Row reduction cannot create or destroy solutions of $A\mathbf{x} = \mathbf{0}$,
so "$n$ pivots", "no free variables" and "only the trivial solution" are three
descriptions of one echelon form.

#### Why squareness is load-bearing

With $m \neq n$ the pivot count maxes out in one direction only. A $3 \times 2$
matrix can have independent columns and still not be invertible; it has no
inverse to have. <mark style="background: #FF5582A6;">Never apply this to a non-square matrix.</mark>

### Read more

- [[Full title of the determinant test note]]
- [[Full title of the row-reduction preserves solutions note]]
- [[Linear Algebra MOC]]
```

### Worked technique

```markdown
---
aliases: [Gram-Schmidt, Gram-Schmidt process]
tags: [linear-algebra, technique, lay-ch6]
---

Given any basis of a subspace you often want an orthogonal one instead, because
orthogonal bases make coordinates computable by dot products alone.

### The procedure

$$\mathbf{v}_k = \mathbf{x}_k - \sum_{j<k} \frac{\mathbf{x}_k \cdot \mathbf{v}_j}{\mathbf{v}_j \cdot \mathbf{v}_j}\,\mathbf{v}_j$$

Each step subtracts [[Full title of the projection note|the projection onto everything built so far]], leaving only the genuinely new direction.

---

### The invariant

<mark style="background: #ABF7F7A6;">After step $k$, the span of $\mathbf{v}_1 \dots \mathbf{v}_k$ equals the span
of $\mathbf{x}_1 \dots \mathbf{x}_k$, and the $\mathbf{v}$'s are mutually
orthogonal.</mark>

That invariant is the whole correctness argument.

---

### When it applies, and how it fails

Any linearly independent set in an inner product space.

<mark style="background: #FF5582A6;">If the inputs are dependent, some $\mathbf{v}_k$ comes out zero and the next
division is undefined.</mark> Numerically, classical Gram-Schmidt also loses
orthogonality on near-dependent inputs, which is why libraries use Householder QR.

### Read more

- [[Full title of the projection note]]
- [[Full title of the QR factorization note]]
- [[Linear Algebra MOC]]
```

### Formula

```markdown
---
aliases: [normal equations, least squares equations]
tags: [linear-algebra, formula, lay-ch6]
---

When $A\mathbf{x} = \mathbf{b}$ has no solution you still want the best available
$\mathbf{x}$. The normal equations are the algebraic form of "best".

### The formula

$$A^{\mathsf{T}}A\,\hat{\mathbf{x}} = A^{\mathsf{T}}\mathbf{b}$$

What each symbol does:

- $A$ spans every output the model can produce, its column space.
- $\mathbf{b}$ is the target, generally sitting outside that span.
- $A^{\mathsf{T}}$ reports a vector's dot product with each column, so multiplying
  by it says every column is orthogonal to the residual.
- $\hat{\mathbf{x}}$ holds the coordinates of the projection, not of $\mathbf{b}$.

---

### The idea it encodes

<mark style="background: #ABF7F7A6;">Multiplying by $A^{\mathsf{T}}$ replaces an unsolvable tall system with a
solvable square one, and the replacement is exactly projection onto the column
space.</mark>

#### Why not just invert

<mark style="background: #FF5582A6;">$A^{\mathsf{T}}A$ is invertible only when $A$ has independent columns.</mark>
With collinear features it is singular, which is multicollinearity wearing a
linear-algebra costume.

### Read more

- [[Full title of the projection note]]
- [[Full title of the least-squares-is-projection ML note]]
- [[Linear Algebra MOC]]
```

### Counterexample

```markdown
---
aliases: [shear determinant one, area preserving not rotation]
tags: [linear-algebra, counterexample, lay-ch3]
---

Once you learn that the determinant measures area scaling, it is tempting to
conclude that determinant one means the transformation is rigid. It does not.

### The tempting claim

"If $\det A = 1$ then $A$ preserves lengths and angles, so $A$ is a rotation."

### The object that refutes it

$$A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}, \qquad \det A = 1$$

This shear sends $(0,1)$ to $(1,1)$. Area is preserved, but that vector's length
went from $1$ to $\sqrt{2}$ and the angle between the basis vectors collapsed
from ninety degrees to forty-five.

---

### Which hypothesis this forces in

<mark style="background: #FF5582A6;">Area preservation is strictly weaker than length preservation.</mark> To get a
rotation you must add orthogonality of the columns, $A^{\mathsf{T}}A = I$, not
merely $\det A = 1$.

### What it fixes about the mental picture

The determinant sees one number. It cannot distinguish a square from a
parallelogram of equal area, so the area picture is genuinely incomplete rather
than merely informal.

### Read more

- [[Full title of the determinant-as-area note]]
- [[Full title of the orthogonal matrix note]]
- [[Linear Algebra MOC]]
```

### Intuition

```markdown
---
aliases: [matrix multiplication as composition, matrices transform space]
tags: [linear-algebra, intuition, lay-ch2]
---

The grid-of-numbers definition of matrix multiplication is unmemorable because it
describes the bookkeeping rather than the act. Here is the act.

### The picture

<mark style="background: #FFF3A3A6;">A matrix is a transformation of space, and its columns record where the basis
vectors land.</mark>

Whatever the transformation does to the whole plane is fully determined by where
$\mathbf{e}_1$ and $\mathbf{e}_2$ end up, because every other vector is a
combination of them and the transformation respects combinations.

![[matrix-as-transformation.png]]

---

### Why the multiplication rule looks like that

$AB$ means apply $B$, then apply $A$. Column $j$ of $AB$ is where $B$ sends
$\mathbf{e}_j$, pushed through $A$. The row-times-column sum is that sentence in
coordinates.

#### The immediate payoff

Non-commutativity stops being a rule to memorise. Rotating then shearing is
visibly not shearing then rotating, and the algebra had no choice.

---

### Where this picture stops

<mark style="background: #FF5582A6;">It is honest only for square matrices over $\mathbb{R}^2$ or $\mathbb{R}^3$.</mark>
A $3 \times 5$ matrix still composes, but "where the basis vectors land" lands
them in a different space.

### Read more

- [[Full title of the composition-of-transformations note]]
- [[Full title of the determinant-as-area note]]
- [[Linear Algebra MOC]]
```

### Math to ML

```markdown
---
aliases: [SVD and PCA, why PCA uses SVD]
tags: [linear-algebra, ml-payoff, lay-ch7]
---

Lay introduces the singular value decomposition as the factorization that works
for every matrix, then applies it to statistics in the same chapter. This note
names that application precisely.

### The payoff in one sentence

<mark style="background: #ABF7F7A6;">The SVD is what makes PCA computable, because the right singular vectors of a
mean-centred data matrix are exactly the eigenvectors of its covariance matrix.</mark>

### The exact correspondence

For mean-centred $X$ with $X = U\Sigma V^{\mathsf{T}}$:

$$\frac{1}{n-1}X^{\mathsf{T}}X = \frac{1}{n-1}V\Sigma^{2}V^{\mathsf{T}}$$

- Columns of $V$ are the principal component directions.
- $\sigma_i^2/(n-1)$ is the variance explained by component $i$.
- Columns of $U\Sigma$ are the scores, the data in the new coordinates.

---

### Why it is done this way in practice

Forming $X^{\mathsf{T}}X$ squares the condition number, so scikit-learn's `PCA`
runs an SVD on $X$ directly and never builds the covariance matrix.
<mark style="background: #FF5582A6;">Skipping mean-centring makes the first component point at the data's mean
rather than its direction of greatest variance.</mark>

### Read more

- [[Full title of the singular values note]]
- [[Full title of the spectral theorem note]]
- [[Linear Algebra MOC]]
```

**Connection notes link both directions.** The SVD note's `### Read more` gains the ML note.
That reciprocity is what makes the payoff discoverable from the math side, which is where he
will be sitting when he needs it.

---

## 4. MOC structure

Three patterns exist in the wild: by textbook chapter, by concept dependency, and by question
([Obsidian forum](https://forum.obsidian.md/t/how-use-obsidian-with-mathematics-at-the-university-zettelkasten-and-or-anything-else/90472);
[mathwiki's typed links](https://github.com/zhaoshenzhai/mathwiki);
[problem dossiers](https://forum.zettelkasten.de/discussion/1946/using-a-zettelkasten-in-mathematics-research)).

**Use chapter order as the spine, with dependency carried by inline links rather than a
hand-maintained graph.** Luhmann's objection to content-based order, that it binds you to one
arrangement for decades, targets the *storage* layer; here storage is a flat folder plus
links, so the MOC is a reading path, not a filing system. A learner walking Lay linearly needs
a linear index. A prerequisite graph is the theoretically correct structure and the wrong
deliverable: expensive to maintain, duplicating what inline links already encode, and rendered
for free by backlinks and the graph view.

Two cross-cutting sections earn their place because chapter order cannot show them:
**Counterexamples and boundaries**, and **ML payoffs**. Those are the two axes a
doctorate-bound engineer queries most.

The MOC ends with a four-line **Teaching Progress** marker: last taught with a date, next,
blocked on, open loop. It lives in the MOC rather than the skill, so it sits next to the
roadmap it indexes and survives across sessions.

**MOC bullet rule, from `CLAUDE.md`.** Each bullet is exactly one link and the alias is a
compressed teaching statement, not a name. Nothing after the closing brackets. Pending topics
with no note stay as plain checkbox text with no link, and the checkbox is replaced by a link
only once the note exists.

---

## 4b. Notation

Maths is MathJax, never ASCII in a code fence. `$inline$` and `$$block$$` render natively.
Align a system on its operators and equals sign so a missing term leaves a visible gap; that
gap is what makes the augmented matrix obvious later. Use `\mathbb{R}` inside maths and a
plain ℝ in prose.

<mark style="background: #FF5582A6;">In flashcards `$...$` does not render.</mark> The sync
script runs card text through Markdown, which strips the backslashes, and Anki does not read
`$`. Wrap card maths in a raw `<div>` block, which Markdown passes through untouched. Full
rules are in `CLAUDE.md`.

---

## 5. Figures

Figures are matplotlib PNGs written into `Assets/` by a script that lives beside the note.
The figure should **compute** the mathematics rather than illustrate it: a projection figure
that calls `A @ np.linalg.solve(A.T@A, A.T@y)` is the theorem rendered, and a wrong picture
becomes a failing script rather than a subtly misleading drawing. For §6.3, §6.4, §6.5 and
§7.4 the figure and the theorem check each other.

Three constraints. Use a transparent background and light strokes, because the vault runs a
dark theme. Give every figure a descriptive filename and alt text stating its claim, because
PNGs are opaque to search and to the graph view. And prefer a PNG over any plugin-rendered
block, because notes must survive export to Anki.
