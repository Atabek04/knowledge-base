---
created: 2025-01-04
tags: [git/automation]
sr-due:
sr-interval:
sr-ease:
---

# Git hooks automate actions at specific points in the workflow

**Git hooks** are scripts that run automatically before or after Git events like commits, pushes, or merges. They enable automation, policy enforcement, and integration with other tools.

Hooks live in `.git/hooks/` directory. Each hook is an executable script named after the event it handles.

**Client-side hooks (run locally):**
- `pre-commit` — runs before commit; abort if exits non-zero (lint, format, test)
- `commit-msg` — validate/modify commit message
- `pre-push` — runs before push; can run tests or checks

**Server-side hooks (run on remote):**
- `pre-receive` — reject pushes that don't meet criteria
- `post-receive` — trigger deployments, notifications

**Setting up a hook:**
```bash
cd .git/hooks
mv pre-commit.sample pre-commit
chmod +x pre-commit
# edit script content
```

**Problem:** Hooks in `.git/hooks/` aren't version controlled—each developer must set them up manually.

**Solution:** Use tools like **Husky** (Node.js) or **pre-commit** (Python) to manage hooks via config files that ARE version controlled. This ensures team-wide consistency.

Hooks can be bypassed with `--no-verify` flag, but this should be rare and justified.

## Links
- [[Git MOC]]
