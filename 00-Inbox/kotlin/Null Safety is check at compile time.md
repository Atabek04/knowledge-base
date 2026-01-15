
Null safety - to prevent issues with `null` values. It detects potential problems with `null` values at compile time, rather than at runtime.

---

Null safety is a combination of features that allow you to:

- Explicitly declare `null` values
	- by default, all variables are non-null.
- Check for `null` values
- Use **safe calls** to properties or functions that may contain `null` values.
- Declare actions to take if `null` values are detected.

---

### Permission for null values

As we said earlier, by default, a type is not allowed to accept `null` values.

In order to allow `null` values, you should explicitly add `?` after the type declaration.

So yes, you should write type declaration.
You can't infer type, when value is `null`.