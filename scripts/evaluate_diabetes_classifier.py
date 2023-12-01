# evaluate_diabetes_classifier.py
# author: Angela Chen
# date: 2023-12-01

import click
import os
import sys
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

@click.command()
@click.option('--id', type=int, help='UCI repository ID') 
@click.option('--write-to', type=str, help='Path to directory where raw data will be stored in')
@click.option('--random', type=int, help="Random seed", default=123)
@click.option('--split-data-to', type=str, help="Path to directory where split data will be stored")
@click.option('--split-ratio',type=float, help="Ratio used to split data into test data")

def main(id, write_to, random, split_data_to, split_ratio):

    final_knn = KNeighborsClassifier(n_neighbors=100)
    final_knn.fit(X_train, y_train)

    y_pred_knn = final_knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred_knn)
    print(f'Accuracy of knn model of n=100: {accuracy}')

    # Additional metrics
    print(classification_report(y_test, y_pred_knn))
    print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred_knn))
    print('AUC-ROC Score:', roc_auc_score(y_test, final_knn.predict_proba(X_test)[:, 1]))

    final_logistic = LogisticRegression(max_iter=1000)
    final_logistic.fit(X_train, y_train)

    y_pred_log = final_logistic.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred_log)
    print(f'Accuracy of logistic model: {accuracy}')

    # Additional metrics
    print(classification_report(y_test, y_pred_log))
    print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred_log))
    print('AUC-ROC Score:', roc_auc_score(y_test, 
                                        final_logistic.predict_proba(X_test)[:, 1]))

if __name__ == '__main__':
    main()