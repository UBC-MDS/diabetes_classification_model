import pytest
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import sys
import os

# Import the get_feature_importance function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.get_feature_importance import get_feature_importances

# Sample data for testing
X_train = pd.DataFrame({"Feature1": [1, 2, 3], "Feature2": [4, 5, 6]})
y_train = [0, 1, 0]
target_column_name = "Diabetes_binary"

def test_get_feature_importances_with_valid_input():
    """Test when valid input is provided"""
    result_df = get_feature_importances(X_train, y_train, target_column_name)
    
    # Check if the result DataFrame has the expected columns
    assert all(col in result_df.columns for col in ["features", "coefficients"])
    
    # Check if the number of rows in the result DataFrame matches the number of features
    assert len(result_df) == len(X_train.columns)
    
    # Check if coefficients are numbers and not NaN
    assert result_df["coefficients"].dtype.kind in "fi"
    assert not result_df["coefficients"].isnull().any()

# def test_get_feature_importances_with_invalid_target_column():
#     """Test when an invalid target column name is provided"""
#     with pytest.raises(KeyError):
#         get_feature_importances(X_train, y_train, "Invalid_Target_Column")

def test_get_feature_importances_with_empty_input():
    """Test when empty input data is provided"""
    with pytest.raises(ValueError):
        get_feature_importances(pd.DataFrame(), pd.Series(), target_column_name)

def test_get_feature_importances_with_non_numeric_input():
    """Test when non-numeric input data is provided"""
    X_train_non_numeric = pd.DataFrame({"Feature1": ["A", "B", "C"], "Feature2": ["D", "E", "F"]})
    with pytest.raises(ValueError):
        get_feature_importances(X_train_non_numeric, y_train, target_column_name)

def test_get_feature_importances_with_missing_values():
    """Test when input data contains missing values"""
    X_train_missing_values = pd.DataFrame({"Feature1": [1, 2, np.nan], "Feature2": [4, np.nan, 6]})
    with pytest.raises(ValueError):
        get_feature_importances(X_train_missing_values, y_train, target_column_name)


