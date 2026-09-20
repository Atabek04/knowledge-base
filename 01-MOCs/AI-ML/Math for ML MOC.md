---
created: 2026-01-31
tags: [moc]
---

Mathematical foundations essential for understanding machine learning algorithms.
Covers linear algebra for data representation, calculus for optimization, probability for uncertainty, and discrete math for algorithmic thinking.
Linear algebra is taught from Lay. The worked notes live below; the full chapter roadmap and its checkbox spine live in the child MOC. The calculus, probability and discrete sections are still an outline of Jon Krohn's course, not a note index.

## Linear Algebra

Worked from Lay, 5th edition, section by section, with the `math-professor` skill.
Teaching progress is tracked here, per section; the chapter roadmap lives in the child MOC.

- [[Linear Algebra MOC|Linear Algebra — the full Lay roadmap, Ch 1, 2, 3, 5, 6, 7]]

### Systems of Linear Equations

> **Teaching progress — 2026-09-09:** §1.1 read to p. 26, all 16 notes written and carded. Next: work the Practice Problems on p. 26, then §1.1's exercises, then §1.2 echelon form.

- [[An equation is linear when every variable stands alone to the first power and is multiplied only by a constant|Linear equation — variable alone, first power, times a constant]]
    - [[Each family of nonlinear equation breaks exactly one criterion of linearity|Nonlinear families — each breaks one criterion of linearity]]
    - [[Subscript notation lets one formula describe any number of unknowns|Subscripts — one formula for any number of unknowns]]
