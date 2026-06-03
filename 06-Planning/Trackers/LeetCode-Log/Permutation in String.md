---
difficulty: Medium
status: Not started
topic: [Sliding Window]
tags: [hash-table, two-pointers, string, sliding-window, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/permutation-in-string/"
---

### Problem
Given strings `s1` and `s2`, return `true` if any permutation of `s1` appears as a contiguous substring in `s2`. In other words, check whether `s2` contains an anagram of `s1` somewhere inside it.

### Constraints
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.

### Examples
```
s1 = "ab", s2 = "eidbaooo"  →  true     ("ba" is a permutation of "ab" at index 3)
s1 = "ab", s2 = "eidboaoo"  →  false
```

### Next solve approach
1. Brute Force first — generate all permutations of s1 and check if any is a substring of s2
2. Optimized — fixed-size sliding window of length s1.length; use a character count array and a "need" counter to check match in O(1)

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean checkInclusion(String s1, String s2) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.checkInclusion("ab", "eidbaooo")); // expected: true
        System.out.println(sol.checkInclusion("ab", "eidboaoo")); // expected: false
    }
}
```

### Python

```python
def check_inclusion(s1: str, s2: str) -> bool:
    # TODO: implement
    pass


print(check_inclusion("ab", "eidbaooo"))  # expected: True
print(check_inclusion("ab", "eidboaoo"))  # expected: False
```
