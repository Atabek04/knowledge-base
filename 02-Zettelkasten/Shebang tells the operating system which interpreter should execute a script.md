---
created: 2026-01-21
tags: [linux, bash, shell-scripting, shebang]
---

The **shebang** is the first line of a script starting with `#!` followed by the path to an interpreter (e.g., `#!/bin/bash`). It tells the operating system which program should execute the script. The name "shebang" comes from "sharp" (#) and "bang" (!).

Shebangs enable running scripts directly (`./script.sh`) without explicitly specifying the interpreter.

## Why is it called shebang?

The name combines two symbols: `#` (sharp, used in music notation) and `!` (bang, an exclamation point). Together they form "sharp-bang" which was shortened to "shebang."

---

What happens if you run a script without a shebang?

Without a shebang, you must explicitly specify the interpreter: `bash script.sh` or `python3 script.py`. With a shebang and execute permission, you can run: `./script`

---

What is the difference between #!/bin/bash and #!/usr/bin/env bash?

`#!/bin/bash` directly specifies the bash location (less portable if bash is installed elsewhere), while `#!/usr/bin/env bash` uses the `env` program to search for bash in PATH (more portable and recommended).

---

What interpreters can you use in a shebang?

Any interpreter on the system: `#!/bin/bash` (shell), `#!/usr/bin/python3` (Python), `#!/usr/bin/perl` (Perl), `#!/usr/bin/env node` (Node.js), `#!/bin/sh` (POSIX shell).

---

Can a shebang make a script executable by itself?

No, the shebang alone doesn't make a script executable. You must also add execute permission with `chmod +x script.sh`. The shebang tells the OS *which* interpreter to use, but execute permission is required to *run* the script directly.

---

## Common Shebang Examples

```bash
#!/bin/bash
# Bash script

#!/bin/sh
# POSIX shell (portable)

#!/usr/bin/python3
# Python 3 script

#!/usr/bin/env python3
# Python 3 (finds in PATH, more portable)

#!/usr/bin/perl
# Perl script

#!/usr/bin/env node
# Node.js script

#!/usr/bin/ruby
# Ruby script

#!/usr/bin/env ruby
# Ruby (portable)
```

## When to Use Which Shebang

```bash
# Maximum portability (scripts run on any Unix-like system)
#!/bin/sh

# Linux-specific (assumes bash is at /bin/bash)
#!/bin/bash

# Portable (finds interpreter in PATH)
#!/usr/bin/env python3

# System-specific (if you know exact location)
#!/usr/bin/python3
```

## Script Execution Flow

```bash
# Without shebang, must specify interpreter:
bash script.sh

# With shebang and execute permission, OS finds interpreter automatically:
./script.sh
```

## Full Script Example

```bash
#!/bin/bash
# Simple file backup script

# Script content
backup_file() {
    local source=$1
    local dest=$2
    cp "$source" "$dest/$(date +%Y%m%d_%H%M%S)_$(basename "$source")"
    echo "Backed up to $dest"
}

# Call function
backup_file "/home/user/data.txt" "/backups"
```

## Related Notes

- [[Shell scripts automate Linux tasks by combining multiple commands in a text file]]
- [[Shell interprets user commands and translates them into system calls for the kernel]]
- [[Bash variables store data and command output for reuse in scripts]]
- [[Bash functions encapsulate reusable code blocks that accept parameters and return exit codes]]
- [[Linux file permissions control read, write, and execute access for owner, group, and others]]

## Flashcards

?
What does a shebang line do?

Tells the **OS** which **interpreter** to use to execute the script.

---

?
What is the format of a shebang line?

`#!<path_to_interpreter>` (e.g., `#!/bin/bash`)

---

?
Why is it called a shebang?

From "sharp" (#) and "bang" (!), combined from the first two characters.

---

?
What is the difference between #!/bin/bash and #!/usr/bin/env bash?

`#!/bin/bash` specifies exact location (less portable), `#!/usr/bin/env bash` searches PATH (more portable).

---

?
Can you run a script with a shebang but no execute permission?

No, you must use `chmod +x` to add execute permission before running with `./script`

---

?
What shebang should you use for maximum portability?

`#!/bin/sh` (POSIX shell, works on all Unix-like systems).

---

?
What shebang should you use for Python scripts?

`#!/usr/bin/env python3` (portable, finds Python 3 in PATH).

---

?
What happens if you don't have a shebang?

You must explicitly specify the interpreter: `bash script.sh` or `python3 script.py`
