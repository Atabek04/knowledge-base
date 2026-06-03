---
aliases: [Sliding Window]
---

Sliding Window is a coding pattern for problems that ask about a **contiguous** run of elements in an array or string. A naive solution re-scans every subarray (O(n²)); the window slides one step at a time and **reuses the overlap** between consecutive subarrays, so each element is added and removed once — O(n).

The name is the mnemonic: picture a fixed frame sliding across the data — what leaves the back you subtract, what enters the front you add.

### Trigger — when to reach for it

<mark style="background: #FFF3A3A6; font-weight: bold;">Recognition signals</mark> in the problem statement:

- Linear structure: **array or string**, and you need a **contiguous** subarray/substring (not a subsequence)
- Asks for the **longest / shortest / max-sum / min / count** of windows meeting a constraint
- Keywords: <mark style="background: #ABF7F7A6;">"size K"</mark>, "at most K distinct", "containing", "consecutive", "no-repeat", "after replacement / K flips"
- Brute force would check **all subarrays in O(n²)** — the window collapses it to O(n)

<mark style="background: #FF9D9DA6;">Not Sliding Window if</mark> the elements aren't contiguous (subsequence → DP) or the array must be sorted/reordered first.

### How it works

Two indices, `left` and `right`, bound the current window.
`right` always advances, growing the window and updating a running aggregate (sum, char count).
`left` advances only to restore validity — shrinking the window when a constraint breaks.
Because indices only move forward, total work is O(n).

### Variants

- <mark style="background: #ABF7F7A6;">**Fixed window**</mark> — window size K is known. Slide a constant-width frame; add the entering element, subtract the leaving one.
- <mark style="background: #ABF7F7A6;">**Variable window**</mark> — size unknown. Grow `right` greedily; shrink `left` in a `while` until the window is valid again. Track best size/count along the way.

### Template

```java
// Fixed window — max sum of any subarray of size K
int windowSum = 0, maxSum = 0;
for (int right = 0; right < arr.length; right++) {
    windowSum += arr[right];
    if (right >= k - 1) {            // window full
        maxSum = Math.max(maxSum, windowSum);
        windowSum -= arr[right - k + 1]; // drop leftmost
    }
}

// Variable window — longest valid window
int left = 0, best = 0;
for (int right = 0; right < arr.length; right++) {
    add(arr[right]);                 // extend
    while (!valid()) {               // shrink until valid
        remove(arr[left]);
        left++;
    }
    best = Math.max(best, right - left + 1);
}
```

### Complexity

- Time: **O(n)** — each element enters and leaves the window at most once
- Space: **O(1)** for sums, **O(k)** when tracking a frequency map of window contents

### Pitfalls

- <mark style="background: #FF9D9DA6;">Common mistake:</mark> shrinking with `if` instead of `while` in a variable window — one removal may not be enough to restore validity.
- Off-by-one on the fixed window: it becomes full at `right == k - 1`, and the element to drop is `arr[right - k + 1]`.
- Forgetting to update the answer **before** shrinking when the problem counts every valid window.

### Practice problems

- [[Maximum Sum Subarray of Size K]] — Easy
- [[Smallest Subarray with a Given Sum]] — Easy
- [[Best Time to Buy and Sell Stock]] — Easy
- [[Longest Substring with K Distinct Characters]] — Medium
- [[Fruits into Baskets]] — Medium
- [[Longest Substring Without Repeating Characters]] — Medium
- [[Longest Repeating Character Replacement]] — Medium
- [[Permutation in String]] — Medium
- [[Subarrays with Product Less than a Target]] — Medium
- [[No-repeat Substring]] — Hard
- [[Longest Substring with Same Letters after Replacement]] — Hard
- [[Longest Subarray with Ones after Replacement]] — Hard
- [[Minimum Window Substring]] — Hard
- [[Sliding Window Maximum]] — Hard
- [[Sliding Window Median]] — Hard

### Read more
- [[Coding Interview Patterns - MOC]]
