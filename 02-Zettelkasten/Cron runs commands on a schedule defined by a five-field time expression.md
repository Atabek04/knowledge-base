---
created: 2026-07-01
tags: [linux, scheduling, cron, automation]
aliases: [cron, crontab, cron expression, cron job]
---

Almost every system needs work that runs *on a clock* rather than in response to a user: rotate logs at midnight, email a report every Monday, purge stale sessions each hour. On Unix systems this is the job of <mark style="background: #FFF3A3A6;">cron</mark> — a background daemon that wakes up every minute, checks a table of scheduled jobs, and runs whichever ones are due.

The name comes from *chronos* (Greek for "time") — cron is the system's timekeeper.

---

### The crontab and its five fields

Jobs live in a <mark style="background: #FFF3A3A6;">crontab</mark> ("cron table") — a plain-text file where each line is one scheduled job. A line is <mark style="background: #ABF7F7A6;">five time fields followed by the command</mark> to run:

```
┌───────── minute        (0–59)
│ ┌─────── hour          (0–23)
│ │ ┌───── day of month  (1–31)
│ │ │ ┌─── month         (1–12)
│ │ │ │ ┌─ day of week   (0–6, Sun=0)
│ │ │ │ │
* * * * *  /path/to/command
```

Each field answers *"at which values of this unit should the job fire?"* A `*` means **every** value.

- `0 0 * * *` → every day at 00:00 (midnight)
- `*/15 * * * *` → every 15 minutes
- `0 9 * * 1` → 09:00 every Monday
- `0 3 1 * *` → 03:00 on the 1st of every month

The `*/n` step syntax means "every n units"; a comma list (`0,30`) and a range (`9-17`) narrow a field further.

---

### Cron is a matching engine, not a timer

The key mental model: cron does **not** count down an interval. Every minute it asks, for each job, *"does the current wall-clock time match this expression?"* — and runs the ones that match.

<mark style="background: #FFB8EBA6;">This is why cron cannot express "every 90 minutes" cleanly</mark> — 90 minutes doesn't align to a fixed minute-and-hour pattern. Cron fires at *calendar positions*, not on elapsed durations. When you need "N units after the last run finished," that is a **fixed-delay** interval, a different model (see [[Spring @Scheduled runs a method on a fixed interval or cron expression]]).

---

### Six-field variants add seconds

Standard Unix cron has **five** fields; its finest granularity is one minute. Schedulers built for applications — Quartz, and Spring's own `CronExpression` — prepend a **seconds** field, giving six:

```
second minute hour day-of-month month day-of-week
0      0      9    *            *     MON-FRI      → 09:00:00 on weekdays
```

Same matching model, one unit finer. When reading a cron string, always check whether the source is 5-field (OS cron) or 6-field (app scheduler) — the fields shift by one.

---

### Read more

- [[Spring @Scheduled runs a method on a fixed interval or cron expression]]
- [[Shell scripts automate Linux tasks by combining multiple commands in a text file]]
- [[Linux MOC]]
