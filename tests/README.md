# Diabetes Classification Models - Test suite developer notes

## Running the tests:

To execute the tests, use the `pytest` command at the project's root.

## Test teardown

`check_imbalance.py` contains the code to check whether a dataframe
with a given feature name is correctly calculating the balance of
the binary features.

`count_null.py` contains the code to check if the function correctly
count the number of null values in every columns of the data frame.

`get_feature_importance.py` contains the code to check if the function
correctly gather the feature importance data correctly.
