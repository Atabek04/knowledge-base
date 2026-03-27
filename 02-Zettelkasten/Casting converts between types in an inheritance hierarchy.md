---
aliases: [casting, upcasting, downcasting]
created: 2026-03-26
tags: [java, oop, types]
---

### Upcasting (child → parent)

Automatic, no syntax needed. A `Dog` *is* an `Animal`.

```java
Dog dog = new Dog();
Animal animal = dog;  // implicit upcast — always safe
```

---

### Downcasting (parent → child)

Manual — you use `(Type)` to tell the compiler: <mark style="background: #FFF3A3A6;">"trust me, this is actually a Dog."</mark>

<mark style="background: #BBFABBA6;">The key: look at the actual object, not the variable type.</mark>

`Animal animal = new Dog()` — the variable says `Animal`, but the actual thing in memory is a `Dog`. It was always a Dog — we just put it in an Animal-shaped box.

Downcasting is saying: "I know you *look* like an Animal from the variable type, but I know the real object inside is a Dog. Let me access it as a Dog again."

You're not turning an Animal *into* a Dog. You're **revealing** that it was a Dog all along.

```java
Animal animal = new Dog();     // variable says Animal, but real object is Dog
Dog dog = (Dog) animal;        // ✅ revealing what it always was
```

If the real object is something else:

```java
Animal animal = new Cat();
Dog dog = (Dog) animal;        // 💥 ClassCastException — it's a Cat, not a Dog
```

If the object was never a child type to begin with:

```java
Animal animal = new Animal();  // born as Animal, nothing more
Dog dog = (Dog) animal;        // 💥 ClassCastException — there's nothing to reveal
```

---

### Why use downcasting?

When you accept a parent type for flexibility but need child-specific behavior:

```java
void makeSound(Animal animal) {
    animal.eat();  // ✅ all animals eat

    if (animal instanceof Dog) {
        Dog dog = (Dog) animal;
        dog.fetch();  // 🎾 only dogs fetch
    }
}
```

Or when reading from a collection that stores a parent type:

```java
List<Animal> shelter = getAnimals();

for (Animal a : shelter) {
    if (a instanceof Cat) {
        Cat cat = (Cat) a;
        cat.purr();  // 🐱 cat-specific
    }
}
```

<mark style="background: #FF5582A6;">Always use `instanceof` before downcasting to avoid `ClassCastException`.</mark>

---

### Casting vs Autoboxing

| | Casting | Autoboxing |
|---|---|---|
| What | Moving up/down inheritance hierarchy | Converting primitive ↔ wrapper |
| Example | `(Dog) animal` | `int` ↔ `Integer` |
| About | Same object, different type perspective | Same data, different representation |

---

Read more:

- [[Java has dual type system because JVM optimizes primitives for performance]]
- [[Primitive types store actual value, references store only address in memory]]
- [[Java MOC]]
