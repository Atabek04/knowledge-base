---
difficulty: Easy
status: Cheated
topic: [Sliding Window]
solved: 0
last_solved: 2026-06-01
link: ""
---

### Problem
Given an array of positive integers and a positive integer K, find the maximum sum of any contiguous subarray of size K.

### Constraints
- 1 <= K <= arr.length
- Array contains positive integers

### Examples
```
[2, 1, 5, 1, 3, 2], K=3  →  9   (subarray [5, 1, 3])
[2, 3, 4, 1, 5],    K=2  →  7   (subarray [3, 4])
[1, 1, 1, 1, 1],    K=1  →  1
```

### Next solve approach
1. Brute Force first — nested loop, O(n*k)
2. Sliding Window — drop left, add right, O(n)

---

### Java

```java
public class MaxSumSubarray {

    // TODO: implement
    public static int maxSumSubarray(int[] arr, int k) {
        return 0;
    }

    public static void main(String[] args) {
        System.out.println(maxSumSubarray(new int[]{2, 1, 5, 1, 3, 2}, 3)); // expected: 9
        System.out.println(maxSumSubarray(new int[]{2, 3, 4, 1, 5}, 2));    // expected: 7
        System.out.println(maxSumSubarray(new int[]{1, 1, 1, 1, 1}, 1));    // expected: 1
        System.out.println(maxSumSubarray(new int[]{5}, 1));                 // expected: 5
    }
}
```

### Python

```python
def max_sum_subarray(arr: list[int], k: int) -> int:
    # TODO: implement
    return 0


# Test cases
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # expected: 9
print(max_sum_subarray([2, 3, 4, 1, 5], 2))      # expected: 7
print(max_sum_subarray([1, 1, 1, 1, 1], 1))      # expected: 1
print(max_sum_subarray([5], 1))                   # expected: 5
```
