
A comprehensive learning roadmap for Machine Learning Engineering covering the full spectrum from foundational concepts to advanced applications.

## Overview

Machine learning is a subset of AI where models learn patterns from data instead of being explicitly programmed.

- [[Differences of - AI, ML, DL, GenAI]] — how AI, ML, Deep Learning, and GenAI relate to each other
- [[Machine learning is called learning because the model improves from data not instructions|Why "machine learning"]] — the name comes from machines discovering patterns from data, not instructions
- [[Types of ML]] — supervised, unsupervised, reinforcement, and more
- [[Machine learning follows five stages from problem framing to deployment|ML Process Stages]] — the end-to-end workflow every ML project follows

### Core Vocabulary

- [[Feature is an input variable the model uses to make predictions|Feature]] — input variable the model uses to make predictions
- [[Target is the output variable the model learns to predict|Target]] — output variable the model learns to predict
- [[X represents features and y represents target in ML notation|X and y notation]] — uppercase matrix vs lowercase vector convention
- [[Supervised learning means the model learns from labeled data with known answers|Supervised learning]] — model learns from labeled data with known answers
- [[Regression predicts a continuous number|Regression]] — predicting a continuous number
- [[Classification predicts a discrete category|Classification]] — predicting a discrete category

## Types of Machine Learning

### Supervised Learning

[[Supervised learning means the model learns from labeled data with known answers|Supervised learning]] — the model learns from labeled data where the correct answer is known.

#### Regression

[[Regression predicts a continuous number|Regression]] — predicting continuous numerical values (how much? how many?).

##### Simple Linear Regression
[[Simple linear regression predicts a target using one feature and a straight line|Simple Linear Regression]] — one feature, one target, one straight line.

- [[Ordinary Least Squares minimizes the sum of squared errors to find the best-fit line|OLS]]: finding best-fit line by minimizing squared errors algebraically
- Linear regression assumptions: linearity, homoscedasticity, independence, and normality of residuals

##### Multiple Linear Regression
Using multiple independent variables to predict continuous outcome.

- P-values: measuring statistical significance of predictor variables in determining true effect
- Backward elimination: iteratively removing insignificant variables from model to improve parsimony
- Multicollinearity: detecting and handling correlated predictor variables that distort coefficients

##### Polynomial Regression
Modeling non-linear relationships using polynomial features of varying degrees.

##### Support Vector Regression (SVR)
Using support vectors with kernel trick for regression tasks.

- RBF kernel: radial basis function kernel for non-linear SVR transformations in high dimensions

##### Decision Tree Regression
Recursive binary splitting on features to create predictive leafs.

##### Random Forest Regression
Ensemble of decision trees voting for final prediction value.

#### Classification

[[Classification predicts a discrete category|Classification]] — predicting discrete class labels (which one? what type?).

- [[Classification outputs probability scores to express confidence in predictions|Probability scores]] — models output confidence levels, not just labels

##### Linear Classification Models

- Logistic Regression: predicting binary/multiclass outcomes using sigmoid function and probability thresholds
- Maximum Likelihood Estimation: finding parameters that maximize probability of observed training data
- Decision boundary: threshold separating different predicted classes in feature space

##### Instance-Based Learning

- K-Nearest Neighbors (K-NN): classifying based on majority vote of K nearest neighbors in training data
- Distance metrics: Euclidean and Manhattan distances for measuring similarity between instances
- K selection: choosing appropriate number of neighbors to balance bias-variance tradeoff

##### Support Vector Machines

- Support Vector Machine (SVM): finding optimal hyperplane maximizing margin between class boundaries
- Kernel SVM: using kernel trick for non-linear classification in transformed feature spaces
- Kernel functions: transforming data into higher dimensions for linear separability (RBF, polynomial, linear)
- Margin maximization: prioritizing examples near decision boundary for robust generalization

##### Probabilistic Models

- Naive Bayes: probabilistic classifier using Bayes' theorem with feature independence assumption
- Conditional probability: calculating likelihood of features given class for prediction

##### Tree-Based Classification

- Decision Tree Classification: hierarchical binary splitting based on feature thresholds and information gain
- Information gain: reduction in entropy when splitting on a feature to select best split
- Random Forest Classification: ensemble of decision trees using bootstrap aggregation and majority voting

### Unsupervised Learning

Finding patterns in unlabeled data without predefined labels.

#### Clustering
Grouping similar data points into clusters based on distance or density metrics.

- K-Means clustering: partitioning data into K clusters by iteratively assigning points to nearest centroid
- Hierarchical clustering: building tree of clusters through agglomerative or divisive approaches
- DBSCAN: density-based clustering identifying core points and expanding clusters from them
- Silhouette score: measuring cluster quality by comparing intra-cluster and inter-cluster distances

