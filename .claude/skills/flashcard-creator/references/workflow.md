# Obsidian → Anki Workflow

How card files get into Anki. The files are inert markdown until the `Obsidian_to_Anki`
plugin syncs them.

## Setup (One-time)

1. Install [AnkiConnect](https://ankiweb.net/shared/info/2055492159) addon in Anki
2. Configure AnkiConnect: Tools → Add-ons → AnkiConnect → Config:
```json
{
  "webCorsOriginList": ["app://obsidian.md"]
}
```
3. Install `Obsidian_to_Anki` plugin in Obsidian
4. Set scan folder: `05-Flashcards/`

## Daily Workflow

```
Atomic Note → Claude Code → 05-Flashcards/{category}/{topic}.md → Sync → Anki
```

1. **Create/Edit** flashcard `.md` file in `05-Flashcards/{category}/{topic}.md` structure
2. **Sync**: Click Anki ribbon icon (Anki must be running)
3. **Done** — cards created/updated in Anki

## Folder Structure

```
05-Flashcards/
├── {category}/
│   └── {topic}.md → TARGET DECK: Tech-KB::Category::Topic
```

**Examples:**
- `05-Flashcards/java/concurrency.md` → Deck: `Tech-KB::Java::Concurrency`
- `05-Flashcards/networking/tcp.md` → Deck: `Tech-KB::Networking::TCP`

**Naming conventions:**
- Category folders: lowercase, kebab-case (e.g., `system-design/`)
- Topic files: lowercase, kebab-case (e.g., `tcp-handshake.md`)
- Deck mapping in `TARGET DECK:` header: `Tech-KB::{Category}::{Topic}` (capitalized)

**Suggested categories:** `java/`, `kotlin/`, `spring/`, `networking/`, `security/`,
`git/`, `linux/`, `system-design/`

Category folders organize related topics. Each file creates one Anki deck. Folders are
created on-demand when generating flashcards.

## Updating Cards

- Edit the `.md` file directly
- Re-sync (same button)
- Progress preserved — only content updates

## Renaming a deck does NOT move existing cards

A footgun worth knowing before you touch a `TARGET DECK:` line on an already-synced file:
the plugin keys cards to Anki by their `<!--ID:-->`, not by deck path. So if you change
`TARGET DECK: Old::Path` to `TARGET DECK: New::Path`, the next sync **creates the new
(empty) deck but leaves the old cards — and all their review history — in the old deck.**

To actually migrate without losing scheduling progress, do it inside Anki:
- Right-click the old deck → **Rename** → type the full new name (preserves cards + reviews), **or**
- Browser → select the cards → **Cards → Change Deck** → pick the new deck

Then update the `TARGET DECK:` line to match. Editing the file alone is never enough.

## Key Rules

- Anki must be running during sync
- One deck per file via `TARGET DECK:` header
- Delete card from `.md` → auto-deletes from Anki (if enabled)
- New cards get an `<!--ID:-->` stamped on first sync — never hand-edit these IDs
- Renaming a deck path in the file doesn't migrate synced cards — do it in Anki (above)
