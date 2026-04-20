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
END

START
Coding Questions
What is Java's design mistake with inner classes?
Back: The **dangerous option is the default** — non-static inner classes silently hold an outer reference and risk memory leaks.

Developers must remember to add `static` every time to opt out of this behavior.

Kotlin fixed this — nested classes are static by default.
Tags: java classes inner-class
END
