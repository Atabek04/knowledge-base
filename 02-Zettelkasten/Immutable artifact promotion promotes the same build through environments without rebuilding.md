---
created: 2026-05-21
tags: [git/workflow, branching-strategy, deployment]
aliases: [immutable artifact promotion, artifact promotion]
sr-due:
sr-interval:
sr-ease:
---

# Immutable artifact promotion promotes the same build through environments without rebuilding

**Build once, promote many times.** Every commit to trunk produces a versioned artifact — Docker image, JAR, or binary — tagged with the commit SHA. That same artifact moves through environments unchanged.

```
trunk commit → build artifact (sha: a1b2c3)
    └─▶ deploy to staging  (same artifact)
    └─▶ deploy to prod     (same artifact)
```

**Promotion is a config/deploy action, not a git operation.** No re-merge, no new branch, no rebuild. The environment config (e.g. Helm values, deploy pipeline) points to the new artifact tag.

**Consequences:**
- "What's in staging?" → read the deployed artifact tag.
- Release notes are auto-generated from commits between the last two deploy tags.
- The substantive PR description is written once when the feature merged to trunk. There is no promotion MR.
- Bugs from "works in staging, fails in prod" caused by differing builds are eliminated — the bytes are identical.

**Standard at:** Google, Facebook, Netflix, Spotify — all run [[Trunk-based development keeps a single main branch with short-lived feature branches|trunk-based]] and pair it with this model.

**Contrast:** [[GitLab Flow uses environment branches as sequential deploy stages|GitLab Flow]] promotes by merging between environment branches. That requires a promotion MR but adds a git-visible deploy ledger.

### Read more

- [[Trunk-based development keeps a single main branch with short-lived feature branches]]
- [[GitLab Flow uses environment branches as sequential deploy stages]]
- [[Tag-driven promotion deploys by tagging commits rather than merging between environment branches]]
- [[Git MOC]]
