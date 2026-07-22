TARGET DECK: Tech-KB::DevOps::Kubernetes
Tags: devops kubernetes probes
**Related:** [[DevOps - MOC]]

START
Coding Questions
In Kubernetes health-checking, who owns the health *logic* and who only *calls* it?
Back:
- The **application** (container) owns the logic — it implements and exposes the check
- The **kubelet** (node agent) only *calls* the check on a schedule and reacts to the result
Kubernetes does not know health by itself.
Tags: devops kubernetes probes
<!--ID: 1782190015160-->
END

START
Coding Questions
What is a Kubernetes **probe**?
Back: A diagnostic the **kubelet** runs against a container on a schedule, hitting an endpoint or command the container exposes and reading success/failure.
Tags: devops kubernetes probes
<!--ID: 1782190015192-->
END

START
Coding Questions
What are the three kinds of Kubernetes probe?
Back:
- **Liveness** — is the process alive, or wedged?
- **Readiness** — can it serve traffic right now?
- **Startup** — has the app finished booting yet?
Tags: devops kubernetes probes
<!--ID: 1782190015218-->
END

START
Coding Questions
What does the kubelet do when a **liveness** probe fails repeatedly, and why?
Back: It **restarts the container** — betting a fresh start clears a deadlock or wedged state that a still-"running" process can't recover from on its own.
Tags: devops kubernetes probes
<!--ID: 1782190015244-->
END

START
Coding Questions
What should a liveness endpoint (`/livez`) check, and what must it never check?
Back:
- **Check:** only "am I deadlocked?" → return `200` immediately. A trivial `200 OK` handler is often correct.
- **Never:** external dependencies (DB, cache, broker).
Tags: devops kubernetes probes
<!--ID: 1782190015271-->
END

START
Coding Questions
Why is putting a database check inside a **liveness** probe dangerous?
Back: Liveness failure → **restart**. If `/livez` pings the DB and the DB has an outage, every pod fails → every pod restarts → cluster-wide **restart loop** — and restarting fixes nothing about a down database.
Tags: devops kubernetes probes
<!--ID: 1782190015296-->
END

START
Coding Questions
What does the kubelet do when a **readiness** probe fails — and what does it pointedly *not* do?
Back:
- **Does:** removes the pod from the **Service's endpoints**, so the load balancer stops routing traffic to it.
- **Not:** does not restart the container — the pod keeps running, just receives no traffic until ready again.
Tags: devops kubernetes probes
<!--ID: 1782190015322-->
END

START
Coding Questions
Why is "drain traffic, don't restart" the right reaction to a readiness failure?
Back: Readiness failures are usually **temporary and recoverable** (dependency blip, cache rebuild). Restarting wouldn't help and throws away warm state. Draining routes traffic to healthy pods and lets this one recover quietly, then rejoin.
Tags: devops kubernetes probes
<!--ID: 1782190015349-->
END

START
Coding Questions
A Kubernetes Service load-balances across pod IPs. What decides membership in that endpoint set?
Back: The **readiness** probe — only pods passing readiness are kept in the Service's endpoints and receive traffic.
Tags: devops kubernetes probes
<!--ID: 1782190015376-->
END

START
Coding Questions
Liveness and readiness use the same delivery mechanisms — so what is the *real* difference between them?
Back: **What your code checks inside the endpoint**, dictated by the reaction:
- **Liveness must be shallow** — failure restarts (destructive), so depend on nothing external.
- **Readiness can be deep** — failure only drains traffic (cheap/reversible), so checking dependencies is safe.
Tags: devops kubernetes probes
<!--ID: 1782190015403-->
END

START
Coding Questions
Why may a readiness probe safely check dependencies while a liveness probe may not?
Back: It follows from the **reactions**:
- Readiness fail → **drain traffic** = cheap, reversible → dependency checks safe
- Liveness fail → **restart** = destructive → a dependency blip would cause a restart storm
Tags: devops kubernetes probes
<!--ID: 1782190015429-->
END

START
Coding Questions
Per the Kubernetes docs, what can a liveness probe that depends on external services cause?
Back: **Cascading failures** across the system. Liveness passes when the app itself is healthy; readiness additionally checks that each required back-end service is available.
Tags: devops kubernetes probes
<!--ID: 1782190015456-->
END

START
Coding Questions
What are the four mechanisms a Kubernetes probe can be delivered by?
Back:
- `httpGet` — HTTP GET to path+port (success = `2xx`/`3xx`)
- `tcpSocket` — open a TCP connection (success = port accepts)
- `exec` — run a command in the container (success = exit `0`)
- `grpc` — standard gRPC health service (success = `SERVING`)
Tags: devops kubernetes probes
<!--ID: 1782190015481-->
END

START
Coding Questions
Are probe *kind* (liveness/readiness/startup) and probe *mechanism* (httpGet/tcp/exec/grpc) coupled?
Back: No — they're **independent**. The kind decides what the kubelet does with the result; the mechanism decides how it asks. Any kind can use any mechanism.
Tags: devops kubernetes probes
<!--ID: 1782190015507-->
END

START
Coding Questions
Why do stateful infra pods (Postgres, Kafka, Redis) usually use `tcpSocket` or `exec` instead of `httpGet`?
Back: They typically **speak no HTTP health protocol**, so they can't answer an `httpGet`. They're probed by opening their port (`tcpSocket`) or running their own CLI (`exec`), e.g. `pg_isready`, `redis-cli ping` → `PONG`.
Tags: devops kubernetes probes
<!--ID: 1782190015534-->
END

START
Coding Questions
Which probe mechanism fits a normal app vs stateful infra?
Back:
- **App** (Spring Boot, Node) → `httpGet` against a real health endpoint
- **Stateful infra** (DB, broker, cache) → `tcpSocket` or `exec`, since they don't speak HTTP health
Tags: devops kubernetes probes
<!--ID: 1782190015560-->
END

START
Coding Questions
What problem does a **startup** probe solve?
Back: Slow-booting apps (JVM warmup, cache load, migrations) aren't dead — just not up yet. A startup probe tells the kubelet "boot finished," and **holds back liveness + readiness until it succeeds**, preventing a premature liveness restart loop.
Tags: devops kubernetes probes
<!--ID: 1782190015586-->
END

START
Coding Questions
Without a startup probe, what awkward trade-off are you forced into for slow-booting apps?
Back: You must slacken liveness with a large `initialDelaySeconds` to survive boot — which then makes **real deadlocks slow to detect** once running. The startup probe lets liveness stay aggressive without punishing a slow start.
Tags: devops kubernetes probes
<!--ID: 1782190015612-->
END

START
Coding Questions
How does Spring Boot Actuator map onto Kubernetes' two probes?
Back: Two ready-made health **groups**:
- `/actuator/health/liveness` → is the application context running?
- `/actuator/health/readiness` → are the app's dependencies usable?
Enable with `management.endpoint.health.probes.enabled=true`.
Tags: devops kubernetes spring
<!--ID: 1782190015638-->
END

START
Coding Questions
How does Actuator enforce "shallow liveness, deep readiness" for you automatically?
Back:
- **Liveness group** reflects only whether the Spring **application context** is live — no DataSource/Redis.
- **Readiness group** folds in `DataSource`, Redis, Kafka health indicators.
So a DB outage flips readiness `DOWN` (drain) without touching liveness (no restart).
Tags: devops kubernetes spring
<!--ID: 1782190015662-->
END
