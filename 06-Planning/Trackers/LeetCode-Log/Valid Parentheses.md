---
difficulty: Easy
status: Not started
topic: [Stack]
tags: [stack, string, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/valid-parentheses/"
---

### Problem
Given a string containing only the bracket characters `(`, `)`, `{`, `}`, `[`, and `]`, determine whether the string is valid. A string is valid only when every opening bracket is closed by the same type of bracket, brackets are closed in the correct order, and every closing bracket has a matching opener somewhere before it.

### Constraints
- 1 <= s.length <= 10^4
- s consists of parentheses only `()[]{}`.

### Examples
```
"()"      →  true
"()[]{}"  →  true
"(]"      →  false
"([])"    →  true
"([)]"    →  false
```

### Next solve approach
1. Brute Force first — repeatedly replace valid pairs "()", "[]", "{}" until none remain, check if empty
2. Optimized — use a stack: push on open bracket, pop and match on close bracket

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean isValid(String s) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isValid("()"));       // expected: true
        System.out.println(sol.isValid("()[]{}"));   // expected: true
        System.out.println(sol.isValid("(]"));       // expected: false
        System.out.println(sol.isValid("([])"));     // expected: true
        System.out.println(sol.isValid("([)]"));     // expected: false
    }
}
```

### Python

```python
def is_valid(s: str) -> bool:
    # TODO: implement
    pass


print(is_valid("()"))      # expected: True
print(is_valid("()[]{}"))  # expected: True
print(is_valid("(]"))      # expected: False
print(is_valid("([])"))    # expected: True
print(is_valid("([)]"))    # expected: False
```
