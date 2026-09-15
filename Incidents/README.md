---
tags: [incident, index]
---

> One note per real incident: a dated war story, not a timeless concept, which is why it lives here and not in `02-Zettelkasten/`.

Use `Templates/Incident Report.md`. Four sections, about 150 words: Symptom, Root cause, Where to look next time, Lessons.

This folder is published on the public wiki, so an incident describes the <b>mechanism</b>, never the system:

- No company, product, customer, colleague or project names; no hostnames, IPs, repo names, ticket ids, commit hashes, table or column names, config values.
- Name the class of component ("a ClickHouse view", "an OCSP verifier", "a systemd unit"). Framework and library class names are fine (`OncePerRequestFilter`, `SseEmitter`).
- Every incident promotes its reusable lesson into an atomic note under `02-Zettelkasten/` and links it from `### Lessons`. The incident is the story; the atomic note is the principle.

### Read more
- [[Debugging & Troubleshooting - MOC]]
