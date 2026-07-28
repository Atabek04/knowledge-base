---
created: 2026-07-28
tags: [incident]
aliases: [old-booking SMS silent fail, Celery DiskFull crash, send-code false success, mainapp_trialpracticeexam bloat]
severity: high
status: resolved
---

> `/send-code` kept answering `{"sent":true}` for 4 days while zero SMS went out. The API told the truth about *queuing*, not *delivery* — and nothing downstream of the queue was alive to tell the difference.

---

### Symptom

`POST /send-code` (old-booking clone, `booking-vmv`, host `tc1`) returned `{"sent":true}` on every call. No error, no 5xx, no log line hinting at failure. Users reported never receiving the SMS. Silent — API contract gave no signal anything was wrong.

### Impact

All phone-verification SMS on `tc1` since **2026-07-24**, ~4 days, zero delivered. No alert fired because nothing in the request path ever returned non-2xx.

### Root cause chain

1. **Disk exhaustion.** `tc1` root disk hit 96–100% full.
2. **Unbounded table.** A Celery Beat task, `generate_trial_practice_exams`, runs daily against `mainapp_trialpracticeexam` with **no cleanup job** — unlike its sibling `clean_null_rags_slots` (which prunes `rags`). It accumulated ~600M unbooked placeholder rows (~81GB), dating back to 2024, never pruned.
3. **Write failure → crash.** A Postgres write to `mainapp_trialpracticeexam` threw `DiskFull`. That exception propagated up and crashed `celery_worker.service`.
4. **Crash-loop → permanent death.** The worker restarted, hit the same `DiskFull` write, crashed again — repeating until systemd's `start-limit-burst` tripped. Systemd marked the unit `failed` and **stopped restarting it**. Zero workers alive from `2026-07-24` onward.
5. **API blind to worker health.** `PhoneNumberVerificationView.send-code` queues `send_sms` as an async Celery task via `.delay()`/`.apply_async()` and returns `{"sent":true}` **immediately** — success means "message reached the broker," not "a worker executed it." With no consumer alive, every task piled up in the queue and the endpoint kept reporting success regardless.

### Investigation

The status code told the truth about the wrong thing. `sent:true` is accurate for *what Django did* (enqueued a task) and false for *what the user cares about* (an SMS arrived) — two different claims wearing one boolean. Checking worker liveness (`systemctl status celery_worker`, `failed` + crash-loop in `journalctl`) surfaced the real state in seconds; the API response never would have.

### Fix

- Freed disk: pruned `mainapp_trialpracticeexam` backlog.
- Added a cleanup job for `mainapp_trialpracticeexam`, mirroring `clean_null_rags_slots`.
- Restarted and re-enabled `celery_worker.service`.
- (Follow-up, ticketed) `send-code` should reflect actual delivery/queue health, not bare enqueue success — e.g. check worker heartbeat or surface a queued-vs-delivered state.

### Prevention

- **Every recurring Celery Beat task that writes rows needs a paired cleanup job**, decided at the time the task is written — not after 2 years and 600M rows.
- **Disk usage alerting** on hosts running Postgres + Celery — `DiskFull` should page before it crash-loops a worker into `failed`.
- **`systemd` `failed` state on a queue consumer is a silent outage** — alert on unit state, don't rely on the API surface to notice.

---

### Lessons

- **Fire-and-forget task queues report queuing, not delivery.** `{"sent":true}` from an async `.delay()` call means "accepted by the broker" — it says nothing about whether any worker is alive to consume it.
- **A crash-looping systemd service goes silent, not loud.** After `start-limit-burst`, systemd stops retrying and marks the unit `failed` — no further crash noise, just permanent silence. Absence of new crash logs is not health.
- **Unbounded write-only tables eventually take down the disk that hosts them.** A Beat task with no matching cleanup job is a slow leak — 600M rows and 81GB took 2 years to surface as an outage.

### Read more
- [[Debugging & Troubleshooting - MOC]]
