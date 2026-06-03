---
difficulty: Medium
status: Not started
topic: [1-D Dynamic Programming]
tags: [two-pointers, string, dynamic-programming, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/palindromic-substrings/"
---

### Problem
Given a string s, count the total number of palindromic substrings it contains. A single character always counts as a palindrome. Substrings at different positions are considered distinct even if they have the same characters.

### Constraints
- 1 <= s.length <= 1000
- s consists of lowercase English letters

### Examples
```
s = "abc"  →  3    ("a", "b", "c")
s = "aaa"  →  6    ("a","a","a","aa","aa","aaa")
```

### Next solve approach
1. Brute Force first — generate every substring and check each one for palindrome property
2. Optimized — expand-around-center for each of the 2n-1 possible centers; increment count for every valid expansion (O(n^2) time, O(1) space)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int countSubstrings(String s) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.countSubstrings("abc")); // expected: 3
        System.out.println(sol.countSubstrings("aaa")); // expected: 6
    }
}
```

### Python

```python
def count_substrings(s: str) -> int:
    # TODO: implement
    pass


print(count_substrings("abc")) # expected: 3
print(count_substrings("aaa")) # expected: 6
```
