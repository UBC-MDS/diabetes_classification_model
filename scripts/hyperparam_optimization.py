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
@click.option('--models_to', type=str, help="Path to directory where optimized knn model and decision tree model object will be written to")
@click.option('--table_to', type=str, help="Path to directory where crossvalidation results for optimized model will be written to")

def main(training_data, preprocessor, models_to, table_to):
    '''Execute hyper parameter optimization for a knn model and a decision tree model.'''
    set_config(transform_output="pandas")

    # read in data & preprocessor
    train_df = pd.read_csv(training_data)
    X_train = train_df.drop(['Diabetes_binary'], axis = 1)
    y_train = train_df['Diabetes_binary']
    preprocessor = pickle.load(open(preprocessor, "rb"))

    # optimize knn model
    knn = KNeighborsClassifier()
    knn_pipeline = make_pipeline(preprocessor, knn)

    knn_parameter_grid = {
        "kneighborsclassifier__n_neighbors": [50, 100, 200, 300, 500]
    }

    knn_search = RandomizedSearchCV(knn_pipeline, param_distributions=knn_parameter_grid, n_iter=10, n_jobs= -1, return_train_score=True, random_state=123) 

    knn_search.fit(X_train, y_train)

    with open(os.path.join(models_to, "knn_pipeline.pickle"), 'wb') as f: 
        pickle.dump(knn_search.best_estimator_, f)
    

    # optimize decision tree model
    tree = DecisionTreeClassifier()
    tree_pipeline = make_pipeline(preprocessor, tree)

    tree_parameter_grid = {
        "decisiontreeclassifier__max_depth": [5,10, 50, 100, 500, 1000]
    }

    tree_search = RandomizedSearchCV(tree_pipeline, param_distributions=tree_parameter_grid, n_iter=10, n_jobs= -1, return_train_score=True, random_state = 123) 

    tree_search.fit(X_train, y_train)

    pickle.dump(tree_search.best_estimator_, open(os.path.join(models_to, "tree_model.pickle"), "wb"))

    #write out df with cross val results for knn
    models = {"knn": knn_search.best_estimator_, "decision tree": tree_search.best_estimator_}
    results_df = pd.DataFrame({"n_neighbours" : [knn_search.best_params_["kneighborsclassifier__n_neighbors"]], "max_depth" : [tree_search.best_params_['decisiontreeclassifier__max_depth']]}).reset_index(drop=True)
    results_df.to_csv(os.path.join(table_to,"best_hyperparams.csv"))
if __name__ == '__main__':
    main()