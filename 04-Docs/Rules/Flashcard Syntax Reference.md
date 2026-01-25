# Flashcard Syntax Reference

## Requirements

1. Tag file with `#flashcards` or `#flashcards/topic` in frontmatter
2. Use correct syntax for card type
3. Plugin adds `<!--SR:...-->` scheduling data automatically

---

## Critical Syntax Warning

**Do NOT use angle brackets `< >` in cloze deletions** — they break the == == syntax.

```
❌ Wrong: ==git reset HEAD <file>==
✓ Correct: ==git reset HEAD {file}==
```

Use `{name}`, `{branch}`, `{hash}`, `{file}`, etc.

---

## Card Types

| Type                  | Syntax              | Cards          | Example                                                          |
| --------------------- | ------------------- | -------------- | ---------------------------------------------------------------- |
| **Basic**             | `question::answer`  | 1              | `What does git stash do?::Temporarily saves uncommitted changes` |
| **Bidirectional**     | `term:::definition` | 2              | `DVCS:::Distributed Version Control System`                      |
| **Multi-line**        | `text\n?\nanswer`   | 1              | See below                                                        |
| **Multi-directional** | `text\n??\ntext`    | 2              | See below                                                        |
| **Cloze**             | ==hidden==          | 1 per deletion | `TCP ensures ==reliable== delivery`                              |
| **Cloze Hint**        | ==answer==^[hint]   | 1              | `Capital of France: ==Paris==^[Europe]`                          |

---

## Multi-Line Format

```
Question on front
?
Answer on back
(multiple lines ok)
```

Blank line ends card.

---

## Multi-Paragraph Answers

Configure plugin setting: **"Characters denoting the end of clozes and multiline flashcards"** = `---`

Then end cards with `---`:

```
Question?
?
First paragraph.

Second paragraph.

---
```

---

## Sources

- [Flashcards Overview](https://www.stephenmwangi.com/obsidian-spaced-repetition/flashcards/flashcards-overview/)
- [Q&A Cards](https://www.stephenmwangi.com/obsidian-spaced-repetition/flashcards/q-and-a-cards/)
- [Cloze Cards](https://www.stephenmwangi.com/obsidian-spaced-repetition/flashcards/cloze-cards/)
