---
difficulty: Easy
status: Not started
topic: [Modified Binary Search, Arrays, Binary Search]
tags: [modified-binary-search, array, binary-search, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a bitonic array — one that strictly increases and then strictly decreases — find the maximum element. The peak is the single point where the array switches from increasing to decreasing. No two adjacent elements are equal.

### Constraints
- 1 <= arr.length
- arr[i] != arr[i+1] for all valid i
- Array is bitonic (increasing then decreasing; may be entirely increasing or entirely decreasing)
- Integer values

### Examples
```
[1, 3, 8, 12, 4, 2]  →  12   (peak at index 3)
[3, 8, 3, 1]          →   8   (peak at index 1)
[1, 3, 8, 12]         →  12   (entirely increasing, peak at end)
[10, 9, 8]            →  10   (entirely decreasing, peak at start)
```

### Next solve approach
1. Brute Force first — linear scan tracking max, O(n)
2. Optimized (Modified Binary Search) — if arr[mid] > arr[mid+1], peak is in left half (including mid); else peak is in right half; converge to peak

---

### Java

```java
class MaxInBitonicArray {

    // TODO: implement
    public static int findMax(int[] arr) {
        // TODO
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(MaxInBitonicArray.findMax(new int[]{1, 3, 8, 12, 4, 2})); // expected: 12
        System.out.println(MaxInBitonicArray.findMax(new int[]{3, 8, 3, 1}));         // expected: 8
        System.out.println(MaxInBitonicArray.findMax(new int[]{1, 3, 8, 12}));        // expected: 12
        System.out.println(MaxInBitonicArray.findMax(new int[]{10, 9, 8}));           // expected: 10
    }
}
```

### Python

```python
def find_max(arr: list[int]) -> int:
    # TODO: implement
    pass


print(find_max([1, 3, 8, 12, 4, 2]))  # expected: 12
print(find_max([3, 8, 3, 1]))          # expected: 8
print(find_max([1, 3, 8, 12]))         # expected: 12
print(find_max([10, 9, 8]))            # expected: 10
```
