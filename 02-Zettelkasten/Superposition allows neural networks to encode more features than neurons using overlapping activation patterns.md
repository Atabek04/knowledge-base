---
aliases: [superposition, neural superposition]
---

The intuitive mental model of neural networks assumes each neuron learns one concept: one fires for "dog," another for "color," another for "verb." This would make inspection tractable — you could build a dictionary.

Anthropic's mechanistic interpretability research discovered this is wrong. Neural networks use **superposition**: they pack far more "features" than they have neurons by encoding features as linear combinations of neuron activations — overlapping, partially interfering patterns spread across many neurons simultaneously.

Think of it like storing ten different images in the same set of pixels by exploiting the fact that each image uses different pixel combinations. Each image can be recovered by the right decoding, but no single pixel "belongs" to any one image.

Why do networks do this? Because it is computationally efficient. A model with 100,000 neurons can represent millions of features this way — at the cost of interpretability.

The consequence: you cannot understand what a model "knows" by reading individual neurons. Concepts live in directions in high-dimensional activation space, not in identifiable units. Finding them requires Sparse Autoencoders (SAEs) and other indirect probing tools.

---

### Read more

- [[Polysemantic neurons respond to multiple unrelated concepts making them individually uninterpretable]]
- [[Neural network weights are compressed statistical patterns not human-readable instructions]]
- [[Mechanistic interpretability reverse-engineers neural network computations into readable circuits]]
- [[Black-box AI models prevent auditing of decision-making processes]]
