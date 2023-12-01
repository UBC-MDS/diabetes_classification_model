# evaluate_diabetes_classifier.py
# author: Angela Chen
# date: 2023-12-01

import click
import os
import sys
import pandas as pd
import pickle
from sklearn import set_config
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

@click.command()
@click.option('--models', type=dict, help="Path to directory where optimized knn model and decision tree model object") 
@click.option('--train_df', type=str, help='Path to train_df')
@click.option('--test_df', type=str, help="Path to test_df")
@click.option('--knn_from', type=str, help="Path to the folder where the fit knn pipeline object lives")
@click.option('--DT_from', type=str, help="Path to the folder where the fit Decision tree pipeline object lives")
@click.option('--results-to', type=str, help="Path to the folder where the result will be written to")


def main(models, train_df, test_df, knn_from, DT_from, results_to):
    '''Evaluates the diabetes classifier on the test data 
    and saves the evaluation results.'''
    set_config(transform_output="pandas")

    #preparing the X_train, y_train, X_test, y_test
    train_df = pd.read_csv(train_df)
    test_df = pd.read_csv(test_df)
    X_train = train_df.drop(['Diabetes_binary'], axis = 1)
    y_train = train_df['Diabetes_binary']
    X_test = test_df.drop(['Diabetes_binary'], axis = 1)
    y_test = test_df['Diabetes_binary']

    with open(knn_from, 'rb') as f:
        final_knn = pickle.load(f)
    with open(DT_from, 'rb') as f2:
        final_DT = pickle.load(f2)

    final_knn = models["knn"]
    final_knn.fit(X_train, y_train)

    y_pred_knn = final_knn.predict(X_test)
    print(classification_report(y_test, y_pred_knn))
    print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred_knn))

    final_DT = models["decision tree"]
    final_DT.fit(X_train, y_train)

    y_pred_DT = final_DT.predict(X_test)

    print(classification_report(y_test, y_pred_DT))
    print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred_DT))
    
    confusion_matrix.to_csv(os.path.join(results_to, "confusion_matrix.csv"))

if __name__ == '__main__':
    main()