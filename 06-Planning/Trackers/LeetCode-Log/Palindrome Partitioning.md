---
difficulty: Medium
status: Not started
topic: [Backtracking]
tags: [string, dynamic-programming, backtracking, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/palindrome-partitioning/"
---

### Problem
Given a string s, split it into substrings so that every substring is a palindrome. Return all possible ways to do this partitioning. Every character must belong to exactly one substring in each valid partition.

### Constraints
- 1 <= s.length <= 16
- s contains only lowercase English letters

### Examples
```
s = "aab"  →  [["a","a","b"],["aa","b"]]
s = "a"    →  [["a"]]
```

### Next solve approach
1. Brute Force first — try all ways to split the string, verify each substring is a palindrome
2. Optimized — precompute palindrome check table with DP, then backtracking DFS choosing cut points

---

### Java

```java
public class Solution {

    // TODO: implement
    public List<List<String>> partition(String s) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.partition("aab")); // expected: [["a","a","b"],["aa","b"]]
        System.out.println(sol.partition("a"));   // expected: [["a"]]
    }
}
```

### Python

```python
def partition(s: str) -> list[list[str]]:
    # TODO: implement
    pass


print(partition("aab"))  # expected: [["a","a","b"],["aa","b"]]
print(partition("a"))    # expected: [["a"]]
```
