TARGET DECK: Tech-KB::DSA::Sliding Window
Tags: dsa sliding-window
**Related:** [[LeetCode - MOC]]

---

START
Coding Questions
What problem signals tell you to use the **Sliding Window** pattern?
Back: **Sliding Window** fits problems over a **contiguous** subarray/substring of an array or string.
- Asks for the **longest / shortest / max-sum / min / count** window meeting a constraint
- Keywords: "size K", "at most K distinct", "containing", "consecutive", "no-repeat", "after K replacements/flips"
- Brute force checks all subarrays in **O(n²)** → window reuses overlap → **O(n)**
Tags: dsa sliding-window
<!--ID: 1782128729837-->
END

START
Coding Questions
Why is **Sliding Window** O(n) and not O(n²)?
Back: It **reuses the overlap** between consecutive subarrays instead of recomputing.
- `left` and `right` only ever move **forward**
- Each element is added once and removed once
- So total work is linear: **O(n)**
Tags: dsa sliding-window
<!--ID: 1782128729840-->
END

START
Coding Questions
Difference between a **fixed** and a **variable** Sliding Window?
Back:
- **Fixed** — window size K is known. Slide a constant-width frame: add the entering element, subtract the leaving one.
- **Variable** — size unknown. Grow `right` greedily, then **shrink `left` in a `while`** until the window is valid again.
Tags: dsa sliding-window
<!--ID: 1782128729843-->
END

START
Coding Questions
What is the most common **bug** in a variable Sliding Window?
Back: Shrinking with `if` instead of `while`.
- One removal may not restore validity — you must shrink repeatedly: `while (!valid()) { remove(arr[left]); left++; }`
Tags: dsa sliding-window
<!--ID: 1782128729846-->
END
