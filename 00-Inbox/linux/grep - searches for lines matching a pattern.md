
### grep stands for

**G**lobally search a 
**R**egular 
**E**xpression and 
**P**rint

---

> `grep` - searches for lines matching a pattern in files or stdin.

```bash
grep "error" file.log
ps aux | grep java
grep -r "function_name" src/  # recursive search
grep -i "ERROR" file.log      # case-insensitive
```

---

#### Alternatives

| Command | Use Case                  |
| ------- | ------------------------- |
| `awk`   | Extract columns           |
| `sed`   | Replace/tranform text     |
| rg      | Faster `grep` alternative |
| fzf     | interactive fuzzy search  |
| find    | search by filename        |
