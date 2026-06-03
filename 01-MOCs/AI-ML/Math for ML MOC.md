---
created: 2026-01-31
tags: [moc]
---

Mathematical foundations essential for understanding machine learning algorithms.
Covers linear algebra for data representation, calculus for optimization, probability for uncertainty, and discrete math for algorithmic thinking.
Based on Mathematical Foundations of Machine Learning course by Jon Krohn.

## Linear Algebra

Mathematical framework for representing and manipulating data in high-dimensional spaces.

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

## Practice

- [[Math for ML|04-Flashcards/Math for ML]] — spaced repetition cards for mathematical foundations

## External Resources

- [Mathematical Foundations of Machine Learning - Jon Krohn](https://www.jonkrohn.com/foundation)
- [Mathematics for Machine Learning - Deisenroth, Faisal, Ong](https://mml-book.github.io/)
- [3Blue1Brown Essence Series](https://www.3blue1brown.com/essence-of-algebra)
- [Khan Academy Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [Khan Academy Calculus](https://www.khanacademy.org/math/calculus-1)
- [Khan Academy Statistics and Probability](https://www.khanacademy.org/math/statistics-probability)
