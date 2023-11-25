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
imbalanced_data_output = pd.Series({0: 3, 1: 4})
balanced_data_output = pd.Series({0: 2, 1: 2})
empty_data_output = pd.Series(dtype=int)
imbalanced_data_with_duplicates_output = pd.Series({0: 6, 1: 8})

# Test for correct return type
def test_check_imbalance_returns_series():
    result = check_imbalance(imbalanced_data, "Diabetes_binary")
    assert isinstance(result, pd.Series), "check_imbalance should return a pandas Series"

# Test for correct values in the Series
def test_check_imbalance_values():
    a = check_imbalance(imbalanced_data, "Diabetes_binary").sort_index().reset_index(drop=True)
    b = imbalanced_data_output.sort_index().reset_index(drop=True).rename('count')
    pd.testing.assert_series_equal(a, b)

    c = check_imbalance(balanced_data, "Diabetes_binary").sort_index().reset_index(drop=True)
    d = balanced_data_output.sort_index().reset_index(drop=True).rename('count')
    pd.testing.assert_series_equal(c, d)

    e = check_imbalance(empty_data, "Diabetes_binary").sort_index().reset_index(drop=True)
    f = empty_data_output.sort_index().reset_index(drop=True).rename('count')
    pd.testing.assert_series_equal(e, f)

    g = check_imbalance(imbalanced_data_with_duplicates, "Diabetes_binary").sort_index().reset_index(drop=True)
    h = imbalanced_data_with_duplicates_output.sort_index().reset_index(drop=True).rename('count')

    pd.testing.assert_series_equal(g, h)
# Test for correct error handling for incorrect type of feature name
def test_check_imbalance_type_error():
    with pytest.raises(KeyError):
        check_imbalance(imbalanced_data, 1)

# Test for correct error handling for incorrect object type 
# (not a pandas data frame)
def test_check_imbalance_attribute_error():
    with pytest.raises(TypeError):
        check_imbalance([{"Diabetes_binary": 0, "feature": 1}], "Diabetes_binary")
