TARGET DECK: Tech-KB::Linux::Shell Scripting
Tags: linux bash scripting
**Related:** [[Linux MOC]]

START
Coding Questions
What is a shell script?
Back: A text file containing **shell commands** that runs as a program to **automate tasks** — repeatable, schedulable, supports complex logic.
Tags: linux bash scripting
END

START
Coding Questions
What are three main uses for shell scripts?
Back:
- **Automate** repetitive commands
- **Chain** multiple tools together
- **Schedule** jobs with cron
Tags: linux bash scripting
END

START
Coding Questions
How do you make a shell script executable?
Back: `chmod +x script.sh` — adds execute permission before you can run `./script.sh`
Tags: linux bash scripting
END

START
Coding Questions
What happens if you run a script without execute permission?
Back: Must explicitly call the interpreter: `bash script.sh` instead of `./script.sh`
Tags: linux bash scripting
END

START
Coding Questions
What is a shebang?
Back: The **first line** of a script — `#!<interpreter_path>` — tells the OS which program should execute the script.
Tags: linux bash scripting shebang
END

START
Coding Questions
Why is it called a shebang?
Back: From "**sharp**" (#) and "**bang**" (!) — the names of the first two characters.
Tags: linux bash scripting shebang
END

START
Coding Questions
What is the difference between `#!/bin/bash` and `#!/usr/bin/env bash`?
Back:
- `#!/bin/bash` — hardcoded path, less portable
- `#!/usr/bin/env bash` — searches PATH, more portable across systems
Tags: linux bash scripting shebang
END

START
Coding Questions
What shebang should you use for maximum portability across Unix systems?
Back: `#!/bin/sh` (POSIX shell — works on all Unix-like systems).
Tags: linux bash scripting shebang
END

START
Coding Questions
What is the primary role of a shell?
Back: A **shell** interprets user commands and translates them into **system calls** that the **kernel** executes.
Tags: linux bash shell
END

START
Coding Questions
What are the five steps a shell uses to process a command?
Back:
1. **Read** input from user/script
2. **Tokenize** (split into words)
3. **Parse** (check syntax)
4. **Expand** (variables, globs: `*`, `?`)
5. **Execute** (run command)
Tags: linux bash shell
END

START
Coding Questions
What are the three main shells and their key difference?
Back:
- **sh** — minimal POSIX standard, maximum compatibility
- **bash** — extends sh with history, aliases, arrays
- **zsh** — modern, user-friendly, context-aware completion
Tags: linux bash shell
END

START
Coding Questions
How do you create a Bash variable?
Back: `variable_name=value` — **no spaces** around the `=` sign.
Tags: linux bash variables
END

START
Coding Questions
How do you reference a variable's value?
Back: `$variable_name` or `${variable_name}` — curly braces recommended for clarity and concatenation.
Tags: linux bash variables
END

START
Coding Questions
How do you store command output in a variable?
Back: Use **command substitution**: `variable=$(command)`
Example: `today=$(date +%Y-%m-%d)`
Tags: linux bash variables
END

START
Coding Questions
What does `$#` represent in a Bash script?
Back: The **total number** of positional parameters (arguments passed to the script).
Tags: linux bash variables
END

START
Coding Questions
What does `$0` contain?
Back: The **script name** itself.
Tags: linux bash variables
END

START
Coding Questions
What is the difference between `$@` and `$*`?
Back:
- `$@` — all arguments as **separate** items (preserves quoting, better for loops)
- `$*` — all arguments as a **single** string
Tags: linux bash variables
END

START
Coding Questions
What does `$1` represent?
Back: The **first command-line argument** passed to the script.
Tags: linux bash positional-params
END

START
Coding Questions
How do you check if a required argument was provided?
Back: `if [ -z "$1" ]; then echo "Error: missing argument"; exit 1; fi`
Tags: linux bash positional-params
END

START
Coding Questions
How do you loop through all script arguments?
Back: `for arg in "$@"; do echo "$arg"; done`
Tags: linux bash positional-params
END

START
Coding Questions
What does the `read` command do?
Back: Captures **user input** from **stdin** and stores it in a variable — pauses script until user presses Enter.
Tags: linux bash read
END

START
Coding Questions
How do you display a prompt with `read`?
Back: Use the `-p` flag: `read -p "Enter value: " variable`
Tags: linux bash read
END

START
Coding Questions
How do you read a password without echoing it to the terminal?
Back: Use the `-s` flag (silent): `read -sp "Enter password: " password`
Tags: linux bash read
END

START
Coding Questions
How do you set a timeout for `read`?
Back: Use the `-t` flag: `read -t 5 -p "Enter value: " var` (stops after 5 seconds)
Tags: linux bash read
END

START
Coding Questions
What is the basic Bash if statement syntax?
Back:
```bash
if [ condition ]; then
    # commands
fi
```
Tags: linux bash conditionals
END

START
Coding Questions
What is the difference between `-eq` and `=` in Bash conditions?
Back:
- `-eq` — **numeric** comparison: `[ $num -eq 5 ]`
- `=` — **string** comparison: `[ "$str" = "value" ]`
Tags: linux bash conditionals
END

START
Coding Questions
What does `[ -f filename ]` test?
Back: Tests if a **file exists** and is a regular file.
Tags: linux bash conditionals
END

START
Coding Questions
What does `[ -d path ]` test?
Back: Tests if a **directory exists**.
Tags: linux bash conditionals
END

START
Coding Questions
What does `[ -z "$var" ]` test?
Back: Tests if a string is **empty** (zero length).
Tags: linux bash conditionals
END

START
Coding Questions
What does `[ -r filename ]` test?
Back: Tests if a file is **readable** (has read permission).
Tags: linux bash conditionals
END

START
Coding Questions
How do you use AND and OR in a Bash if statement?
Back:
- AND: `[ condition1 ] && [ condition2 ]`
- OR: `[ condition1 ] || [ condition2 ]`
Tags: linux bash conditionals
END

START
Coding Questions
What is the basic for loop syntax in Bash?
Back: `for variable in list; do ... done`
Tags: linux bash loops
END

START
Coding Questions
What is the basic while loop syntax in Bash?
Back: `while [ condition ]; do ... done`
Tags: linux bash loops
END

START
Coding Questions
How do you create a for loop over numbers 1 to 10?
Back: `for i in {1..10}; do echo $i; done`
Tags: linux bash loops
END

START
Coding Questions
How do you loop over all .txt files in the current directory?
Back: `for file in *.txt; do ... done`
Tags: linux bash loops
END

START
Coding Questions
What does `break` do in a loop?
Back: **Exits** the current loop immediately.
Tags: linux bash loops
END

START
Coding Questions
What does `continue` do in a loop?
Back: **Skips** remaining commands in the current iteration and moves to the next.
Tags: linux bash loops
END

START
Coding Questions
How do you create an infinite loop?
Back: `while true; do ... done` — must use `break` to exit.
Tags: linux bash loops
END

START
Coding Questions
How do you read lines from a file in a while loop?
Back: `while IFS= read -r line; do ... done < filename`
Tags: linux bash loops
END

START
Coding Questions
What is the basic Bash function syntax?
Back:
```bash
function_name() {
    # commands
    return value
}
```
Tags: linux bash functions
END

START
Coding Questions
How do Bash functions receive arguments?
Back: Via **positional parameters**: `$1` (first), `$2` (second), `$#` (count), `$@` (all).
Tags: linux bash functions
END

START
Coding Questions
What does `return` do in a Bash function?
Back: Sets the **exit code** — `0` for success, non-zero for failure. Access with `$?` after calling.
Tags: linux bash functions
END

START
Coding Questions
What is the difference between `echo` and `return` in a function?
Back:
- **echo** — outputs text to stdout (capture with `$()`)
- **return** — sets the exit code only (check with `$?`)
Tags: linux bash functions
END

START
Coding Questions
What does the `local` keyword do in a function?
Back: Limits a variable's scope to the **function only** — prevents polluting global scope.
Tags: linux bash functions
END

START
Coding Questions
Must Bash functions be defined before they are called?
Back: Yes — functions must be **defined before** the code that calls them.
Tags: linux bash functions
END

START
Coding Questions
Why should you always quote `$1` inside a function?
Back: To prevent **word splitting** if the argument contains spaces: `cp "$1" dest/` not `cp $1 dest/`
Tags: linux bash functions
END
