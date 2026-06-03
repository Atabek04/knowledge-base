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
last_solved: 2026-06-03
link: https://neetcode.io/solutions/longest-substring-with-at-most-k-distinct-characters
---

### Problem
Given a string and an integer k, find the length of the longest contiguous substring that contains at most k distinct characters. You need to consider all valid substrings and return the maximum length.

### Constraints
- 1 <= k <= 26
- String contains lowercase English letters
- Input fits in memory

### Examples
```
"araaci", k=2  →  4   (substring "araa")
"araaci", k=1  →  2   (substring "aa")
"cbbebi", k=3  →  5   (substring "cbbeb" or "bbebi")
```

### Next solve approach
1. Brute Force first — check every substring, count distinct chars, track maximum length, O(n²)
2. Optimized (Sliding Window) — use a frequency map; shrink left when distinct count exceeds k, O(n)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static int findLength(String str, int k) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(findLength("araaci", 2)); // expected: 4
        System.out.println(findLength("araaci", 1)); // expected: 2
        System.out.println(findLength("cbbebi", 3)); // expected: 5
    }
}
```

### Python

```python
def find_length(s: str, k: int) -> int:
    # TODO: implement
    pass


print(find_length("araaci", 2))  # expected: 4
print(find_length("araaci", 1))  # expected: 2
print(find_length("cbbebi", 3))  # expected: 5
```
