---
created: 2026-01-21
tags: [linux, cli-tools, redirection, stdout-stderr]
---

Output redirection operators in Linux allow you to redirect command output to files instead of the terminal. The `>` operator overwrites files, `>>` appends, and `2>` redirects errors. These operators work with the **stdout** and **stderr** streams to control where output goes.

## What is the difference between > and >>?

The `>` operator **overwrites** the file, replacing its entire contents with the new output. The `>>` operator **appends**, adding output to the end of the file without removing existing content.

---

What does 2> do?

The `2>` operator redirects **stderr** (error messages, file descriptor 2) to a file instead of the terminal. Use `2>` for errors and `>` for normal output.

---

How do you redirect both stdout and stderr to the same file?

Use `2>&1` to redirect stderr (2) to stdout (1), then redirect stdout to the file: `command > output.txt 2>&1` or use the shorthand `&>` on modern systems.

---

What is the syntax for redirecting stderr separately from stdout?

Use separate redirection operators: `command > output.txt 2> errors.txt` sends normal output to output.txt and errors to errors.txt.

---

Can you redirect input as well as output?

Yes, the `<` operator redirects a file to **stdin**: `command < input.txt` reads from the file instead of the keyboard.

---

## Redirection Operators Reference

| Operator | Purpose | Example |
|----------|---------|---------|
| `>` | Redirect stdout (overwrite) | `command > file.txt` |
| `>>` | Redirect stdout (append) | `command >> file.txt` |
| `2>` | Redirect stderr (overwrite) | `command 2> errors.txt` |
| `2>>` | Redirect stderr (append) | `command 2>> errors.txt` |
| `&>` | Redirect stdout + stderr | `command &> output.txt` |
| `<` | Redirect input from file | `command < input.txt` |
| `<<` | Here document | `command << EOF ... EOF` |

## Common Examples

```bash
# Save grep results to file
grep "error" logs.txt > errors.txt

# Append output to file
echo "new line" >> errors.txt

# Save multiple commands output
cat file1.txt | grep "pattern" > results.txt

# Pipe and redirect
ps aux | grep java > processes.txt

# Redirect stderr (errors only)
command 2> errors.log

# Redirect both stdout and stderr
command > output.txt 2>&1

# Save output and suppress errors
command > output.txt 2>/dev/null

# Read input from file
sort < unsorted.txt > sorted.txt

# Use multiple redirections
cat file1.txt file2.txt > combined.txt 2> errors.txt
```

## Common Pitfalls

```bash
# WRONG - stderr still goes to terminal
grep "pattern" file.txt > output.txt

# CORRECT - redirect stderr separately
grep "pattern" file.txt > output.txt 2> errors.txt

# WRONG - appending to overwrites previous
command1 > file.txt
command2 > file.txt  # This overwrites command1's output

# CORRECT - use append
command1 >> file.txt
command2 >> file.txt  # This keeps both outputs
```

## Related Notes

- [[Every program has 3 built-in streams - stdin, stdout, stderr]]
- [[Pipe operator chains Linux commands by connecting stdout of one to stdin of another]]
- [[Shell interprets user commands and translates them into system calls for the kernel]]

## Flashcards

?
What does > do in shell redirection?

Redirects **stdout** to a file, **overwriting** any existing contents.

---

?
What does >> do in shell redirection?

Redirects **stdout** to a file, **appending** to the end without overwriting.

---

?
What does 2> do?

Redirects **stderr** (file descriptor 2) to a file.

---

?
What does 2>&1 accomplish?

Merges **stderr** (2) to **stdout** (1) so both go to the same destination.

---

?
What is the &> operator used for?

Redirects both **stdout** and **stderr** to the same file (modern syntax).

---

?
What does < do?

Redirects a file to **stdin** (input) instead of reading from keyboard.

---

?
How would you save output and errors separately?

`command > output.txt 2> errors.txt`

---

?
How would you suppress error messages?

Redirect stderr to `/dev/null`: `command 2>/dev/null`
