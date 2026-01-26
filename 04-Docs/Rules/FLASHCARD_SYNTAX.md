# Flashcard Syntax Reference

## File Header

```markdown
TARGET DECK: Category::Subcategory
FILE TAGS: tag1 tag2
```

---

## Q&A One-liner

```markdown
Q: What is Tawhid?
A: The oneness of Allah in His lordship, worship, and names/attributes

Q: What does JVM stand for?
A: Java Virtual Machine
```

---

## Q&A Multi-line Answer

```markdown
Q: What are the three categories of Tawhid?
A: 
1. **Rububiyyah** — Lordship (Allah is sole Creator/Sustainer)
2. **Uluhiyyah** — Worship (Allah alone deserves worship)
3. **Asma wa Sifat** — Names & Attributes (unique to Allah)

Q: What are the four OOP principles?
A:
- Encapsulation — bundling data with methods
- Inheritance — child class extends parent
- Polymorphism — same interface, different behavior
- Abstraction — hiding implementation details
```

---

## Cloze

```markdown
The {five} pillars of Islam are {2:Shahada}, {3:Salah}, {4:Zakat}, {5:Sawm}, and {6:Hajj}

The JVM converts bytecode to {native machine code} via the {2:JIT compiler}

In Java, {synchronized} keyword prevents {2:race conditions} in multithreading
```

**Cloze with hints:**
```markdown
The {{c1::Quran::holy book}} was revealed to {{c2::Prophet Muhammad ﷺ::final messenger}}
```

---

## Images

**Basic:**
```markdown
Q: What is the JVM architecture?
A: ![[jvm-architecture.png]]

Q: Identify this prayer position
A: ![[rukoo.jpg]]
This is Rukoo (bowing position)
```

**Standard markdown syntax:**
```markdown
Q: What does this diagram show?
A: ![JVM Memory Model](attachments/jvm-memory.png)
```

**Image in question:**
```markdown
Q: ![[unknown-component.png]]
What JVM component is highlighted?
A: The Class Loader subsystem
```

**Cloze with image:**
```markdown
The prayer position shown is called {Sujood}
![[sujood.jpg]]
```

> **Note:** Images must exist in your vault. They auto-copy to Anki's media folder on sync.
