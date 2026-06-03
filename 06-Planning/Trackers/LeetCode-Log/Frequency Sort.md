---
difficulty: Medium
status: Not started
topic: [Top K Elements, Strings, Heap]
tags: [top-k-elements, string, heap, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a string, rearrange its characters so that they are sorted in decreasing order of frequency. Characters with the same frequency can appear in any relative order among themselves. Return any valid rearrangement.

### Constraints
- Input is a non-empty string of printable characters
- Characters are case-sensitive ('P' and 'p' are different)
- Multiple valid outputs exist when frequencies tie

### Examples
```
"Programming"  →  "rrggmmPiano"   (r, g, m each appear twice; rest appear once)
"abcbab"       →  "bbbaac"        (b×3, a×2, c×1)
```

### Next solve approach
1. Brute Force first — count frequencies, sort characters by count descending, build output string, O(n log n)
2. Optimized (Top K Elements) — use a max-heap ordered by frequency; pop the most frequent character and append it repeatedly, O(n log d) where d is distinct chars

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static String sortCharacterByFrequency(String str) {
        // TODO
        return "";
    }

    public static void main(String[] args) {
        System.out.println(sortCharacterByFrequency("Programming")); // expected: rrggmmPiano (or equivalent)
        System.out.println(sortCharacterByFrequency("abcbab"));      // expected: bbbaac
    }
}
```

### Python

```python
def sort_character_by_frequency(s: str) -> str:
    # TODO: implement
    pass


print(sort_character_by_frequency("Programming"))  # expected: rrggmmPiano (or equivalent)
print(sort_character_by_frequency("abcbab"))       # expected: bbbaac
```
