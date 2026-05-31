# Flashcard Question Quality Principles

Read this whenever a card feels weak, trivial, or like trivia — it's the craft of *what
makes a question worth asking*.

## Core Principle: Effortful Retrieval

**Testing Effect**: Answering strengthens memory ~2x more than passive review — but only
if the question forces genuine cognitive effort.

Three requirements:
1. **Specificity** — One retrievable idea, clearly defined
2. **No Pattern-Matching** — Answer isn't contained in the question
3. **Connection** — Linked to your broader knowledge network

---

## Question Type Effectiveness

| Type               | Best For                                            | Effectiveness |
| ------------------ | --------------------------------------------------- | ------------- |
| **Open-Ended Q&A** | Conceptual understanding, mechanisms, relationships | ⭐⭐⭐⭐⭐         |
| **Definition**     | Prerequisites in new domains                        | ⭐⭐            |

**Strategy**: Create understanding with Q&A first, then use cloze for maintenance drilling.

---

## Question Templates

### Definition/Terminology
```
What is [concept]?
Define [term] in the context of [domain].
```

### Mechanism (How)
```
How does [mechanism] work?
What steps are involved in [process]?
```

### Causality (Why)
```
Why does [system] use [mechanism]?
What problem does [mechanism] solve?
What would happen without [mechanism]?
```

### Relationship (Comparison)
```
How does [A] differ from [B]?
What is the trade-off between [A] and [B]?
When would you choose [A] over [B]?
```

### Application
```
When would you use [concept] in practice?
How would you apply [principle] to [scenario]?
```

---

## Answer Writing Rules

### Use the term in the definition

When defining a concept, use the word itself (or its verb/adjective form) in the answer.
This creates a natural association between the term and its meaning.

- **Classification** → "Classifying input into a discrete category or group"
- **Regression** → "Predicting a continuous number by fitting a line through data"
- **Normalization** → "Normalizing features to a fixed [0, 1] range"

Avoid generic phrasing like "a technique that does X" — instead, show what the term
*means* by using it.

### Structure answers for readability

Break answers into scannable chunks — don't write a wall of text. Use:

- **Line breaks** between distinct ideas
- **Bullet lists** for multiple points, steps, or comparisons
- **Bold** for key terms within the answer

❌ Bad: `Back: Classification is a type of supervised learning where the model predicts which category an input belongs to. It outputs probability scores. Common algorithms include logistic regression, KNN, and SVM.`

✓ Good:
```
Back: **Classifying** input into a discrete category or group (which one? what type?).
- Outputs **probability scores** expressing confidence in each class
- Common algorithms: Logistic Regression, KNN, SVM, Decision Trees
```

---

## Common Pitfalls

| Problem                                                | Fix                                                                                |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| **Ambiguous question** (multiple valid answers)        | Specify the retrieval target: "What guarantees does TCP provide that UDP doesn't?" |
| **Hidden hints** (answer revealed in question)         | Remove descriptive context. Make it a pure retrieval cue.                          |
| **Multi-concept questions** (5 ideas in one card)      | Split into atomic cards. One concept per card.                                     |
| **Orphan cards** (disconnected from knowledge network) | Link to MOC or related concepts. Ask: "Does this relate to my broader knowledge?"  |
| **Question-answer mismatch** (depth/scope don't align) | Ensure both require same level of retrieval.                                       |

---

## Phrasing and cross-card rules

These catch the failure modes that survive a per-card read but hurt over a whole batch.

**No yes/no stems.** "Is TCP connection-oriented?" trains recognition — you can guess and
feel right. Rephrase with *what / how / why / when / which*: "What does TCP's three-way
handshake establish before data flows?" A good stem forces production, not a coin flip.

**Recall, not recognition.** Never write multiple-choice / "which of these" cards. Your
deck trains you to *produce* the answer; the real exam (or interview) supplies the
distractors. A card that hands you options does the retrieval for you.

**The 70% spoiler test.** Cover the answer, read the stem alone. If someone who never
studied could guess it ≥70% of the time, the stem leaks the answer — strip the descriptive
context until the stem is a pure cue.

**Check interference across the batch.** After writing a set, read the stems in sequence.
If two stems would cue the *same* answer in their first few words, they'll collide on
review. Add a distinctive landmark to each (a specific term, a system name, the consequence)
so every stem uniquely points to one answer.

**Cap the answer.** Keep an answer to ≤ ~1 sentence or ≤ 3 bullets. If it runs longer,
that's usually two cards wearing a trench coat — split it.

**Split enumerations.** A list of 4+ items can't be retrieved as one answer, and cloze
doesn't rescue it. Break it into a count card + one card per item. The mechanical protocol
is in `quality-checklist.md`.

---

## Extraction sweep: what's card-worthy in a tech note

Don't skip substance — walk the note and make a card for each type present:

- **Definition** — what a term means (use the term in the answer)
- **Mechanism** — how something works, step by step
- **Why / trade-off** — the reason a design exists, what it costs, what it buys
- **Formula / complexity** — equations, Big-O, capacity math
- **Command / syntax** — the exact invocation, flags, signature
- **Code pattern** — an idiom worth reproducing from memory
- **Gotcha / edge case** — the thing that breaks, the failure mode
- **Comparison** — A vs B, when to choose which

If the note states it and it's testable, it earns a card.

---

## Quality gate

The pre-sync checklist lives in **`quality-checklist.md`** — run it over every batch before
syncing. This file is the *craft* (why questions work); that file is the *gate* (fast pass
to catch failures).

---

## Workflow: Fleeting → Atomic → Flashcards

1. **Fleeting Notes** — Capture raw insights
2. **Atomic Notes** — Refine into single complete-statement titles
   - Example: *"TCP maintains sequence numbers to detect missing packets"*
3. **Extract Questions** — Ask: "What would I need to *retrieve* to explain this?"
   - "How do sequence numbers help TCP detect missing packets?"
   - "Why is packet ordering important?"
4. **Create Cards** — Use Q&A format (recommended) or cloze

---

## Red Flags During Review

| Signal                                      | Meaning                        | Fix                                      |
| ------------------------------------------- | ------------------------------ | ---------------------------------------- |
| "I can never remember this"                 | Too hard or poorly defined     | Simplify or rewrite                      |
| "I knew the answer but don't understand it" | Surface-level pattern-matching | Remove hints; require deeper retrieval   |
| "This feels like trivia"                    | Orphaned, disconnected card    | Link to MOC; create related cards        |
| "I got it right but guessed"                | Ambiguous question             | Tighten phrasing                         |
| "This is too easy"                          | No retrieval challenge         | Combine with related concept; ask deeper |

---

## Key Insight

**The spacing algorithm is only as good as your question quality.**

A poor question wastes intervals. A good question produces lasting understanding through
effortful retrieval.
