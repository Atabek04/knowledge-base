---
created: 2026-05-14
aliases: [cat]
tags: [linux, cli-tools, cat]
---

`cat` (**con**c**at**enate) reads one or more files and writes their contents to stdout in order. Named for concatenation, but most often used to dump a single file or pipe content into another command.

## Why use cat?

Quick view of small files. Merge files. Feed file content into a pipeline. Create files via heredoc or redirection.

---

What is the basic syntax?

`cat file.txt` prints a single file. `cat a.txt b.txt > merged.txt` concatenates multiple files into one.

---

What does the `-n` flag do?

Numbers **all** output lines. `-b` numbers only non-blank lines.

---

When should you NOT use cat?

For **large files** — `cat` dumps everything at once, flooding the terminal. Use `less` instead. Also avoid the "useless use of cat" anti-pattern: `cat file | grep x` → just `grep x file`.

## Common flags

| Flag | Purpose |
|------|---------|
| `-n` | number all lines |
| `-b` | number non-blank lines |
| `-A` | show all (tabs as `^I`, line endings as `$`) |
| `-s` | squeeze multiple blank lines into one |
| `-E` | show line endings as `$` |
| `-T` | show tabs as `^I` |

## Common examples

```bash
# Print file
cat file.txt

# Concatenate into a new file
cat header.txt body.txt footer.txt > combined.txt

# Append a file's contents to another
cat extra.txt >> log.txt

# Reveal hidden whitespace / line endings
cat -A file.txt

# Create a small file inline
cat > notes.txt
type some text
press Ctrl+D to end
```

## Read more

- [[less command displays files one screen at a time with navigation and search]]
- [[Heredoc passes multi-line text as stdin using cat and EOF marker]]
- [[Output redirection operators write command output to files in Linux]]
- [[Linux MOC]]
