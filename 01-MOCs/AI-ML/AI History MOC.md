The evolution of AI told as a chain of problems and breakthroughs. Each milestone exists because the previous one hit a wall.

### Overview

AI history is best understood as a sequence of limitations being broken. Every architecture on this list was born to fix something the previous one couldn't do.

---

### Prerequisites

Concepts you need before the Perceptron makes sense. Missing atomic notes to create:

- Dot product is the sum of element-wise products of two vectors
- Linear separability means two classes can be divided by a straight line or hyperplane
- Activation function decides whether a neuron fires based on its input sum
- Step function outputs 1 if input crosses a threshold and 0 otherwise

---

### 0. McCulloch-Pitts Neuron (1943)

The cybernetics era. The first mathematical model of a neuron, before anything could learn.

- [ ] Cybernetics framed the 1940s to 1960s as the study of control and communication in animals and machines
- [ ] McCulloch and Pitts built the first mathematical model of a neuron as a threshold unit
- [ ] Networks of McCulloch-Pitts neurons can compute any logical function

### 1. Perceptron (1958)

The first trainable artificial neuron. A single-layer linear classifier invented by Frank Rosenblatt.

- Perceptron is a single neuron that learns a linear decision boundary
- Perceptron learning rule updates weights when a prediction is wrong
- Perceptron cannot solve XOR because XOR is not linearly separable
- The XOR problem triggered the first AI winter
- [ ] Minsky and Papert's Perceptrons proved the single-layer limits and cut neural network funding

### 1b. Backpropagation and Self-Organisation (1974вЂ“1980)

Two breakthroughs made during the first winter and ignored at the time.

- [ ] Werbos discovered backpropagation in 1974, a decade before anyone used it
- [ ] Fukushima's Cognitron learned visual features by self-organisation and prefigured CNNs

### 2. Multi-Layer Perceptron (1986)

Stacking perceptrons with hidden layers + backpropagation solved XOR and launched neural networks.

- MLP adds hidden layers to learn non-linear decision boundaries
- Backpropagation trains MLPs by propagating error gradients backward
- Universal approximation theorem says an MLP can approximate any continuous function
- Non-linear activation functions are what make hidden layers useful
- [ ] Parallel Distributed Processing reframed cognition as computation spread across many simple units
- [ ] Elman networks feed the hidden state back as input so the network can learn sequence structure

### 3. LeNet-5 (1998)

Yann LeCun's convolutional network for handwritten digit recognition. Introduced the architectural priors that define modern vision models.

- LeNet-5 introduced convolution and pooling for image recognition
- Weight sharing in convolutions drastically reduces parameters
- Local receptive fields encode the prior that nearby pixels are related
- LeNet-5 worked in production on bank checks long before deep learning was mainstream
- [ ] The second AI winter came from hardware and data limits, not a theoretical wall

### 3b. Deep Belief Networks (2006)

Hinton's restart. Layer-wise pretraining made deep models trainable and gave the field its name.

- [ ] Deep Belief Networks used greedy layer-wise pretraining to make deep models trainable

### 4. AlexNet (2012)

The ImageNet winner that started the deep learning revolution. Same ideas as LeNet, but scaled up with GPUs.

- AlexNet won ImageNet 2012 by a huge margin and started the deep learning era
- ReLU activation made deep networks trainable by avoiding vanishing gradients
- Dropout regularization prevents overfitting by randomly disabling neurons
- GPU training made large-scale deep networks practical for the first time
- [ ] ResNet's skip connections let networks go hundreds of layers deep

### 5. ChatGPT (2022)

Transformer + scale + RLHF. The jump from perception to language and reasoning.

- [ ] Attention is All You Need introduced the Transformer in 2017
- Transformer architecture replaced recurrence with self-attention
- Self-attention lets every token directly attend to every other token
- Scaling laws show that bigger models and more data predictably improve performance
- RLHF aligns language models with human preferences through reward modeling
- ChatGPT made large language models usable by the general public

---

