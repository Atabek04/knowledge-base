---
name: note-validator
description: >-
  Validate inbox notes against Zettelkasten standards before they move from 00-Inbox into
  the permanent 02-Zettelkasten/ collection. Use this whenever the user wants to process,
  review, promote, or "graduate" inbox notes, asks "is this note ready", "validate this
  note", "check my inbox", "can this go into the zettelkasten", or is cleaning out 00-Inbox.
  Also trigger when the user pastes a draft note and asks whether it's atomic, whether the
  title is good, or whether it's ready to file — even if they don't say the word "validate".
  The skill judges atomicity, title quality, and content, then returns a PASS / SPLIT /
  REWRITE verdict. It does NOT rewrite the user's content — it diagnoses like a mentor.
argument-hint: "[note-path or pasted draft]"
---

# Note Validator

A gate between `00-Inbox/` (fleeting capture) and `02-Zettelkasten/` (permanent notes).
A note earns promotion only when it holds **one idea, stated as a complete thought, in the
user's own words, and connectable to the rest of the vault**. The job here is to *judge*
against that bar and tell the user exactly what's missing — not to silently fix it.

Why judge instead of fix: the value of a Zettelkasten is that the user did the thinking.
If the validator rewrites the note, the understanding never transfers. So diagnose
precisely, point to the gap, and let the user close it. Act as an expert mentor, not a
ghostwriter.

## The three checks

Run all three. A note must clear all of them to PASS.

### 1. Atomicity — one idea, not many

The note must contain exactly **one** atomic idea. If you can split it into two notes that
each stand alone, it isn't atomic yet.

- Tell: the note says "A, and also B" where A and B are independently linkable concepts.
- The fix is not to trim — it's to **split** into separate notes, each with its own title.

### 2. Title quality — a complete statement, not a label

The title must teach something on its own. It's a claim, not a topic tag.

- ❌ Label: "WebSocket", "TCP", "Async", "Backpropagation"
- ✓ Statement: "WebSocket enables full-duplex communication over TCP", "Backpropagation
  propagates gradients backward through layers using the chain rule"
- Test: read the title alone with the note hidden. Does it assert a fact you could agree or
  disagree with? If it only *names* a thing, it fails.

### 3. Content — rephrased, clear, linkable

- **In the user's own words** — not copy-pasted from a source. Pasted prose is a fleeting
  note, not a permanent one.
- **Clear and self-contained** — understandable without its source open.
- **Intentionally linkable** — it connects to at least one other note or a MOC. A note
  with no possible link is an orphan and shouldn't enter the permanent collection.

## The verdict

Return exactly one of these, with the specific reason:

| Verdict | When | What to tell the user |
|---|---|---|
| **✓ PASS** | All three checks clear | Approve the move. Then do the post-validation steps below. |
| **⚠ SPLIT** | Atomicity fails — multiple ideas | Name the distinct ideas you see and propose one title per note. The user splits them, then re-validates each. |
| **✗ REWRITE** | Title is a label, or content is copy-pasted / unclear / unlinkable | Point to the exact weakness (which check, which line). Suggest a direction — e.g. a stronger title phrasing — but let the user make the edit. |

Be specific about *which* check failed and *why*. "This is two ideas: X and Y" beats "not
atomic." A vague verdict forces the user to guess.

## Post-validation (only after PASS)

When a note passes, prepare it for the permanent collection:

1. Add frontmatter:
   ```
   tags: [keyword1, keyword2]
   date: YYYY-MM-DD
   ```
2. Confirm it has at least one link (inline `[[]]` and/or a "Read more" section) — an
   orphan never enters `02-Zettelkasten/`.
3. Move it to `02-Zettelkasten/[title].md`.

Do **not** rewrite the note's body during this step. Add metadata and links per the vault's
note conventions in `CLAUDE.md`, but the user's words stay the user's words.

## When validating a batch

Processing several inbox notes at once: validate each independently and report a short
table — note → verdict → one-line reason — so the user can triage quickly. Handle the
PASS notes first (cheap wins out of the inbox), then walk the SPLIT/REWRITE ones.
