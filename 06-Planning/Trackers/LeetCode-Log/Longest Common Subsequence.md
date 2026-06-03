---
difficulty: Medium
status: Not started
topic: [2-D Dynamic Programming]
tags: [string, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/longest-common-subsequence/"
---

### Problem
Given two strings text1 and text2, find the length of their longest common subsequence. A subsequence is formed by deleting some (or no) characters from a string without changing the relative order of the remaining characters. If the two strings share no common subsequence, return 0.

### Constraints
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters

### Examples
```
text1 = "abcde", text2 = "ace"  →  3     (LCS is "ace")
text1 = "abc",   text2 = "abc"  →  3     (LCS is "abc")
text1 = "abc",   text2 = "def"  →  0     (no common subsequence)
```

### Next solve approach
1. Brute Force first — generate all subsequences of both strings, find longest match
2. Optimized — 2-D DP where dp[i][j] = dp[i-1][j-1]+1 if chars match, else max(dp[i-1][j], dp[i][j-1])

---

### Java

```java
public class Solution {

    // TODO: implement
    public int longestCommonSubsequence(String text1, String text2) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.longestCommonSubsequence("abcde", "ace")); // expected: 3
        System.out.println(sol.longestCommonSubsequence("abc", "abc"));   // expected: 3
        System.out.println(sol.longestCommonSubsequence("abc", "def"));   // expected: 0
    }
}
```

### Python

```python
def longest_common_subsequence(text1: str, text2: str) -> int:
    # TODO: implement
    pass


print(longest_common_subsequence("abcde", "ace"))  # expected: 3
print(longest_common_subsequence("abc", "abc"))    # expected: 3
print(longest_common_subsequence("abc", "def"))    # expected: 0
```
