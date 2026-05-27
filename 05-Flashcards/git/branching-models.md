TARGET DECK: Tech-KB::Git::Branching Models
Tags: git workflow branching-strategy
**Chapter:** Branching Models
**Related:** [[Git MOC]]

---

START
Coding Questions
What is Gitflow?
Back: A branching model (Vincent Driessen, 2010) with **two permanent branches** + three supporting types.

**Permanent:**
- `main` → production, every commit tagged with a version
- `develop` → integration branch for next release

**Supporting:**
- `feature/*` → from `develop`, back to `develop`
- `release/*` → from `develop` → merged into **both** `main` (tagged) and `develop`
- `hotfix/*` → from `main` → merged into both `main` (new tag) and `develop`

Fits **versioned software** (mobile, desktop, libraries). Bad fit for continuous delivery.
Tags: gitflow
END

START
Coding Questions
What is trunk-based development (TBD)?
Back: One long-lived branch — `main` ("trunk"). All developers integrate continuously.

**Two flavors:**
- Direct commit to trunk (small teams)
- Short-lived feature branches (**< 1–2 days**), PR-reviewed, CI-gated

**Required practices:**
- **Feature flags** → merge unfinished code dark, toggle on later
- **Fast, reliable CI** → broken trunk blocks everyone
- **No release branches** → `main` always releasable
- **Forward-fix only** → no back-porting

Standard at Google, Facebook, Netflix.
Tags: trunk-based tbd
END

START
Coding Questions
When pick Gitflow vs trunk-based?
Back:

**Gitflow** when:
- Versioned releases (mobile, desktop, libraries, on-prem)
- Must support **multiple released versions in parallel**
- Release cadence in weeks/months

**Trunk-based** when:
- Continuously deployed service (web app, API, SaaS)
- Fast CI + feature flags available
- Multiple deploys per day

Anti-patterns:
- Gitflow on daily-deploy service → release branches become bottleneck
- TBD without feature flags → half-built features ship to prod
Tags: branching-strategy decision
END

START
Coding Questions
Why do long-lived branches cause problems?
Back: Divergence cost grows with branch lifetime.
- More commits land on the base branch while the feature is open
- Eventual merge has more conflicts to resolve
- Resolving conflicts late = without context of why the changes were made
- Risk of "merge hell" — multi-day untangling
- Feature flags + short branches (< 2 days) avoid this entirely → why TBD works
Tags: branching divergence
END

START
Coding Questions
What is immutable artifact promotion?
Back: Build once from trunk commit → versioned artifact (Docker image, JAR, binary) tagged with commit SHA. That **same artifact** promotes through all environments unchanged.

- Promotion = config/deploy action, not a git operation. No re-merge, no rebuild.
- "What's in staging?" → read the deployed artifact tag.
- Release notes auto-generated from commits between deploy tags.
- PR description written once on the original trunk merge; no promotion MR.
- Eliminates "works in staging, fails in prod" divergence — bytes are identical.

Standard model at Google, Facebook, Netflix, Spotify.
Tags: artifact-promotion deployment
END

START
Coding Questions
What is GitLab Flow?
Back: Trunk-based development extended with **environment branches**: `dev → test → prod`. Each branch = what is currently deployed in that environment.

- Promotion = `--no-ff` merge to next environment branch (deploy ledger).
- Squash on feature → dev; **not** on promotion merges.
- Feature → dev MR holds the "why"; promotion MRs are terse + auto-generated PR list.
- Auto-generated bodies: `git-cliff`, `release-please`, or a CI script diffs `test..dev`.

Trade-off vs artifact promotion: git-visible deploy history, but adds merge overhead and MR duplication.
Tags: gitlab-flow environment-branches
END

START
Coding Questions
What is tag-driven promotion?
Back: Promotion without branches. Tag a commit on dev with a pattern like `test-1.4.0` → CI detects the tag and deploys to the matching environment.

```
dev: ──●──●──[tag: test-1.4.0]──●──[tag: release-1.4.0]
                  ↓                        ↓
             deploy test                deploy prod
```

- No test/prod branch needed.
- Eliminates promotion MRs entirely.
- Rollback = deploy previous tag.
- Works naturally with immutable artifact promotion.
Tags: tag-driven deployment
END

START
Coding Questions
What's the difference between trunk-based development and GitHub Flow?
Back: **GitHub Flow** is essentially trunk-based with PR gating.
- Single `main` branch
- Short-lived feature branches
- PR review required before merge
- Deploy from `main`

Pure trunk-based **direct commit** skips PR review (small teams only). GitHub Flow adds the PR gate while keeping all other TBD properties. Most "trunk-based" teams in practice run GitHub Flow.
Tags: github-flow trunk-based
END
