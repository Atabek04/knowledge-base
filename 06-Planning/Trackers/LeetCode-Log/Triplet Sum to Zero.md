---
difficulty: Medium
status: Not started
topic: [Two Pointers, Arrays]
tags: [two-pointers, array, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given an unsorted array of integers, find all unique triplets that sum to zero. Each triplet must use three different indices, and the result must not contain duplicate triplets. Return a list of all such triplets.

### Constraints
- Array is unsorted and may contain duplicates
- Triplets in the output must be unique
- 0 <= arr.length <= 3000
- Values fit in int range

### Examples
```
[-3, 0, 1, 2, -1, 1, -2]  →  [[-3,1,2], [-2,0,2], [-2,1,1], [-1,0,1]]
[-5, 2, -1, -2, 3]         →  [[-5,2,3], [-2,-1,3]]
```

### Next solve approach
1. Brute Force first — three nested loops checking all index triples, deduplicate with a set, O(n³)
2. Optimized (Two Pointers) — sort array, fix one element and use two pointers on the rest, skip duplicates, O(n²)

---

### Java

```java
import java.util.*;

public class Solution {

    // TODO: implement
    public static List<List<Integer>> searchTriplets(int[] arr) {
        List<List<Integer>> triplets = new ArrayList<>();
        // TODO
        return triplets;
    }

    public static void main(String[] args) {
        System.out.println(searchTriplets(new int[]{-3, 0, 1, 2, -1, 1, -2}));  // expected: [[-3,1,2], [-2,0,2], [-2,1,1], [-1,0,1]]
        System.out.println(searchTriplets(new int[]{-5, 2, -1, -2, 3}));         // expected: [[-5,2,3], [-2,-1,3]]
    }
}
```

### Python

```python
def search_triplets(arr: list[int]) -> list[list[int]]:
    # TODO: implement
    pass


print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))  # expected: [[-3,1,2], [-2,0,2], [-2,1,1], [-1,0,1]]
print(search_triplets([-5, 2, -1, -2, 3]))          # expected: [[-5,2,3], [-2,-1,3]]
```
