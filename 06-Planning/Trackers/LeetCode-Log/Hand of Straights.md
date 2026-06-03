---
difficulty: Medium
status: Not started
topic: [Greedy]
tags: [greedy, array, hash-table, sorting, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/hand-of-straights/"
---

### Problem
Given an array of card values and a required group size, determine whether all cards can be arranged into groups where each group contains exactly groupSize consecutive integers. Every card must be used exactly once.

### Constraints
- 1 <= hand.length <= 10^4
- 0 <= hand[i] <= 10^9
- 1 <= groupSize <= hand.length

### Examples
```
hand=[1,2,3,6,2,3,4,7,8], groupSize=3  →  true     ([1,2,3],[2,3,4],[6,7,8])
hand=[1,2,3,4,5],          groupSize=4  →  false
```

### Next solve approach
1. Brute Force first — sort cards, try to greedily form groups starting from smallest; O(n * groupSize)
2. Optimized — sort + hash map: count frequencies, iterate sorted unique values, consume groupSize consecutive counts

---

### Java

```java
public class Solution {

    // TODO: implement
    public boolean isNStraightHand(int[] hand, int groupSize) {
        // TODO
        return false;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isNStraightHand(
            new int[]{1,2,3,6,2,3,4,7,8}, 3)); // expected: true
        System.out.println(sol.isNStraightHand(
            new int[]{1,2,3,4,5}, 4));           // expected: false
    }
}
```

### Python

```python
def is_n_straight_hand(hand: list[int], group_size: int) -> bool:
    # TODO: implement
    pass


print(is_n_straight_hand([1,2,3,6,2,3,4,7,8], 3))  # expected: True
print(is_n_straight_hand([1,2,3,4,5], 4))            # expected: False
```
