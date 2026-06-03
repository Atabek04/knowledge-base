---
difficulty: Medium
status: Not started
topic: [Stack]
tags: [stack, design, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/min-stack/"
---

### Problem
Design a stack data structure that supports the standard push, pop, and top operations, while also providing a way to retrieve the current minimum element — all in O(1) time. Every one of these four operations must run in constant time regardless of stack size.

### Constraints
- -2^31 <= val <= 2^31 - 1
- Methods pop, top, and getMin will always be called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.

### Examples
```
MinStack(), push(-2), push(0), push(-3), getMin()  →  -3
pop(), top()                                        →  0
getMin()                                            →  -2
```

### Next solve approach
1. Brute Force first — scan the entire stack on every getMin() call, O(n) per query
2. Optimized — maintain a parallel min-stack that tracks the running minimum at each level

---

### Java

```java
public class Solution {

    static class MinStack {

        // TODO: implement
        public MinStack() {
            // TODO
        }

        public void push(int val) {
            // TODO
        }

        public void pop() {
            // TODO
        }

        public int top() {
            // TODO
            return 0;
        }

        public int getMin() {
            // TODO
            return 0;
        }
    }

    public static void main(String[] args) {
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        System.out.println(minStack.getMin()); // expected: -3
        minStack.pop();
        System.out.println(minStack.top());    // expected: 0
        System.out.println(minStack.getMin()); // expected: -2
    }
}
```

### Python

```python
class MinStack:
    def __init__(self) -> None:
        # TODO: implement
        pass

    def push(self, val: int) -> None:
        # TODO
        pass

    def pop(self) -> None:
        # TODO
        pass

    def top(self) -> int:
        # TODO
        return 0

    def get_min(self) -> int:
        # TODO
        return 0


min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.get_min())  # expected: -3
min_stack.pop()
print(min_stack.top())      # expected: 0
print(min_stack.get_min())  # expected: -2
```
