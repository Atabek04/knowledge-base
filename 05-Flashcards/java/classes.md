TARGET DECK: Tech-KB::Java::Classes
Tags: java classes oop
**Chapter:** Classes
**Related:** [[Java MOC]]

---

START
Coding Questions
What hidden field does Java automatically add to every non-static inner class?
Back: A hidden field called **`this$0`** — a reference to the outer class instance that created the inner object.

```java
class School {
    class Student {
        // compiler secretly adds: final School this$0;
    }
}
```

This is why inner classes can access outer class fields — they secretly hold a pointer back to the outer instance.
Tags: java classes inner-class
<!--ID: 1780311507600-->
END

START
Coding Questions
Why do non-static inner classes risk memory leaks?
Back: The hidden `this$0` reference keeps the **outer instance alive** even when nothing else uses it.

```java
class Activity {
    byte[] heavyData = new byte[10_000_000]; // 10MB

    class Listener {
        // holds hidden reference to Activity
        // heavyData can't be GC'd as long as Listener exists
    }
}
```

GC can't free the outer object because the inner class still holds a reference to it.
Tags: java classes inner-class memory
<!--ID: 1780311507620-->
END

START
Coding Questions
How do you fix the memory leak risk from non-static inner classes?
Back: Declare the inner class as **`static`** — this removes the hidden `this$0` reference.

```java
class School {
    static class Metadata {
        // no hidden reference to School
        // can be created independently: new School.Metadata()
    }
}
```

Trade-off: static nested class can no longer access outer instance fields.
Tags: java classes inner-class memory
<!--ID: 1780311507640-->
END

START
Coding Questions
What is Java's design mistake with inner classes?
Back: The **dangerous option is the default** — non-static inner classes silently hold an outer reference and risk memory leaks.

Developers must remember to add `static` every time to opt out of this behavior.

Kotlin fixed this — nested classes are static by default.
Tags: java classes inner-class
<!--ID: 1780311507661-->
END

START
Coding Questions
What does the inherited `Object.equals()` compare by default?
Back: **Reference identity** — it is literally `this == obj`.

It returns `true` only for the *same instance in memory*, not for two objects with identical field values.

```java
new Point(1,2).equals(new Point(1,2)); // false — different objects
```
Tags: java classes equals-hashcode
END

START
Coding Questions
By default, do two distinct objects with identical fields share a `hashCode()`?
Back: **No.** The inherited `Object.hashCode()` is identity-based (typically derived from the memory address), so distinct instances almost always get **different** hash codes — even with identical fields.
Tags: java classes equals-hashcode
END

START
Coding Questions
When should you override `equals()` and `hashCode()` instead of keeping the defaults?
Back: When the class is a **value object** — equality should depend on *contents*, not identity.

- Used as a `HashMap` key or in a `HashSet`
- Money, `Point`, `Range`, DTOs

Keep the identity default for objects unique by identity (a `Thread`, a DB connection).
Tags: java classes equals-hashcode
END

START
Coding Questions
What are the five clauses of the `equals()` contract?
Back: For non-null `x, y, z`:

- **Reflexive** — `x.equals(x)` is true
- **Symmetric** — `x.equals(y)` ⟺ `y.equals(x)`
- **Transitive** — `x.equals(y)` ∧ `y.equals(z)` → `x.equals(z)`
- **Consistent** — repeated calls return the same result
- **Non-null** — `x.equals(null)` is false

(Equivalence relation + consistent + non-null.)
Tags: java classes equals-hashcode
END

START
Coding Questions
What is the binding rule linking `equals()` and `hashCode()`?
Back: **If two objects are equal, their hash codes must be equal.**

The reverse does NOT hold — equal hash codes do *not* imply equal objects (just a bucket collision).
Tags: java classes equals-hashcode
END

START
Coding Questions
Why does a `HashMap` lookup fail if you override `equals()` but not `hashCode()`?
Back: Lookup is two steps: **hashCode picks the bucket, equals confirms the key**.

With the identity `hashCode()`, an equal-but-different key lands in a **different bucket**, so the map never reaches the `equals()` check.

```java
var m = new HashMap<Point,String>();
m.put(new Point(1,2), "x");
m.get(new Point(1,2)); // null ❌
```
Tags: java classes equals-hashcode
END

START
Coding Questions
What does `instanceof` pattern matching add over a traditional `instanceof` check?
Back: It combines the type check and cast into one step, binding the result to a variable:

```java
// Before (Java <16)
if (obj instanceof String) {
    String s = (String) obj; // redundant cast
    System.out.println(s.length());
}

// Java 16+
if (obj instanceof String s) {
    System.out.println(s.length()); // s already bound, no cast
}
```

The binding variable is only in scope where the check is provably true.
Tags: java pattern-matching oop
END

START
Coding Questions
What are the scope rules for `instanceof` pattern binding variables?
Back:
- ✅ **`&&`** — right side is guarded; `s` is in scope: `obj instanceof String s && s.length() > 5`
- ❌ **`||`** — right side is unguarded; compile error: `obj instanceof String s || s.length() > 5`
- ✅ **Negation + early return** — binding available *after* the block (flow typing):

```java
if (!(obj instanceof String s)) return;
System.out.println(s.length()); // s in scope here
```
Tags: java pattern-matching oop
END
