---
editor_options: 
  markdown: 
    wrap: 72
---

# Diabetes Classification Models

Members: Angela Chen, Ella Hein, Scout McKee, and Sharon Voon.

## Contents

-   analysis.ipynb: Our data analysis file
-   data/: A directory containing csv's of all data used for analysis

Milestone 1 project for DSCI 522.

## About

In this project, we try to create models for predicting diabetes. We try
several different models such as logistic regression, k- nearest
neighbours (k-nn), and decision tree. The logistic regression model was
most accurate and the k-nn model was second best. We attempted to
optimize the hyperparameters of the k-nn model to see if we could make it
as accurate as the logistic regression in predicting diabetes.

At the end we evaluated our following best performing models based on accuracy,
precision, recall, and AUC-ROC score using the test dataset:
- logistic regression model
- k- nearest neighbours (k-nn) with n_neighbours = 100
Based on the evaluation metrics, the Logistic Regression model performs better
than the K-Nearest Neighbors model on the provided test dataset. Considering
these results and the fact that Logistic Regression also offers interpretability
of feature coefficients, we decided to recommend the logistic regression model.

The data set used for this project was created through funding from the
CDC to "better understand the relationship between lifestyle and
diabetes in the US". It can be found in the UC Irvine Machine Learning
Repository
(<https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators>).
Each row is data for one patient. As explained in the UC Irvine Machine
Learning Repository for this data, there are 35 features which consist
of some demographics, lab test results, and answers to survey questions
for each patient.

## Report

The final report can be found [here](LINK%20TO%20THE%20HTML).

## Usage

First time running the project, run the following from the root of this
repository:

``` bash
conda env create --file env-dsci-522.yaml
```

To run the analysis, run the following from the root of this repository:

``` bash
conda activate Diabetes_Prediction
jupyter lab 
```

Open `diabetes_classification_model_report.ipynb` in Jupyter Lab and under the "Kernel" menu click
"Restart Kernel and Run All Cells...".

## Important note on obtaining the dataset

The UC Irvine Machine Learning Repository gives a link to download the
dataset off Kaggle. Since this requires authenication, here is a more
direct way to obtain the data form UC Irvine without using Kaggle.

On the command line run: pip install ucimlrepo

Then paste the following code at the beginning of the analysis document,
replacing the current section which reads in the data.

from ucimlrepo import fetch_ucirepo \# fetch dataset
cdc_diabetes_health_indicators = fetch_ucirepo(id=891) \# data (as
pandas dataframes) X = cdc_diabetes_health_indicators.data.features y =
cdc_diabetes_health_indicators.data.targets

## Dependencies

-   `conda` (version 23.7.4)
-   `nb_conda_kernels` (version 2.3.1)
-   Python and packages listed in `env-dsci-522.yaml`

## License

The Diabetes Prediction materials here are licensed under the Creative
Commons Attribution-NonCommercial-NoDerivs 4.0 International (CC
BY-NC-ND 4.0 DEED) and the MIT license. If re-using/re-mixing please
provide attribution and link to this webpage.

## References

CDC. 2014. "CDC Diabetes Health Indicators." University of California,
Irvine, School of Information; Computer Sciences. Retrieved November
14th 2023 from
<https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators>

Sapra A, Bhandari P. Diabetes. [Updated 2023 Jun 21]. In: StatPearls
[Internet]. Treasure Island (FL): StatPearls Publishing; 2023
Jan-.Available from: <https://www.ncbi.nlm.nih.gov/books/NBK551501/>
