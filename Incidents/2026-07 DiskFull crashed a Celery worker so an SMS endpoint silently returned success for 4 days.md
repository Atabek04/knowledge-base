---
created: 2026-07-28
tags: [incident]
aliases: [SMS silent fail, Celery DiskFull crash, send-code false success]
severity: high
status: resolved
---

> A send-code endpoint answered success for four days while zero SMS went out. The API reported queuing, not delivery, and nothing downstream of the queue was alive to tell the difference.

### Symptom

Every call returned `{"sent": true}`. No error, no 5xx, no alert. Users never received the SMS.

### Root cause

A daily Celery Beat task wrote placeholder rows into a table that had no matching cleanup job; two years later the table filled the disk. A Postgres write then threw `DiskFull`, the worker crashed, restarted into the same write, and crash-looped until systemd's start-limit marked the unit `failed` and stopped retrying. The endpoint enqueued `send_sms` with `.delay()` and returned success as soon as the broker accepted the task, so with no consumer alive it kept saying yes.

### Where to look next time

- A fire-and-forget queue reports queuing, not delivery: check worker liveness (`systemctl status`, `journalctl`) before trusting the API.
- A crash-looping systemd unit goes silent, not loud: absence of new crash logs is not health. Alert on unit state.
- Every recurring task that writes rows needs a paired cleanup job, decided when the task is written.

### Lessons

- Fire-and-forget task queues report queuing, not delivery.
- Unbounded write-only tables eventually take down the disk that hosts them.

### Read more
- [[Debugging & Troubleshooting - MOC]]
