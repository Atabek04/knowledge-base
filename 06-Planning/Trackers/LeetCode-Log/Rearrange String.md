---
difficulty: Hard
status: Not started
topic: [Top K Elements, Strings, Heap]
tags: [top-k-elements, string, heap, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a string, determine if its characters can be rearranged so that no two adjacent characters are the same. If such a rearrangement exists, return any valid one. If it is impossible (e.g., one character appears too many times), return an empty string.

### Constraints
- A valid rearrangement exists only if the most frequent character appears at most ceil(n/2) times
- Input contains only printable characters (case-sensitive)
- Multiple valid outputs exist; return any one

### Examples
```
"aappp"       →  "papap"              (no two same chars adjacent)
"Programming" →  "rgmrgmPiano" (etc.) (r, g, m each appear twice; rest once)
"aapa"        →  ""                   (a appears 3 times in length-4 string — impossible)
```

### Next solve approach
1. Brute Force first — generate all permutations, check each for adjacent duplicates, O(n!)
2. Optimized (Top K Elements) — max-heap by frequency; greedily place the most frequent char, then the next most frequent, alternating; if two same chars would be adjacent, it's impossible, O(n log d)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static String rearrangeString(String str) {
        // TODO
        return "";
    }

    public static void main(String[] args) {
        System.out.println(rearrangeString("aappp"));       // expected: "papap" (or any valid)
        System.out.println(rearrangeString("Programming")); // expected: any valid rearrangement with no adjacent duplicates
        System.out.println(rearrangeString("aapa"));        // expected: ""
    }
}
```

### Python

```python
def rearrange_string(s: str) -> str:
    # TODO: implement
    pass


print(rearrange_string("aappp"))        # expected: "papap" (or any valid)
print(rearrange_string("Programming"))  # expected: any valid rearrangement with no adjacent duplicates
print(rearrange_string("aapa"))         # expected: ""
```