### 6. Can Machines Think? — Philosophy & Interpretability

The question behind all AI history: what counts as intelligence, and do these systems have it?

- [[Turing Test replaces the question of machine thinking with behavioral indistinguishability|Turing Test: behavior replaces "thinking"]]
- [[Searle's Chinese Room shows that symbol manipulation without understanding cannot constitute thought|Chinese Room: symbol manipulation ≠ understanding]]
- [[Chollet's ARC benchmark exposes the gap between pattern memorization and genuine reasoning|ARC benchmark: memorization vs reasoning gap]]
- [[LeCun argues LLMs lack world models needed for general intelligence|LeCun: LLMs lack world models]]
- [[Gary Marcus argues deep learning lacks compositionality required for systematic generalization|Marcus: deep learning lacks compositionality]]
- [[Black-box AI models prevent auditing of decision-making processes|Black-box AI prevents auditing decisions]]
- [[Black-box AI has caused measurable harm in healthcare, criminal justice, and finance|Black-box AI has caused real-world harm]]
- [[Mechanistic interpretability reverse-engineers neural network computations into readable circuits|Mechanistic interpretability: weights → circuits]]
- [[Chain-of-thought in LLMs may be constrained imitation of human reasoning patterns rather than genuine inference|CoT may be imitation, not genuine inference]]
- [[Unfaithful chain-of-thought means visible reasoning traces may not reflect actual model computation|Unfaithful CoT: traces may not reflect computation]]

### 6b. Why We Don't Know How AI Works — The Technical Reality

- [[Neural network weights are compressed statistical patterns not human-readable instructions|NN weights: compressed statistics, not instructions]]
- [[Superposition allows neural networks to encode more features than neurons using overlapping activation patterns|Superposition: more features than neurons]]
- [[Polysemantic neurons respond to multiple unrelated concepts making them individually uninterpretable|Polysemantic neurons fire for many concepts]]

### 8. AI Consciousness & Existential Risk

Why some of the people who built these systems are afraid of them.

- [[The Hard Problem of Consciousness asks why physical processes produce subjective experience|Hard Problem: why physical processes feel like something]]
- [[Hinton's substrate independence argument suggests AI systems may already have subjective experience|Hinton: substrate independence → AI may experience]]
- [[Instrumental convergence means sufficiently capable goal-seeking systems develop self-preservation sub-goals regardless of their original objective|Instrumental convergence: self-preservation sub-goals emerge]]
- [[The paperclip maximizer illustrates how any terminal goal pursued without constraint conflicts with human survival|Paperclip maximizer: unconstrained goals conflict with survival]]
- [[The alignment problem is ensuring AI optimization targets remain consistent with human values as capability scales|Alignment problem: targets stay aligned as capability scales]]

### 7. Reasoning Models — How "Thinking" Actually Works

What changed when o1, o3, and DeepSeek-R1 appeared — technically and philosophically.

- [[Autoregressive token prediction generates responses in a single forward pass without deliberation|Autoregressive prediction: one forward pass, no deliberation]]
- [[Chain-of-thought prompting uses model output as a working memory scratchpad|Chain-of-thought: output as a scratchpad]]
- [[Reasoning models use reinforcement learning on outcome rewards to discover thinking strategies|Reasoning models: RL on outcome rewards]]
- [[GRPO trains reasoning models by comparing outcome rewards across sampled response groups|GRPO: compare rewards across sampled groups]]
- [[Thinking tokens create a bounded scratchpad that separates deliberation from final output|Thinking tokens: bounded deliberation scratchpad]]
- [[Inference-time compute scaling trades token cost for accuracy on hard reasoning tasks|Inference-time compute: tokens for accuracy]]

### 9. Reflections on the Pattern

What the three cycles of hype and winter say about where the field is now.

- [ ] AGI hype risks a third AI winter if expectations outrun results
- [ ] Neural networks and biological brains differ in goals, learning signals, and structure

---

### Read more

- [[Machine Learning MOC]]
- [[Math for ML MOC]]
