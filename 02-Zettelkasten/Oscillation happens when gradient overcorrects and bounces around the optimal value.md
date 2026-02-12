---
created: 2026-02-12
tags:
  - ml/training
---

> **Oscillation** is when the model keeps **bouncing above and below** the correct answer, overshooting in one direction, then overcorrecting in the other.

Think of it like pushing a swing too hard — it doesn't stop in the middle, it flies past to the other side, then back again.

This happens because the gradient **overcorrects**: the error is large → the gradient is large → the weight changes too much → now the error is large in the **opposite direction**.

---

### Oscillation in action

Simplified to one feature: $\hat{y} = w \times x$, where $x = 1000$ (sqft), actual price = $200k, $\alpha = 0.0000008$

| Step | Weight | Prediction | Error | What happened |
|------|--------|------------|-------|---------------|
| 0 | 0 | $0k | -$200k | Way too low |
| 1 | 320 | $320k | +$120k | Overshot! Too high |
| 2 | 128 | $128k | -$72k | Corrected too far back |
| 3 | 243 | $243k | +$43k | Overshot again |
| 4 | 174 | $174k | -$26k | Back too far |
| 5 | 216 | $216k | +$16k | Still bouncing |
| 6 | 191 | $191k | -$9k | Getting closer... |
| 7 | 206 | $206k | +$6k | Still bouncing |
| 8 | 197 | $197k | -$3k | Almost there |
| 9 | 202 | $202k | +$2k | Close |

**Pattern:** Each overshoot is ~60% of the previous one. The model **does** converge, but wastes many iterations bouncing.

> ⚠️ With an even larger learning rate, oscillations can get **bigger** each step instead of smaller. The model **diverges** — loss goes to infinity, and it never learns.

---

### Compare: unscaled vs scaled

With [[Feature scaling transforms features to similar ranges for efficient training|scaled features]], the error **shrinks steadily** in one direction. No bouncing. The gradient is small enough that the learning rate doesn't cause overshooting, yet large enough to converge quickly.

---

Read more:
- [[Unscaled features cause learning rate conflict in gradient descent]]
- [[Feature scaling transforms features to similar ranges for efficient training]]
