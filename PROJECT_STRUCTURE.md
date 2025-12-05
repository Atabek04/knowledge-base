# Project Structure

Detailed explanation of each folder and what it contains.

---

## 00-Inbox/

**Purpose:** Capture zone for raw knowledge before processing.

**What goes here:**
- Ideas from reading/watching
- Code snippets to remember
- Questions that arise
- Links to articles
- Raw highlights from books

**Key rule:** Process within 7 days—convert to permanent notes or discard.

Inbox is temporary by design. Don't let it accumulate.

See [[WORKFLOW]] → Phase 1 for capture details.

---

## 01-MOCs/

**Purpose:** Navigation hubs for related atomic notes.

**What goes here:**
- One file per major topic (Git MOC, Java MOC, System Design MOC)
- Links to all related atomic notes
- Organized by subtopic sections
- Brief context for each link

**Why needed:**
Atomic notes are isolated. MOCs connect them into coherent learning paths.

Think of MOC as a "table of contents" for a topic.

**Examples:**
- Git MOC → links to all Git concepts (merge, rebase, reset, etc.)
- System Design MOC → links to distributed systems, databases, caching, etc.

---

## 02-Zettelkasten/

**Purpose:** Core knowledge storage. Permanent, atomic notes.

**What goes here:**
- One idea per note
- Statement-style titles (not "Recursion" but "Recursion involves function calling itself with base case")
- 3-15 sentences explanation
- Links to related notes and parent MOC
- Flat structure (no subfolders)

**How it differs from Reference:**
Reference = "How do I...?" (lookup)
Zettelkasten = "Why does...?" (understanding)

**Example structure:**
```
Git reset removes commits while revert creates inverse commits.md
Git merge preserves history while rebase linearizes it.md
Distributed VCS gives every developer full repository copy.md
```

**Key principle:** Each note must be linked to prevent orphans.

See [[WORKFLOW]] → Phase 3A for atomic note creation.

---

## 03-Reference/

**Purpose:** Quick-lookup material. Not for learning—for retrieval.

**What goes here:**
- Commands (git, vim, obsidian)
- Syntax cheatsheets
- API documentation
- Configuration references
- Step-by-step procedures

**Structure:**
Hierarchical by tool/topic.

```
03-Reference/
├── Git/
│   └── Commands.md
├── Vim/
│   └── Shortcuts.md
├── Obsidian/
│   └── Shortcuts.md
└── IntelliJ IDEA/
    └── Shortcuts.md
```

**Format:**
Tables for scanning speed.
Code blocks for examples.
No deep explanation needed.

You search here when you forget syntax. You don't need to memorize.

See [[WORKFLOW]] → Phase 3B for reference note creation.

---

## 04-Flashcards/

**Purpose:** Active recall for memorization and retention.

**What goes here:**
- Core commands worth memorizing (daily use)
- Key concepts for spaced repetition
- One file per topic (Git.md, Vim.md, etc.)

**Card types:**
- Single-line Q&A: `question::answer`
- Multi-line Q&A: separated by `?`
- Cloze deletion: `==hidden==`
- Bidirectional: `term:::definition`

**How it works:**
Plugin tracks due dates and intervals automatically.
Review 5-10 minutes daily for long-term retention.

Don't use flashcards for reference material (use 03-Reference/ instead).

See [[WORKFLOW]] → Phase 3C for flashcard creation and syntax guide.

---

## 05-Projects/

**Purpose:** Active learning workspace. Temporary, focused study.

**What goes here:**
- Course notes and exercises
- Certification study sprints
- Book chapter notes
- Research projects
- Learning experiments

**Why separate from permanent notes:**
Projects are work-in-progress and often become reference material.
Keep active projects visible.
Archive when completed.

**Workflow:**
Work here while learning → Extract key concepts to Zettelkasten → Move to Archive when done.

---

## 06-Archive/

**Purpose:** Completed projects and outdated notes. Searchable but out of active workflow.

**What goes here:**
- Finished courses/certifications (projects)
- Superseded understanding (old zettelkasten notes)
- Outdated reference material
- Completed study sprints

**Why keep it:**
Historical context—useful for revisiting old knowledge.
Searchable—can dig up archived notes if needed.
Keeps active vault clean and focused.

**When to archive:**
After project completion → Move entire 05-Projects/ folder here.
If understanding changes → Archive old note, create new one.

---

## Templates/

**Purpose:** Reusable templates for consistent note formatting.

**What goes here:**
- Atomic Note template (for Zettelkasten)
- Flashcard Deck template (for creating new card files)
- MOC template (for creating maps of content)

**How to use:**
Obsidian → insert template when creating new note.
Templates plugin or core Templates plugin.

Templates ensure consistency across all notes.

---

## Root-Level Docs

### README.md
High-level overview of the knowledge base.
Start here for new users.

### CLAUDE.md
Configuration and style guide for Claude Code.
Used for AI-assisted note generation.

### WORKFLOW.md
Complete workflow for note creation, processing, and review.
Reference when unsure where something goes or how to proceed.

### PROJECT_STRUCTURE.md (this file)
Detailed explanation of each folder's purpose and contents.

---

## Decision Flowchart

```
New knowledge captured
       ↓
Is it a quick fact to look up?
  ├─ YES → 03-Reference/
  └─ NO → Continue

Is it a concept I need to understand deeply?
  ├─ YES → 02-Zettelkasten/
  └─ NO → Continue

Am I actively learning a topic?
  ├─ YES → 05-Projects/
  └─ NO → Continue

Should I memorize this for daily use?
  ├─ YES → 04-Flashcards/
  └─ NO → Continue

Discard or Save to 00-Inbox/ for later processing
```

---

## Key Principles

**Atomic:** One idea per note, not monolithic topics.

**Linked:** Every note connects to related notes and parent MOC.

**Organized:** Clear separation between learning (Zettelkasten) and lookup (Reference).

**Temporary → Permanent:** Inbox → Process → Permanent structure → Archive.

**Spaced Repetition:** Flashcards for memorization, Zettelkasten for understanding.

See [[WORKFLOW]] for step-by-step instructions on how to use these folders.
