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

START
Coding Questions
What does `sed` stand for and do?
Back: **Stream editor** — reads text line by line and applies edit commands non-interactively. Used for find-and-replace, deletion, insertion, extraction.
Tags: linux cli sed
END

START
Coding Questions
What is the basic sed substitute syntax?
Back: `sed 's/old/new/'` replaces first match per line. Add `g` flag for all: `sed 's/old/new/g'`.
Tags: linux cli sed
END

START
Coding Questions
What does `sed -i` do?
Back: Edits the file **in place**. Use `sed -i.bak` to keep a backup.
Tags: linux cli sed
END

START
Coding Questions
What does `sed -n '/pattern/p'` do?
Back: `-n` suppresses default printing; `p` prints only lines matching the pattern.
Tags: linux cli sed
END

START
Coding Questions
What does `sed -E` enable?
Back: **Extended regex** — no backslash escaping for `+`, `?`, `()`, `|`.
Tags: linux cli sed
END

START
Coding Questions
How do you delete blank lines with sed?
Back: `sed '/^$/d' file.txt`
Tags: linux cli sed
END

START
Coding Questions
What is the difference between `find` and `grep`?
Back: `find` searches **for** files by name/type/attribute. `grep` searches **inside** files for text patterns.
Tags: linux cli find
END

START
Coding Questions
What is the basic find syntax?
Back: `find <path> <expression>`. Example: `find . -name "*.log"`.
Tags: linux cli find
END

START
Coding Questions
What does `find -type` accept?
Back: `f` regular file, `d` directory, `l` symlink, `s` socket.
Tags: linux cli find
END

START
Coding Questions
What does `find -exec cmd {} \;` do?
Back: Runs `cmd` on each match. `{}` is the matched filename, `\;` terminates the command.
Tags: linux cli find
END

START
Coding Questions
How do you find files modified in the last 24 hours?
Back: `find . -mtime -1` (days). Use `-mmin -60` for last 60 minutes.
Tags: linux cli find
END

START
Coding Questions
How do you find files larger than 100MB?
Back: `find . -type f -size +100M`
Tags: linux cli find
END

START
Coding Questions
What does `cat` stand for?
Back: **Concatenate** — reads files and writes contents to stdout in order.
Tags: linux cli cat
END

START
Coding Questions
What is the "useless use of cat" anti-pattern?
Back: `cat file | grep x` — wastes a process. Use `grep x file` directly.
Tags: linux cli cat
END

START
Coding Questions
What does `cat -A` show?
Back: All hidden characters — tabs as `^I`, line endings as `$`.
Tags: linux cli cat
END

START
Coding Questions
What is a heredoc?
Back: Shell syntax that feeds multi-line text into a command's stdin. Form: `cmd << DELIMITER ... DELIMITER`. `EOF` is convention, not required.
Tags: linux cli bash heredoc
END

START
Coding Questions
What is the difference between `<< EOF` and `<< 'EOF'`?
Back: Unquoted `EOF` **expands** `$vars` and `$(cmds)`. Quoted `'EOF'` treats content **literally** with no expansion.
Tags: linux cli bash heredoc
END

START
Coding Questions
What does `<<-` do in a heredoc?
Back: Strips **leading tab characters** from each line, allowing indentation inside scripts. Only tabs are stripped, not spaces.
Tags: linux cli bash heredoc
END

START
Coding Questions
What does `<<<` do?
Back: **Here-string** — feeds a single string as stdin. Example: `grep foo <<< "$var"`.
Tags: linux cli bash heredoc
END

START
Coding Questions
What is the relationship between `test` and `[ ]`?
Back: `[ expr ]` is an alias for `test expr` — same command, just prettier. Spaces inside brackets are required.
Tags: linux cli bash test
END

START
Coding Questions
What does `test -f path` check?
Back: True if `path` exists **and** is a regular file (not a directory or device).
Tags: linux cli bash test
END

START
Coding Questions
Difference between test `-e`, `-f`, `-d`?
Back: `-e` exists (any type). `-f` exists and is a regular file. `-d` exists and is a directory.
Tags: linux cli bash test
END

START
Coding Questions
What does test `-z` check?
Back: String is **empty** (zero length). Opposite: `-n` (non-empty).
Tags: linux cli bash test
END

START
Coding Questions
Difference between `[ ]` and `[[ ]]` in bash?
Back: `[ ]` is the POSIX `test` command. `[[ ]]` is a Bash keyword with extras: regex `=~`, no word splitting, `&&`/`||` inside.
Tags: linux cli bash test
END

START
Coding Questions
What does curl stand for and what does it do?
Back: **Client URL** — transfers data to/from servers over HTTP, HTTPS, FTP, and many other protocols. CLI equivalent of Postman.
Tags: linux cli curl http
END

START
Coding Questions
What does `curl -X` do?
Back: Sets the HTTP method (`POST`, `PUT`, `DELETE`). Not needed for GET, or when `-d` is used (auto-sets POST).
Tags: linux cli curl http
END

START
Coding Questions
What does `curl -d` do?
Back: Sends a request **body**. `-d '{"k":"v"}'` for inline, `-d @file.json` to read from file.
Tags: linux cli curl http
END

START
Coding Questions
What does `curl -H` do?
Back: Adds a request **header**. Repeat for multiple: `-H "Authorization: Bearer ..." -H "Content-Type: application/json"`.
Tags: linux cli curl http
END

START
Coding Questions
What does `curl -i` vs `-v` show?
Back: `-i` includes response **headers** in output. `-v` is **verbose** — full request/response trace including TLS handshake. Best debugging flag.
Tags: linux cli curl http
END

