# Knowledge Base Workflow

The complete process for capturing, processing, and retaining knowledge in this Zettelkasten.

---

## Phase 1: Capture (00-Inbox/)

**Deadline: Process within 7 days**

**What goes here:**
- Ideas during reading/learning
- Code snippets you want to remember
- Questions that arise
- Links to articles/resources
- Raw highlights from books

**How:**
1. Quick capture without formatting
2. Minimal structure — just the idea
3. No need for perfect wording

**Example:**
```
Git reset rewrites history but reset doesn't
Need to understand this better
```

---

## Phase 2: Process

Convert inbox captures into permanent knowledge. Decide the destination.

### Decision Tree

```
Is this a quick fact to look up?
  → 03-Reference/ (Cheatsheet, command, API docs)

Is this a concept I need to understand?
  → 02-Zettelkasten/ (Atomic note)

Am I actively learning a topic?
  → 05-Projects/ (Course work, study sprint)

Is this outdated/irrelevant?
  → Delete or 06-Archive/
```

---

## Phase 3: Create

### 3A. Atomic Notes (02-Zettelkasten/)

**When:** Concept you need to deeply understand

**Steps:**

1. **Write statement-style title** (not "Reset" but "Git reset removes commits by moving branch pointer")
2. **Explain in own words** (3-15 sentences)
3. **Add frontmatter:**
   ```yaml
   ---
   created: YYYY-MM-DD
   tags: [topic/subtopic]
   sr-due:
   sr-interval:
   sr-ease:
   ---
   ```
4. **Link to related notes** (at least 1)
5. **Link to parent MOC**
6. **Review:** Does the title stand alone? Are key terms bolded?

**Quality Check:**
- ✓ Title is a complete statement
- ✓ Explanation in own words (not copied)
- ✓ Linked to related concepts
- ✓ Linked to MOC
- ✓ No orphan notes

---

### 3B. Reference Notes (03-Reference/)

**When:** Quick lookup (commands, syntax, procedures)

**Structure:**
```
03-Reference/
├── Git/
│   └── Commands.md
├── Vim/
│   └── Shortcuts.md
└── IntelliJ IDEA/
    └── Shortcuts.md
```

**Format:**
- Tables for quick scanning
- Code blocks for examples
- No explanation needed
- Group by operation type

**Example:**
```markdown
## Stashing

| Command | Action |
|---------|--------|
| git stash | Save changes |
| git stash pop | Restore and remove |
```

---

### 3C. Flashcards (04-Flashcards/)

**When:** Memorizing core commands/concepts for daily use

**Steps:**

1. Create file: `04-Flashcards/{Topic}.md`
2. Add frontmatter: `tags: [flashcards/topic]`
3. Choose card type and syntax:

**Single-line Q&A (::):**
```
What command undoes a commit?::`git reset --soft HEAD~1`
```

**Multi-line Q&A (?):**
```
What is rebasing?
?
Moving commits on top of another branch to create linear history.
Rewrites commit SHAs, so never rebase pushed commits.
```

**Cloze deletion (==):**
```
Git reset moves the branch pointer ==backward==.
```

**Bidirectional (:::):**
```
DVCS:::Distributed Version Control System
```

4. Bold **key terms** in both question and answer
5. Keep one concept per card
6. Use active recall (question requires retrieval)

---

### 3D. Maps of Content (01-MOCs/)

**When:** Creating a navigation hub for related atomic notes

**Steps:**

1. Create file: `01-MOCs/{Topic} MOC.md`
2. Add frontmatter: `tags: [moc]`
3. Organize by subtopics:

```markdown
# Git MOC

## Fundamentals
- [[Distributed VCS gives every developer full copy]]
- [[HEAD is a pointer to current branch]]

## History & Undoing
- [[Git reset removes commits]]
- [[Git revert creates inverse commits]]

## Branching Strategies
- [[Git merge preserves history]]
- [[Git rebase linearizes history]]
```

4. Include brief context for each link
5. Link back from atomic notes: `[[Git MOC]]`

---

## Phase 4: Review & Reinforce

### 4A. Spaced Repetition (Daily)

**How:**
1. Open Obsidian
2. `Ctrl+P` → "Review flashcards"
3. Answer due cards (5-10 min)
4. Rate: Hard / Good / Easy

**Note:** SR plugin adds scheduling automatically (`<!--SR:!2025-01-15,4,270-->`)

### 4B. Note Review (Weekly)

1. Check for orphan notes (no links)
2. Add missing connections to MOCs
3. Refine explanations if unclear

### 4C. Concept Deep Dive

1. Read related atomic notes (via links)
2. Check if understanding is complete
3. Add/refine notes if gaps exist

---

## Phase 5: Maintain

### Linking Rules

**Every atomic note must have:**
- At least 1 link to related note
- 1 link to parent MOC
- Clear bidirectional connections

### Orphan Detection

Notes with 0 incoming links are orphaned:
1. Use backlinks panel to check
2. Either delete or connect to MOC
3. Never leave notes without context

### Archival

**Move to 06-Archive/ when:**
- Course/project completed
- Topic becomes irrelevant
- Superseded by newer understanding

**Keep searchable:**
- Archived notes remain accessible
- Use for historical context if needed
- Don't delete permanently

---

## Decision: Reference vs Zettelkasten

| Aspect | Reference (03-Reference/) | Zettelkasten (02-Zettelkasten/) |
|--------|--------------------------|--------------------------------|
| **Purpose** | Lookup | Understanding |
| **Question** | "How do I...?" | "Why does...?" |
| **Format** | Commands, syntax, steps | Concepts, explanations |
| **Retention** | Don't need to memorize | Build mental model |
| **Flashcards?** | Maybe (frequent use) | Yes (foundational) |

**Rule:** If you'd look it up the same way twice, it's Reference. If you need to understand it deeply, it's Zettelkasten.

---

## Workflow at a Glance

```
Raw Idea
   ↓
00-Inbox/ (Capture)
   ↓
Decide: Lookup? Understand? Project? Archive?
   ↓
┌──────────────────────────────────────────┐
│                                          │
↓                                          ↓
03-Reference/                         02-Zettelkasten/
(Commands,                           (Concepts,
Cheatsheets)                         Atomic Notes)
   ↓                                    ↓
   └────────────┬──────────────────────┘
                ↓
          01-MOCs/
        (Navigation
         Hub)
                ↓
          04-Flashcards/
          (Active Recall)
                ↓
           Daily Review
           (SR Plugin)
                ↓
          Long-term Retention
```

---

## Daily Routine

1. **Morning (5 min):** Review due flashcards
2. **During Learning:** Capture in Inbox
3. **Evening (15 min):** Process inbox → create notes
4. **Weekly (30 min):** Review connections, audit orphans

---

## Quality Checklist

Before considering a note "complete":

- [ ] Title is a complete statement (not just topic)
- [ ] Explanation in own words (not copy-paste)
- [ ] Key terms are **bolded**
- [ ] Linked to related notes (min 1)
- [ ] Linked to parent MOC
- [ ] No spelling/grammar errors
- [ ] Frontmatter includes created date and tags

---

## Tips & Gotchas

✓ **Do:**
- Start simple, refine later
- Link generously (connections create understanding)
- Review MOC when learning new topic
- Use flashcards for daily reinforcement

✗ **Don't:**
- Create monolithic "Git" note (split into atomic)
- Copy-paste without rewording
- Leave notes orphaned
- Make titles too vague ("Concepts" vs "Git reset removes commits")
- Try to memorize reference material
