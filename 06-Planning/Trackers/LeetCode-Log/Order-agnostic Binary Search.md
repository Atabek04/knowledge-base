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
Given a sorted array that may be in either ascending or descending order, determine if a given key exists in the array. The array may contain duplicates. Return the index of the key if found, or -1 if not present. Since we don't know the sort direction upfront, the algorithm must detect it first and adjust the comparison logic accordingly.

### Constraints
- 1 <= arr.length <= 10^6
- Array is sorted (ascending or descending), may have duplicates
- Integer values; key fits within int range

### Examples
```
[4, 6, 10], key=10              →  2   (ascending, key at end)
[1, 2, 3, 4, 5, 6, 7], key=5   →  4   (ascending)
[10, 6, 4], key=10              →  0   (descending, key at start)
[10, 6, 4], key=4               →  2   (descending, key at end)
```

### Next solve approach
1. Brute Force first — linear scan O(n)
2. Optimized (Modified Binary Search) — detect sort order from first vs last element, flip comparison direction accordingly

---

### Java

```java
class BinarySearch {

    // TODO: implement
    public static int search(int[] arr, int key) {
        // TODO
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(BinarySearch.search(new int[]{4, 6, 10}, 10));             // expected: 2
        System.out.println(BinarySearch.search(new int[]{1, 2, 3, 4, 5, 6, 7}, 5));  // expected: 4
        System.out.println(BinarySearch.search(new int[]{10, 6, 4}, 10));             // expected: 0
        System.out.println(BinarySearch.search(new int[]{10, 6, 4}, 4));              // expected: 2
    }
}
```

### Python

```python
def search(arr: list[int], key: int) -> int:
    # TODO: implement
    pass


print(search([4, 6, 10], 10))             # expected: 2
print(search([1, 2, 3, 4, 5, 6, 7], 5))  # expected: 4
print(search([10, 6, 4], 10))             # expected: 0
print(search([10, 6, 4], 4))              # expected: 2
```
