---
difficulty: Medium
status: Not started
topic: [2-D Dynamic Programming]
tags: [string, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/edit-distance/"
---

### Problem
Given two strings word1 and word2, return the minimum number of operations needed to convert word1 into word2. The three allowed operations are: insert a character, delete a character, or replace a character. This is the classic Levenshtein distance problem.

### Constraints
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters

### Examples
```
word1 = "horse", word2 = "ros"         →  3     (replace h→r, delete r, delete e)
word1 = "intention", word2 = "execution"  →  5
```

### Next solve approach
1. Brute Force first — recursively try insert, delete, replace at each mismatch, return minimum depth
2. Optimized — 2-D DP where dp[i][j] = min ops to convert word1[0..i-1] to word2[0..j-1]; match = dp[i-1][j-1], else 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

---

### Java

```java
public class Solution {

    // TODO: implement
    public int minDistance(String word1, String word2) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.minDistance("horse", "ros"));          // expected: 3
        System.out.println(sol.minDistance("intention", "execution")); // expected: 5
    }
}
```

### Python

```python
def min_distance(word1: str, word2: str) -> int:
    # TODO: implement
    pass


print(min_distance("horse", "ros"))           # expected: 3
print(min_distance("intention", "execution")) # expected: 5
```
