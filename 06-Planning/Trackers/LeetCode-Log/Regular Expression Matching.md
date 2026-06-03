---
difficulty: Hard
status: Not started
topic: [2-D Dynamic Programming]
tags: [recursion, string, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/regular-expression-matching/"
---

### Problem
Given an input string s and a pattern p, implement regular expression matching that supports '.' (matches any single character) and '*' (matches zero or more of the preceding element). The match must cover the entire input string, not just a substring.

### Constraints
- 1 <= s.length <= 20
- 1 <= p.length <= 20
- s contains only lowercase English letters
- p contains only lowercase English letters, '.', and '*'
- Each '*' is guaranteed to have a valid preceding character

### Examples
```
s = "aa", p = "a"   →  false    ("a" cannot match "aa")
s = "aa", p = "a*"  →  true     ('a*' matches zero or more 'a')
s = "ab", p = ".*"  →  true     ('.*' matches any sequence)
```

### Next solve approach
1. Brute Force first — recursive match with '*' trying 0 or more repeats, '.' matching any character
2. Optimized — 2-D DP where dp[i][j] = whether s[0..i-1] matches p[0..j-1]; handle '*' by looking back two positions or extending match

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean isMatch(String s, String p) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isMatch("aa", "a"));   // expected: false
        System.out.println(sol.isMatch("aa", "a*"));  // expected: true
        System.out.println(sol.isMatch("ab", ".*"));  // expected: true
    }
}
```

### Python

```python
def is_match(s: str, p: str) -> bool:
    # TODO: implement
    pass


print(is_match("aa", "a"))   # expected: False
print(is_match("aa", "a*"))  # expected: True
print(is_match("ab", ".*"))  # expected: True
```
