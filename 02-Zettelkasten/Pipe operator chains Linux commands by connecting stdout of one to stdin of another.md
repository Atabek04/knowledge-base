---
created: 2026-01-21
tags: [linux, cli-tools, pipes, stdin-stdout]
---

The pipe operator `|` connects the standard output of one command to the standard input of another, allowing commands to be chained together to process data step by step. Pipes are fundamental to Unix philosophy and enable powerful data processing by combining simple tools.

## How does the pipe operator work?

The pipe `|` takes the **stdout** of the left command and feeds it as **stdin** to the right command. Data flows through the pipeline: `command1 | command2 | command3` where output from command1 becomes input to command2, and so on.

---

What is the basic syntax for using pipes?

The basic syntax is `command1 | command2`. You can chain multiple pipes: `command1 | command2 | command3 | command4` to process data through multiple stages.

---

Why are pipes considered a powerful Unix feature?

Pipes enable **composition** of simple, focused tools into complex data processing operations. Instead of writing one large program, you combine many small programs each doing one thing well, following the Unix philosophy.

---

Can you pipe to commands that don't accept stdin?

No, the receiving command must read from **stdin**. Most CLI tools accept stdin (grep, sort, awk, wc), but some only accept filenames as arguments. For those, use command substitution `$(...)` or redirection `<` instead.

---

What happens to stderr when using pipes?

By default, pipes only redirect **stdout**. **stderr** still goes to the terminal. To redirect stderr through a pipe, use `2>&1` to merge streams: `command1 2>&1 | command2`.

---

## Common Examples

```bash
# Search for specific lines, then count them
cat file.txt | grep "error" | wc -l

# List files, sort by name, then view with pager
ls -l | sort | less

# Find processes containing "java", show only names
ps aux | grep java | awk '{print $1}'

# Count unique users
cat /etc/passwd | cut -d: -f1 | sort | uniq | wc -l

# Complex pipeline with grep, sort, uniq
cat log.txt | grep "ERROR" | cut -d: -f1 | sort | uniq

# Pipe stderr and stdout
command 2>&1 | grep "pattern"
```

## Common Tools Used in Pipes

| Tool | Purpose |
|------|---------|
| `cat` | Display file contents |
| `grep` | Filter lines matching pattern |
| `wc` | Count lines, words, characters |
| `sort` | Sort lines alphabetically |
| `uniq` | Remove/count duplicate lines |
| `cut` | Extract columns from text |
| `awk` | Process text by columns/patterns |
| `sed` | Stream editor (find/replace) |
| `tr` | Translate/delete characters |
| `head` | Show first N lines |
| `tail` | Show last N lines |

## Related Notes

- [[Every program has 3 built-in streams - stdin, stdout, stderr]]
- [[Output redirection operators write command output to files in Linux]]
- [[grep searches files for lines matching text patterns using regular expressions]]
- [[Shell interprets user commands and translates them into system calls for the kernel]]

## Flashcards

?
What does the pipe operator | do?

Connects the **stdout** of one command to the **stdin** of the next command.

---

?
What is the basic syntax for a pipe?

`command1 | command2` where output from command1 becomes input to command2.

---

?
How do you chain multiple pipes together?

`command1 | command2 | command3 | command4` — data flows through each stage sequentially.

---

?
Does stderr get redirected through pipes?

No, by default only **stdout** is piped. Use `2>&1` to merge stderr: `command1 2>&1 | command2`

---

?
Can you pipe to any command?

Only commands that read from **stdin**. Commands that only accept filenames must use `<` redirection or `$(...)` command substitution instead.

---

?
What does this command do: cat file.txt | grep "error" | wc -l

Displays file contents, filters lines with "error", then **counts** the matching lines.

---

?
What does this command do: ps aux | grep java | awk '{print $1}'

Lists all processes, filters for "java", then extracts only the **first column** (usernames).
