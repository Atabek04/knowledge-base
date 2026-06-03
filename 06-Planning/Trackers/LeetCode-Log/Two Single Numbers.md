---
difficulty: Medium
status: Not started
topic: [Bitwise XOR, Arrays, Bit Manipulation]
tags: [bitwise-xor, array, bit-manipulation, grokking-patterns]
solved: 0
last_solved: 
link: ""
---

### Problem
Given a non-empty array where every element appears exactly twice except for two numbers that each appear only once, return those two unique numbers. The result can be in any order.

### Constraints
- Array is non-empty
- Exactly two numbers appear only once; all others appear exactly twice
- Array length is at least 2

### Examples
```
[1, 4, 2, 1, 3, 5, 6, 2, 3, 5]  →  [4, 6]   (4 and 6 each appear once)
[2, 1, 3, 2]                     →  [1, 3]   (1 and 3 each appear once)
```

### Next solve approach
1. Brute Force first — use a HashMap to count frequency, collect all keys with count == 1
2. Optimized (Bitwise XOR) — XOR all elements to get n1 ^ n2; use the rightmost set bit to split array into two groups, XOR each group to isolate each unique number

---

### Java

```java
public class Solution {

    // TODO: implement
    public static int[] findSingleNumbers(int[] nums) {
        // TODO
        return new int[0];
    }

    public static void main(String[] args) {
        int[] result = findSingleNumbers(new int[]{1, 4, 2, 1, 3, 5, 6, 2, 3, 5});
        System.out.println(result[0] + ", " + result[1]); // expected: 4, 6

        result = findSingleNumbers(new int[]{2, 1, 3, 2});
        System.out.println(result[0] + ", " + result[1]); // expected: 1, 3
    }
}
```

### Python

```python
def find_single_numbers(nums: list[int]) -> list[int]:
    # TODO: implement
    pass


print(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))  # expected: [4, 6]
print(find_single_numbers([2, 1, 3, 2]))                      # expected: [1, 3]
```