- [[The number of variables sets the dimension and each equation draws a shape one dimension lower|Variables set the dimension, each equation drops one]]
- [[Solving a linear system means finding where the shapes its equations draw intersect|Solving — find where all the equations' shapes intersect]]
    - [[A linear system has zero, one, or infinitely many solutions and never any other count|Solution counts — zero, one, or infinitely many, never other]]
- [[Elimination replaces an equation, so solving a system means rewriting it|Elimination is rewriting — each step trades one system for another]]
    - [[Two true equations can be added or subtracted side by side and stay true|Equals combined with equals: what licenses every elimination step]]
    - [[Deriving an equation prevents losing a solution but not gaining one|Derivation blocks losing a solution, never gaining one]]
- [[A rewrite is safe exactly when the move that produced it can be undone|Reversibility — a move you can undo changes no answers]]
    - [[The three row operations are legal precisely because each one can be undone|Three row operations — swap, scale, add, each reversible]]
- [[Two systems are equivalent when they have the same solution set|Equivalence — same solution set licenses every rewrite]]
- [[A matrix records a linear system's numbers, with column position replacing the variable names|Matrix notation — position replaces the variable names]]
    - [[Row equivalent matrices are linked by the route between them, since a matrix has no solution set to compare|Row equivalent — matrices linked by the moves, not the look]]
- [[Elimination clears one variable per column going down, then clears back up until each row names one variable|The algorithm — clear down the columns, then back up]]
    - [[Elimination runs in floating point on a computer, so every stored number is an approximation|Floating point — the machine's arithmetic is approximate, the theory is not]]
- [[Existence and uniqueness are the only two questions a linear system has to answer|Existence and uniqueness — the two questions that decide everything]]
    - [[A row reading zero equals a nonzero number proves the system is inconsistent|The 0 = nonzero row — instant proof of no solution]]

### Data Structures for ML

- Scalar: single numerical value representing a quantity
- Vector: one-dimensional array of scalars with both magnitude and direction
- Matrix: two-dimensional array of scalars arranged in rows and columns
- Tensor: n-dimensional generalization of matrices for higher-order data
- Norm: measure of vector magnitude or size in vector space
- Basis vectors: fundamental vectors that span a vector space
- Orthogonal vectors: vectors that are perpendicular with zero dot product
- Orthonormal vectors: orthogonal vectors with unit magnitude

### Tensor Operations

- Transposition: flipping matrix dimensions from rows×columns to columns×rows
- Element-wise arithmetic: adding or multiplying matrices element by element
- Hadamard product: element-wise multiplication of two matrices
- Dot product: scalar resulting from multiplying vector components and summing
- Linear systems: solving Ax = b equations using matrix operations
- Matrix-vector multiplication: transforming vectors by linear transformation

### Matrix Properties

- Frobenius norm: measure of matrix size using all elements
- Matrix multiplication: non-commutative operation combining two matrices
- Symmetric matrix: square matrix equal to its transpose
- Identity matrix: diagonal matrix with ones producing no transformation
- Matrix inversion: finding inverse matrix when solving Ax = b equations
- Diagonal matrix: matrix with values only on main diagonal
- Orthogonal matrix: square matrix with orthonormal columns

### Eigendecomposition

- Linear transformation: mapping vectors from one space to another
- Affine transformation: linear transformation plus translation
- Eigenvector: vector unchanged in direction under linear transformation
- Eigenvalue: scalar multiplier of eigenvector under transformation
- Determinant: scalar value describing volume change under transformation
- Eigenvalue decomposition: expressing matrix as product of eigenvector and eigenvalue matrices
- Diagonalization: transforming matrix into diagonal form using eigendecomposition
- Applications: simplifying computations, understanding geometric meaning

### Matrix Operations for ML

- Singular Value Decomposition (SVD): decomposing matrix into three components for dimensionality reduction
- Data compression: reducing storage using SVD for low-rank approximation
- Pseudoinverse: computing Moore-Penrose inverse for non-square matrices
- Regression: using matrix operations to solve least-squares problems
- Trace operator: sum of diagonal elements with applications in optimization
- Principal Component Analysis (PCA): finding principal vectors explaining data variance

### Where it shows up in an LLM

Each bullet pairs one linear-algebra idea with the exact place it runs inside a transformer. Fill in as the Lay track reaches the idea.

- [ ] Token embedding is a lookup row in a matrix: token id selects one vector of d_model numbers
- [ ] Vector arithmetic on embeddings: king minus man plus woman lands near queen, because meaning directions add
- [ ] A linear layer is matrix times vector: the weights are the matrix, the forward pass is a chain of them
- [ ] Dot product as similarity: attention scores are query dot key, big product means look here
- [ ] Attention as one matrix product: QK^T gives the whole token-by-token score table at once
- [ ] Softmax turns a score vector into a probability vector that sums to one
- [ ] Rank and low-rank approximation: LoRA fine-tunes by adding a rank-r product to a frozen weight matrix
- [ ] SVD and PCA compress and inspect activation spaces
- [ ] Output head: final vector times vocabulary matrix gives one logit per next token
- [ ] Norms and layer normalisation: rescaling a vector to unit size keeps activations stable
- [ ] Gradient is a vector and backprop is chain-rule matrix products (bridge to the Calculus section)

## Calculus

Mathematical tools for understanding change and optimization in continuous functions.

### Limits and Foundations

- Differential calculus: studying rates of change and instantaneous slopes
- Integral calculus: studying accumulation and area under curves
- Method of exhaustion: ancient technique for computing limits through approximation
- Infinitesimal: infinitely small but non-zero quantity
- Limit: value function approaches as input approaches a point
- Continuity: property of functions with no breaks or jumps
- Calculating limits: using algebraic manipulation and limit laws

### Derivatives and Differentiation

- Delta method: using small changes (deltas) to approximate derivative
- [[Derivative measures how fast something is changing at a specific point|Derivative: instantaneous rate of change at a point]]
- [[Slope measures how much y changes when x changes|Slope: how much y changes per x]]
- [[Tangent line touches curve at exactly one point and shows instantaneous slope|Tangent line: shows the instantaneous slope]]
- [[Two methods to find slope of a curve - calculation or visual estimation|Finding curve slope: calculation vs visual]]
- Derivative rules for constant: derivative of constant is zero
- Derivative rules for power: power rule for polynomial terms
- Derivative rules for sum: derivative of sum equals sum of derivatives
- Derivative rules for product: product rule for multiplied functions
- Derivative rules for quotient: quotient rule for divided functions
- Chain rule: derivative of composite functions
- Optimization: using derivatives to find minima and maxima
- Critical points: points where derivative is zero
- Second derivative test: determining local maxima and minima

### Automatic Differentiation

- Autodiff concept: computing derivatives efficiently through computational graphs
- Computational graph: directed graph representing function composition
- PyTorch implementation: automatic differentiation framework for tensor operations
- TensorFlow implementation: another autodiff framework for machine learning
- Forward mode autodiff: computing derivatives from inputs to outputs
- Reverse mode autodiff: computing derivatives from outputs to inputs (backpropagation)
- Gradient tape: recording operations for automatic differentiation

### Partial Derivatives and Gradients

- Partial derivative: derivative with respect to one variable holding others constant
- Multivariate chain rule: chain rule extended to multiple variables
- Gradient vector: vector of all partial derivatives
- Cost function: function measuring error or loss in optimization
- Gradient descent: iterative algorithm moving opposite to gradient for minimization
- Learning rate: step size controlling gradient descent updates
- Backpropagation: computing gradients through neural networks via chain rule
- Hessian matrix: matrix of all second partial derivatives

### Integral Calculus

- Integration: inverse operation of differentiation
- Indefinite integral: antiderivative without specific bounds
- Definite integral: integral between two bounds computing area
- Integration rules: power rule, logarithmic rule, exponential rule
- Numeric integration: approximating integrals when analytical solution unavailable
- Area under curve: geometric interpretation of definite integral
- Receiver Operating Characteristic (ROC): curve showing true positive vs false positive tradeoff
- Area Under Curve (AUC): metric for classifier performance

## Probability and Statistics

Tools for modeling uncertainty and making inferences from data.

### Probability Foundations

- Probability history: development from gambling to modern applications
- Event: possible outcome in sample space
- Sample space: set of all possible outcomes
- Independent observations: events unaffected by each other
- Combinatorics: counting principles for arrangements and selections
- Permutation: ordered arrangement of items
- Combination: unordered selection of items
- Conditional probability: probability of event given another event occurred
- Bayes' theorem: relating conditional probabilities of related events
- Joint probability: probability of two events both occurring
- Marginal probability: probability of one variable ignoring others

### Statistical Concepts

- Distribution: probability model describing random variable behavior
- Normal distribution: bell-shaped symmetric distribution
- Binomial distribution: distribution of binary outcomes over trials
- Uniform distribution: equal probability across range
- [[Mean is the sum of all values divided by the count|Mean: sum ÷ count, sensitive to outliers]]
- [[Median is the middle value when data is sorted|Median: middle of sorted data, robust to outliers]]
- Expected value: long-run average of random variable
- Variance: measure of spread from expected value
- Standard deviation: square root of variance
- Hypothesis testing: statistical test of claim about population
- Statistical inference: drawing conclusions about population from sample
- Confidence interval: range of values containing parameter with given confidence
- P-value: probability of observing data if null hypothesis true
- Type I error: rejecting true null hypothesis (false positive)
- Type II error: failing to reject false null hypothesis (false negative)

## Discrete Mathematics

Foundational concepts for algorithmic and logical thinking.

### Foundational Concepts

- Logic: study of valid reasoning and inference
- Proposition: statement that is either true or false
- Boolean operations: AND, OR, NOT operations on propositions
- Truth table: table showing all possible truth values
- Set theory: study of collections of objects
- Set operations: union, intersection, complement of sets
- Graph theory: study of networks of connected vertices and edges
- Vertex: node in a graph
- Edge: connection between vertices
- Combinatorics: counting and arrangements of discrete objects
- Algorithm: step-by-step procedure for solving a problem
- Algorithmic complexity: analyzing time and space requirements

## Related MOCs

- [[Machine Learning MOC]] — parent hub for all machine learning topics
- [[Math Foundations MOC]] — number systems, fractions and notation underneath all of this

## Practice

Spaced-repetition cards live under `05-Flashcards/math/`, deck root `Tech-KB::Math for ML`. Files: `calculus.md`, `probability.md`, and `linear-algebra.md` once Block 1 opens.

## External Resources

- [Mathematical Foundations of Machine Learning - Jon Krohn](https://www.jonkrohn.com/foundation)
- [Mathematics for Machine Learning - Deisenroth, Faisal, Ong](https://mml-book.github.io/)
- [3Blue1Brown Essence Series](https://www.3blue1brown.com/essence-of-algebra)
- [Khan Academy Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [Khan Academy Calculus](https://www.khanacademy.org/math/calculus-1)
- [Khan Academy Statistics and Probability](https://www.khanacademy.org/math/statistics-probability)
