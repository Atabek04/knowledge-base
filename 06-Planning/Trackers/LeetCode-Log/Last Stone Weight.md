---
difficulty: Easy
status: Not started
topic: [Heap / Priority Queue]
tags: [array, heap, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/last-stone-weight/"
---

### Problem
You have a pile of stones with given weights. Each round you pick the two heaviest stones and smash them together. If they are equal both are destroyed; if one is heavier, the lighter one is destroyed and the heavier one loses the lighter one's weight. Repeat until at most one stone remains and return its weight, or 0 if none are left.

### Constraints
- 1 <= stones.length <= 30
- 1 <= stones[i] <= 1000

### Examples
```
stones = [2,7,4,1,8,1]  →  1     (8-7=1, 4-2=2, 2-1=1, 1-1=0, last stone: 1)
stones = [1]             →  1
```

### Next solve approach
1. Brute Force first — sort on each round, pop two largest, push difference if nonzero
2. Optimized — max-heap to always access the two heaviest stones in O(log n) per round

---

### Java

```java
public class Solution {

    // TODO: implement
    public int lastStoneWeight(int[] stones) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.lastStoneWeight(new int[]{2, 7, 4, 1, 8, 1})); // expected: 1
        System.out.println(sol.lastStoneWeight(new int[]{1}));                 // expected: 1
    }
}
```

### Python

```python
from typing import List

def last_stone_weight(stones: List[int]) -> int:
    # TODO: implement
    pass


print(last_stone_weight([2, 7, 4, 1, 8, 1])) # expected: 1
print(last_stone_weight([1]))                 # expected: 1
```
