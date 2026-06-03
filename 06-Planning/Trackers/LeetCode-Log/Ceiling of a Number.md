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
Given an ascending-sorted array, find the index of the ceiling of a given key. The ceiling is the smallest element in the array that is greater than or equal to the key. If no such element exists (key is larger than all elements), return -1.

### Constraints
- 1 <= arr.length <= 10^6
- Array sorted in ascending order
- Integer values; key may be outside the array range

### Examples
```
[4, 6, 10], key=6           →  1   (6 >= 6, index 1)
[1, 3, 8, 10, 15], key=12   →  4   (15 is smallest >= 12, index 4)
[4, 6, 10], key=17          → -1   (no element >= 17)
[4, 6, 10], key=-1          →  0   (4 is smallest >= -1, index 0)
```

### Next solve approach
1. Brute Force first — linear scan until element >= key, O(n)
2. Optimized (Modified Binary Search) — standard binary search; when key is not found, right pointer ends at the ceiling index

---

### Java

```java
class CeilingOfANumber {

    // TODO: implement
    public static int searchCeilingOfANumber(int[] arr, int key) {
        // TODO
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(CeilingOfANumber.searchCeilingOfANumber(new int[]{4, 6, 10}, 6));          // expected: 1
        System.out.println(CeilingOfANumber.searchCeilingOfANumber(new int[]{1, 3, 8, 10, 15}, 12));  // expected: 4
        System.out.println(CeilingOfANumber.searchCeilingOfANumber(new int[]{4, 6, 10}, 17));          // expected: -1
        System.out.println(CeilingOfANumber.searchCeilingOfANumber(new int[]{4, 6, 10}, -1));          // expected: 0
    }
}
```

### Python

```python
def search_ceiling_of_a_number(arr: list[int], key: int) -> int:
    # TODO: implement
    pass


print(search_ceiling_of_a_number([4, 6, 10], 6))           # expected: 1
print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))   # expected: 4
print(search_ceiling_of_a_number([4, 6, 10], 17))           # expected: -1
print(search_ceiling_of_a_number([4, 6, 10], -1))           # expected: 0
```
