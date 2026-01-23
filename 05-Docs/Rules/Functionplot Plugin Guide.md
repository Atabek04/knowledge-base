**Quick reference for rendering math graphs in Obsidian.**

---
## Basic Syntax

```functionplot
---
title: Graph Title
xLabel: X Axis
yLabel: Y Axis
bounds: [minX, maxX, minY, maxY]
grid: true
---
f(x)=x^2
g(x)=2*x+1
```

---

## Key Points

| Element | Purpose | Example |
|---|---|---|
| `title` | Graph name | "Loss Function" |
| `xLabel` | X-axis label | "Weight (w)" |
| `yLabel` | Y-axis label | "Loss" |
| `bounds` | Axis ranges | [0, 10, 0, 25] = x: 0-10, y: 0-25 |
| `grid` | Show grid | true / false |
| `f(x)=...` | Function definition | f(x)=x^2 or f(x)=(x-5)^2 |

---
## Multiple Functions

Define each on a new line:

```functionplot
---
title: Comparison
xLabel: x
yLabel: y
bounds: [0, 5, 0, 30]
---
f(x)=x^2
g(x)=2*x+5
```

---