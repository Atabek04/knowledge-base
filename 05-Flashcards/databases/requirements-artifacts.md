TARGET DECK: Tech-KB::Databases::Requirements Artifacts
Tags: data-modeling requirements system-analysis
**Chapter:** Requirements Artifacts for Data
**Related:** [[Databases - MOC]]

---

START
Coding Questions
What is a data dictionary, and what question does it answer for every field?
Back:
A formal **catalog** defining every data element — name, meaning, type, constraints, allowed values — in one authoritative place.

For any field it answers: *what is this exactly, and what rules govern it?*

It bridges the **business glossary** and the **physical schema**.
Tags: data-modeling data-dictionary requirements
<!--ID: 1782128729802-->
END

START
Coding Questions
What expensive class of bug does a data dictionary prevent?
Back:
**Two teams meaning different things by the same word.**

- Does `customer` include unregistered guests? Is `revenue` gross or net? Is a date UTC or local?
- A shared, agreed definition removes the ambiguity **before** code is written
Tags: data-modeling data-dictionary
<!--ID: 1782128729804-->
END

START
Coding Questions
What is a CRUD matrix and what are its axes?
Back:
A grid mapping **entities** (rows) against **processes/actors** (columns); each cell holds the **C/R/U/D** operations that process performs on that entity.

It cross-checks the **process model** against the **data model** — every entity should have a clear lifecycle owned by some process.
Tags: data-modeling crud-matrix requirements
<!--ID: 1782128729808-->
END

START
Coding Questions
What design smells does a CRUD matrix reveal through gaps in the grid?
Back:
- **No C** for an entity → who creates this data? (missing process / external source)
- **No U or D** → can stale data be corrected or removed? (retention gap)
- **Read everywhere, created by no one** → an **unowned entity** (needs a data owner)
- **One process touching every entity** → a possible **god process**
Tags: data-modeling crud-matrix analysis
<!--ID: 1782128729810-->
END
