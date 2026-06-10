---
difficulty: Medium
status: Solved
topic:
  - Sliding Window
  - Strings
tags:
  - sliding-window
  - string
  - grokking-patterns
solved: 1
last_solved: 2026-06-08
link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
---

### Problem
Given a string, find the length of the longest contiguous substring in which no character appears more than once. Every character within the window must be unique.

### Constraints
- String contains ASCII characters
- String length >= 1
- Input fits in memory

### Examples
```
"aabccbb"  →  3   (substring "abc")
"abbbb"    →  2   (substring "ab")
"abccde"   →  3   (substring "abc" or "cde")
```

### Next solve approach
1. Brute Force first — check every substring for uniqueness, track maximum length, O(n²)
2. Optimized (Sliding Window) — use a map of char→last seen index; when a repeat is found, jump left past its previous occurrence, O(n)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static int findLength(String str) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(findLength("aabccbb")); // expected: 3
        System.out.println(findLength("abbbb"));   // expected: 2
        System.out.println(findLength("abccde"));  // expected: 3
    }
}
```

### Python

```python
def find_length(s: str) -> int:
    # TODO: implement
    pass


print(find_length("aabccbb"))  # expected: 3
print(find_length("abbbb"))    # expected: 2
print(find_length("abccde"))   # expected: 3
```
