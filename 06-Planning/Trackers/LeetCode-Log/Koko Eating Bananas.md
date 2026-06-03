---
difficulty: Medium
status: Not started
topic: [Binary Search]
tags: [array, binary-search, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/koko-eating-bananas/"
---

### Problem
Koko has n piles of bananas and h hours before the guards return. Each hour she picks one pile and eats up to k bananas from it; if a pile has fewer than k bananas she finishes the pile in that hour. Find the minimum integer eating speed k that allows her to finish all piles within h hours.

### Constraints
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9

### Examples
```
piles = [3,6,7,11], h = 8   →  4
piles = [30,11,23,4,20], h = 5  →  30
piles = [30,11,23,4,20], h = 6  →  23
```

### Next solve approach
1. Brute Force first — try every speed from 1 to max(piles), return first that finishes in time
2. Optimized — binary search over speed range [1, max(piles)]; check if ceil(piles[i]/mid) sum <= h

---

### Java

```java
public class Solution {

    // TODO: implement
    public int minEatingSpeed(int[] piles, int h) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.minEatingSpeed(new int[]{3, 6, 7, 11}, 8));        // expected: 4
        System.out.println(sol.minEatingSpeed(new int[]{30, 11, 23, 4, 20}, 5));  // expected: 30
        System.out.println(sol.minEatingSpeed(new int[]{30, 11, 23, 4, 20}, 6));  // expected: 23
    }
}
```

### Python

```python
def min_eating_speed(piles: list[int], h: int) -> int:
    # TODO: implement
    pass


print(min_eating_speed([3, 6, 7, 11], 8))        # expected: 4
print(min_eating_speed([30, 11, 23, 4, 20], 5))  # expected: 30
print(min_eating_speed([30, 11, 23, 4, 20], 6))  # expected: 23
```
