---
created: 2025-01-04
tags: [git/fundamentals]
sr-due:
sr-interval:
sr-ease:
---

# Distributed VCS gives every developer a full repository copy

Version control systems fall into three categories: local, centralized, and distributed.

**Local VCS** (e.g., RCS): Tracks versions on a single machine. No collaboration support—just file history on your computer.

**Centralized VCS** (e.g., SVN, CVS): Single server holds the repository. Developers checkout files, make changes, commit back to server. Requires network access for most operations. Single point of failure—if server dies, history is lost.

**Distributed VCS** (e.g., Git, Mercurial): Every developer clones the entire repository including full history. You can commit, branch, view history—all offline. The "server" is just another repository you sync with.

**Git's advantages as DVCS:**
- Work offline: commit, branch, view history without network
- No single point of failure: any clone can restore the project
- Fast operations: everything is local
- Flexible workflows: peer-to-peer, centralized, or hybrid

The "origin" remote is a convention, not a requirement. You can push/pull between any repositories. GitHub/GitLab are just convenient central meeting points, not architectural necessities.

## Links
- [[Git MOC]]
