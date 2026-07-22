---
created: 2026-06-24
tags: [incident]
aliases: [phantom 401, ClickHouse view desync, masked 500, applicant_iin null]
severity: high
status: resolved
---

> Report-service drill-down returned an empty-body **401** on every detail request. The token was fine — the real fault was a ClickHouse `NULL` three layers down, refracted through three services into something that looked exactly like an auth failure.

---

### Symptom

`GET /api/v1/reports/{id}/details?groupKey=A` → **401, empty body**. Same JWT worked for `/summary` (200) and produced a JSON **404** for a non-existent report id. So: same endpoint, same token, *different* outcomes depending on the data.

Backend log on the failing call (the real signal, ignored by the 401):

```
ERROR ... dispatcherServlet ... threw exception
  [DataIntegrityViolationException ... Code: 349. DB::Exception:
   Cannot convert NULL value to non-Nullable type:
   ... source column applicant_iin to destination column applicant_iin
   (CANNOT_INSERT_NULL_IN_ORDINARY_COLUMN)]
```

### Impact

All drill-down **detail** reports, **every environment** (master / dev / test / prod) — the bug predated the branch under test. Aggregated summaries kept working, so the outage was partial and easy to misread as "intermittent auth flakiness." Compounded by a frontend that logged users out silently on the 401.

### Timeline

- `12:41` — first `/details` request fails; backend logs the ClickHouse `Code: 349`, client sees empty 401
- `12:41–12:46` — repeated identical failures; `/summary` and a dummy-id 404 captured as control cases
- *(analysis)* — single-service root cause documented (`drilldown-401-debugging.md`)
- *(analysis)* — new fact "unpushed branch, yet master/dev also 401" forces a cross-service investigation
- *(resolved)* — origin commit `fc87e4c` identified in core-service; `V5` view-recreate migration written; report-service handler added

### Investigation

**The status code lied.** A 401 screams "auth." But the *earliest* error in the log was a ClickHouse type error, not an auth event. Anchoring on the final status would have burned hours in the JWT filter; anchoring on the earliest log line pointed straight at the data.

**The differential cracked it open.** Three near-identical requests diverged on exactly one variable each:
- dummy id → JSON 404 (handler ran), real id → empty 401 (handler *didn't*) → the divergence is *after* auth, in error handling.
- `/summary` (aggregated, `GROUP BY`) works; `/details` (`SELECT *`) dies → the difference is *which columns are materialized*. Only `SELECT *` touches `applicant_iin`.
- `details-count` (`SELECT count()`) succeeds; `details-data` (`SELECT *`) throws → same conclusion, tighter.

**Absence of a log line was evidence.** The failing request had *no* `GlobalExceptionHandler` line (handler never caught it) and later cascade requests had *no* `JwtAuthenticationFilter` warning (no token was even sent). What was *missing* localised the fault as precisely as what was present.

**Why a 500 became a 401 (the masking cascade):** the unhandled `DataIntegrityViolationException` escaped to Tomcat's `/error` dispatch. `JwtAuthenticationFilter` is a `OncePerRequestFilter`, and `shouldNotFilterErrorDispatch()` defaults `true` → the filter is **skipped** on the error dispatch → empty `SecurityContext` → `HttpStatusEntryPoint` → empty-body 401. One genuine 500, disguised by a re-dispatch through a stripped security context.

**The boundary break.** Initial analysis stayed inside report-service and was self-consistent. Then one fact arrived: *the fix branch was never pushed, yet master and dev 401 too.* An uncommitted change cannot cause a shared failure → the mental boundary was wrong. Widened it:
- `git diff origin/master origin/dev` on the JWT signing code **exonerated auth-service** — proof by diff, not hunch.
- Pulled core-service, traced the `application_facts_view` history → commit `fc87e4c`.
- Read the frontend interceptor → found the amplifier.

### Root cause

Two stacked faults, plus an amplifier:

1. **Origin (core-service, commit `fc87e4c`, "some fixes"):** migration `V4` ran `ALTER TABLE application_analytics MODIFY COLUMN applicant_iin Nullable(String)` but did **not** recreate `application_facts_view`. ClickHouse freezes a view's output column types at creation, so the view kept emitting `applicant_iin` as non-`Nullable` `String`. Once SHEP delivered an application with no IIN, reading any `NULL` row through the view threw `Code: 349`.
2. **Mask (report-service):** the ClickHouse error had no exception handler → escaped to `/error` → re-dispatch skipped the JWT filter → reported as 401 instead of 500.
3. **Amplifier (frontend):** the axios interceptor deletes the token on *any* 401 with no refresh-retry and no redirect → every subsequent request goes out tokenless and also 401s → one detail row's `NULL` poisons the whole session and looks like a global auth outage.

Five Whys bottoms out at: **a base-object migration changed a column without refreshing its dependent view, and the change was shipped under an opaque "some fixes" message with no cross-team notice.**

### Fix

- **core-service:** `V5__recreate_application_facts_view.sql` — `DROP VIEW` + `CREATE VIEW` with the identical body, so the view re-infers `Nullable` types from the current table. No data touched.
- **report-service:** added `@ExceptionHandler(DataAccessException)` → returns honest `500 + REPORT_GENERATION_FAILED` JSON instead of the phantom 401. `WebMvcTest` proves a CH failure now returns 500, not 401.
- **frontend (ticketed):** refresh-and-retry once on 401 before clearing session + redirecting; never fire tokenless requests.

### Prevention

- **Never `ALTER` a base table under a view without recreating the view** in the same migration — ClickHouse views freeze column types at creation.
- **No CH/JDBC path should be able to escape unhandled** — a catch-all `DataAccessException` handler keeps a data fault from masquerading as an auth fault ever again.
- **A global 401 handler must distinguish "token rejected" from "any 401"** — reacting to the symptom (log out) amplifies unrelated failures into outages.
- **Opaque commit messages on schema changes** ("some fixes") are a process smell — schema migrations need a callout to downstream consumers.

---

### Lessons

- **An HTTP status says *where* a request died, not *why*.** Anchor on the earliest error in the log, not the final status code. → [[Read the error message literally before forming any theory]]
- **An unhandled error re-dispatched through another layer surfaces disguised** (500 → 401 via `/error` + a skipped filter). When a status makes no sense, look for a re-dispatch/proxy that re-evaluated the request in a stripped context.
- **Absence of an expected log line is evidence.** No handler line = it escaped; no auth-filter line = no token was sent.
- **A bug's blast radius equals whoever handles its error most aggressively.** A global handler reacting to a symptom turns a local fault into a system-wide outage.
- **When an unpushed change "causes" a shared bug, your system boundary is wrong — widen it.** The fault predates your branch or lives in a neighbor service or the client. → [[Differential debugging asks what changed since the system last worked]]
- **Exonerate a component with a diff, not a hunch.** "auth is fine" became trustworthy only after `git diff origin/master origin/dev` on the signing code showed nothing changed.
- **The differential narrows to one variable.** summary vs details, count vs data, dummy vs real id — each pair isolates the cause to its single difference. → [[Change one variable at a time when debugging to keep cause and effect clear]]

### Read more
- [[Debugging & Troubleshooting - MOC]]
- [[The Five Whys traces a symptom to its root cause by asking why repeatedly]]
