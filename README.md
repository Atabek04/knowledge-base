# Tech Knowledge Base

A personal **Zettelkasten** for technical knowledge.

Optimized for **deep understanding**, **long-term retention**, and **active recall**.

---

## What is This?

A knowledge management system based on the Zettelkasten method.

You capture ideas → process them → convert to permanent knowledge → practice with spaced repetition.

Focus areas: **Backend**, **DevOps**, **System Design**.

---

## How It Works

**Capture** raw ideas in Inbox.

**Create** two types of permanent knowledge:
- **Atomic Notes** — conceptual understanding (Zettelkasten)
- **Flashcards** — memorization (spaced repetition)

**Navigate** with Maps of Content (MOCs) to connect related notes.

**Review** flashcards daily for retention.

---

## Quick Links

| [[CLAUDE.md]] | Configuration for Claude Code |

**Operational rules now live as Claude Code skills** (under `.claude/skills/`, hidden from Obsidian) rather than as vault docs:

| Skill               | Purpose                                                                            |
| ------------------- | ---------------------------------------------------------------------------------- |
| `flashcard-creator` | Flashcard syntax, deck hierarchy, question quality, vocab cards, Anki sync          |
| `note-validator`    | Pre-move Zettelkasten validation (atomicity, title, content → PASS/SPLIT/REWRITE)   |

---

## Folder Overview

```
00-Inbox/           Raw captures (process within 7 days)
01-MOCs/            Navigation hubs for topics
02-Zettelkasten/    Atomic permanent notes (core)
05-Flashcards/      Spaced repetition cards (Obsidian → Anki)
06-Planning/        Interview prep, trackers, schedules
Assets/             Images and attachments
scripts/            Maintenance scripts
.claude/skills/     Operational workflow skills (flashcard-creator, note-validator)
```

---

## Key Principles

**Atomic:** One idea per note.

**Linked:** Every note connects to related notes & parent MOC.

**Permanent:** Inbox → Process → Permanent → Archive.

---