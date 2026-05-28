# NeetCode 150

**Source:** [neetcode.io/practice](https://neetcode.io/practice/practice/neetcode150) — verified against the canonical 150 list.
**Progress:** 0 / 150 · **Core (⭐):** 0 / 52

Real LeetCode problems, **reordered into 6 phases by priority** (not NeetCode's default order). ⭐ = the ~52 core problems you actually solve. Unstarred = optional menu — do them only if a pattern feels shaky or you have spare time. **Don't grind all 150** — mastering ~15-20 patterns beats a 150 checkmark.

---

### How to use this with Grokking (one loop, per pattern)

These two trackers are **two halves of one loop**, not competing tracks. Work **one pattern at a time**:

1. **Grokking** → read the pattern, understand the template + the *signal* that triggers it
2. **NeetCode (here)** → solve that pattern's ⭐ problems, easy → hard
3. **Re-solve** ~30-40% a week later, blind → promote into `LeetCode-Log/` with `status=Cheated` if you needed help
4. Pass the **gate** → next pattern

**Per-problem protocol:**
- **Classify before coding** — name the pattern + signal, *then* write
- **~25 min struggle cap** — stuck past that, study the solution + watch the video
- **After solving**, write 2-3 sentences: what signal hinted the pattern · what constraint killed brute force · the one-line explanation you'd give an interviewer
- **Gate to advance a phase:** can ID each pattern's signal in <2 min, and re-solve its ⭐ problems blind

---

### Order at a glance

| Phase | Patterns | ⭐ Core | Grokking pattern it maps to |
|---|---|---|---|
| **1 — Linear foundations** | Arrays & Hashing · Two Pointers · Sliding Window · Stack | 15 | Sliding Window, Two Pointers |
| **2 — Search & lists** | Binary Search · Linked List | 10 | Modified Binary Search, Fast & Slow + In-place Reversal |
| **3 — Trees & heaps** | Trees · Heap / Priority Queue | 10 | Tree BFS + Tree DFS, Two Heaps + Top K + K-way Merge |
| **4 — Recursion & graphs** | Backtracking · Graphs | 9 | Subsets, Topological Sort |
| **5 — DP & intervals** | 1-D DP · Intervals | 8 | 0/1 Knapsack, Merge Intervals |
| **6 — Optional / advanced** | Tries · Greedy · 2-D DP · Adv Graphs · Math · Bit | (5) | Bitwise XOR (+ new) |

Phases 1-5 = the core ~52. Phase 6 = circle back only if time. Within each phase, finish one pattern before starting the next.

---

## Phase 1 — Linear foundations

### Arrays & Hashing

- [ ] ⭐ [Two Sum](https://leetcode.com/problems/two-sum/) (easy)
- [ ] ⭐ [Group Anagrams](https://leetcode.com/problems/group-anagrams/) (medium)
- [ ] ⭐ [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (medium)
- [ ] ⭐ [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (medium)
- [ ] ⭐ [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) (medium)
- [ ] [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (easy)
- [ ] [Valid Anagram](https://leetcode.com/problems/valid-anagram/) (easy)
- [ ] [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (medium)
- [ ] [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) (medium)

### Two Pointers

- [ ] ⭐ [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (easy)
- [ ] ⭐ [3Sum](https://leetcode.com/problems/3sum/) (medium)
- [ ] ⭐ [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (medium)
- [ ] [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (medium)
- [ ] [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (hard)

### Sliding Window

- [ ] ⭐ [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (easy)
- [ ] ⭐ [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (medium)
- [ ] ⭐ [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) (medium)
- [ ] ⭐ [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (hard)
- [ ] [Permutation in String](https://leetcode.com/problems/permutation-in-string/) (medium)
- [ ] [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (hard)

### Stack

- [ ] ⭐ [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (easy)
- [ ] ⭐ [Min Stack](https://leetcode.com/problems/min-stack/) (medium)
- [ ] ⭐ [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) (medium)
- [ ] [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) (medium)
- [ ] [Car Fleet](https://leetcode.com/problems/car-fleet/) (medium)
- [ ] [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) (hard)

---

## Phase 2 — Search & lists

### Binary Search

- [ ] ⭐ [Binary Search](https://leetcode.com/problems/binary-search/) (easy)
- [ ] ⭐ [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) (medium)
- [ ] ⭐ [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) (medium)
- [ ] ⭐ [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) (medium)
- [ ] [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) (medium)
- [ ] [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) (medium)
- [ ] [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) (hard)

### Linked List

- [ ] ⭐ [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (easy)
- [ ] ⭐ [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) (easy)
- [ ] ⭐ [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (easy)
- [ ] ⭐ [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (medium)
- [ ] ⭐ [LRU Cache](https://leetcode.com/problems/lru-cache/) (medium)
- [ ] ⭐ [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (hard)
- [ ] [Reorder List](https://leetcode.com/problems/reorder-list/) (medium)
- [ ] [Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) (medium)
- [ ] [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) (medium)
- [ ] [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) (medium)
- [ ] [Reverse Nodes in K-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) (hard)

---

## Phase 3 — Trees & heaps

### Trees

- [ ] ⭐ [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) (easy)
- [ ] ⭐ [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) (easy)
- [ ] ⭐ [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) (medium)
- [ ] ⭐ [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) (medium)
- [ ] ⭐ [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) (medium)
- [ ] ⭐ [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) (hard)
- [ ] [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) (easy)
- [ ] [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) (easy)
- [ ] [Same Tree](https://leetcode.com/problems/same-tree/) (easy)
- [ ] [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) (easy)
- [ ] [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) (medium)
- [ ] [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) (medium)
- [ ] [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) (medium)
- [ ] [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) (medium)
- [ ] [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) (hard)

### Heap / Priority Queue

- [ ] ⭐ [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) (medium)
- [ ] ⭐ [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) (medium)
- [ ] ⭐ [Task Scheduler](https://leetcode.com/problems/task-scheduler/) (medium)
- [ ] ⭐ [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) (hard)
- [ ] [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) (easy)
- [ ] [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) (easy)
- [ ] [Design Twitter](https://leetcode.com/problems/design-twitter/) (medium)

---

## Phase 4 — Recursion & graphs

### Backtracking

- [ ] ⭐ [Subsets](https://leetcode.com/problems/subsets/) (medium)
- [ ] ⭐ [Combination Sum](https://leetcode.com/problems/combination-sum/) (medium)
- [ ] ⭐ [Permutations](https://leetcode.com/problems/permutations/) (medium)
- [ ] ⭐ [Word Search](https://leetcode.com/problems/word-search/) (medium)
- [ ] [Subsets II](https://leetcode.com/problems/subsets-ii/) (medium)
- [ ] [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) (medium)
- [ ] [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) (medium)
- [ ] [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) (medium)
- [ ] [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) (medium)
- [ ] [N-Queens](https://leetcode.com/problems/n-queens/) (hard)

### Graphs

- [ ] ⭐ [Number of Islands](https://leetcode.com/problems/number-of-islands/) (medium)
- [ ] ⭐ [Clone Graph](https://leetcode.com/problems/clone-graph/) (medium)
- [ ] ⭐ [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) (medium)
- [ ] ⭐ [Course Schedule](https://leetcode.com/problems/course-schedule/) (medium)
- [ ] ⭐ [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) (medium)
- [ ] [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) (medium)
- [ ] [Walls and Gates](https://leetcode.com/problems/walls-and-gates/) (medium)
- [ ] [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) (medium)
- [ ] [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) (medium)
- [ ] [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) (medium)
- [ ] [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) (medium)
- [ ] [Redundant Connection](https://leetcode.com/problems/redundant-connection/) (medium)
- [ ] [Word Ladder](https://leetcode.com/problems/word-ladder/) (hard)

---

## Phase 5 — DP & intervals

### 1-D Dynamic Programming

- [ ] ⭐ [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (easy)
- [ ] ⭐ [House Robber](https://leetcode.com/problems/house-robber/) (medium)
- [ ] ⭐ [Coin Change](https://leetcode.com/problems/coin-change/) (medium)
- [ ] ⭐ [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) (medium)
- [ ] ⭐ [Word Break](https://leetcode.com/problems/word-break/) (medium)
- [ ] [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) (easy)
- [ ] [House Robber II](https://leetcode.com/problems/house-robber-ii/) (medium)
- [ ] [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) (medium)
- [ ] [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) (medium)
- [ ] [Decode Ways](https://leetcode.com/problems/decode-ways/) (medium)
- [ ] [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) (medium)
- [ ] [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) (medium)

### Intervals

- [ ] ⭐ [Insert Interval](https://leetcode.com/problems/insert-interval/) (medium)
- [ ] ⭐ [Merge Intervals](https://leetcode.com/problems/merge-intervals/) (medium)
- [ ] ⭐ [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (medium)
- [ ] [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) (medium)
- [ ] [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) (easy)
- [ ] [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) (hard)

---

## Phase 6 — Optional / advanced (circle back only if time)

Lower hit-rate for backend interviews. If you do any, prioritize the ⭐ classics below.

### Tries

- [ ] ⭐ [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) (medium)
- [ ] [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) (medium)
- [ ] [Word Search II](https://leetcode.com/problems/word-search-ii/) (hard)

### Greedy

- [ ] ⭐ [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (medium)
- [ ] ⭐ [Jump Game](https://leetcode.com/problems/jump-game/) (medium)
- [ ] [Jump Game II](https://leetcode.com/problems/jump-game-ii/) (medium)
- [ ] [Gas Station](https://leetcode.com/problems/gas-station/) (medium)
- [ ] [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) (medium)
- [ ] [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) (medium)
- [ ] [Partition Labels](https://leetcode.com/problems/partition-labels/) (medium)
- [ ] [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) (medium)

### 2-D Dynamic Programming

- [ ] ⭐ [Unique Paths](https://leetcode.com/problems/unique-paths/) (medium)
- [ ] ⭐ [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) (medium)
- [ ] [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) (medium)
- [ ] [Coin Change II](https://leetcode.com/problems/coin-change-ii/) (medium)
- [ ] [Target Sum](https://leetcode.com/problems/target-sum/) (medium)
- [ ] [Interleaving String](https://leetcode.com/problems/interleaving-string/) (medium)
- [ ] [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) (hard)
- [ ] [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) (hard)
- [ ] [Edit Distance](https://leetcode.com/problems/edit-distance/) (medium)
- [ ] [Burst Balloons](https://leetcode.com/problems/burst-balloons/) (hard)
- [ ] [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) (hard)

### Advanced Graphs

- [ ] [Network Delay Time](https://leetcode.com/problems/network-delay-time/) (medium)
- [ ] [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) (hard)
- [ ] [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) (medium)
- [ ] [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) (hard)
- [ ] [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) (hard)
- [ ] [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) (medium)

### Math & Geometry

- [ ] [Rotate Image](https://leetcode.com/problems/rotate-image/) (medium)
- [ ] [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) (medium)
- [ ] [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) (medium)
- [ ] [Happy Number](https://leetcode.com/problems/happy-number/) (easy)
- [ ] [Plus One](https://leetcode.com/problems/plus-one/) (easy)
- [ ] [Pow(x, n)](https://leetcode.com/problems/powx-n/) (medium)
- [ ] [Multiply Strings](https://leetcode.com/problems/multiply-strings/) (medium)
- [ ] [Detect Squares](https://leetcode.com/problems/detect-squares/) (medium)

### Bit Manipulation

- [ ] [Single Number](https://leetcode.com/problems/single-number/) (easy)
- [ ] [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) (easy)
- [ ] [Counting Bits](https://leetcode.com/problems/counting-bits/) (easy)
- [ ] [Reverse Bits](https://leetcode.com/problems/reverse-bits/) (easy)
- [ ] [Missing Number](https://leetcode.com/problems/missing-number/) (easy)
- [ ] [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) (medium)
- [ ] [Reverse Integer](https://leetcode.com/problems/reverse-integer/) (medium)
</content>
