# evaluate_diabetes_classifier.py
# author: Angela Chen
# date: 2023-12-01

import click
import os
import sys
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

@click.command()
@click.option('--models', type=dict, help='Models determined after hyperparameter optimization') 
@click.option('--X_train', type=pd.DataFrame, help='X_Train')
@click.option('--y_train', type=pd.DataFrame, help="y_train")
@click.option('--X_test', type=pd.DataFrame, help="X_test")
@click.option('--y_test',type=pd.DataFrame, help="y_test")

def main(models, X_train, y_train, X_test, y_test):
    
    final_knn = models["knn"]
    final_knn.fit(X_train, y_train)

    y_pred_knn = final_knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred_knn)
    print(f'Accuracy of the best knn model: {accuracy}')

    # Additional metrics
    print(classification_report(y_test, y_pred_knn))
    print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred_knn))
    print('AUC-ROC Score:', roc_auc_score(y_test, final_knn.predict_proba(X_test)[:, 1]))

    final_DT = models["decision tree"]
    final_DT.fit(X_train, y_train)

    y_pred_DT = final_DT.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred_log)
    print(f'Accuracy of Decision tree model: {accuracy}')

    # Additional metrics
    print(classification_report(y_test, y_pred_DT))
    print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred_DT))
    print('AUC-ROC Score:', roc_auc_score(y_test, 
                                        final_DT.predict_proba(X_test)[:, 1]))

if __name__ == '__main__':
    main()