START
Coding Questions
What does `curl -L` do?
Back: **Follows redirects** (3xx responses).
Tags: linux cli curl http
END

START
Coding Questions
What does `curl -fsSL` do?
Back: Common CI combo — **fail** on HTTP errors, **silent** (no progress bar), **show** errors, follow **redirects**.
Tags: linux cli curl http
END

START
Coding Questions
How do you POST JSON with curl?
Back:
```bash
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice"}'
```
Tags: linux cli curl http
END

START
Coding Questions
How do you print only the HTTP status code with curl?
Back: `curl -s -o /dev/null -w "%{http_code}\n" https://example.com`
Tags: linux cli curl http
END

START
Coding Questions
How do you upload a file with curl?
Back: `curl -X POST url -F "file=@photo.jpg"` — `-F` sends multipart/form-data.
Tags: linux cli curl http
END

START
Coding Questions
What is `jq`?
Back: CLI JSON processor — pretty-prints, extracts fields, filters arrays, transforms structure. Structure-aware `sed`/`grep` for JSON.
Tags: linux cli jq json
END

START
Coding Questions
What does the `.` filter do in jq?
Back: **Identity** — outputs input unchanged. Most common use: `curl ... | jq` to pretty-print JSON.
Tags: linux cli jq json
END

START
Coding Questions
How do you extract a nested field with jq?
Back: `jq '.user.email'` — dot-path descent. Use `.items[0]` for array index, `.items[]` for every element.
Tags: linux cli jq json
END

START
Coding Questions
What does `jq -r` do?
Back: **Raw** output — strips surrounding quotes from string values. Needed when piping into another shell command.
Tags: linux cli jq json
END

START
Coding Questions
How do you filter an array in jq?
Back: `map(select(condition))`. Example: `.users | map(select(.active == true))` keeps only active users.
Tags: linux cli jq json
END

START
Coding Questions
How do you reshape JSON objects in jq?
Back: `{newKey: .oldKey}`. Example: `.users[] | {id, name}` keeps only id and name fields.
Tags: linux cli jq json
END

START
Coding Questions
How do you pass a shell variable into a jq filter?
Back: `jq --arg uid "$USER_ID" '.users[] | select(.id == $uid)'` — `--arg` for strings, `--argjson` for JSON values.
Tags: linux cli jq json
END

START
Coding Questions
How do you "edit in place" with jq?
Back: `jq` has no `-i` flag. Use temp file: `jq '.k = "v"' file.json > tmp && mv tmp file.json`.
Tags: linux cli jq json
END

START
Coding Questions
What does `2>&1` mean?
Back: Redirects **stderr** (fd 2) to the same destination as **stdout** (fd 1). The `&` marks `1` as a file-descriptor reference, not a filename.
Tags: linux cli redirection
END

START
Coding Questions
Why does pipe order matter: `cmd > file 2>&1` vs `cmd 2>&1 > file`?
Back: Redirections apply **left to right**. `> file 2>&1` ✓ both go to file. `2>&1 > file` ✗ stderr copies stdout's current target (terminal) before stdout switches to the file — stderr stays on terminal.
Tags: linux cli redirection
END

START
Coding Questions
How do you discard all output (stdout + stderr)?
Back: `command > /dev/null 2>&1` or Bash shorthand `command &> /dev/null`.
Tags: linux cli redirection
END

START
Coding Questions
How do you pipe both stdout and stderr to grep?
Back: `command 2>&1 | grep pattern` — pipes only forward stdout by default, so stderr must be merged first.
Tags: linux cli redirection
END

START
Coding Questions
What does `echo "msg" >&2` do?
Back: Writes `msg` to **stderr** instead of stdout (`>&2` is short for `1>&2`). Standard idiom for error messages in shell scripts.
Tags: linux cli redirection
END

START
Coding Questions
What does `grep -E` do?
Back: Enables **extended regex** (ERE) — no backslash escaping for `+ ? | ( ) { }`. Example: `grep -E "foo|bar"` instead of `grep "foo\|bar"`. Equivalent to deprecated `egrep`.
Tags: linux cli grep regex
END

START
Coding Questions
What is the difference between `grep -E` and `grep -F`?
Back: `-E` = **extended regex** (metacharacters active). `-F` = **fixed strings** (no regex, treat pattern literally). `-F` is fastest for plain text search.
Tags: linux cli grep regex
END

START
Coding Questions
What do `grep -A`, `-B`, `-C` do?
Back: Print **context** lines around each match.
- `-A N` → N lines **after**
- `-B N` → N lines **before**
- `-C N` → N lines on **both** sides
Tags: linux cli grep context
END

START
Coding Questions
What does `grep -o` do?
Back: Prints only the **matched portion** of each line, not the entire line. Useful for extraction: `grep -oE "[0-9]+" file`.
Tags: linux cli grep
END

START
Coding Questions
What does `grep -w` do?
Back: Matches **whole words only** — `grep -w "test"` won't match "testing" or "contest".
Tags: linux cli grep
END

START
Coding Questions
What does `grep -l` do?
Back: Prints only the **filenames** containing matches, not the matching lines. Use `-L` for the inverse (files with no matches).
Tags: linux cli grep
END

START
Coding Questions
What does `grep -q` do?
Back: **Quiet mode** — produces no output, just exits 0 if pattern found, 1 if not. Used in shell conditionals: `if grep -q "ERROR" log; then ...`
Tags: linux cli grep
END

START
Coding Questions
How do you grep recursively but only in Java files?
Back: `grep -rn "pattern" . --include="*.java"`
Tags: linux cli grep
END
