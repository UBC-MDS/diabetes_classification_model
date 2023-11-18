# DSCI_522_Group2
Members: Angela Chen, Ella Hein, Scout McKee, and Sharon Voon.

Contents
- analysis.ipynb: Our data analysis file
- data/: A directory containing csv's of all data used for analysis



## K-Nearest Neighbors (KNN):

Accuracy: 72.81%
Precision (1.0): 71%
Recall (1.0): 78%
F1-Score (1.0): 74%
Confusion Matrix:
True Positives (1.0): 5396
True Negatives (0.0): 4660
False Positives: 2252
False Negatives: 1504
AUC-ROC Score: 0.802

## Logistic Regression:
Accuracy: 74.62%
Precision (1.0): 74%
Recall (1.0): 77%
F1-Score (1.0): 75%
Confusion Matrix:
True Positives (1.0): 5300
True Negatives (0.0): 5006
False Positives: 1906
False Negatives: 1600
AUC-ROC Score: 0.821

Comments and Evaluation:
Accuracy:

The Logistic Regression model outperforms the KNN model in terms of accuracy (74.62% vs. 72.81%).
Precision, Recall, and F1-Score:

Both models have comparable precision, recall, and F1-score for class 1.0 (a person as diabetes), but Logistic Regression slightly outperforms KNN in all these metrics.
Confusion Matrix:

Logistic Regression has a lower number of false positives and false negatives compared to KNN. This indicates that the Logistic Regression model is making fewer errors in both positive and negative predictions.
AUC-ROC Score:

The AUC-ROC score, which measures the model's ability to distinguish between classes(have diabetes versus does not have diabetes, is higher for the Logistic Regression model (0.821) compared to the KNN model (0.802).

Conclusion:
Based on the evaluation metrics, the Logistic Regression model performs better than the K-Nearest Neighbors model on the provided test dataset. It achieves higher accuracy, precision, recall, and AUC-ROC score, indicating a better overall performance.

Therefore, considering these results and the fact that Logistic Regression also offers interpretability of feature coefficients, it seems reasonable to prefer the Logistic Regression model for this specific classification task. 