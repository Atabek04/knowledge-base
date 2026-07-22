---
created: 2026-07-01
tags: [spring, scheduling, cron, backend]
aliases: [Scheduled annotation, EnableScheduling, fixedRate, fixedDelay, Spring scheduling]
---

Background work on a clock — send reminder emails, expire unpaid bookings, refresh a cache — shouldn't need an external Unix [[Cron runs commands on a schedule defined by a five-field time expression|cron]] daemon shelling out to your app. Spring brings the scheduler *inside* the application: annotate a method with <mark style="background: #FFF3A3A6; font-weight: bold;">@Scheduled</mark> and the container calls it automatically on the schedule you declare.

You must switch the feature on once with <mark style="background: #ABF7F7A6;">`@EnableScheduling`</mark> on a `@Configuration` class — otherwise the annotations are silently ignored.

```java
@Configuration
@EnableScheduling
class SchedulingConfig {}

@Component
class ReminderJob {
    @Scheduled(cron = "0 0 9 * * *")   // 09:00 every day
    void sendReminders() { ... }
}
```

---

### Three ways to declare *when*

`@Scheduled` takes exactly one timing attribute:

- <mark style="background: #ABF7F7A6;">`fixedRate`</mark> — start a new run every N ms **measured start-to-start**. Runs fire on a steady drumbeat regardless of how long each takes (if one overruns, the next may queue).
- <mark style="background: #ABF7F7A6;">`fixedDelay`</mark> — wait N ms **after the previous run finishes** before starting the next. The gap is between *end* and *next start*, so slow runs push the whole schedule later.
- <mark style="background: #ABF7F7A6;">`cron`</mark> — fire at calendar positions matching a **six-field** cron expression (seconds first). This is the [[Cron runs commands on a schedule defined by a five-field time expression#Cron is a matching engine, not a timer|matching-engine]] model, not an interval.

`initialDelay` delays only the first `fixedRate`/`fixedDelay` run. `fixedRate`/`fixedDelay` express *elapsed duration*; `cron` expresses *wall-clock alignment* — pick by which question you're answering.

#### fixedRate vs fixedDelay — the mnemonic

The name says it: **rate** is a frequency you hold *fixed* (start every N ms, come what may); **delay** is a pause you hold *fixed* *after* each run (rest N ms, then go again). Rate measures start→start; delay measures end→start.

---

### One thread by default — the hidden gotcha

Out of the box Spring schedules all `@Scheduled` methods on a <mark style="background: #FFB8EBA6;">single-threaded executor</mark>. Every scheduled method across your whole app shares **one** thread, so a long-running job **blocks every other scheduled job** from firing on time. Configure a pooled `TaskScheduler` (or `@EnableScheduling` with a `ThreadPoolTaskScheduler` bean) when you have more than one job or any job that isn't near-instant.

---

### Runs once *per instance* — not once per system

`@Scheduled` fires inside **every running instance** of the application. On a single server that's fine. But deploy the same app as several replicas (pods) behind a load balancer and **each pod's scheduler fires the job independently** — the "daily reminder" now sends N times. Spring has no built-in awareness of its siblings. Coordinating "run this on exactly one instance" is a separate problem, solved by a distributed lock such as ShedLock.

---

### Read more

- [[Cron runs commands on a schedule defined by a five-field time expression]]
- [[Spring Ecosystem - MOC]]
