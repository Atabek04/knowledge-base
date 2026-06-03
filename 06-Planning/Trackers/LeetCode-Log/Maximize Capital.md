---
difficulty: Hard
status: Not started
topic: [Two Heaps, Heap, Greedy]
tags: [two-heaps, heap, greedy, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
You have a list of projects, each with a required capital to start and an expected profit. Given an initial capital and a limit on how many projects you can pick, choose at most that many projects (one at a time, in any order) to maximize your total capital. After completing a project, its profit is added to your available capital and can be used to fund the next project.

### Constraints
- 1 <= numberOfProjects <= capital.length
- initialCapital >= 0
- profits[i] >= 0, capital[i] >= 0
- Input fits in memory

### Examples
```
capital=[0,1,2], profits=[1,2,3], initialCapital=1, numberOfProjects=2  →  6
    (pick project 2: capital→3, then project 3: capital→6)

capital=[0,1,2,3], profits=[1,2,3,5], initialCapital=0, numberOfProjects=3  →  8
    (pick project 1: capital→1, pick project 2: capital→3, pick project 4: capital→8)
```

### Next solve approach
1. Brute Force first — at each step, scan all affordable projects, pick max profit, repeat, O(n^2 * k)
2. Optimized (Two Heaps) — min-heap on capital to surface affordable projects; max-heap on profit to greedily pick highest-profit affordable project; repeat k times

---

### Java

```java
import java.util.*;

class MaximizeCapital {

    public static int findMaximumCapital(int[] capital, int[] profits, int numberOfProjects, int initialCapital) {
        // TODO: Write your code here
        return -1;
    }

    public static void main(String[] args) {
        int result = MaximizeCapital.findMaximumCapital(new int[]{0, 1, 2}, new int[]{1, 2, 3}, 2, 1);
        System.out.println("Maximum capital: " + result); // expected: 6

        result = MaximizeCapital.findMaximumCapital(new int[]{0, 1, 2, 3}, new int[]{1, 2, 3, 5}, 3, 0);
        System.out.println("Maximum capital: " + result); // expected: 8
    }
}
```

### Python

```python
def find_maximum_capital(capital: list[int], profits: list[int], number_of_projects: int, initial_capital: int) -> int:
    # TODO: implement
    return -1


print(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1))       # expected: 6
print(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)) # expected: 8
```
