---
difficulty: Medium
status: Not started
topic: [Modified Binary Search, Arrays, Binary Search]
tags: [modified-binary-search, array, binary-search, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given an ascending-sorted array that may contain duplicates, find the first and last positions of a given key. Return them as a two-element array [first, last]. If the key does not appear in the array, return [-1, -1].

### Constraints
- 1 <= arr.length <= 10^6
- Array sorted in ascending order, may have duplicates
- Integer values

### Examples
```
[4, 6, 6, 6, 9], key=6    →  [1, 3]    (6 appears at indices 1, 2, 3)
[1, 3, 8, 10, 15], key=10  →  [3, 3]    (10 appears only at index 3)
[1, 3, 8, 10, 15], key=12  →  [-1, -1]  (12 not in array)
```

### Next solve approach
1. Brute Force first — linear scan to find first and last occurrence, O(n)
2. Optimized (Modified Binary Search) — run binary search twice: once biased left for first occurrence, once biased right for last occurrence

---

### Java

```java
class FindRange {

    // TODO: implement
    public static int[] findRange(int[] arr, int key) {
        int[] result = new int[]{-1, -1};
        // TODO
        return result;
    }

    public static void main(String[] args) {
        int[] result = FindRange.findRange(new int[]{4, 6, 6, 6, 9}, 6);
        System.out.println("Range: [" + result[0] + ", " + result[1] + "]"); // expected: [1, 3]

        result = FindRange.findRange(new int[]{1, 3, 8, 10, 15}, 10);
        System.out.println("Range: [" + result[0] + ", " + result[1] + "]"); // expected: [3, 3]

        result = FindRange.findRange(new int[]{1, 3, 8, 10, 15}, 12);
        System.out.println("Range: [" + result[0] + ", " + result[1] + "]"); // expected: [-1, -1]
    }
}
```

### Python

```python
def find_range(arr: list[int], key: int) -> list[int]:
    # TODO: implement
    pass


print(find_range([4, 6, 6, 6, 9], 6))      # expected: [1, 3]
print(find_range([1, 3, 8, 10, 15], 10))    # expected: [3, 3]
print(find_range([1, 3, 8, 10, 15], 12))    # expected: [-1, -1]
```
