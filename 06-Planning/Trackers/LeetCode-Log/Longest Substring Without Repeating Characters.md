---
difficulty: Medium
status: Not started
topic: [Sliding Window]
tags: [hash-table, string, sliding-window, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/longest-substring-without-repeating-characters/"
---

### Problem
Given a string `s`, find the length of the longest substring that contains no duplicate characters. A substring is a contiguous sequence of characters within the string, not a subsequence.

### Constraints
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols, and spaces.

### Examples
```
s = "abcabcbb"  →  3     (longest is "abc")
s = "bbbbb"     →  1     (longest is "b")
s = "pwwkew"    →  3     (longest is "wke")
```

### Next solve approach
1. Brute Force first — check every substring for uniqueness in O(n²) or O(n³)
2. Optimized — sliding window with a character-count array; shrink left when a duplicate enters the window

---

### Java

```java
public class Solution {

    // TODO: implement
    public int lengthOfLongestSubstring(String s) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.lengthOfLongestSubstring("abcabcbb")); // expected: 3
        System.out.println(sol.lengthOfLongestSubstring("bbbbb"));    // expected: 1
        System.out.println(sol.lengthOfLongestSubstring("pwwkew"));   // expected: 3
    }
}
```

### Python

```python
def length_of_longest_substring(s: str) -> int:
    # TODO: implement
    pass


print(length_of_longest_substring("abcabcbb"))  # expected: 3
print(length_of_longest_substring("bbbbb"))      # expected: 1
print(length_of_longest_substring("pwwkew"))     # expected: 3
```
