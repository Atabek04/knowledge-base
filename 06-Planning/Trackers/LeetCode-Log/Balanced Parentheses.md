---
difficulty: Hard
status: Not started
topic: [Subsets, Strings, Backtracking]
tags: [subsets, string, backtracking, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a number N, generate every valid string made of exactly N opening and N closing parentheses. A string is valid when every closing bracket is matched by a preceding unmatched opening bracket. Return all such combinations.

### Constraints
- 1 <= N <= 8
- Output strings contain only '(' and ')'
- Each result string has exactly 2*N characters

### Examples
```
N=2  →  "(())", "()()"
N=3  →  "((()))", "(()())", "(())()", "()(())", "()()()"
```

### Next solve approach
1. Brute Force first — generate all 2^(2N) binary strings, keep only the valid ones
2. Optimized (Subsets/Backtracking) — build the string character by character; add '(' only if open count < N, add ')' only if close count < open count

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static List<String> generateValidParentheses(int num) {
        // TODO
        return new ArrayList<String>();
    }

    public static void main(String[] args) {
        System.out.println(generateValidParentheses(2)); // expected: [(()), ()()]
        System.out.println(generateValidParentheses(3)); // expected: [((())), (()()), (())(), ()(()), ()()()]
    }
}
```

### Python

```python
def generate_valid_parentheses(num: int) -> list[str]:
    # TODO: implement
    pass


print(generate_valid_parentheses(2))  # expected: ['(())', '()()']
print(generate_valid_parentheses(3))  # expected: ['((()))', '(()())', '(())()', '()(())', '()()()']
```
