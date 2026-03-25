# Flashcard Syntax Reference

## Note Type: Coding Questions

Fields: `Front`, `Back`

**Anki setup:** Tools → Manage Note Types → Add → Blank → Name: `Coding Questions` → Fields: Front, Back → Cards: Front `{{Front}}`, Back `{{Back}}`

---

## Deck Hierarchy

### Machine Learning

```
Machine Learning::Fundamentals
Machine Learning::Data Preprocessing
Machine Learning::Model Training
Machine Learning::Regression
Machine Learning::Classification
Machine Learning::Unsupervised
Machine Learning::Model Evaluation
Machine Learning::Dimensionality Reduction
Machine Learning::Model Selection
```

### Python

```
Python::NumPy
Python::Pandas
Python::Matplotlib
Python::Scikit-learn
```

---

## File Header

```markdown
TARGET DECK: Machine Learning::Regression
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
