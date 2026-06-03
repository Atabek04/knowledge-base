---
difficulty: Medium
status: Not started
topic: [Greedy]
tags: [stack, greedy, string, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/valid-parenthesis-string/"
---

### Problem
Given a string containing '(', ')', and '*' characters, determine if it's valid. A valid string has every '(' matched by a ')' that comes after it, and vice versa. The '*' is a wildcard that can act as '(', ')', or an empty string, giving you flexibility to balance the parentheses.

### Constraints
- 1 <= s.length <= 100
- s[i] is '(', ')' or '*'

### Examples
```
"()"   →  true
"(*)"  →  true
"(*))" →  true
```

### Next solve approach
1. Brute Force first — recursively try all three interpretations of '*' and check if any leads to a valid string
2. Optimized — greedy two-pass: left-to-right treating '*' as '(' to ensure all ')' are matched; right-to-left treating '*' as ')' to ensure all '(' are matched

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean checkValidString(String s) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.checkValidString("()"));   // expected: true
        System.out.println(sol.checkValidString("(*)"));  // expected: true
        System.out.println(sol.checkValidString("(*))"));  // expected: true
    }
}
```

### Python

```python
def check_valid_string(s: str) -> bool:
    # TODO: implement
    pass


print(check_valid_string("()"))    # expected: True
print(check_valid_string("(*)"))   # expected: True
print(check_valid_string("(*))"))  # expected: True
```
