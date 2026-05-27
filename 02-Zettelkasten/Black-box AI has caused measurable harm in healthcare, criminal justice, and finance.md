---
aliases: [black-box harm, AI accountability failures]
---

The black-box problem is not theoretical — it has produced documented real-world failures across high-stakes domains.

**Healthcare:** A review of 516 ML studies in medicine found that 94% failed the first stage of clinical validation. Models performed well on benchmarks but failed on real patients — often because they learned spurious correlations invisible to developers. One notorious example: a pneumonia risk model learned that asthma patients had lower risk, because asthma patients were sent to ICUs proactively and therefore survived more often. The model encoded the bias in the data, not the biology.

**Criminal justice:** COMPAS, a recidivism prediction tool used in US courts to influence sentencing and parole decisions, was found to produce racially biased predictions — incorrectly labeling Black defendants as higher risk at twice the rate of white defendants. The algorithm was proprietary. Defendants could not challenge the reasoning. Courts could not audit it.

**Finance:** The 2010 Flash Crash — the Dow Jones dropped 1,000 points in minutes — resulted from interacting automated trading systems producing emergent behavior no engineer had designed or predicted. No single algorithm was "at fault." The combined behavior of opaque systems was.

In each case, the harm was enabled by the same gap: a system producing decisions without an auditable reasoning process.

---

### Read more

- [[Black-box AI models prevent auditing of decision-making processes]]
- [[Neural network weights are compressed statistical patterns not human-readable instructions]]
- [[Mechanistic interpretability reverse-engineers neural network computations into readable circuits]]
