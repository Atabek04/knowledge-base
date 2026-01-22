---
created: 2026-01-21
tags: [linux, shell, io-streams, system-calls]
---

Every running program in Linux has three standard input/output streams automatically available: standard input (stdin), standard output (stdout), and standard error (stderr). These streams are numbered 0, 1, and 2 respectively and allow programs to communicate with users and the operating system.

Understanding these streams is fundamental to working with pipes, redirection, and shell scripting since they form the basis of how data flows between commands.

## What is stdin and what is its file descriptor number?

**Standard Input (stdin)** is file descriptor **0** and represents data flowing INTO a program. By default, stdin reads from the keyboard but can be redirected to read from files or other commands using the `<` operator.

---

What is stdout and what is its file descriptor number?

**Standard Output (stdout)** is file descriptor **1** and represents normal output FROM a program. By default, stdout displays on the terminal screen but can be redirected to write to files or pipe to other commands using `>` or `|`.

---

What is stderr and what is its file descriptor number?

**Standard Error (stderr)** is file descriptor **2** and represents error messages FROM a program. By default, stderr displays on the terminal screen but can be redirected separately from stdout using `2>` to capture errors independently.

---

Why would you redirect stderr separately from stdout?

You might redirect **stderr** separately to log errors to a file while sending **stdout** to another destination, or to suppress error messages while keeping regular output visible. For example, `command > output.txt 2> errors.txt` captures output and errors separately.

---

What does the syntax 2>&1 mean when used in shell commands?

The syntax `2>&1` means redirect **stderr** (file descriptor 2) to the same place as **stdout** (file descriptor 1). This merges both streams together so error and normal output go to the same destination.

---

## Examples

```bash
# Read from file instead of keyboard
command < input.txt

# Write output to file (overwrite)
command > output.txt

# Write output to file (append)
command >> output.txt

# Write errors to separate file
command 2> errors.txt

# Merge errors and output to same file
command > output.txt 2>&1

# Read from file, write output elsewhere, error elsewhere
command < input.txt > output.txt 2> errors.txt
```

## Related Notes

- [[Pipe operator chains Linux commands by connecting stdout of one to stdin of another]]
- [[Output redirection operators write command output to files in Linux]]
- [[Shell interprets user commands and translates them into system calls for the kernel]]

## Flashcards

?
What are the three standard streams and their file descriptor numbers?

**stdin** (0) — input, **stdout** (1) — normal output, **stderr** (2) — error output.

---

?
What is the default source for stdin in a terminal?

The **keyboard**.

---

?
What is the default destination for stdout and stderr in a terminal?

The **terminal screen** (stdout) and **terminal screen** (stderr) — both visible by default.

---

?
What does 2> do in a shell command?

Redirects **stderr** (file descriptor 2) to a file.

---

?
What does 2>&1 accomplish?

Merges **stderr** (2) to the same destination as **stdout** (1), combining error and normal output.

---

?
How do you read input from a file instead of keyboard?

Use the `<` operator: `command < input.txt`

---

?
How do you append output to a file instead of overwriting?

Use the `>>` operator: `command >> output.txt`
