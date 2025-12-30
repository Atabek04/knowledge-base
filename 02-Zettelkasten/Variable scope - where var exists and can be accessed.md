#### Class Scope

- Var inside class's brackets `{}` with `private` access modifier, but outside any method
- Can be used everywhere in the class, but not outside of it.

#### Method Scope

- Var inside a method
- Can be valid only inside the same method

#### Loop Scope

- Var inside a loop
- Available only inside the loop

#### Bracket Scope

- You can define additional scopes anywhere using curly braces
- Variables accessible only that bracket

```java
public class BracketScopeExample {
    public void mathOperationExample() {
        Integer sum = 0;

        {
            Integer number = 2;
            sum = sum + number;
        }
    }
}
```
