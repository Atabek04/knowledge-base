---
difficulty: Medium
status: Not started
topic: [2-D Dynamic Programming]
tags: [string, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/interleaving-string/"
---

### Problem
Given strings s1, s2, and s3, determine whether s3 can be formed by interleaving s1 and s2 while preserving the relative character order of each. An interleaving means splitting each string into substrings and alternating them to form s3. If the combined lengths don't match, the answer is immediately false.

### Constraints
- 0 <= s1.length, s2.length <= 100
- 0 <= s3.length <= 200
- s1, s2, and s3 consist of lowercase English letters

### Examples
```
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"  →  true
s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"  →  false
s1 = "",       s2 = "",       s3 = ""            →  true
```

### Next solve approach
1. Brute Force first — recursively pick next character from s1 or s2, check if s3 is formed
2. Optimized — 2-D DP where dp[i][j] = true if first i chars of s1 and j chars of s2 form first i+j chars of s3

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean isInterleave(String s1, String s2, String s3) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac")); // expected: true
        System.out.println(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc")); // expected: false
        System.out.println(sol.isInterleave("", "", ""));                      // expected: true
    }
}
```

### Python

```python
def is_interleave(s1: str, s2: str, s3: str) -> bool:
    # TODO: implement
    pass


print(is_interleave("aabcc", "dbbca", "aadbbcbcac"))  # expected: True
print(is_interleave("aabcc", "dbbca", "aadbbbaccc"))  # expected: False
print(is_interleave("", "", ""))                        # expected: True
```
