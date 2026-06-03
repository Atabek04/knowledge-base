---
difficulty: Medium
status: Not started
topic: [Top K Elements, Arrays, Heap, Binary Search]
tags: [top-k-elements, array, heap, binary-search, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a sorted array and two integers K and X, find the K numbers in the array that are closest in value to X. Return these numbers in sorted order. X may or may not exist in the array. When two numbers are equidistant from X, the smaller one is considered closer.

### Constraints
- 1 <= K <= arr.length
- Array is sorted in ascending order
- X can be outside the array's range

### Examples
```
[5, 6, 7, 8, 9], K=3, X=7   →  [6, 7, 8]
[2, 4, 5, 6, 9], K=3, X=6   →  [4, 5, 6]
[2, 4, 5, 6, 9], K=3, X=10  →  [5, 6, 9]
```

### Next solve approach
1. Brute Force first — compute abs distance for each element, sort by distance, take K, sort result, O(n log n)
2. Optimized (Top K Elements) — binary search to find X's position, then use a max-heap of size K on absolute distance; or two-pointer from the closest position outward, O(log n + K)

---

### Java

```java
import java.util.*;

class Entry {
    int key;
    int value;

    public Entry(int key, int value) {
        this.key = key;
        this.value = value;
    }
}

public class Solution {

    // TODO: implement
    public static List<Integer> findClosestElements(int[] arr, int K, Integer X) {
        // TODO
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        System.out.println(findClosestElements(new int[]{5, 6, 7, 8, 9}, 3, 7));  // expected: [6, 7, 8]
        System.out.println(findClosestElements(new int[]{2, 4, 5, 6, 9}, 3, 6));  // expected: [4, 5, 6]
        System.out.println(findClosestElements(new int[]{2, 4, 5, 6, 9}, 3, 10)); // expected: [5, 6, 9]
    }
}
```

### Python

```python
def find_closest_elements(arr: list[int], k: int, x: int) -> list[int]:
    # TODO: implement
    pass


print(find_closest_elements([5, 6, 7, 8, 9], 3, 7))   # expected: [6, 7, 8]
print(find_closest_elements([2, 4, 5, 6, 9], 3, 6))   # expected: [4, 5, 6]
print(find_closest_elements([2, 4, 5, 6, 9], 3, 10))  # expected: [5, 6, 9]
```
