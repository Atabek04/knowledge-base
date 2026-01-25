# Zettelkasten Note Validation Checklist

Before moving inbox notes to `02-Zettelkasten/`, validate using this checklist.

## Validation Steps

**1. Atomicity**
- [ ] Note contains ONE atomic idea (not multiple mixed concepts)
- [ ] If multiple concepts detected → create separate notes instead

**2. Title Quality**
- [ ] Title is a **complete statement**, not a topic label
- ❌ Bad: "WebSocket", "TCP", "Async"
- ✓ Good: "WebSocket enables full-duplex communication over TCP"
- [ ] Title alone teaches something (active knowledge test)

**3. Content**
- [ ] Rephrased in own words (not copy-pasted)
- [ ] Clear, concise, useful
- [ ] Self-contained but intentionally linkable

## Feedback Framework

| Result | Action |
|--------|--------|
| ✓ **PASS** | Move to `02-Zettelkasten/[title].md` + add tags + add date |
| ⚠ **SPLIT** | Suggest atomic divisions → create separate notes first |
| ✗ **REWRITE** | Suggest title/content improvements → fix before moving |

## Post-Validation

Add to note frontmatter:
```
tags: [keyword1, keyword2]
date: YYYY-MM-DD
```

**Do NOT rewrite content.** Suggest improvements as expert mentor only.
