
A comprehensive learning roadmap for Machine Learning Engineering covering the full spectrum from foundational concepts to advanced applications.

## Mathematical Foundations

Core mathematics required for understanding machine learning algorithms.

- [[Math for ML MOC]] — comprehensive guide to linear algebra, calculus, probability, and discrete math for ML

## Model Training Concepts

Core concepts used in training machine learning models.

- [[Parameter is a value that defines how a system behaves]]
- [[Weights define how much each feature matters]]
- [[Bias adds a baseline shift to all predictions]]
- [[Loss function - formula that measures how wrong the model is]]
- [[Gradient adjusts params to reduce loss]]

## Data Collection

Sourcing and gathering data from various origins.

- Data Sources
- Databases (SQL, NoSQL)
- Internet
- APIs
- Mobile Apps
- IoT

## Data Formats

Understanding different data formats used in machine learning.

- JSON
- Parquet
- CSV
- Excel
- Other Data Formats

## Data Cleaning and Preparation

Transforming raw data into usable features for models.

### Data Preprocessing Workflow
Essential techniques for preparing raw data for machine learning.

- Train-test split: dividing dataset into training and testing subsets for unbiased evaluation
- Handling missing data: imputation strategies using mean, median, or mode values
- Encoding categorical variables: converting text categories into numerical format
- One-hot encoding: creating binary columns for each category value to avoid ordinal assumptions
- Label encoding: assigning integer values to categorical labels for simpler categorical variables
- Dummy variable trap: avoiding multicollinearity by dropping one dummy variable from encoded features
- Feature scaling methods: normalization (0-1 range) vs standardization (mean=0, std=1)
- StandardScaler: standardization technique using mean and standard deviation to scale features
- When to apply feature scaling: before vs after train-test split to prevent data leakage

### Feature Engineering
Creating new features from existing data.

### Feature Selection
Identifying the most relevant features for models.

### Outlier Detection and Handling
Identifying and managing anomalous data points that may distort model training.

## Regression

Predicting continuous numerical outcomes using various modeling approaches.

### Linear Regression Models
Modeling relationships between predictors and continuous targets using linear functions.

- Simple Linear Regression: modeling relationship between one predictor and outcome variable
- Ordinary Least Squares (OLS): method for finding best fit line by minimizing squared residuals
- Multiple Linear Regression: using multiple independent variables to predict continuous outcome
- Linear regression assumptions: linearity, homoscedasticity, independence, and normality of residuals
- P-values: measuring statistical significance of predictor variables in determining true effect
- Backward elimination: iteratively removing insignificant variables from model to improve parsimony
- Multicollinearity: detecting and handling correlated predictor variables that distort coefficients

### Non-Linear Regression Models
Capturing complex relationships that violate linearity assumptions.

- Polynomial Regression: modeling non-linear relationships using polynomial features of varying degrees
- Support Vector Regression (SVR): using support vectors with kernel trick for regression tasks
- RBF kernel: radial basis function kernel for non-linear SVR transformations in high dimensions
- Decision Tree Regression: recursive binary splitting on features to create predictive leafs
- Random Forest Regression: ensemble of decision trees voting for final prediction value

### Regression Evaluation Metrics
Quantifying regression model performance and comparing different approaches.

- R-squared: proportion of variance in outcome explained by predictor variables (0 to 1 scale)
- Adjusted R-squared: R-squared adjusted for number of predictors to penalize model complexity
- Mean Absolute Error (MAE): average absolute difference between predicted and actual values
- Mean Squared Error (MSE): average squared difference penalizing large errors more heavily
- Root Mean Squared Error (RMSE): square root of MSE in original units for interpretability
- Model comparison: evaluating different regression algorithms using consistent metrics

## Types of Machine Learning

Different paradigms and approaches to solving problems.

[[Types of ML]] • [[Differences of - AI, ML, DL, GenAI]]

### Supervised Learning
Learning from labeled data to make predictions.

#### Classification
Predicting discrete class labels using various algorithms.

- [[Classification outputs probability scores to express confidence in predictions|Classification]]

**Linear Classification Models**
- Logistic Regression: predicting binary/multiclass outcomes using sigmoid function and probability thresholds
- Maximum Likelihood Estimation: finding parameters that maximize probability of observed training data
- Decision boundary: threshold separating different predicted classes in feature space

**Instance-Based Learning**
- K-Nearest Neighbors (K-NN): classifying based on majority vote of K nearest neighbors in training data
- Distance metrics: Euclidean and Manhattan distances for measuring similarity between instances
- K selection: choosing appropriate number of neighbors to balance bias-variance tradeoff

**Support Vector Machines**
- Support Vector Machine (SVM): finding optimal hyperplane maximizing margin between class boundaries
- Kernel SVM: using kernel trick for non-linear classification in transformed feature spaces
- Kernel functions: transforming data into higher dimensions for linear separability (RBF, polynomial, linear)
- Margin maximization: prioritizing examples near decision boundary for robust generalization

**Probabilistic Models**
- Naive Bayes: probabilistic classifier using Bayes' theorem with feature independence assumption
- Conditional probability: calculating likelihood of features given class for prediction

**Tree-Based Classification**
- Decision Tree Classification: hierarchical binary splitting based on feature thresholds and information gain
- Information gain: reduction in entropy when splitting on a feature to select best split
- Random Forest Classification: ensemble of decision trees using bootstrap aggregation and majority voting

#### Regression
- [[Regression and Classification#Regression|Regression]]
- [[Linear regression finds the best-fit line through data|Linear Regression]]

See Regression section above for detailed regression algorithms and evaluation metrics.

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

## Classification Evaluation Metrics

Quantifying classification model performance using specialized evaluation metrics.

- Confusion Matrix: table showing true positives, false positives, true negatives, and false negatives
- Accuracy: proportion of correct predictions out of total predictions (useful for balanced datasets)
- Precision: proportion of positive predictions that are actually correct (minimizes false positives)
- Recall: proportion of actual positives correctly identified (minimizes false negatives)
- F1-score: harmonic mean of precision and recall for balanced evaluation with imbalanced classes
- ROC curve: plotting true positive rate vs false positive rate across classification thresholds
- AUC (Area Under Curve): aggregate metric summarizing classifier performance across all thresholds
- Decision boundary visualization: plotting predicted regions to understand how classifier separates classes

## Model Evaluation

Assessing model performance and quality across different learning paradigms.

### Validation Techniques
Cross-validation, train-test splits, and evaluation strategies for robust performance assessment.

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

---

**Status:** MOC created with all topics from roadmap.sh/machine-learning
