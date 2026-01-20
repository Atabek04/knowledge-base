---
created: 2026-01-20
tags: [vim/commands]
---

**Vim** uses the **exclamation mark** (`:!`) in different positions to distinguish between **shell command execution** and **forcing Vim commands**, providing powerful integration with the operating system.

**Exclamation Mark as Prefix** (`:!<command>`)
- Execute **external shell commands** while remaining in Vim
- Syntax: `:!shellcommand` from **Command-line mode**
- Examples:
  - `:!ls` — Run the `ls` command and show results
  - `:!python script.py` — Execute Python script
  - `:!git status` — Check git repository status
- Output appears in Vim, then you return to editing

**Exclamation Mark as Suffix** (`:<command>!`)
- **Force execute** a Vim command, overriding warnings and protection
- Syntax: `:<vimcommand>!` from **Command-line mode**
- Common examples:
  - `:q!` — Quit without saving (ignores unsaved changes)
  - `:w!` — Force write, even to read-only files
  - `:e!` — Reload file, discarding all current changes
  - `:wq!` — Force save and quit together

**Critical Distinction**
- **Prefix `!`** — "Execute this **external command**" (shell integration)
- **Suffix `!`** — "**Force** this Vim command" (override safety checks)

This design enables powerful workflows: you can shell out to run system commands without leaving Vim, and you can force destructive operations when necessary while Vim normally protects against accidental data loss.

## Links

- [[Vim MOC]] — Vim text editor fundamentals
- [[Vim operates in six primary modes with normal, insert, and visual being most commonly used]]
