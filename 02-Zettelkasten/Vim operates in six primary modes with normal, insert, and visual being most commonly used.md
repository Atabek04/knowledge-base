---
created: 2026-01-20
tags: [vim/modes]
---

**Vim** distinguishes between six primary **modes**, each serving a different purpose. This **modal design** separates navigation and command execution from text insertion, enabling efficient keyboard-driven workflows.

**The Six Vim Modes**

**Normal Mode** (default)
- Entry: Press `Esc` from any other mode
- Used for: Navigation and executing commands
- Default mode when you open Vim
- Cursor movement and text manipulation

**Insert Mode**
- Entry: Press `i`, `a`, `o`, or similar commands from Normal mode
- Used for: Typing and inserting text
- Similar to regular text editors
- Exit: Press `Esc` to return to Normal mode

**Visual Mode**
- Entry: Press `v`, `V` (line select), or `Ctrl+V` (block select) from Normal mode
- Used for: Selecting text regions
- Enables operations on selected text
- Exit: Press `Esc` or execute command to deselect

**Command-line Mode**
- Entry: Press `:` (for commands), `/` (for search forward), `?` (for search backward)
- Used for: Extended commands like saving, quitting, find-replace
- Example: `:w` saves file, `:q` quits, `:/pattern` searches

**Replace Mode**
- Entry: Press `R` from Normal mode
- Used for: Overwriting existing text character-by-character
- Similar to Insert mode but replaces rather than shifts text

**Select Mode**
- Similar to Visual mode but with different behavior
- Typing replaces the selected text
- Less commonly used than Visual mode

Understanding these modes is essential: **normal mode** is for navigation, **insert mode** is for typing, and **visual mode** is for selection. This modal approach enables powerful keyboard shortcuts without conflicting with text entry.

## Links

- [[Vim MOC]] — Vim text editor fundamentals
- [[Vim insert mode can be entered from different positions using i, a, o and their uppercase variants]]
