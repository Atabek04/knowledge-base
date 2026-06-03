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
Given an ascending-sorted array of lowercase letters, find the smallest letter that is strictly greater than the given key. The array is treated as circular — if no letter in the array is greater than the key, wrap around and return the first letter. Assume the array has at least one element.

### Constraints
- 1 <= letters.length <= 10^4
- All characters are lowercase English letters
- Array is sorted in ascending order
- Array is circular: after the last element wraps back to the first

### Examples
```
['a','c','f','h'], key='f'   →  'h'   (smallest letter > 'f')
['a','c','f','h'], key='b'   →  'c'   (smallest letter > 'b')
['a','c','f','h'], key='m'   →  'a'   (wrap-around, no letter > 'm')
['a','c','f','h'], key='h'   →  'a'   (wrap-around, 'h' is last)
```

### Next solve approach
1. Brute Force first — linear scan for first char > key, wrap to index 0 if none found, O(n)
2. Optimized (Modified Binary Search) — binary search for smallest element > key; if not found, return letters[0]

---

### Java

```java
class NextLetter {

    // TODO: implement
    public static char searchNextLetter(char[] letters, char key) {
        // TODO
        return letters[0];
    }

    public static void main(String[] args) {
        System.out.println(NextLetter.searchNextLetter(new char[]{'a', 'c', 'f', 'h'}, 'f')); // expected: h
        System.out.println(NextLetter.searchNextLetter(new char[]{'a', 'c', 'f', 'h'}, 'b')); // expected: c
        System.out.println(NextLetter.searchNextLetter(new char[]{'a', 'c', 'f', 'h'}, 'm')); // expected: a
        System.out.println(NextLetter.searchNextLetter(new char[]{'a', 'c', 'f', 'h'}, 'h')); // expected: a
    }
}
```

### Python

```python
def search_next_letter(letters: list[str], key: str) -> str:
    # TODO: implement
    pass


print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))  # expected: h
print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))  # expected: c
print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))  # expected: a
print(search_next_letter(['a', 'c', 'f', 'h'], 'h'))  # expected: a
```
