---
difficulty: Hard
status: Not started
topic: [2-D Dynamic Programming]
tags: [string, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/distinct-subsequences/"
---

### Problem
Given two strings s and t, count how many distinct subsequences of s equal t. A subsequence is obtained by deleting some characters from s without changing the order of the remaining characters. The answer is guaranteed to fit in a 32-bit signed integer.

### Constraints
- 1 <= s.length, t.length <= 1000
- s and t consist of English letters

### Examples
```
s = "rabbbit", t = "rabbit"  →  3     (three ways to pick the three b's)
s = "babgbag", t = "bag"     →  5
```

### Next solve approach
1. Brute Force first — recursively match each character of t against s, count all valid selections
2. Optimized — 2-D DP where dp[i][j] = ways to form t[0..j-1] using s[0..i-1]; if chars match, add dp[i-1][j-1]

---

### Java

```java
public class Solution {

    // TODO: implement
    public int numDistinct(String s, String t) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.numDistinct("rabbbit", "rabbit")); // expected: 3
        System.out.println(sol.numDistinct("babgbag", "bag"));    // expected: 5
    }
}
```

### Python

```python
def num_distinct(s: str, t: str) -> int:
    # TODO: implement
    pass


print(num_distinct("rabbbit", "rabbit"))  # expected: 3
print(num_distinct("babgbag", "bag"))     # expected: 5
```
