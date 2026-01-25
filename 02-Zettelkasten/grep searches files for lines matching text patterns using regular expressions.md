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
