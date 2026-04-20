
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

### 1. Perceptron (1958)

The first trainable artificial neuron. A single-layer linear classifier invented by Frank Rosenblatt.

- Perceptron is a single neuron that learns a linear decision boundary
- Perceptron learning rule updates weights when a prediction is wrong
- Perceptron cannot solve XOR because XOR is not linearly separable
- The XOR problem triggered the first AI winter

### 2. Multi-Layer Perceptron (1986)

Stacking perceptrons with hidden layers + backpropagation solved XOR and launched neural networks.

- MLP adds hidden layers to learn non-linear decision boundaries
- Backpropagation trains MLPs by propagating error gradients backward
- Universal approximation theorem says an MLP can approximate any continuous function
- Non-linear activation functions are what make hidden layers useful

### 3. LeNet-5 (1998)

Yann LeCun's convolutional network for handwritten digit recognition. Introduced the architectural priors that define modern vision models.

- LeNet-5 introduced convolution and pooling for image recognition
- Weight sharing in convolutions drastically reduces parameters
- Local receptive fields encode the prior that nearby pixels are related
- LeNet-5 worked in production on bank checks long before deep learning was mainstream

### 4. AlexNet (2012)

The ImageNet winner that started the deep learning revolution. Same ideas as LeNet, but scaled up with GPUs.

- AlexNet won ImageNet 2012 by a huge margin and started the deep learning era
- ReLU activation made deep networks trainable by avoiding vanishing gradients
- Dropout regularization prevents overfitting by randomly disabling neurons
- GPU training made large-scale deep networks practical for the first time

### 5. ChatGPT (2022)

Transformer + scale + RLHF. The jump from perception to language and reasoning.

- Transformer architecture replaced recurrence with self-attention
- Self-attention lets every token directly attend to every other token
- Scaling laws show that bigger models and more data predictably improve performance
- RLHF aligns language models with human preferences through reward modeling
- ChatGPT made large language models usable by the general public

---

### Read more

- [[Machine Learning MOC]]
- [[Math for ML MOC]]
