---
aliases: [interface vs abstract class, Java interface, abstract class, interface, abstract class in Java]
created: 2026-08-19
tags: [java, oop]
---

Both `interface` and `abstract class` let you declare a type that isn't fully implemented, so subclasses/implementers must fill in the rest. The difference is *what each is allowed to carry along with that contract*.

<mark style="background: #FFF3A3A6;"><b>An interface is a pure contract — method signatures (plus `default`/`static` bodies), no instance fields, no constructor. An abstract class can hold real state (instance fields), a constructor, and a mix of finished and unfinished methods.</b></mark>

---

### Interface — contract only

```java
interface Shape {
    double area();          // abstract — no body, implementer must supply it
}
```

A class can implement **any number** of interfaces — there's no "which one wins" problem because interfaces (traditionally) carry no state to conflict over.

### Abstract class — contract plus shared state

```java
abstract class Animal {
    protected String name;              // real instance field

    Animal(String name) {               // real constructor
        this.name = name;
    }

    abstract void makeSound();          // unfinished — subclass must supply it

    void introduce() {                  // finished — shared by every subclass
        System.out.println(name + " says:");
        makeSound();
    }
}
```

A class can `extends` **only one** abstract class — Java has no multiple inheritance for classes, precisely because state conflicts (two parents both wanting to own the same field) would be unresolvable.

---

### When to reach for which

- **Interface** — you want to describe *capability* ("can be compared", "can be run") that unrelated classes might share, or you need a class to satisfy several contracts at once.
- **Abstract class** — the subclasses share real state or common working logic (like `introduce()` above), and they're clearly variations of one thing, not just things that happen to share a method signature.

### Read more

- [[A Java functional interface has exactly one abstract method — default and static methods don't count toward that limit]]
- [[Java MOC]]
