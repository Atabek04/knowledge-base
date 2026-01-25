---
created: 2026-01-20
tags: [vim/navigation]
---

**Vim Normal mode** uses **hjkl keys** for cursor movement instead of arrow keys, enabling efficient navigation without leaving the home row of the keyboard.

**Basic Navigation Keys**

| Key | Movement |
|-----|----------|
| `h` | Left (think: **h**ome) |
| `j` | Down (think: **j**ump down) |
| `k` | Up |
| `l` | Right |

These keys replace arrow keys entirely in Vim workflows. Using hjkl keeps your fingers on the keyboard's home row, eliminating the need to reach for arrow keys during editing sessions.

**Number Multipliers**

Any motion command can be **prefixed with a number** to repeat that motion multiple times:

- `5j` — Move down 5 lines
- `10k` — Move up 10 lines
- `20l` — Move right 20 characters
- `3h` — Move left 3 characters

**Practical Benefits**
- Faster navigation than arrow key + repeated presses
- Keeps hands positioned for efficient typing
- Scales to Vim's other commands (delete `5dd`, copy `3yy`, etc.)
- Mental model: "perform this action N times"

Once you develop muscle memory, hjkl navigation feels natural and becomes significantly faster than arrow keys. This efficiency gain compounds across hours of editing sessions.

## Links

- [[Vim MOC]] — Vim text editor fundamentals
- [[Vim operates in six primary modes with normal, insert, and visual being most commonly used]]
