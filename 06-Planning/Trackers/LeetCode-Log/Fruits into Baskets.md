---
difficulty: Medium
status: Not started
topic: [Sliding Window, Arrays]
tags: [sliding-window, array, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
You have two baskets, each of which can hold only one type of fruit. Given an array of characters where each element represents a fruit tree, pick fruits from consecutive trees starting at any point. Stop as soon as you would need a third distinct fruit type. Return the maximum number of fruits you can collect across both baskets.

### Constraints
- Array length >= 1
- Each element is a single character representing a fruit type
- Exactly 2 baskets (at most 2 distinct types in any valid window)
- Input fits in memory

### Examples
```
['A','B','C','A','C']      →  3   (window ['C','A','C'])
['A','B','C','B','B','C']  →  5   (window ['B','C','B','B','C'])
```

### Next solve approach
1. Brute Force first — try every starting index, extend while at most 2 types, track maximum, O(n²)
2. Optimized (Sliding Window) — use a frequency map of at most 2 fruit types; shrink left when a third type enters, O(n)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static int findLength(char[] arr) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(findLength(new char[]{'A','B','C','A','C'}));      // expected: 3
        System.out.println(findLength(new char[]{'A','B','C','B','B','C'}));  // expected: 5
    }
}
```

### Python

```python
def find_length(arr: list[str]) -> int:
    # TODO: implement
    pass


print(find_length(['A','B','C','A','C']))      # expected: 3
print(find_length(['A','B','C','B','B','C']))  # expected: 5
```
