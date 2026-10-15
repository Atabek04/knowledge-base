TARGET DECK: Tech-KB::DevOps::Deployment Environments
Tags: devops deployment-environments
**Related:** [[DevOps - MOC]]

START
Coding Questions
Deployment environments: what is an **integration environment** (dev) for, and why is it allowed to break?
Back: It **integrates** every merged change into one running system, deployed automatically many times a day.
- Breaking is its job: each failure caught here never reaches a tester or a user
Tags: devops deployment-environments
<!--ID: 1791957189100-->
END

START
Coding Questions
Why must the **QA environment** stay frozen while testers work on it?
Back: So a failing check means a **real bug**, not a new deploy that landed mid-run.
- QA receives a chosen build on a slow schedule and keeps it until testing finishes
Tags: devops deployment-environments
<!--ID: 1791957189223-->
END

START
Coding Questions
Why does one shared server fail both developers and testers?
Back:
- **Developers** need it to change constantly
- **Testers** need it to never change during a run
Merged, either deploys stop while QA tests, or QA files bugs caused by half-finished work.
Tags: devops deployment-environments
<!--ID: 1791957189320-->
END

START
Coding Questions
QA vs UAT: which question does each one ask about a build?
Back:
- **QA**: "did we build it **right**?" (matches the specification)
- **UAT**: "did we build the **right thing**?" (serves the business)
Key: QA judges against the spec, UAT judges against real needs.
Tags: devops deployment-environments testing
<!--ID: 1791957189408-->
END

START
Coding Questions
Why is it called user **acceptance** testing (UAT), and what does it produce?
Back: From contracts: the client **accepts** delivery, like a buyer accepting goods.
- It produces a **formal sign-off** that authorizes the release
Tags: devops deployment-environments testing
<!--ID: 1791957189474-->
END

START
Coding Questions
What must already be true before UAT starts?
Back: **QA has passed the build.** Business users should never be the ones finding broken APIs or missing validation.
Tags: devops deployment-environments testing
<!--ID: 1791957189596-->
END

START
Coding Questions
Which kinds of company usually have **no** UAT environment, and which keep one?
Back:
- **No UAT**: product companies with no external client; the product owner reviews on staging or a preview, and sign-off is a merge approval
- **Keep UAT**: contractual or regulated work (outsourcing, banks, government, healthcare)
Tags: devops deployment-environments testing
<!--ID: 1791957189696-->
END

START
Coding Questions
What is a **staging** environment, and where does the name come from?
Back: An environment matching production as closely as possible (same infrastructure, configuration, production-sized data) to try a release before users see it.
- Name: a **staging area**, where things are assembled and checked before the final move
Tags: devops deployment-environments
<!--ID: 1791957189791-->
END

START
Coding Questions
Staging tests the **deploy**, not just the code. Name the kinds of failure it catches that QA cannot (four).
Back:
- **Migrations** run against realistic data volume (duration, locking)
- **Configuration**: real secrets, timeouts, certificates, toggles
- **Infrastructure**: real load balancer, autoscaling, network rules
- **Performance**: load tests on production-class hardware
Tags: devops deployment-environments
<!--ID: 1791957189864-->
END

START
Coding Questions
Why must staging receive the exact artifact that will go to production, not a rebuild?
Back: A rebuilt binary makes the rehearsal test **something other than what ships**; promoting one immutable artifact keeps the bytes identical.
Tags: devops deployment-environments
<!--ID: 1791957189965-->
END

START
Coding Questions
What must happen to production data before it is copied into staging?
Back: It must be **anonymized**. Real customer records in a less protected environment are a breach waiting to happen.
Tags: devops deployment-environments
<!--ID: 1791957190074-->
END

START
Coding Questions
What is the general rule for when a team adds another deployment environment?
Back: When **two groups need the same server for incompatible work** and keep corrupting each other's results.
- An environment that settles no such collision is pure overhead
Tags: devops deployment-environments
<!--ID: 1791957190153-->
END

START
Coding Questions
Why does running a **load test on the QA box** justify a separate staging environment?
Back: The load makes the app slow, so testers report slowness that is **not a bug**; QA hardware is also too cheap to rehearse a real deploy.
Tags: devops deployment-environments
<!--ID: 1791957190252-->
END

START
Coding Questions
Environment count by company type: typical setup for a **startup**, an **enterprise or regulated** company, and a **test-in-production** team?
Back:
- **Startup**: dev, staging, prod (QA happens on staging)
- **Enterprise / regulated**: dev, QA, UAT, staging, prod (auditors and contracts require acceptance)
- **Test-in-production**: local, CI, prod (no staging)
Key: the count reflects regulation and team size, not engineering skill.
Tags: devops deployment-environments
<!--ID: 1791957190342-->
END

START
Coding Questions
What is **environment drift**?
Back: The gradual **drifting apart** of staging and production as manual fixes, config changes, data growth and traffic patterns pile up on one side only.
Tags: devops deployment-environments
<!--ID: 1791957190427-->
END

START
Coding Questions
Which differences between staging and production can never be fixed, however carefully staging is maintained?
Back: Everything that comes from **real users**: real traffic volume, concurrency, geographic spread and strange inputs. Staging has no users, so it never sees them.
Tags: devops deployment-environments
<!--ID: 1791957190517-->
END

START
Coding Questions
"Testing in production": what does it mean, and what does it **not** mean?
Back:
- **Means**: moving the final check into production behind guardrails (feature flags, canary releases, observability, fast rollback)
- **Does not mean**: testing less. Without those guardrails it is just shipping untested code to users
Tags: devops deployment-environments
<!--ID: 1791957190619-->
END

START
Coding Questions
Why is a **canary release** called that?
Back: The new version takes a small slice of traffic first, like the **canary miners carried** to detect gas before it reached them.
Tags: devops deployment-environments
<!--ID: 1791957190712-->
END

START
Coding Questions
What is an **ephemeral preview environment**?
Back: A complete, isolated copy of the app that CI creates for **one pull request** and destroys on merge or close.
- *Ephemeral*: Greek for "lasting a day"
- Usually: own namespace, own seeded database, a unique URL posted on the PR
Tags: devops deployment-environments
<!--ID: 1791957190809-->
END

START
Coding Questions
What two problems of a **shared** QA or staging server do per-PR preview environments solve?
Back:
- **Queueing**: parallel changes stop waiting for one server
- **Blame**: with no shared state, a failure points to exactly one change
Tags: devops deployment-environments
<!--ID: 1791957190894-->
END

START
Coding Questions
What is the hard part of preview environments, and which data must they never use?
Back: **Dependencies**: databases, queues, third-party APIs, other services. Spinning up the app itself is easy.
- Never **production data**: previews are short-lived, shared by link, and weakly protected
Tags: devops deployment-environments
<!--ID: 1791957191016-->
END
