import click
import os
import sys
import altair as alt
import numpy as np
import pandas as pd
import pickle
from sklearn import set_config
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import fbeta_score, make_scorer
from joblib import dump
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.model_cross_val import model_cross_val

@click.command()
@click.option('--training_data', type=str, help="Path to training data")
@click.option('--preprocessor', type=str, help="Path to preprocessor object")
@click.option('--optimized_knn', type=str, help="Path to optimized k-NN model object")
@click.option('--optimized_tree', type=str, help="Path to optimized decision tree object")

def main(training_data, preprocessor, optimized_knn, optimized_tree):
    """
    Returns a table with the cross validation scores comparing three classification models: 
    k-nn, decision tree, dummy, and logistic regression.
    """
    set_config(transform_output="pandas")

    # read in data & preprocessor
    train_df = pd.read_csv(training_data)
    X_train = train_df.drop(['Diabetes_binary'], axis = 1)
    y_train = train_df['Diabetes_binary']
    preprocessor = pickle.load(open(preprocessor, "rb"))

    # Models to test
    models = {
        "Dummy": make_pipeline(preprocessor, DummyClassifier()),
        "Decision tree": make_pipeline(preprocessor, DecisionTreeClassifier(random_state=123)),
        "Logistic regression": make_pipeline(preprocessor, 
                                         LogisticRegression(max_iter=1000)),
        "Knn": make_pipeline(preprocessor, KNeighborsClassifier())
    }





