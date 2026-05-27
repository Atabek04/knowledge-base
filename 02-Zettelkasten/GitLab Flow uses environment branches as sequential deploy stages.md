---
created: 2026-05-21
tags: [git/workflow, branching-strategy, deployment]
aliases: [GitLab Flow, environment branches]
sr-due:
sr-interval:
sr-ease:
---

# GitLab Flow uses environment branches as sequential deploy stages

**GitLab Flow** adds environment branches to [[Trunk-based development keeps a single main branch with short-lived feature branches|trunk-based development]]: `dev → test → prod`. Each branch represents what is currently deployed in that environment.

```
feature ──▶ dev ──▶ test ──▶ prod
            ↑        ↑        ↑
          deploy   deploy   deploy
```

**Promotion = merge** from one environment branch to the next. Teams use `--no-ff` so the history shows a clear "promoted N commits from dev to test on date X" bubble — each environment branch acts as a **deploy ledger**.

**Promotion MR conventions:**
- Squash on feature → dev, not on promotion merges. Each feature becomes one clean commit on dev; promotions preserve that granularity.
- The feature → dev MR holds the substantive description ("why").
- Promotion MRs are terse: title like `Promote dev to test (2026-W21)`, body = auto-generated list of included PRs with links. No manual rewriting.

**Auto-generating promotion bodies** — tools like `release-please`, `git-cliff`, or a simple CI script diff `test..dev`, collect linked PRs, and produce a bulleted list. The "why" lives in each linked PR.

**Trade-off vs [[Immutable artifact promotion promotes the same build through environments without rebuilding|artifact promotion]]:**
- GitLab Flow preserves a git-visible deploy history; artifact promotion does not.
- Artifact promotion eliminates duplicate description writing and merge overhead entirely.
- GitLab Flow is common at teams of 5–30 engineers who want auditability without full CI/CD infrastructure.

### Read more

- [[Trunk-based development keeps a single main branch with short-lived feature branches]]
- [[Immutable artifact promotion promotes the same build through environments without rebuilding]]
- [[Tag-driven promotion deploys by tagging commits rather than merging between environment branches]]
- [[Driessen mandates --no-ff in Gitflow to preserve the feature bubble for revert]]
- [[Git MOC]]
