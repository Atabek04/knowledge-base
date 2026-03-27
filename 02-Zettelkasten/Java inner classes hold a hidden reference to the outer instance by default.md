---
aliases: [Java inner class, outer reference]
created: 2026-03-27
tags: [java, oop]
---

### What does "holds a reference to outer" mean?

When you create an inner class in Java, the compiler secretly adds a hidden field pointing to the outer instance:

```java
class School {
    String name = "MIT";

    class Student {
        // compiler secretly adds: final School this$0;
        // this$0 = the School instance that created this Student

        void printSchool() {
            System.out.println(name);  // works because of hidden reference
        }
    }
}
```

You never see `this$0` in your code, but it's there. That's why `Student` can access `name` — it secretly has a pointer back to the `School` that created it.

---

### Creating an inner class requires an outer instance

Because of this hidden reference, you can't create a `Student` alone:

```java
School school = new School();
School.Student student = school.new Student();  // needs a School first
//                       ^^^^^^ "attach me to this School"
```

---

### Why is this a problem?

<mark style="background: #FF5582A6;">Memory leak risk.</mark> The inner class keeps the outer instance alive — even if nothing else uses it:

```java
class Activity {
    byte[] heavyData = new byte[10_000_000];  // 10MB

    class Listener {
        // holds hidden reference to Activity
        // heavyData can't be garbage collected
        // as long as this Listener exists
    }
}
```

Even if `Activity` is done, `Listener` still holds a reference to it → garbage collector can't free the 10MB.

---

### The fix — `static` nested class

Adding `static` removes the hidden reference:

```java
class School {
    String name = "MIT";

    static class Metadata {
        // no hidden reference to School
        // can't access name
        // created independently
    }
}

School.Metadata meta = new School.Metadata();  // no School instance needed
```

<mark style="background: #FFF3A3A6;">Java's mistake: the dangerous option (holding outer reference) is the default. You have to remember to add `static` every time.</mark>

This is exactly what [[Kotlin nested classes are static by default unlike Java|Kotlin fixed]] — nested classes are static by default.

---

Read more:

- [[Kotlin nested classes are static by default unlike Java]]
- [[Java MOC]]
