# Email Spam Classifier Project

## Overview

Welcome to the Email Spam Classifier project! This project involves building a machine learning model to classify emails as spam or not spam. The trained model is pickled and then used to create a Streamlit website for easy and interactive classification.

## Project Structure

- 'spam.csv': Contains the dataset used for training and testing the model.
- 'model.pkl': Holds the pickled machine learning model.
- 'NLP Poject (SMS Spam Detection).ipynb': Source code for training the model and creating the Streamlit website.
- Lists the Python dependencies for the project.
- # Streamlit imports
import streamlit as st

# NLTK imports
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
from nltk import classify
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.classify import NaiveBayesClassifier

# Scikit-learn imports (for data preprocessing and splitting)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Other standard data science and visualization libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Model persistence (for pickling and unpickling)
import pickle
