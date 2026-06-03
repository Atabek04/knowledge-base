---
difficulty: Medium
status: Not started
topic: [Backtracking]
tags: [string, dynamic-programming, backtracking, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/generate-parentheses/"
---

### Problem
Given n pairs of parentheses, generate all possible strings of well-formed (valid) parentheses combinations. A string is valid when every opening bracket has a matching closing bracket in the correct order.

### Constraints
- 1 <= n <= 8

### Examples
```
n = 3  →  ["((()))","(()())","(())()","()(())","()()()"]
n = 1  →  ["()"]
```

### Next solve approach
1. Brute Force first — generate all 2^(2n) sequences of brackets, validate each one
2. Optimized — backtracking DFS tracking open/close counts; only add '(' if open < n, only add ')' if close < open

---

### Java

```java
public class Solution {

    // TODO: implement
    public List<String> generateParenthesis(int n) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.generateParenthesis(3)); // expected: ["((()))","(()())","(())()","()(())","()()()"]
        System.out.println(sol.generateParenthesis(1)); // expected: ["()"]
    }
}
```

### Python

```python
def generate_parenthesis(n: int) -> list[str]:
    # TODO: implement
    pass


print(generate_parenthesis(3))  # expected: ["((()))","(()())","(())()","()(())","()()()"]
print(generate_parenthesis(1))  # expected: ["()"]
```
