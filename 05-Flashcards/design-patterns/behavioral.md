TARGET DECK: Tech-KB::Design Patterns::Behavioral
Tags: design-patterns behavioral-patterns
**Related:** [[Design Patterns - MOC]]

---

<!-- Strategy, Observer, Command, Chain of Responsibility, Iterator, Mediator,
     Memento, State, Template Method, Visitor. -->

START
Basic
In the **Java** implementation of Strategy, why use an interface instead of an abstract class?
Back:
- **Abstract class** = hidden coupling; a base-class change silently breaks all concrete strategies
- **Interface** = pure contract; each strategy is fully independent, can extend anything
- Use abstract class only when strategies share genuine non-trivial implementation (rare) — even then, prefer a utility
Tags: design-patterns behavioral strategy java
<!--ID: 1782128729813-->
END

START
Basic
What is wrong with bundling two behaviors into one Strategy class?
Back:
- "Combinations in one strategy" violates Single Responsibility
- Example: `SortAndFilterStrategy` — now you can't use sort-only or filter-only without duplication
- **Rule:** one strategy = one algorithm; behaviors that vary independently get their own strategy family
Tags: design-patterns behavioral strategy
<!--ID: 1782128729815-->
END

START
Basic
What is the difference between composition and inheritance in terms of **when** behavior is resolved?
Back:
- **Inheritance** — resolved at **compile time**; behavior is baked into the subclass, cannot change at runtime
- **Composition** — resolved at **runtime**; the composed field holds an interface reference, any implementation can fill it
- This is why Strategy, Decorator, and State all use composition — they need runtime-swappable behavior
Tags: design-patterns behavioral strategy
<!--ID: 1782128729818-->
END
