---
created: 2026-06-23
tags: [orchestration/kubernetes]
aliases: [startup probe]
---

Some apps boot slowly — a JVM warming up, a large cache loading, migrations running. During that window the app isn't dead, it's just not up yet. A [[A failing liveness probe makes the kubelet restart the container|liveness probe]] that fires too early would see failures and <mark style="background: #FF5582A6;">restart the container before it ever finishes starting</mark>, looping forever.

The **startup probe** exists to break that loop. Its job: <mark style="background: #FFF3A3A6;">tell the kubelet "the app has finished booting" — and until it succeeds, liveness and readiness probes are held back entirely.</mark>

---

#### How it changes the timeline

```
Container starts
  └─ startup probe runs (generous timeout, e.g. up to 5 min)
        └─ once it succeeds → liveness + readiness take over
        └─ if it never succeeds within its budget → container is restarted
```

The startup probe gets a long failure budget for the boot phase; once it passes, the [[Kubernetes probes let the kubelet check container health the app reports|other probes]] run on their normal short intervals.

The win: <mark style="background: #ADCCFFA6;">you keep liveness aggressive for a running app</mark> (fast restart when it wedges) <mark style="background: #ADCCFFA6;">without punishing a slow start.</mark> Without a startup probe you'd have to slacken liveness with a large `initialDelaySeconds`, which then makes real deadlocks slow to detect.

---

### Read more
- [[Kubernetes probes let the kubelet check container health the app reports]]
- [[A failing liveness probe makes the kubelet restart the container]]
- [[A failing readiness probe removes the pod from Service endpoints]]
- [[DevOps - MOC]]
