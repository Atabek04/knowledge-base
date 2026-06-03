---
difficulty: Medium
status: Not started
topic: [Stack]
tags: [stack, array, sorting, monotonic-stack, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/car-fleet/"
---

### Problem
There are n cars on a one-lane road, each at a unique starting position and traveling toward a common target mile marker. A faster car behind a slower car cannot pass — it merges into the slower car's fleet and adopts that fleet's speed. Return the number of distinct car fleets that arrive at the target.

### Constraints
- n == position.length == speed.length
- 1 <= n <= 10^5
- 0 < target <= 10^6
- 0 <= position[i] < target
- All values of position are unique.
- 0 < speed[i] <= 10^6

### Examples
```
target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3]  →  3
target=10, position=[3],          speed=[3]            →  1
target=100, position=[0,2,4],     speed=[4,2,1]        →  1
```

### Next solve approach
1. Brute Force first — simulate every car's position at each time step until all reach target
2. Optimized — sort by position descending, compute each car's time-to-target; a new fleet forms only when a car takes longer than the one ahead

---

### Java

```java
public class Solution {

    // TODO: implement
    public int carFleet(int target, int[] position, int[] speed) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.carFleet(12, new int[]{10, 8, 0, 5, 3}, new int[]{2, 4, 1, 1, 3}));
        // expected: 3

        System.out.println(sol.carFleet(10, new int[]{3}, new int[]{3}));
        // expected: 1

        System.out.println(sol.carFleet(100, new int[]{0, 2, 4}, new int[]{4, 2, 1}));
        // expected: 1
    }
}
```

### Python

```python
from typing import List


def car_fleet(target: int, position: List[int], speed: List[int]) -> int:
    # TODO: implement
    pass


print(car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))  # expected: 3
print(car_fleet(10, [3], [3]))                             # expected: 1
print(car_fleet(100, [0, 2, 4], [4, 2, 1]))               # expected: 1
```
