---
difficulty: Hard
status: Not started
topic: [Sliding Window, Strings]
tags: [sliding-window, string, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a string of lowercase letters and an integer k, you may replace at most k characters in any contiguous substring with any letter you choose. Find the length of the longest substring that consists entirely of a single repeating character after those replacements.

### Constraints
- 0 <= k <= str.length
- String contains lowercase English letters only
- Input fits in memory

### Examples
```
"aabccbb", k=2  →  5   (replace 2 'c's with 'b' → "bbbbb")
"abbcb",   k=1  →  4   (replace 'c' with 'b' → "bbbb")
"abccde",  k=1  →  3   (replace 'b' or 'd' with 'c' → "ccc")
```

### Next solve approach
1. Brute Force first — try every substring, check if replacements needed <= k, track maximum, O(n²)
2. Optimized (Sliding Window) — track the count of the most frequent char in the window; if (window size - max frequency > k), shrink left, O(n)

---

### Java

```java
public class Solution {

    // TODO: implement
    public static int findLength(String str, int k) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(findLength("aabccbb", 2)); // expected: 5
        System.out.println(findLength("abbcb", 1));   // expected: 4
        System.out.println(findLength("abccde", 1));  // expected: 3
    }
}
```

### Python

```python
def find_length(s: str, k: int) -> int:
    # TODO: implement
    pass


print(find_length("aabccbb", 2))  # expected: 5
print(find_length("abbcb", 1))    # expected: 4
print(find_length("abccde", 1))   # expected: 3
```
