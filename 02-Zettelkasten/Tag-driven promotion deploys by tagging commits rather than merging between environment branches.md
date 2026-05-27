---
created: 2026-05-21
tags: [git/workflow, branching-strategy, deployment]
aliases: [tag-driven promotion, tag-driven deployment]
sr-due:
sr-interval:
sr-ease:
---

# Tag-driven promotion deploys by tagging commits rather than merging between environment branches

**Promotion without branches.** Instead of merging dev → test → prod, tag a commit on dev as `test-x.y.z`. CI detects the tag pattern and deploys to the matching environment.

```
dev:  ──●──●──●──●──●
                ↑
           tag: test-1.4.0  →  CI deploys to test
                        ↑
                   tag: release-1.4.0  →  CI deploys to prod
```

**No test or prod branch needed.** The tag is the deploy record. `git log --simplify-by-decoration` shows the full promotion history.

**Key benefits:**
- Eliminates promotion MRs and their duplicate descriptions entirely.
- No merge conflicts between environment branches.
- Rollback = deploy the previous tag. No revert commit or branch gymnastics.
- Works naturally with [[Immutable artifact promotion promotes the same build through environments without rebuilding|artifact promotion]] — the tag identifies both the commit and the artifact version.

**Tag naming conventions vary:**
- `test-1.4.0` / `release-1.4.0` (semantic)
- `staging/2026-05-21` (date-based)
- `deploy/prod/a1b2c3` (SHA-based)

**Contrast with [[GitLab Flow uses environment branches as sequential deploy stages|GitLab Flow]]:** environment branches give a persistent, human-readable deploy ledger in git; tag-driven promotion is lighter-weight but requires reading CI/CD tooling to know current state.

### Read more

- [[Immutable artifact promotion promotes the same build through environments without rebuilding]]
- [[GitLab Flow uses environment branches as sequential deploy stages]]
- [[Trunk-based development keeps a single main branch with short-lived feature branches]]
- [[Git MOC]]
