---
created: 2026-01-21
tags: [linux, cli-tools, pager, less-command]
---

The `less` command is a **pager** that displays file contents one screen at a time, allowing efficient navigation through large files without loading everything into memory. It provides search, scrolling, and jumping capabilities that `cat` does not offer.

Unlike `cat` which dumps the entire file at once, `less` is memory-efficient and better suited for viewing large log files, documents, and data sets.

## Why use less instead of cat for viewing files?

`less` is superior for large files because it displays content one screen at a time (memory-efficient), provides **navigation** (scroll up/down, jump to start/end), **search** functionality, and allows pausing at any point. `cat` dumps everything at once and doesn't allow interaction.

---

What are the main navigation commands in less?

**Space** or **Page Down** — next page, **b** or **Page Up** — previous page, **g** — start of file, **G** — end of file, **q** — quit the pager.

---

How do you search for a pattern within less?

Type `/pattern` to search forward, and press **Enter**. Use `n` for next match and `N` for previous match. Type `?pattern` to search backward.

---

What is the basic syntax for using less?

Simply type `less file.txt` to open the file in the pager. You can also pipe command output to less like `command | less`.

---

When should you use less versus cat versus more?

Use **less** for large files (most common choice), **cat** to quickly display small files or concatenate multiple files, and **more** only if less is unavailable (more is an older, less capable pager).

---

## Navigation Quick Reference

| Command | Action |
|---------|--------|
| `Space` / `Page Down` | Next page |
| `b` / `Page Up` | Previous page |
| `g` | Start of file |
| `G` | End of file |
| `/pattern` | Search forward |
| `?pattern` | Search backward |
| `n` | Next match |
| `N` | Previous match |
| `q` | Quit |
| `h` | Help |

## Examples

```bash
# View a file
less file.txt

# View with line numbers
less -N file.txt

# View compressed file directly
less file.txt.gz

# Pipe command output
ps aux | less
tail -f /var/log/syslog | less

# Jump to specific line
less +10 file.txt    # Start at line 10
```

## Related Notes

- [[Every program has 3 built-in streams - stdin, stdout, stderr]]
- [[Pipe operator chains Linux commands by connecting stdout of one to stdin of another]]
- [[Output redirection operators write command output to files in Linux]]

## Flashcards

?
What is the basic syntax for less?

`less file.txt` opens the file in a pager for interactive viewing.

---

?
What command moves to the next page in less?

**Space** or **Page Down**.

---

?
What command moves to the previous page in less?

**b** or **Page Up**.

---

?
How do you search for a pattern in less?

Type `/pattern` to search forward or `?pattern` to search backward.

---

?
How do you go to the end of a file in less?

Type `G` (uppercase).

---

?
How do you go to the start of a file in less?

Type `g` (lowercase).

---

?
How do you find the next match in less after searching?

Type `n` for next match or `N` for previous match.

---

?
Why is less preferred over cat for large files?

`less` is **memory-efficient** (one screen at a time), **interactive** (scroll, search, navigate), while `cat` dumps entire file at once.
