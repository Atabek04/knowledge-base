---
difficulty: Hard
status: Not started
topic: [Sliding Window]
tags: [hash-table, string, sliding-window, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/minimum-window-substring/"
---

### Problem
Given strings `s` and `t`, find the shortest contiguous substring of `s` that contains every character from `t` (including duplicates). If no such substring exists, return an empty string. The answer is guaranteed to be unique when it exists.

### Constraints
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters.

### Examples
```
s = "ADOBECODEBANC", t = "ABC"  →  "BANC"    (shortest window covering A, B, C)
s = "a", t = "a"                →  "a"
s = "a", t = "aa"               →  ""         (only one 'a' in s, need two)
```

### Next solve approach
1. Brute Force first — check every substring of s to see if it contains all of t in O(m² * n)
2. Optimized — sliding window with two character-count arrays; expand right until valid, then shrink left to minimize

---

### Java

```java
public class Solution {

    // TODO: implement
    public String minWindow(String s, String t) {
        // TODO
        return "";
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.minWindow("ADOBECODEBANC", "ABC")); // expected: "BANC"
        System.out.println(sol.minWindow("a", "a"));               // expected: "a"
        System.out.println(sol.minWindow("a", "aa"));              // expected: ""
    }
}
```

### Python

```python
def min_window(s: str, t: str) -> str:
    # TODO: implement
    pass


print(min_window("ADOBECODEBANC", "ABC"))  # expected: "BANC"
print(min_window("a", "a"))                # expected: "a"
print(min_window("a", "aa"))               # expected: ""
```
