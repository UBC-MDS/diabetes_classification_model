
import os
import sys
import numpy as np
import pandas as pd
import pickle
from sklearn import set_config
from sklearn.model_selection import cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.pipeline import make_pipeline
from sklearn.metrics import fbeta_score, make_scorer
from joblib import dump
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.get_feature_importance import get_feature_importances
from src.model_cross_val import mean_std_cross_val_scores

# author: Ella Hein
# date: 2023-12-06

"""Returns a csv table with the cross validation scores comparing three classification models: 
    k-nn, decision tree, dummy, and logistic regression, in addition to a csv table comparing the feature 
    coefficients generated from logistic regression.

Usage: src/down_data.py --out_type=<out_type> --url=<url> --out_file=<out_file>

Options:
--out_type=<out_type>    Type of file to write locally (script supports either feather or csv)
--url=<url>              URL from where to download the data (must be in standard csv format)
--out_file=<out_file>    Path (including filename) of where to locally write the file
"""

@click.command()
@click.option('--training_data', type=str, help="Path to training data")
@click.option('--preprocessor', type=str, help="Path to preprocessor object")
@click.option('--optimized_knn', type=str, help="Path to optimized k-NN model object")
@click.option('--optimized_tree', type=str, help="Path to optimized decision tree object")
@click.option('--table_to', type=str, help="Path to directory where crossvalidation results for all models will be written to")


def main(training_data, preprocessor, optimized_knn, optimized_tree, table_to):
    """
    Returns a table with the cross validation scores comparing three classification models: 
    k-nn, decision tree, dummy, and logistic regression, in addition to a table comparing the feature 
    coefficients generated from logistic regression.
    """
    set_config(transform_output="pandas")

    # read in data & preprocessor
    train_df = pd.read_csv(training_data)
    X_train = train_df.drop(['Diabetes_binary'], axis = 1)
    y_train = train_df['Diabetes_binary']
    preprocessor = pickle.load(open(preprocessor, "rb"))
    knn_pipeline = pickle.load(open(optimized_knn, "rb"))
    tree_pipeline = pickle.load(open(optimized_tree, "rb"))

    # Models to test
    models = {
        "Dummy": make_pipeline(preprocessor, DummyClassifier()),
        "Decision tree": tree_pipeline,
        "Logistic regression": make_pipeline(preprocessor, 
                                         LogisticRegression(max_iter=1000)),
        "Knn": knn_pipeline
    }
    
    # Evaluate each model
    results = {}
    for name, pipeline in models.items():
        
        # Cross-validation on training data
        results[name] = mean_std_cross_val_scores(
              pipeline, X_train, y_train, cv=10, return_train_score=True, 
        )
    
    results_df = pd.DataFrame(results).T
    results_df.to_csv(os.path.join(table_to,"model_comparison_results.csv"))

    # Get coefficient table from logistic regression
    coef_df = get_feature_importances(X_train, y_train)
    coef_df.to_csv(os.path.join(table_to,"feature_importances.csv"))
    
if __name__ == '__main__':
    main()




