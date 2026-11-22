# Data Science Learning

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-FF6F00?logo=tensorflow&logoColor=white)

The notebooks and assignments from my data science course, arranged in learning order: Python and statistics first, then machine learning, deep learning, NLP and model deployment.

**Author:** Abhiram Jammula · [LinkedIn](https://www.linkedin.com/in/abhiram-jammula-38937224b/) · My MSc projects are in [academics-projects](https://github.com/abhiramjammula-aj/academics-projects).

---

## Contents

- [Repository structure](#repository-structure)
- [Topics covered](#topics-covered)
- [Assignments](#assignments)
- [Getting started](#getting-started)
- [Tech stack](#tech-stack)

---

## Repository structure

```
data-science_learning/
├── 01_python_and_statistics/   Python basics, data structures, descriptive statistics, probability
├── 02_machine_learning/
│   ├── supervised/             Regression, classification, model evaluation
│   ├── unsupervised/           Clustering, PCA, association rules
│   └── time_series/            Visualisation, smoothing, ARIMA
├── 03_deep_learning/           Artificial neural networks
├── 04_nlp/                     Text mining and sentiment analysis
├── 05_deployment/              Streamlit app for a logistic regression model
├── assignments/                21 graded course assignments
├── datasets/                   CSV datasets used by the notebooks
├── extras/                     Practice notebooks made with an AI assistant
└── requirements.txt
```

---

## Topics covered

### 1. Python and statistics: [`01_python_and_statistics`](01_python_and_statistics)

| # | Notebook | What it covers |
| --- | --- | --- |
| 01 | [Python basics](01_python_and_statistics/01_python_basics.ipynb) | Variables, data types, operators |
| 02 | [Data structures](01_python_and_statistics/02_data_structures.ipynb) | Lists, tuples, sets, dictionaries |
| 03 | [Functions and descriptive statistics](01_python_and_statistics/03_functions_and_descriptive_statistics.ipynb) | Built-in functions, modules, summary statistics |
| 04 | [Data cleaning and statistics](01_python_and_statistics/04_data_cleaning_and_statistics.ipynb) | Handling nulls, merging files, statistics with pandas |
| 05 | [Visualisation with Matplotlib](01_python_and_statistics/05_visualisation_with_matplotlib.ipynb) | Plotting a banking dataset |
| 06 | [Probability distributions and tests](01_python_and_statistics/06_probability_distributions_and_tests.ipynb) | Normal distribution, z-tests |

### 2. Machine learning: [`02_machine_learning`](02_machine_learning)

**Supervised learning**

| # | Notebook | What it covers |
| --- | --- | --- |
| 01 | [Data partitioning](02_machine_learning/supervised/01_data_partitioning.ipynb) | Train/test splits, K-fold cross-validation |
| 02 | [Data transformation](02_machine_learning/supervised/02_data_transformation.ipynb) | Label encoding, scaling |
| 03 | [Predictive power score](02_machine_learning/supervised/03_predictive_power_score.ipynb) | Feature relevance with PPS |
| 04 | [Linear regression](02_machine_learning/supervised/04_linear_regression.ipynb) | Simple and multiple regression |
| 05 | [Regularisation](02_machine_learning/supervised/05_regularization.ipynb) | Lasso with cross-validation on house prices |
| 06 | [Best regression models](02_machine_learning/supervised/06_best_regression_models.ipynb) | Elastic Net, gradient boosting and random forest compared |
| 07 | [Logistic regression](02_machine_learning/supervised/07_logistic_regression.ipynb) | Binary classification, evaluation metrics |
| 08 | [K-nearest neighbours](02_machine_learning/supervised/08_knn.ipynb) | Distance-based classification |
| 09 | [Naive Bayes](02_machine_learning/supervised/09_naive_bayes.ipynb) | Probabilistic classification |
| 10 | [Decision tree](02_machine_learning/supervised/10_decision_tree.ipynb) | Tree-based models |
| 11 | [Support vector machine](02_machine_learning/supervised/11_support_vector_machine.ipynb) | Kernels on non-linear data, 3D visualisation |

**Unsupervised learning**

| # | Notebook | What it covers |
| --- | --- | --- |
| 01 | [Clustering](02_machine_learning/unsupervised/01_clustering.ipynb) | Agglomerative and K-means clustering |
| 02 | [PCA](02_machine_learning/unsupervised/02_pca.ipynb) | Dimensionality reduction |
| 03 | [Association rules and recommendations](02_machine_learning/unsupervised/03_association_rules_and_recommendations.ipynb) | Apriori, market basket analysis |

**Time series**

| # | Notebook | What it covers |
| --- | --- | --- |
| 01 | [Visualisation](02_machine_learning/time_series/01_visualisation.ipynb) | Distribution, box and lag plots, autocorrelation |
| 02 | [Smoothing methods](02_machine_learning/time_series/02_smoothing_methods.ipynb) | Exponential and Holt smoothing |
| 03 | [ARIMA model fitting](02_machine_learning/time_series/03_arima_model_fitting.ipynb) | ARIMA forecasting |

### 3. Deep learning: [`03_deep_learning`](03_deep_learning)

| # | Notebook | What it covers |
| --- | --- | --- |
| 01 | [ANN: medical cost prediction](03_deep_learning/01_ann_medical_cost.ipynb) | Feed-forward neural network with TensorFlow/Keras |

### 4. Natural language processing: [`04_nlp`](04_nlp)

| # | Notebook | What it covers |
| --- | --- | --- |
| 01 | [Text mining](04_nlp/01_text_mining.ipynb) | Tokenisation, stemming, lemmatisation, stop words |
| 02 | [Sentiment analysis](04_nlp/02_sentiment_analysis.ipynb) | Polarity scoring with VADER |

### 5. Model deployment: [`05_deployment`](05_deployment)

A Streamlit web app that serves a logistic regression model. See the [deployment guide](05_deployment/README.md) for setup steps.

---

## Assignments

The graded course assignments, in course order, are in [`assignments`](assignments).

| # | Assignment | Dataset |
| --- | --- | --- |
| 01 | [Python basics](assignments/01_python_basics.ipynb) | – |
| 02 | [Data structures, functions, NumPy and pandas](assignments/02_data_structures_numpy_pandas.ipynb) | – |
| 03 | [Basic statistics](assignments/03_basic_statistics.ipynb) | Retail sales |
| 04 | [Confidence intervals](assignments/04_confidence_intervals.ipynb) | Sample data |
| 05 | [Hypothesis testing](assignments/05_hypothesis_testing.ipynb) | Bombay Hospitality operating costs |
| 06 | [Exploratory data analysis](assignments/06_eda_cardiotocographic.ipynb) | Cardiotocographic |
| 07 | [EDA and feature engineering](assignments/07_eda_feature_engineering.ipynb) | Adult income |
| 08 | [Multiple linear regression](assignments/08_multiple_linear_regression.ipynb) | Toyota Corolla |
| 09 | [Logistic regression](assignments/09_logistic_regression.ipynb) + [Streamlit app](assignments/09_logistic_regression_titanic_app.py) | Titanic |
| 10 | [K-nearest neighbours](assignments/10_knn.ipynb) | Zoo |
| 11 | [Decision tree](assignments/11_decision_tree.ipynb) | Heart disease |
| 12 | [Random forest](assignments/12_random_forest.ipynb) | Glass |
| 13 | [XGBoost and LightGBM](assignments/13_xgboost_lightgbm.ipynb) | Titanic |
| 14 | [Support vector machine](assignments/14_svm.ipynb) | Mushroom |
| 15 | [Clustering](assignments/15_clustering.ipynb) | East-West Airlines |
| 16 | [Principal component analysis](assignments/16_pca.ipynb) | Wine |
| 17 | [Association rules](assignments/17_association_rules.ipynb) | Online retail |
| 18 | [Recommendation system](assignments/18_recommendation_system.ipynb) | Anime |
| 19 | [Time series forecasting](assignments/19_time_series.ipynb) | Exchange rates |
| 20 | [NLP: text classification and sentiment](assignments/20_nlp_text_classification.ipynb) | Blogs |
| 21 | [Neural networks with hyperparameter tuning](assignments/21_neural_networks.ipynb) | Alphabets |

> `assignments/my_dir/` holds the Keras Tuner search results created by assignment 21.

---

## Getting started

```bash
# Clone the repository
git clone https://github.com/abhiramjammula-aj/data-science_learning.git
cd data-science_learning

# Create a virtual environment and install dependencies
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

**About data paths:** the notebooks were written on a local Windows machine and Google Colab, so many of them load data from absolute paths such as `D:\Data science\codes\files\...` or `/content/...`. To re-run a notebook, change the path in its `read_csv(...)` cell to the file in [`datasets`](datasets). Some assignment datasets came from the course and aren't in this repo; the [datasets guide](datasets/README.md) lists them.

All notebooks are saved with their outputs, so you can read the results on GitHub without running anything.

---

## Tech stack

| Area | Libraries |
| --- | --- |
| Data handling | NumPy, pandas |
| Visualisation | Matplotlib, Seaborn |
| Statistics | SciPy, statsmodels |
| Machine learning | scikit-learn, XGBoost, LightGBM, apyori, ppscore |
| Deep learning | TensorFlow / Keras, Keras Tuner |
| NLP | NLTK, TextBlob |
| Deployment | Streamlit |