#### Association Rule Learning
Discovering relationships between variables in large datasets.

- Association Rule Learning: finding frequent itemsets and rules showing variable relationships
- Apriori algorithm: level-wise approach finding frequent itemsets by iterating through candidate sets
- Eclat algorithm: depth-first algorithm using vertical data format for association rule mining
- Support: frequency of itemset appearing together in dataset transactions
- Confidence: proportion of transactions containing antecedent that also contain consequent
- Lift: ratio of observed to expected co-occurrence frequency indicating strength of rule

### Semi-supervised Learning
Combining labeled and unlabeled data for training.

### Reinforcement Learning
Learning through interaction and rewards.

### Self-supervised Learning
Using data structure as labels for training.

## Mathematical Foundations

Core mathematics required for understanding machine learning algorithms.

- [[Math for ML MOC]] — comprehensive guide to linear algebra, calculus, probability, and discrete math for ML

## Data

### Data Cleaning and Preparation

Transforming raw data into usable features for models.

#### Data Preprocessing Workflow
Essential techniques for preparing raw data for machine learning.

- [[Train-test split evaluates model performance on unseen data|Train-test split]]: dividing dataset into training and testing subsets for unbiased evaluation
- [[random_state is a seed that makes random operations reproducible|random_state]]: fixing the random seed for reproducible results
- [[Computers generate pseudorandom numbers using a formula not true randomness|PRNG]]: computers use a formula, not true randomness — same seed produces same sequence
- [[42 is not a special seed it is just a convention from pop culture|Why 42]]: the number is a pop culture convention, not mathematically special
- [[Missing data must be handled because most ML algorithms cannot compute with NaN|Handling missing data]]: imputation strategies using mean, median, or mode values
- [[SimpleImputer replaces missing values using fit and transform pattern|SimpleImputer]]: sklearn's fit-transform pattern for replacing NaN values
- [[Categorical data must be encoded into numbers because ML algorithms only compute with numbers|Encoding categorical variables]]: converting text categories into numerical format
- [[One-hot encoding creates a binary column for each category|One-hot encoding]]: creating binary columns for each category value to avoid ordinal assumptions
- [[Label encoding assigns an integer to each category|Label encoding]]: assigning integer values to categorical labels for simpler categorical variables
- [[Irrelevant or unique columns should be dropped before training|Dropping columns]]: removing identifiers and useless string columns before encoding
- [[Dummy variable is a binary column created by one-hot encoding|Dummy variable]]: binary column created by one-hot encoding to represent a category
- [[Dummy variable trap is multicollinearity from redundant one-hot encoded columns|Dummy variable trap]]: avoiding multicollinearity by dropping one dummy variable from encoded features
- [[Feature scaling transforms features to similar ranges for efficient training|Feature scaling]]: normalization (0-1 range) vs standardization (mean=0, std=1)
- [[Unscaled features cause learning rate conflict in gradient descent|Learning rate conflict]]: why unscaled features break gradient descent
- [[Oscillation happens when gradient overcorrects and bounces around the optimal value|Oscillation]]: gradient overcorrection causing bouncing
- [[Normalization scales features to a fixed range using min and max|Normalization]]: min-max scaling to [0, 1] range
- [[Standardization centers features around zero using mean and standard deviation|Standardization]]: z-score scaling (mean=0, std=1)
- [[Feature scaling must happen after train-test split to prevent data leakage|When to apply feature scaling]]: always after split — fit on train only to prevent data leakage

#### Feature Engineering
Creating new features from existing data.

#### Feature Selection
Identifying the most relevant features for models.

#### Outlier Detection and Handling
Identifying and managing anomalous data points that may distort model training.

## Model Training Concepts

Core concepts used in training machine learning models.

- [[Parameter is a value that defines how a system behaves]]
- [[Weights define how much each feature matters]]
- [[Bias adds a baseline shift to all predictions]]
- [[Loss function - formula that measures how wrong the model is]]
- [[Gradient adjusts params to reduce loss]]
- [[fit() trains the model by learning parameters from training data|.fit()]]: the universal scikit-learn method that learns parameters from training data
- [[predict() uses learned parameters to compute outputs for new data|.predict()]]: computes predicted targets using learned parameters
- [[OLS solves linear regression directly while gradient descent iterates toward the solution|OLS vs Gradient Descent]]: when to use direct solution vs iterative optimization

## Model Evaluation

Assessing model performance and quality.

### Regression Metrics

