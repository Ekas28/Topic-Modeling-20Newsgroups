# Data Folder

This folder contains information on the dataset used in this project.

## Dataset: 20 Newsgroups
- Source: [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/Twenty+Newsgroups)
- Description: The 20 Newsgroups dataset is a collection of approximately 20,000 newsgroup documents, partitioned across 20 categories.
- Usage: This dataset is commonly used for text classification and topic modeling.

## How to Load the Dataset
We use **scikit-learn's built-in loader**:
```python
from sklearn.datasets import fetch_20newsgroups

newsgroups = fetch_20newsgroups(subset='all')
texts = newsgroups.data

