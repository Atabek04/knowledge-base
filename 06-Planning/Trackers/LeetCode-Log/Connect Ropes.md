---
difficulty: Easy
status: Not started
topic: [Top K Elements, Heap]
tags: [top-k-elements, heap, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given N ropes of different lengths, connect all of them into one rope. Each connection costs the sum of the two rope lengths being joined. Find the minimum total cost to connect all ropes into one.

### Constraints
- 1 <= N <= 10^4
- All rope lengths are positive integers
- Greedily always join the two shortest ropes to minimize cost

### Examples
```
[1, 3, 11, 5]        →  33   (1+3=4, 4+5=9, 9+11=20 → 4+9+20=33)
[3, 4, 5, 6]         →  36   (3+4=7, 5+6=11, 7+11=18 → 7+11+18=36)
[1, 3, 11, 5, 2]     →  42   (1+2=3, 3+3=6, 6+5=11, 11+11=22 → 3+6+11+22=42)
```

### Next solve approach
1. Brute Force first — repeatedly find and join the two smallest, O(n^2)
2. Optimized (Top K Elements) — min-heap; always pop two smallest, push their sum, accumulate cost, O(n log n)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static int minimumCostToConnectRopes(int[] ropeLengths) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(minimumCostToConnectRopes(new int[]{1, 3, 11, 5}));        // expected: 33
        System.out.println(minimumCostToConnectRopes(new int[]{3, 4, 5, 6}));         // expected: 36
        System.out.println(minimumCostToConnectRopes(new int[]{1, 3, 11, 5, 2}));     // expected: 42
    }
}
```

### Python

```python
def minimum_cost_to_connect_ropes(rope_lengths: list[int]) -> int:
    # TODO: implement
    pass


print(minimum_cost_to_connect_ropes([1, 3, 11, 5]))     # expected: 33
print(minimum_cost_to_connect_ropes([3, 4, 5, 6]))      # expected: 36
print(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2]))  # expected: 42
```