- R-squared: proportion of variance in outcome explained by predictor variables (0 to 1 scale)
- Adjusted R-squared: R-squared adjusted for number of predictors to penalize model complexity
- Mean Absolute Error (MAE): average absolute difference between predicted and actual values
- Mean Squared Error (MSE): average squared difference penalizing large errors more heavily
- Root Mean Squared Error (RMSE): square root of MSE in original units for interpretability
- Model comparison: evaluating different regression algorithms using consistent metrics

### Classification Metrics

- Confusion Matrix: table showing true positives, false positives, true negatives, and false negatives
- Accuracy: proportion of correct predictions out of total predictions (useful for balanced datasets)
- Precision: proportion of positive predictions that are actually correct (minimizes false positives)
- Recall: proportion of actual positives correctly identified (minimizes false negatives)
- F1-score: harmonic mean of precision and recall for balanced evaluation with imbalanced classes
- ROC curve: plotting true positive rate vs false positive rate across classification thresholds
- AUC (Area Under Curve): aggregate metric summarizing classifier performance across all thresholds
- Decision boundary visualization: plotting predicted regions to understand how classifier separates classes

### Validation Techniques

- Cross-validation: K-fold technique for assessing model generalization using multiple train-test splits
- Stratified cross-validation: maintaining class distributions in folds for imbalanced classification
- Hold-out validation: simple approach using single train-test split for performance estimation

## Dimensionality Reduction

Reducing feature space while preserving information for improved efficiency and interpretability.

- Principal Component Analysis (PCA): linear transformation creating uncorrelated principal components
- Explained variance ratio: proportion of information retained by each principal component
- Linear Discriminant Analysis (LDA): supervised dimensionality reduction maximizing class separability
- Kernel PCA: non-linear PCA using kernel trick for complex manifold learning
- Feature importance: identifying most predictive features for selective dimensionality reduction

## Model Selection & Boosting

Techniques for selecting optimal models and improving performance through ensemble methods.

- Model selection strategies: comparing and choosing best performing algorithm for problem
- Grid search: systematically searching hyperparameter combinations to optimize model performance
- Random search: sampling random hyperparameter combinations for efficient exploration
- XGBoost: gradient boosting framework using weak learners for high-performance ensemble learning
- Gradient Boosting: sequentially building trees correcting previous model's errors
- Boosting concept: combining weak learners into strong learner through weighted ensemble

## Advanced Concepts

Specialized applications and cutting-edge techniques for complex problem domains.

### Deep Learning
Building and training neural network architectures for complex pattern recognition.

#### Artificial Neural Networks (ANNs)
Layered networks of interconnected neurons inspired by biological neural systems.

- Neural network architecture: layers of interconnected neurons (input, hidden, output layers)
- Activation functions: non-linear functions (ReLU, sigmoid, tanh) introducing non-linearity to networks
- Backpropagation: training algorithm using gradient descent to update weights through layers
- Forward propagation: passing input through network layers to compute output predictions
- Epochs and batch size: number of training iterations and samples per update affecting convergence

#### Convolutional Neural Networks (CNNs)
Specialized architecture for processing grid-like data such as images.

- Convolution operation: applying learnable filters across input to extract local features
- Pooling layers: downsampling features to reduce dimensionality and computational cost
- CNN architecture: alternating convolution and pooling layers followed by fully-connected layers
- Image classification: using CNNs for computer vision tasks with high accuracy
- Feature maps: outputs of convolution operations representing detected features at different scales

### Natural Language Processing
Processing and understanding human language.

### Deep Learning Frameworks and Libraries
Tools and frameworks for building deep learning models.

- [[Scikit-learn provides ready-to-use ML algorithms and preprocessing tools|Scikit-learn]]
- [[Matplotlib is a Python library for creating static and interactive visualizations|Matplotlib]]

---

### Flashcard Coverage

Flashcards exist only for sections with `[[]]` linked atomic notes. Sections **without flashcards** (no notes yet):
- Classification models (Logistic Regression, KNN, SVM, Naive Bayes, Decision Trees, Random Forest)
- Multiple Linear Regression, Polynomial Regression, SVR, Decision Tree Regression, Random Forest Regression
- Unsupervised Learning (K-Means, Hierarchical, DBSCAN, Association Rules)
- Model Evaluation (all metrics, validation techniques)
- Dimensionality Reduction (PCA, LDA, Kernel PCA)
- Model Selection & Boosting (Grid/Random Search, XGBoost)
- Deep Learning (ANNs, CNNs)
- Semi-supervised, Reinforcement, Self-supervised Learning
- Feature Engineering, Feature Selection, Outlier Detection
- Natural Language Processing

> When creating atomic notes for any of these topics, create flashcards immediately in the corresponding `05-Flashcards/ml/` file.

