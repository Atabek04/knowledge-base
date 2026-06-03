---
difficulty: Hard
status: Not started
topic: [K-way Merge, Arrays, Heap, Binary Search]
tags: [k-way-merge, array, heap, binary-search, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given an N×N matrix where every row and every column is sorted in ascending order, return the K-th smallest element in the matrix. You cannot simply index into it because there is no global ordering across rows.

### Constraints
- 1 <= K <= N * N
- 1 <= N <= 300
- Matrix rows and columns are each sorted in ascending order
- Values are integers (can be negative)

### Examples
```
matrix=[[2,6,8],[3,7,10],[5,8,11]], K=5  →  7   (sorted: [2,3,5,6,7,8,8,10,11], 5th = 7)
```

### Next solve approach
1. Brute Force first — flatten all rows into one array, sort it, return element at index K-1, O(N² log N²)
2. Optimized (K-way Merge) — treat each row as a sorted list; push first element of each row into a min-heap; pop K times, advancing the pointer in the chosen row each time, O(K log N)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static int findKthSmallest(int[][] matrix, int k) {
        // TODO
        return -1;
    }

    public static void main(String[] args) {
        int[][] matrix = {
            {2,  6,  8},
            {3,  7,  10},
            {5,  8,  11}
        };
        System.out.println(findKthSmallest(matrix, 5)); // expected: 7
    }
}
```

### Python

```python
def find_kth_smallest(matrix: list[list[int]], k: int) -> int:
    # TODO: implement
    pass


matrix = [
    [2,  6,  8],
    [3,  7,  10],
    [5,  8,  11],
]
print(find_kth_smallest(matrix, 5))  # expected: 7
```
