---
created: 2026-01-20
tags: [vim/editing]
---

**Vim** provides simple **undo** and **redo** commands in **Normal mode** to reverse or restore changes without requiring menus or key combinations.

**Undo Changes**
- Command: `u` (lowercase)
- Effect: Reverses the last edit operation
- Works in Normal mode only
- Can be repeated (`u u u`) to undo multiple changes

**Redo Changes**
- Command: `Ctrl+R` (Control and R together)
- Effect: Restores a change that was undone
- Works in Normal mode only
- Can be repeated to redo multiple changes

**Workflow Example**
1. Edit text in **Insert mode**
2. Press `Esc` to return to **Normal mode**
3. Press `u` to undo the edit if you made a mistake
4. Press `Ctrl+R` to redo if you changed your mind about undoing

**Important Note**: These commands work from **Normal mode** only. If you're currently in **Insert mode**, you must first press `Esc` to switch to Normal mode before using undo/redo.

The simplicity of `u` for undo makes it easy to memorize and use frequently. Unlike many editors requiring `Ctrl+Z`, Vim's single key undo is faster for rapid edit cycles where you frequently test and adjust changes.

## Links

- [[Vim MOC]] — Vim text editor fundamentals
- [[Vim operates in six primary modes with normal, insert, and visual being most commonly used]]
