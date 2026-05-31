# Flashcard Syntax Reference

Note types, deck hierarchy, file header, and the START/END block format.

## Contents

- Note type: Coding Questions
- Deck hierarchy (by subject)
- File header
- START/END block format (one-liner + multi-line)

---

## Note Type: Coding Questions

Fields: `Front`, `Back`

**Anki setup:** Tools → Manage Note Types → Add → Blank → Name: `Coding Questions` →
Fields: Front, Back → Cards: Front `{{Front}}`, Back `{{Back}}`

(Vocabulary cards use a different note type, `A_English_Translate` — see `vocab.md`.)

---

## Deck Hierarchy

All technical decks live under the `Tech-KB::` root, including English Vocab.

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

### English Vocab

```
Tech-KB::English Vocab::Idioms
Tech-KB::English Vocab::Phrasal Verbs
Tech-KB::English Vocab::Advanced
Tech-KB::English Vocab::IT Terms
Tech-KB::English Vocab::Collocations
```

### Self-Mastery

```
Self-Mastery::Mindset::Recognition & Self-Worth
Self-Mastery::Discipline::Accountability
Self-Mastery::Study Techniques::Caffeine & Cognition
```

The deck list grows on demand — these are the established roots, not a closed set. When a
note belongs to a new subject, extend the hierarchy following the same `Tech-KB::{Category}::{Topic}`
shape.

---

## File Header

Each flashcard file starts with a header that sets the target deck:

```markdown
TARGET DECK: Tech-KB::Machine Learning::Regression
Tags: ml regression
**Related:** [[Link to MOC or concept]]
```

One deck per file. The `TARGET DECK:` value maps the file to its Anki deck.

### Ordering sub-decks that have a natural sequence

Anki sorts sibling decks **alphabetically**, and there's no manual reorder. For most
topic decks that's fine (`Classes`, `Collections`, `Null Safety` — order doesn't matter).
But when siblings carry a real sequence — a DSA pattern progression, a course's chapter
order, a build-up of prerequisites — alphabetical sort scrambles it.

Fix: zero-pad a numeric prefix so the sort respects the sequence.

```
Tech-KB::DSA::01 - Two Pointers
Tech-KB::DSA::02 - Sliding Window
Tech-KB::DSA::03 - Fast & Slow Pointers
```

Use two digits (`01`, not `1`) so the tenth deck doesn't sort before the second. Only do
this where order is meaningful — don't prefix decks that are just an unordered set.

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

The `<!--ID:-->` line is stamped automatically by the plugin on first sync. Never write or
edit it by hand. Leave a blank line between one `END` and the next `START`.
