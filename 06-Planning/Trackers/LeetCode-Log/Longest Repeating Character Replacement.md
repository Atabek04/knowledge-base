---
difficulty: Medium
status: Not started
topic: [Sliding Window]
tags: [hash-table, string, sliding-window, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/longest-repeating-character-replacement/"
---

### Problem
You are given an uppercase string `s` and an integer `k`. You can replace any character in the string with any other uppercase letter, up to `k` times total. Return the length of the longest substring you can produce where all characters are the same after performing at most `k` replacements.

### Constraints
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length

### Examples
```
s = "ABAB", k = 2      →  4     (replace both A's or both B's)
s = "AABABBA", k = 1   →  4     (replace middle A to get "BBBB")
```

### Next solve approach
1. Brute Force first — check every substring and simulate replacements in O(n²)
2. Optimized — sliding window tracking the max frequency character; shrink when (window size - max freq) > k

---

### Java

```java
public class Solution {

    // TODO: implement
    public int characterReplacement(String s, int k) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.characterReplacement("ABAB", 2));      // expected: 4
        System.out.println(sol.characterReplacement("AABABBA", 1));   // expected: 4
    }
}
```

### Python

```python
def character_replacement(s: str, k: int) -> int:
    # TODO: implement
    pass


print(character_replacement("ABAB", 2))      # expected: 4
print(character_replacement("AABABBA", 1))   # expected: 4
```
