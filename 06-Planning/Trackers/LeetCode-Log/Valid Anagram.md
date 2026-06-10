---
difficulty: Easy
status: Cheated
topic:
  - Arrays & Hashing
tags:
  - hash-table
  - string
  - sorting
  - neetcode-150
solved: 0
last_solved: 2026-06-10
link: https://leetcode.com/problems/valid-anagram/
---

### Problem
Given two strings s and t, return true if t is an anagram of s — meaning both strings contain exactly the same characters with the same frequencies. If the lengths differ they cannot be anagrams. Only lowercase English letters are present.

### Constraints
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

### Examples
```
s = "anagram", t = "nagaram"  →  true
s = "rat",     t = "car"      →  false
```

### Next solve approach
1. Brute Force first — sort both strings and compare character by character
   - Time: O(n log n)
   - Space: O(n) (sort buffer)
2. HashMap counters — two maps, count each char in s and t, compare maps
   - Time: O(n)
   - Space: O(n) — up to 26 keys, but scales with alphabet size
3. Single count array — one int[26], increment for s, decrement for t, check all zeros
   - Time: O(n)
   - Space: O(1) — fixed 26-element array

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean isAnagram(String s, String t) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isAnagram("anagram", "nagaram")); // expected: true
        System.out.println(sol.isAnagram("rat", "car"));         // expected: false
    }
}
```

### Python

```python
def is_anagram(s: str, t: str) -> bool:
    # TODO: implement
    pass


print(is_anagram("anagram", "nagaram"))  # expected: True
print(is_anagram("rat", "car"))          # expected: False
```
