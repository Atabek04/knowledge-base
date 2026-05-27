---
created: 2026-01-21
tags: [linux, cli-tools, text-processing, grep, regex]
---

The `grep` command searches for lines matching text patterns in files or standard input. The name stands for "**G**lobally search a **R**egular **E**xpression and **P**rint." It's one of the most powerful text-filtering tools in Linux and works with regular expressions for flexible pattern matching.

## What does grep do fundamentally?

`grep` searches through text and prints only the lines that match a given **pattern**. It can search files or read from stdin (often through pipes), making it versatile for filtering command output.

---

What is the basic syntax for grep?

The basic syntax is `grep "pattern" file.txt`. You can also pipe output to grep like `command | grep "pattern"` to filter results.

---

What does the -i flag do with grep?

The `-i` flag makes grep search **case-insensitive**, so `grep -i "ERROR"` will match "error", "ERROR", "Error", and any other case variation.

---

What does the -r flag do with grep?

The `-r` flag performs a **recursive search** through directories and subdirectories, allowing you to search all files in a folder structure with `grep -r "pattern" directory/`.

---

What other tools can perform similar text search operations?

Similar tools include: **awk** (extract columns), **sed** (replace/transform text), **rg** (faster grep alternative), **fzf** (interactive fuzzy search), **find** (search by filename).

---

What does the `-E` flag do?

Enables **extended regex** (ERE) — no backslash escaping for `+`, `?`, `{}`, `()`, `|`. Write `grep -E "foo|bar"` instead of `grep "foo\|bar"`. Equivalent to the deprecated `egrep`.

---

What do `-A`, `-B`, `-C` show?

**Context** around matches: `-A N` prints N lines **after** each match, `-B N` prints N lines **before**, `-C N` prints N lines on **both** sides. Useful for reading log errors with surrounding context.

---

What does `-o` do?

Prints **only the matched portion** of each line, not the whole line. Useful for extracting values: `grep -oE '[0-9]+' file` pulls every number.

## Full flag reference

| Flag | Purpose |
|------|---------|
| `-i` | case-insensitive |
| `-r` | recursive into directories |
| `-n` | show line numbers |
| `-c` | count matching lines |
| `-v` | invert match (non-matching lines) |
| `-E` | extended regex (no escaping for `+ ? \| ( ) { }`) |
| `-F` | fixed-string match (no regex — fast literal search) |
| `-w` | match whole words only |
| `-x` | match whole lines only |
| `-o` | print only matched portion |
| `-l` | print only **filenames** with matches |
| `-L` | print only filenames **without** matches |
| `-A N` | print N lines after match |
| `-B N` | print N lines before match |
| `-C N` | print N lines before and after (context) |
| `-q` | quiet — exit 0 if match found, no output (for scripts) |
| `--include="*.ext"` | restrict recursive search to filename pattern |
| `--exclude-dir=dir` | skip directory during recursive search |

## Common Examples

```bash
# Search in a file
grep "error" file.log

# Search in command output (pipe)
ps aux | grep java

# Recursive search in directory
grep -r "function_name" src/

# Case-insensitive search
grep -i "ERROR" file.log

# Show line numbers
grep -n "pattern" file.txt

# Count matching lines
grep -c "pattern" file.txt

# Invert match (show non-matching lines)
grep -v "pattern" file.txt

# Extended regex - alternation without escaping
grep -E "error|warning|fatal" app.log

# Context: 3 lines around each match
grep -C 3 "Exception" app.log

# Only the matched part (extract IPs)
grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" access.log

# Whole word match (won't match "testing" when searching "test")
grep -w "test" file.txt

# Fixed-string (no regex) — match a literal "a.b.c"
grep -F "a.b.c" file.txt

# Just list filenames containing the pattern
grep -rl "TODO" src/

# Restrict recursive search to certain files
grep -rn "deprecated" . --include="*.java"

# Quiet mode in scripts
if grep -q "ERROR" app.log; then echo "found"; fi
```

## Related Notes

- [[Pipe operator chains Linux commands by connecting stdout of one to stdin of another]]
- [[Every program has 3 built-in streams - stdin, stdout, stderr]]
- [[Shell interprets user commands and translates them into system calls for the kernel]]

## Flashcards

?
What does grep stand for?

**G**lobally search a **R**egular **E**xpression and **P**rint.

---

?
What is the basic grep syntax?

`grep "pattern" file.txt` or `command | grep "pattern"`

---

?
What does grep -i do?

Performs **case-insensitive** search, matching any case variation of the pattern.

---

?
What does grep -r do?

Performs **recursive** search through directories and subdirectories.

---

?
What does grep -n do?

Shows **line numbers** of matching lines.

---

?
What does grep -c do?

**Counts** the number of matching lines.

---

?
What does grep -v do?

Shows lines that do **NOT** match the pattern (**invert** match).

---

?
How would you search for "error" in all .log files recursively?

`grep -r "error" . --include="*.log"` or `find . -name "*.log" -exec grep "error" {} \;`
