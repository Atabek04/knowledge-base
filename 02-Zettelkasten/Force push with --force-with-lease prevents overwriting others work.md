---
created: 2025-01-04
tags: [git/remote]
sr-due:
sr-interval:
sr-ease:
---

# Force push with --force-with-lease prevents overwriting others work

After rebasing or amending commits, you need to force push because the remote has different commit history. Regular `git push --force` is dangerous—it blindly overwrites the remote branch, potentially destroying commits pushed by teammates.

`git push --force-with-lease` is a safer alternative. It only succeeds if the remote branch is in the state you expect (based on your last fetch). If someone else has pushed commits since your last fetch, the push fails, protecting their work.

**How it works:**
1. Git checks if remote branch matches your local tracking reference
2. If matches: push proceeds, overwriting remote
3. If different: push rejected with error

**Workflow:**
```bash
git fetch origin           # update tracking refs
git rebase main            # rewrite local history
git push --force-with-lease origin feature
```

This doesn't guarantee safety—if you fetched after a teammate pushed but before you rebased, you could still overwrite their work. But it catches the most common case of concurrent pushes.

Always communicate with your team before force pushing to shared branches.

## Links
- [[Git rebase rewrites history by replaying commits on a new base]]
- [[Git MOC]]
