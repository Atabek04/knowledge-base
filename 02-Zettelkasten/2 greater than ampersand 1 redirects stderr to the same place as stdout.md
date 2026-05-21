---
created: 2026-05-14
aliases: ["2>&1", redirect stderr to stdout, merge stderr and stdout]
tags: [linux, cli-tools, bash, redirection, streams]
---

`2>&1` is shell redirection that sends **stderr** (file descriptor 2) to wherever **stdout** (file descriptor 1) is currently going. The `&` distinguishes "file descriptor 1" from a file literally named `1`.

## Why use 2>&1?

Capture both normal output and error messages in the same place — a log file, a pipe, `/dev/null`. By default, pipes (`|`) only forward stdout; stderr bypasses them. To grep over both streams, you must merge first.

## Decoding the syntax

| Token | Meaning |
|-------|---------|
| `2` | source file descriptor (stderr) |
| `>` | redirect |
| `&1` | target = whatever fd 1 (stdout) points to right now |

Without the `&`, `2>1` would write stderr to a file named `1`.

---

What does `command > file 2>&1` do?

Sends stdout to `file`, **then** redirects stderr to the same place as stdout — both end up in `file`.

---

Why does order matter in `> file 2>&1` vs `2>&1 > file`?

Redirections evaluate **left to right**. `> file 2>&1` ✓ stdout goes to file, stderr follows. `2>&1 > file` ✗ stderr copies stdout's current target (the terminal), **then** stdout switches to file — stderr stays on terminal.

---

What is the modern shorthand?

Bash supports `&> file` — redirects both stdout and stderr to a file. Equivalent to `> file 2>&1` but shorter.

---

How do you discard all output?

`command > /dev/null 2>&1` — both streams go to the null device. Bash shorthand: `command &> /dev/null`.

## Common patterns

```bash
# Merge into log file
./build.sh > build.log 2>&1

# Pipe both streams to grep
./build.sh 2>&1 | grep -i error

# Discard everything
./noisy-script.sh > /dev/null 2>&1

# Bash shorthand (same as above two)
./build.sh &> build.log
./noisy-script.sh &> /dev/null

# Capture stderr only
./script.sh 2> errors.log

# Swap streams (stderr to terminal, stdout to file)
./script.sh > out.log 2>&1 1>/dev/tty   # rare, but possible
```

## The reverse: 1>&2

`1>&2` (or `>&2`) sends stdout **to** stderr. Useful in scripts when printing errors:

```bash
echo "fatal: config missing" >&2
exit 1
```

## Read more

- [[Every program has 3 built-in streams - stdin, stdout, stderr]]
- [[Output redirection operators write command output to files in Linux]]
- [[Pipe operator chains Linux commands by connecting stdout of one to stdin of another]]
- [[Linux MOC]]
