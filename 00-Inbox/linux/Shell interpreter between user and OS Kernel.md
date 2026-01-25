
> Shell - command interface (bash, zsh, sh)
> OS/Kernel - core system managing resources (CPU, memory, processes, files)

---
#### How they work together

```bash
ls /home          # User types command
```
  
- Shell interprets and converts to system call
- Kernel executes (reads directory, manages memory)
- Returns results to shell

```bash
drwxr-xr-x user    # Shell displays output
```

---
**Shell → Kernel communication**

Shell makes system calls (requests to kernel):
- open() — open file
- read() — read data
- fork() — create process
- execve() — execute program
---
### Shell Implementations

| Shell | Origin | Key Feature | Common Use |
|-------|--------|------------|-----------|
| **sh** (Bourne) | 1979 | Minimal, POSIX standard | System scripts, portability |
| **bash** | 1989 | Extended sh, history/aliases | Linux default, most scripts |
| **zsh** | 1990 | Modern, user-friendly | macOS default (now), enthusiasts |
| **ksh** | 1983 | Fast, scripting-focused | System administration |
| **fish** | 2005 | Modern syntax, interactive | Beginners, desktop use |

---
#### How They Read Commands (Parsing)

All shells follow similar pattern:

```
1. Read input from user/script
2. Tokenize (split into words)
3. Parse (check syntax)
4. Expand (variables, globs: *, ?)
5. Execute (run command)
```

**Parsing Differences:**

| Aspect | sh | bash | zsh |
|--------|----|----|-----|
| **Variables** | `$var` | `$var`, `${var}` | `$var`, `${var}` |
| **Arrays** | ❌ None | ✅ `arr=(a b c)` | ✅ `arr=(a b c)` |
| **Functions** | Basic | Advanced | Advanced |
| **Tab completion** | None | Basic | Smart, context-aware |
| **History** | None | Yes | Yes + shared |
| **Syntax** | Strict POSIX | POSIX + extensions | POSIX + modern extensions |

---

#### Key Takeaway

- **sh** = Bare minimum, maximum compatibility
- **bash** = sh + features, backward compatible
- **zsh** = Modern, user experience focused, not always POSIX

For scripts: use **sh** or **bash**
For interactive shell: use **bash** or **zsh**
