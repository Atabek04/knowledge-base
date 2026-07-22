---
aliases: [Flyway clean vs repair, Flyway checksum mismatch, Reset Flyway history]
tags: [databases, backend, flyway, migrations, devops]
created: 2026-07-09
---

Flyway records each applied migration's <mark style="background: #FFF3A3A6;">checksum</mark> in the `flyway_schema_history` table.

Editing an already-applied migration file changes its checksum but not the stored one, so the next `migrate` aborts with:

```
Migration checksum mismatch for migration version 3
```

There are two ways out, and they solve different problems.

---

### `migrate` — the baseline command

`mvn flyway:migrate` is the normal command: it scans the `V{n}__*.sql` files, applies every <mark style="background: #FFF3A3A6;">pending</mark> one in **version order**, and records each in `flyway_schema_history` with its checksum.

Already-applied versions are skipped. It is the checksum comparison during this scan that raises the mismatch when a past file was edited — so `clean` and `repair` both exist to get `migrate` running again.

```bash
mvn flyway:migrate
```

---

### `clean` — drop everything, re-apply from scratch

`mvn flyway:clean` <mark style="background: #FF5582A6;">drops all objects</mark> in the configured schema — tables, history, sequences, everything.

The follow-up `migrate` then replays every migration file against an empty schema, so edited files apply cleanly with fresh checksums.

```bash
mvn flyway:clean    # needs cleanDisabled=false
mvn flyway:migrate
```

Equivalent raw-SQL reset when you can't run Maven:

```sql
DROP SCHEMA public CASCADE; CREATE SCHEMA public;
```

Use `clean` whenever the edit <mark style="background: #BBFABBA6;">changes the actual schema</mark> (new column, renamed table, altered type) — only a full re-apply makes the DB match the edited DDL.

---

### `repair` — realign checksums, keep the data

`mvn flyway:repair` <mark style="background: #ADCCFFA6;">rewrites the checksums</mark> stored in `flyway_schema_history` to match the current files, and removes failed-migration rows.

It does **not** drop anything and does **not** re-run any DDL — the live schema is untouched.

So `repair` only fixes the *mismatch error*; it never applies your schema change. Use it only when the edit is <mark style="background: #BBFABBA6;">cosmetic</mark> (a comment, whitespace, formatting) and the schema is already correct.

---

### Which one

| Edit changed... | Command |
|---|---|
| The schema itself (DDL) | `clean` + `migrate` |
| Only text, schema already right | `repair` |

<mark style="background: #FF5582A6; font-weight: bold;">Pre-launch only.</mark> Editing applied migration files is safe only before the app ships and while every environment can be wiped. `clean` destroys all data — running it against a live DB is a disaster.

<mark style="background: #FF5582A6;">After launch, migrations are forward-only</mark>: never touch an applied file — add a new `V{next}__change.sql` for every schema change instead.

---

### Best practices worth adding

- **One change per migration file** — small, reviewable, independently revertible.
- **Never edit an applied migration in a shared/prod env** — even a typo fix; add a new version.
- **Keep migrations idempotent-safe** — `IF NOT EXISTS` / `IF EXISTS` guards survive partial re-runs.
- **Test migrations on a throwaway DB** (Testcontainers) before merging — catches ordering and checksum issues early.
- **Destructive change coming?** Take a targeted `pg_dump -t table` first as a one-time safety net.

---

### Read more

- [[Database migrations version schema changes while backups recover data loss — they are never substitutes]]
- [[Databases - MOC]]
