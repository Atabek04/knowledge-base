---
created: 2026-01-20
tags: [vim/modes]
---

**Vim Insert mode** can be entered from six different positions using lowercase and uppercase variants of `i`, `a`, and `o` commands. Each command places the cursor at a different location relative to the current position.

**Lowercase Commands (Relative to Cursor)**

| Command | Insertion Point | Mnemonic |
|---------|-----------------|----------|
| `i` | Before cursor (insert) | **i**nsert |
| `a` | After cursor (append) | **a**ppend |
| `o` | New line below | **o**pen line below |

**Uppercase Commands (Line-Based)**

| Command | Insertion Point |
|---------|-----------------|
| `I` | Beginning of line |
| `A` | End of line |
| `O` | New line above |

**Practical Differences**

If your cursor is at the middle of a line:
- `i` places you before the cursor (useful for inserting in the middle)
- `a` places you after the cursor (useful for continuing at that position)
- `I` jumps to line start, useful for adding indentation or prefixes
- `A` jumps to line end, useful for adding suffixes or comments
- `o` and `O` create new lines for organized text entry

All six commands enter **Insert mode** where you can type normally. The difference is purely where the cursor appears when entering Insert mode. After completing your edits, press `Esc` to return to **Normal mode**.

## Links

- [[Vim MOC]] — Vim text editor fundamentals
- [[Vim operates in six primary modes with normal, insert, and visual being most commonly used]]
