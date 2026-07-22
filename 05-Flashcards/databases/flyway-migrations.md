TARGET DECK: Tech-KB::Databases::Flyway
Tags: databases flyway migrations
**Related:** [[Flyway clean drops and re-applies migrations while repair only realigns checksums]]

START
Coding Questions
What does `flyway:migrate` do when run?
Back: Scans the `V{n}__*.sql` files and applies every **pending** one in **version order**.
Records each in `flyway_schema_history` with its **checksum**; already-applied versions are skipped.
END

START
Coding Questions
Why does editing an already-applied Flyway migration file break the next `migrate`?
Back: Flyway stored the file's **checksum** in `flyway_schema_history`.
Editing changes the file's checksum but not the stored one → **checksum mismatch**, and `migrate` aborts.
END

START
Coding Questions
What does `flyway:clean` do, and what must follow it to reset an edited migration?
Back: **Cleans** (drops) every object in the schema — tables, history, sequences.
Follow with `flyway:migrate` to replay all files against an empty schema with fresh checksums.
END

START
Coding Questions
What does `flyway:repair` change, and what does it deliberately not do?
Back: **Repairs** `flyway_schema_history` — rewrites stored checksums to match current files, removes failed rows.
Does **not** drop anything and does **not** re-run any DDL.
END

START
Coding Questions
After editing a migration file, when do you use `clean` + `migrate` vs `repair`?
Back:
- Edit changed the **schema** (DDL) → `clean` + `migrate` (only a re-apply makes the DB match)
- Edit was **cosmetic** (comment/whitespace), schema already correct → `repair`
END

START
Coding Questions
You edit a migration's DDL and run only `flyway:repair` — is your schema change applied?
Back: **No.** Repair only realigns checksums; it never re-runs DDL.
The schema stays unchanged — you need `clean` + `migrate` to actually apply it.
END

START
Coding Questions
Why is editing an applied migration file safe only pre-launch?
Back: The reset relies on `clean`, which **drops all data** — safe only while every environment can be wiped.
After launch, migrations are **forward-only**: add a new `V{next}__*.sql` per change instead of editing.
END
