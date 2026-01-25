```bash
-rw-r--r-- 1 user group 1024 Jan 20 10:30 file.txt
```

#### File Type

> The first character shows you file type.

| Char | File Type        |
| ---- | ---------------- |
| -    | regular file     |
| d    | directory        |
| c    | char device file |
| l    | symbolic link    |

#### Permissions divided into 3 parts

| Char | Operation     |
| ---- | ------------- |
| r    | Read          |
| w    | Write         |
| x    | Exectue       |
| -    | No permission |

You have 3 combos of `rwx` for:
1. File owner
2. File group
3. Other
---
#### Execute permission for files

> By default, execute permission:
> - omitted in files (for security reasons)
> - directories have exec by default

Even if you created the file, and you're owner, 
you should first give exec permission and only then run.

##### Files needing exec permission:

1. Shell scripts (`.sh`, `.bash`, etc.)
2. Binary execs
3. Python/Ruby/Perl - scripts with shebang
4. Directories - exec allows entering/listing contents

> ⚠️ If script doesn't have `shebang`
> no need for exec permission

Read more:
- [[shebang - first line of a script]]

---
# 3 ways to set permission

1. Symbolic mode
2. Set permission
3. Numeric mode
---
### Adding and Removing Permission

Removing exec from all 3 types:

```bash
sudo chmod -x <fileName>
```

Add exec back to all 3:

```bash
chmod +x fileName
```

---

##### For specific types

- u = user/owner
- g = group
- o = others

```bash
# User only
chmod u+x fileName

# Group only
chmod g+x fileName

# Others only
chmod o+x fileName

# User and group
chmod u+x,g+x fileName

# All except others
chmod u+x,g+x,o-x fileName
```

---

### Writing permission block

```bash
chmod <type:u,g,o>=<permissions:rwx> fileName
```

>  ⚠️ Important: = replaces all permissions for that type. 
> Use +/- to add/remove.

```bash
# User: rwx, Group: r-x, Others: r--
chmod u=rwx,g=rx,o=r file.txt
# Result: -rwxr-xr--
```

```bash
# User: rw-, Group: rw-, Others: none
chmod u=rw,g=rw,o= file.txt
# Result: -rw-rw----
```

```bash
# All: read-only
chmod a=r file.txt
# Result: -r--r--r--
```

```bash
# User: rwx, Group: none, Others: none
chmod u=rwx,g=,o= file.txt
# Result: -rwx------
```

```bash
# Directory: User rwx, Group rx, Others rx
chmod u=rwx,g=rx,o=rx dir/
# Result: drwxr-xr-x
```

---

### Setting permissions with numeric values

```bash
chmod [3 digits] fileName
```
 
Where each digit represents:
- Position 1 = user
- Position 2 = group
 - Position 3 = others

Each digit calculated by adding these numbers:

| Symbolic | Numeric | Permission |
| -------- | ------- | ---------- |
| `---`    | 0       | None       |
| `--x`    | 1       | Execute    |
| `-w-`    | 2       | Write      |
| `r--`    | 4       | Read       |

| Symbolic | Numeric | Permission          |
| -------- | ------- | ------------------- |
| `-wx`    | 3       | Write + Exec        |
| `r-x`    | 5       | Read + Write        |
| `rw-`    | 6       | Read + Write        |
| `rwx`    | 7       | Read + Write + Exec |

```bash
chmod 754 file.txt
# Result: -rwxr-xr--

chmod 660 file.txt
# Result: -rw-rw----

chmod 764 file.txt
# Result: -rwxrw-r--

chmod 444 file.txt
# Result: -r--r--r--
```