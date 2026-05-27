# Flashcard Syntax Reference

## Note Type: Coding Questions

Fields: `Front`, `Back`

**Anki setup:** Tools → Manage Note Types → Add → Blank → Name: `Coding Questions` → Fields: Front, Back → Cards: Front `{{Front}}`, Back `{{Back}}`

---

## Deck Hierarchy

### Machine Learning

```
Tech-KB::Machine Learning::Fundamentals
Tech-KB::Machine Learning::Data Preprocessing
Tech-KB::Machine Learning::Model Training
Tech-KB::Machine Learning::Regression
Tech-KB::Machine Learning::Classification
Tech-KB::Machine Learning::Unsupervised
Tech-KB::Machine Learning::Model Evaluation
Tech-KB::Machine Learning::Dimensionality Reduction
Tech-KB::Machine Learning::Model Selection
```

### Math for ML

```
Tech-KB::Math for ML::Calculus
Tech-KB::Math for ML::Probability
```

### Software Engineering

```
Tech-KB::Software Engineering::Requirements Engineering
```

### Economics

```
Tech-KB::Economics::AI and Labor
```

### Python

```
Tech-KB::Python::NumPy
Tech-KB::Python::Pandas
Tech-KB::Python::Matplotlib
Tech-KB::Python::Scikit-learn
```

### Linux

```
Tech-KB::Linux::Command-Line Tools
Tech-KB::Linux::Shell Scripting
Tech-KB::Linux::Permissions
```

### DSA (one deck per pattern)

```
Tech-KB::DSA::Sliding Window
Tech-KB::DSA::Two Pointers
Tech-KB::DSA::Fast & Slow Pointers
Tech-KB::DSA::Merge Intervals
Tech-KB::DSA::Trees
Tech-KB::DSA::Graphs
Tech-KB::DSA::Dynamic Programming
(… one per NeetCode/Grokking pattern)
```

### System Design

```
Tech-KB::System Design::Non-Functional Requirements
Tech-KB::System Design::Building Blocks
Tech-KB::System Design::Designs
```

### Design Patterns

```
Tech-KB::Design Patterns::Creational
Tech-KB::Design Patterns::Structural
Tech-KB::Design Patterns::Behavioral
Tech-KB::Design Patterns::Enterprise
```

### Behavioral

```
Tech-KB::Behavioral::STAR Method
Tech-KB::Behavioral::Story Bank
Tech-KB::Behavioral::Negotiation
```

---

## File Header

```markdown
TARGET DECK: Tech-KB::Machine Learning::Regression
Tags: ml regression
**Related:** [[Link to MOC or concept]]
```

---

## START/END Block Format

### One-liner

```markdown
START
Coding Questions
What does OLS stand for?
Back: Ordinary Least Squares — finds best-fit line by minimizing sum of squared errors
Tags: ml regression
<!--ID: 1771415062868-->
END
```

### Multi-line

```markdown
START
Coding Questions
What are the three properties that describe the structure of a NumPy array?
Back:
- `.shape` → rows × columns as tuple, e.g. `(2, 3)`
- `.ndim` → number of dimensions, e.g. `2`
- `.size` → total element count, e.g. `6`
Tags: python numpy
<!--ID: 1771415062870-->
END
```
