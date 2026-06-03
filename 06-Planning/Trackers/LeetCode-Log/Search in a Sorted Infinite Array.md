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
Given an infinite sorted array of unknown size (accessed via a reader interface that returns Integer.MAX_VALUE for out-of-bounds indices), find the index of a given key. Return -1 if the key is not present. Since we cannot compute the length, we must dynamically expand the search window until we find bounds that contain the key, then apply binary search within those bounds.

### Constraints
- Array is sorted in ascending order with unknown length
- ArrayReader.get(index) returns Integer.MAX_VALUE if index is out of bounds
- Integer values; key fits within int range

### Examples
```
[4,6,8,10,12,14,16,18,20,22,24,26,28,30], key=16   →   6   (found at index 6)
[4,6,8,10,12,14,16,18,20,22,24,26,28,30], key=11   →  -1   (not in array)
[1, 3, 8, 10, 15], key=15                           →   4   (found at index 4)
[1, 3, 8, 10, 15], key=200                          →  -1   (not in array)
```

### Next solve approach
1. Brute Force first — increment index one by one until found or MAX_VALUE, O(n)
2. Optimized (Modified Binary Search) — double the window (start=0, end=1, then end*=2) until key <= arr[end]; binary search within [start, end]

---

### Java

```java
class ArrayReader {
    int[] arr;
    ArrayReader(int[] arr) { this.arr = arr; }
    public int get(int index) {
        if (index >= arr.length) return Integer.MAX_VALUE;
        return arr[index];
    }
}

class SearchInfiniteSortedArray {

    // TODO: implement
    public static int search(ArrayReader reader, int key) {
        // TODO
        return -1;
    }

    public static void main(String[] args) {
        ArrayReader reader = new ArrayReader(new int[]{4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30});
        System.out.println(SearchInfiniteSortedArray.search(reader, 16));  // expected: 6
        System.out.println(SearchInfiniteSortedArray.search(reader, 11));  // expected: -1

        reader = new ArrayReader(new int[]{1, 3, 8, 10, 15});
        System.out.println(SearchInfiniteSortedArray.search(reader, 15));  // expected: 4
        System.out.println(SearchInfiniteSortedArray.search(reader, 200)); // expected: -1
    }
}
```

### Python

```python
class ArrayReader:
    def __init__(self, arr: list[int]):
        self.arr = arr

    def get(self, index: int) -> int:
        if index >= len(self.arr):
            return float('inf')
        return self.arr[index]


def search(reader: ArrayReader, key: int) -> int:
    # TODO: implement
    pass


reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
print(search(reader, 16))   # expected: 6
print(search(reader, 11))   # expected: -1

reader = ArrayReader([1, 3, 8, 10, 15])
print(search(reader, 15))   # expected: 4
print(search(reader, 200))  # expected: -1
```
