---
aliases: [polysemantic neurons, neuron polysemanticity]
---

A monosemantic neuron activates for one identifiable concept. A polysemantic neuron activates for multiple unrelated concepts — "dog," "curved shapes," and "Python syntax errors" might all trigger the same neuron.

This is not a bug. It is a direct consequence of superposition: the network is encoding more features than it has neurons, so each neuron participates in representing many different features depending on which combination of other neurons are also active.

The problem for interpretability: if a neuron means different things in different contexts, you cannot assign it a stable meaning. The same activation value carries different information depending on the surrounding activation pattern — which you would also need to decode.

Anthropic's research in 2024–2025 applied Sparse Autoencoders (SAEs) to decompose model activations into more monosemantic components. This is the current best approach to "translating" polysemantic neurons into interpretable features — but it remains incomplete and does not yet scale to full models.

---

### Read more

- [[Superposition allows neural networks to encode more features than neurons using overlapping activation patterns]]
- [[Neural network weights are compressed statistical patterns not human-readable instructions]]
- [[Mechanistic interpretability reverse-engineers neural network computations into readable circuits]]
