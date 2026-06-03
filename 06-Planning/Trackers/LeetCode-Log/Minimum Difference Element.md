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
Given an ascending-sorted array, find the element with the smallest absolute difference from a given key. If the key is present in the array, return it directly. Otherwise, after binary search narrows down, the answer is either the element just below or just above where the key would sit — compare those two neighbors and return the closer one.

### Constraints
- 1 <= arr.length <= 10^6
- Array sorted in ascending order
- Integer values; key may be outside the array range

### Examples
```
[4, 6, 10], key=7          →   6   (|6-7|=1 < |10-7|=3)
[4, 6, 10], key=4          →   4   (exact match)
[1, 3, 8, 10, 15], key=12  →  10   (|10-12|=2 < |15-12|=3)
[4, 6, 10], key=17         →  10   (10 is closest)
```

### Next solve approach
1. Brute Force first — scan all elements tracking minimum absolute difference, O(n)
2. Optimized (Modified Binary Search) — binary search until low > high; at that point arr[high] and arr[low] are the two candidates, return whichever is closer to key

---

### Java

```java
class MinimumDifference {

    // TODO: implement
    public static int searchMinDiffElement(int[] arr, int key) {
        // TODO
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(MinimumDifference.searchMinDiffElement(new int[]{4, 6, 10}, 7));          // expected: 6
        System.out.println(MinimumDifference.searchMinDiffElement(new int[]{4, 6, 10}, 4));          // expected: 4
        System.out.println(MinimumDifference.searchMinDiffElement(new int[]{1, 3, 8, 10, 15}, 12));  // expected: 10
        System.out.println(MinimumDifference.searchMinDiffElement(new int[]{4, 6, 10}, 17));         // expected: 10
    }
}
```

### Python

```python
def search_min_diff_element(arr: list[int], key: int) -> int:
    # TODO: implement
    pass


print(search_min_diff_element([4, 6, 10], 7))           # expected: 6
print(search_min_diff_element([4, 6, 10], 4))           # expected: 4
print(search_min_diff_element([1, 3, 8, 10, 15], 12))   # expected: 10
print(search_min_diff_element([4, 6, 10], 17))          # expected: 10
```
