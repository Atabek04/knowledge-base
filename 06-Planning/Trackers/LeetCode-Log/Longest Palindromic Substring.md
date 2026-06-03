---
difficulty: Medium
status: Not started
topic: [1-D Dynamic Programming]
tags: [two-pointers, string, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/longest-palindromic-substring/"
---

### Problem
Given a string s, find and return the longest contiguous substring that is a palindrome (reads the same forwards and backwards). If multiple substrings of equal maximum length exist, returning any one of them is acceptable.

### Constraints
- 1 <= s.length <= 1000
- s consists of only digits and English letters

### Examples
```
s = "babad"  →  "bab"    ("aba" is also valid)
s = "cbbd"   →  "bb"
```

### Next solve approach
1. Brute Force first — check every substring with a helper isPalindrome function, track the longest seen
2. Optimized — expand-around-center: for each index treat it as the center of an odd and even palindrome, expand outward while chars match (O(n^2) time, O(1) space)

---

### Java

```java
public class Solution {

    // TODO: implement
    public String longestPalindrome(String s) {
        // TODO
        return "";
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.longestPalindrome("babad")); // expected: "bab" (or "aba")
        System.out.println(sol.longestPalindrome("cbbd"));  // expected: "bb"
    }
}
```

### Python

```python
def longest_palindrome(s: str) -> str:
    # TODO: implement
    pass


print(longest_palindrome("babad")) # expected: "bab" (or "aba")
print(longest_palindrome("cbbd"))  # expected: "bb"
```
