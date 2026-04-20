TARGET DECK: Tech-KB::Linux::Command-Line Tools
Tags: linux cli
**Related:** [[Linux MOC]]

START
Coding Questions
What are the three standard I/O streams and their file descriptor numbers?
Back:
- **stdin** (0) — standard input, data flowing INTO a program
- **stdout** (1) — standard output, normal output FROM a program
- **stderr** (2) — standard error, error messages FROM a program
Tags: linux cli streams
END

START
Coding Questions
What is the default source for stdin in a terminal?
Back: The **keyboard**.
Tags: linux cli streams
END

START
Coding Questions
What is the default destination for stdout and stderr?
Back: The **terminal screen** — both are visible on the terminal by default.
Tags: linux cli streams
END

START
Coding Questions
What does `2>` do in a shell command?
Back: Redirects **stderr** (file descriptor 2) to a file. Example: `command 2> errors.log`
Tags: linux cli streams
END

START
Coding Questions
What does `2>&1` accomplish?
Back: Merges **stderr** (2) to the same destination as **stdout** (1) — error and normal output go to the same place.
Tags: linux cli streams
END

START
Coding Questions
What does grep stand for?
Back: **G**lobally search a **R**egular **E**xpression and **P**rint.
Tags: linux cli grep
END

START
Coding Questions
What is the basic grep syntax?
Back: `grep "pattern" file.txt` or pipe output to it: `command | grep "pattern"`
Tags: linux cli grep
END

START
Coding Questions
What does `grep -i` do?
Back: Performs **case-insensitive** search — matches "error", "ERROR", "Error", etc.
Tags: linux cli grep
END

START
Coding Questions
What does `grep -r` do?
Back: Performs **recursive** search through directories and subdirectories.
Tags: linux cli grep
END

START
Coding Questions
What does `grep -n` do?
Back: Shows **line numbers** of matching lines.
Tags: linux cli grep
END

START
Coding Questions
What does `grep -c` do?
Back: **Counts** the number of matching lines.
Tags: linux cli grep
END

START
Coding Questions
What does `grep -v` do?
Back: Shows lines that do **NOT** match the pattern (inverted match).
Tags: linux cli grep
END

START
Coding Questions
What is the `less` command used for?
Back: Displaying file content **one screen at a time** — a pager that allows scrolling, searching, and navigation without loading the whole file into memory.
Tags: linux cli less
END

START
Coding Questions
Why is `less` preferred over `cat` for large files?
Back: `less` is **memory-efficient** (loads one screen at a time) and **interactive** (scroll, search, jump). `cat` dumps the entire file at once.
Tags: linux cli less
END

START
Coding Questions
What key moves to the next page in less?
Back: **Space** or **Page Down**.
Tags: linux cli less
END

START
Coding Questions
What key moves to the previous page in less?
Back: **b** or **Page Up**.
Tags: linux cli less
END

START
Coding Questions
How do you search for a pattern in less?
Back: Type `/pattern` to search forward. Use `n` for next match, `N` for previous match.
Tags: linux cli less
END

START
Coding Questions
How do you jump to the end / start of a file in less?
Back: **G** (uppercase) = end of file, **g** (lowercase) = start of file.
Tags: linux cli less
END

START
Coding Questions
What does `ls -a` do?
Back: Shows **all** files including hidden files (those starting with `.`).
Tags: linux cli ls
END

START
Coding Questions
What does `ls -l` do?
Back: Displays **long format** showing: permissions, hard link count, owner, group, size (bytes), modification date/time, filename.
Tags: linux cli ls
END

START
Coding Questions
How do you list all files including hidden ones in long format?
Back: `ls -al` or `ls -la`
Tags: linux cli ls
END

START
Coding Questions
What does the pipe operator `|` do?
Back: Connects the **stdout** of one command to the **stdin** of the next — chains commands to process data step by step.
Tags: linux cli pipe
END

START
Coding Questions
What is the basic pipe syntax?
Back: `command1 | command2` — output from command1 becomes input to command2.
Tags: linux cli pipe
END

START
Coding Questions
Does stderr get redirected through pipes by default?
Back: No — only **stdout** is piped. Use `2>&1` to merge stderr: `command1 2>&1 | command2`
Tags: linux cli pipe
END

START
Coding Questions
What does this pipeline do: `cat file.txt | grep "error" | wc -l`
Back: Reads file, filters lines containing "error", then **counts** the matching lines.
Tags: linux cli pipe
END

START
Coding Questions
What does `>` do in shell redirection?
Back: Redirects **stdout** to a file, **overwriting** any existing content.
Tags: linux cli redirection
END

START
Coding Questions
What does `>>` do in shell redirection?
Back: Redirects **stdout** to a file, **appending** to the end without overwriting.
Tags: linux cli redirection
END

START
Coding Questions
How do you save stdout and stderr to separate files?
Back: `command > output.txt 2> errors.txt`
Tags: linux cli redirection
END

START
Coding Questions
How do you suppress all error messages from a command?
Back: Redirect stderr to `/dev/null`: `command 2>/dev/null`
Tags: linux cli redirection
END

START
Coding Questions
What does the `&>` operator do?
Back: Redirects both **stdout** and **stderr** to the same file (modern shorthand for `> file 2>&1`).
Tags: linux cli redirection
END
