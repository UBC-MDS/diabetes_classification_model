import pandas as pd
import pytest
import sys
import os

# Import the check_imbalance function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.check_imbalance import check_imbalance

# Test data
imbalanced_data = pd.DataFrame({"Diabetes_binary": [0, 1, 1, 0, 1, 0, 1]})
balanced_data = pd.DataFrame({"Diabetes_binary": [0, 1, 0, 1]})
empty_data = pd.DataFrame(columns=["Diabetes_binary"])
imbalanced_data_with_duplicates = pd.concat([imbalanced_data, imbalanced_data])

# Expected outputs
imbalanced_data_output = pd.Series({0: 2, 1: 5})
balanced_data_output = pd.Series({0: 2, 1: 2})
empty_data_output = pd.Series(dtype=int)
imbalanced_data_with_duplicates_output = pd.Series({0: 2, 1: 5})

# Test for correct return type
def test_check_imbalance_returns_series():
    result = check_imbalance(imbalanced_data, "Diabetes_binary")
    assert isinstance(result, pd.Series), "check_imbalance should return a pandas Series"

# Test for correct values in the Series
def test_check_imbalance_values():
    pd.testing.assert_series_equal(check_imbalance(imbalanced_data, "Diabetes_binary"), imbalanced_data_output)
    pd.testing.assert_series_equal(check_imbalance(balanced_data, "Diabetes_binary"), balanced_data_output)
    pd.testing.assert_series_equal(check_imbalance(empty_data, "Diabetes_binary"), empty_data_output)
    pd.testing.assert_series_equal(
        check_imbalance(imbalanced_data_with_duplicates, "Diabetes_binary"),
        imbalanced_data_with_duplicates_output
    )

# Test for correct error handling for incorrect type of feature name
def test_check_imbalance_type_error():
    with pytest.raises(KeyError):
        check_imbalance(imbalanced_data, 1)

# Test for correct error handling for incorrect object type 
# (not a pandas data frame)
def test_check_imbalance_attribute_error():
    with pytest.raises(AttributeError):
        check_imbalance([{"Diabetes_binary": 0, "feature": 1}], "Diabetes_binary")
