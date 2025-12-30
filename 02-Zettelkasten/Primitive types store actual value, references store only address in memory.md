### <mark style="background: #BBFABBA6;">Primitive variables store actual values directly</mark>

```java
int age = 25;  // age contains the value 25
```

### <mark style="background: #BBFABBA6;">Reference variables store a pointer/address to an object in memory, not the object itself</mark>

```java
String name = new String("John");  // 0x7a8f9b2
```

---

```java
int a = 5;
int b = a;  // b now has its own copy of 5
```

```java
String s1 = new String("Hello");
String s2 = s1;
```

Both `s1` and `s2` point to the same String object in memory.

If you modify the object through `s1`, you see the change through `s2`
because they reference the same thing.
