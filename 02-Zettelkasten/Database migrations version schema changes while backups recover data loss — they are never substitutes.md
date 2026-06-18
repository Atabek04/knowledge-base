---
aliases: [DB migrations vs backups, Schema migrations, Online schema change, Expand-contract pattern]
tags: [databases, backend, devops, migrations, production-engineering]
created: 2026-06-04
---

### Core distinction

**Migrations** and **backups** solve orthogonal problems. Confusing them causes production disasters.

| | Migration files | Backups (PITR) |
|---|---|---|
| **Solves** | Schema versioning, reproducible deploys, schema drift | Disaster recovery, hardware failure, data corruption |
| **Protects against** | Code/schema mismatch between environments, bad deploys | Accidental `DROP TABLE`, silent data corruption, ransomware |
| **Rollback use** | Only non-destructive changes (add column → drop). **Never for data loss.** | Only tool that recovers data written after a bad migration |
| **Data loss** | None (schema only) | Yes — anything written after backup timestamp is lost |
| **Downtime** | Zero (if done right) | Yes — restoring from backup requires downtime |

**The maxim from production engineering (Stripe, GitHub, Shopify):** backups are for disaster recovery; migrations are for schema evolution. **Fix-forward** (deploy a compensating migration) is almost always the right rollback strategy — restoring a backup is too slow and loses real data.

---

### Do large companies auto-generate migration files?

No — at least not at Google, Stripe, GitHub, Meta scale.

- **Stripe**: all migrations hand-authored; dual-write sequences written as deliberate refactors
- **GitHub**: developers maintain **declarative SQL schema** (source of truth); Skeema *diffs* it against production and generates SQL as a **PR comment for human review** — generated SQL is never applied without a reviewer
- **Meta**: manually operated OSC tool, no auto-generation
- **Shopify**: vanilla Rails migrations (human-authored), executed via a safety-checked pipeline

**Schema-as-code** (Atlas, Prisma Migrate) is the middle ground used by smaller teams: define the desired schema declaratively → tool computes the diff → **human reviews the generated SQL** before applying. Generated SQL is a convenience, never a fire-and-forget.

---

### Online schema change tools (big tables in production)

A naive `ALTER TABLE` locks the table for hours on large datasets. Large companies use ghost-table techniques:

| Tool | Who | Mechanism |
|---|---|---|
| **gh-ost** | GitHub (built it), Shopify | Triggerless; tails binlog, builds ghost table, atomic `RENAME` cutover (~ms) |
| **pt-online-schema-change** | Meta/Percona | Trigger-based; mirrors writes via INSERT/UPDATE/DELETE triggers |
| **OSC** | Meta | Python rewrite of pt-osc; moving toward triggerless via row-based replication |
| **LHM** | Shopify | Ruby gem; shadow-table for MySQL |
| **pg_repack** | PostgreSQL | Non-blocking table reorg + bloat cleanup |

Flyway/Liquibase handle *versioning and sequencing*; gh-ost/OSC handle *online execution*. They are complementary.

---

### Expand/Contract pattern (zero-downtime schema evolution)

Universal pattern at scale. Stripe calls it "dual-write"; Google calls it "dual-format coexistence"; PlanetScale calls it "deploy requests."

```
1. EXPAND   → Add new column/table as nullable. Old code ignores it.
2. WRITE    → New code writes to both old and new. Old code still writes to old.
3. BACKFILL → Background job migrates existing rows.
4. VALIDATE → Parallel reads; compare results (Stripe used GitHub's Scientist library).
5. CUT READ → Switch reads to new column.
6. CUT WRITE→ Stop writing to old column.
7. CONTRACT → Drop old column/table.
```

Each step = a separate deploy. The full sequence can span days or weeks on a live system.

**When to skip it:** empty tables, dev/staging, or new features with no existing data. Use `ALTER TABLE` directly.

---

### When backup restore IS the right answer

The one scenario where only a backup saves you: **silent data corruption by a bad migration, not caught for 48+ hours**. Migrations can re-apply schema changes from any point; only a backup (PITR via WAL archiving) can recover the corrupted rows themselves.

Pre-flight insurance: before any destructive migration (`DROP COLUMN`, `DROP TABLE`), take a targeted `pg_dump -t tablename` as a one-time safety net.

---

### Sources

- [Stripe: Online Migrations at Scale](https://stripe.com/blog/online-migrations)
- [GitHub: Automating MySQL Schema Migrations with Skeema + gh-ost](https://github.blog/enterprise-software/automation/automating-mysql-schema-migrations-with-github-actions-and-more/)
- [Shopify: Safely Adding NOT NULL Columns](https://shopify.engineering/add-not-null-colums-to-database)
- [Meta: OnlineSchemaChange Rebuilt in Python](https://engineering.fb.com/2017/05/05/production-engineering/onlineschemachange-rebuilt-in-python/)
- [Google Cloud: Spanner 6-exabyte Storage Migration](https://cloud.google.com/blog/products/databases/spanner-modern-columnar-storage-engine)
- [gh-ost (GitHub)](https://github.com/github/gh-ost)
- [Prisma Data Guide: Expand and Contract Pattern](https://www.prisma.io/dataguide/types/relational/expand-and-contract-pattern)
- [Atlas: Schema-as-Code vs Flyway/Liquibase](https://atlasgo.io/atlas-vs-others)

---

See also:
- [[Databases - MOC]]
- [[A CRUD matrix maps entities against operations to expose missing or unowned data lifecycles]]
- [[A domain model captures behavior and rules while a data model captures storage structure]]
