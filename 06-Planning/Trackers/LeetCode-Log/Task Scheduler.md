---
difficulty: Medium
status: Not started
topic: [Heap / Priority Queue]
tags: [greedy, array, hash-table, counting, sorting, heap, neetcode-150]
solved: 0
last_solved: 
link: "https://leetcode.com/problems/task-scheduler/"
---

### Problem
You are given a list of CPU tasks labeled A–Z and a cooldown integer n. The CPU must wait at least n intervals before running the same task type again; it can idle during that gap. Return the minimum number of CPU intervals needed to finish all tasks.

### Constraints
- 1 <= tasks.length <= 10^4
- tasks[i] is an uppercase English letter
- 0 <= n <= 100

### Examples
```
tasks = ["A","A","A","B","B","B"], n = 2  →  8     (A->B->idle->A->B->idle->A->B)
tasks = ["A","C","A","B","D","B"], n = 1  →  6     (A->B->C->D->A->B)
tasks = ["A","A","A","B","B","B"], n = 3  →  10    (A->B->idle->idle->A->B->idle->idle->A->B)
```

### Next solve approach
1. Brute Force first — simulate a queue with a cooldown set, pick the highest-count available task each tick
2. Optimized — greedy formula: answer = max(tasks.length, (maxFreq - 1) * (n + 1) + countOfMaxFreq)

---

### Java

```java
public class Solution {

    // TODO: implement
    public int leastInterval(char[] tasks, int n) {
        // TODO
        return 0;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.leastInterval(new char[]{'A','A','A','B','B','B'}, 2)); // expected: 8
        System.out.println(sol.leastInterval(new char[]{'A','C','A','B','D','B'}, 1)); // expected: 6
        System.out.println(sol.leastInterval(new char[]{'A','A','A','B','B','B'}, 3)); // expected: 10
    }
}
```

### Python

```python
from typing import List

def least_interval(tasks: List[str], n: int) -> int:
    # TODO: implement
    pass


print(least_interval(["A","A","A","B","B","B"], 2)) # expected: 8
print(least_interval(["A","C","A","B","D","B"], 1)) # expected: 6
print(least_interval(["A","A","A","B","B","B"], 3)) # expected: 10
```
