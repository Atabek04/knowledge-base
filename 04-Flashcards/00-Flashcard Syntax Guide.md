---
created: 2025-01-04
tags: [reference]
---

# Flashcard Syntax Guide

## Requirements

1. **Tag the file** with `#flashcards` or `#flashcards/topic` in frontmatter
2. Use correct syntax for each card type (see below)
3. Cards are stored in the same file — plugin adds `<!--SR:...-->` scheduling data

## ⚠️ Critical Syntax Warning

**Do NOT use angle brackets `< >` in cloze deletions** — they break the `== ==` highlighter syntax.

**❌ Wrong:**
```
To unstage a file: ==git reset HEAD <file>==
```

**✅ Correct (use curly braces instead):**
```
To unstage a file: ==git reset HEAD {file}==
```

Apply this to all placeholders: `{name}`, `{branch}`, `{hash}`, `{file}`, etc.

---

## Card Types

### 1. Single-Line Basic

```
question::answer
```

**Example:**
```
What does git stash do?::Temporarily saves uncommitted changes to a stack
```

Creates **1 card**: question → answer

---

### 2. Single-Line Bidirectional

```
term:::definition
```

**Example:**
```
DVCS:::Distributed Version Control System
```

Creates **2 cards**: term → definition AND definition → term

---

### 3. Multi-Line Basic

```
Question on front
?
Answer on back
(can be multiple lines)
```

**Example:**
```
What is the difference between reset and revert?
?
**Reset** moves branch pointer backward (rewrites history).
**Revert** creates inverse commit (preserves history).
```

Creates **1 card**. Blank line ends the card.

---

### 4. Multi-Line Bidirectional

```
Side A content
??
Side B content
```

Creates **2 cards**: A → B and B → A

---

### 5. Cloze Deletion

```
Text with ==hidden part== visible.
```

**Example:**
```
Git reset --soft keeps changes ==staged==.
```

Creates **1 card** per =deletion=

**Multiple clozes = multiple cards:**
```
==Reset== rewrites history, ==revert== preserves it.
```
Creates **2 cards** — each hides one, shows the other.

---

### 6. Cloze with Hint

```
The capital of France is ==Paris==^[European city]
```

Hint appears during review.

---

## Quick Reference

| Type                      | Separator | Cards Created  |
| ------------------------- | --------- | -------------- |
| Single-line basic         | `::`      | 1              |
| Single-line bidirectional | `:::`     | 2              |
| Multi-line basic          | `?`       | 1              |
| Multi-line bidirectional  | `??`      | 2              |
| Cloze                     | =text=    | 1 per deletion |

---

## Sources

- [Flashcards Overview](https://www.stephenmwangi.com/obsidian-spaced-repetition/flashcards/flashcards-overview/)
- [Q&A Cards](https://www.stephenmwangi.com/obsidian-spaced-repetition/flashcards/q-and-a-cards/)
- [Cloze Cards](https://www.stephenmwangi.com/obsidian-spaced-repetition/flashcards/cloze-cards/)
