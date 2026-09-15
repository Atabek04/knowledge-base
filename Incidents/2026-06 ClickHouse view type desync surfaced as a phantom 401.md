---
created: 2026-06-24
tags: [incident]
aliases: [phantom 401, ClickHouse view desync, masked 500]
severity: high
status: resolved
---

> A detail endpoint returned an empty-body 401 on every request while the token was fine. The real fault was a ClickHouse NULL three layers down, re-dispatched through a stripped security context until it looked like an auth failure.

### Symptom

Detail requests: 401, empty body. The aggregated summary endpoint and a 404 for a fake id worked with the same JWT, so the divergence was after auth. The earliest log line on the failing call was a ClickHouse `Cannot convert NULL value to non-Nullable type` error, not an auth event.

### Root cause

A migration made a base-table column `Nullable` without recreating the view over it. ClickHouse freezes a view's column types at creation, so the first NULL row threw on read. The exception had no handler, escaped to the `/error` dispatch, and the JWT filter (a `OncePerRequestFilter`, which skips error dispatches by default) never ran there: empty context, 401. The frontend then dropped the token on any 401, turning one bad row into a session-wide outage.

### Where to look next time

- A status code that makes no sense: read the earliest error in the log, then look for a re-dispatch or proxy that re-evaluated the request in a stripped context.
- A missing log line (no handler, no auth filter) localises the fault as well as a present one.
- An unpushed branch "causing" a shared failure means the system boundary is wrong; widen it and exonerate components by diff.

### Lessons

- [[Read the error message literally before forming any theory]]
- [[Differential debugging asks what changed since the system last worked]]
- [[Change one variable at a time when debugging to keep cause and effect clear]]
- [[The Five Whys traces a symptom to its root cause by asking why repeatedly]]

### Read more
- [[Debugging & Troubleshooting - MOC]]
