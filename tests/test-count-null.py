import pandas as pd
import pytest
import sys
import os

#Importing the check_null function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.count_null import count_null

#Test data
data_frame_1_col_2_nulls = pd.DataFrame(
    {'name': ['name1', 'name2','name3', None, None ]}
)
data_frame_1_col_1_nulls = pd.DataFrame(
    {'name': [None]}
)
data_frame_2_cols_1_null = pd.DataFrame(
    {'name': ['name1', 'name2','name3', 'name4', None ],
    'col2': ['col21', 'col22','col23',  'col24', 'col25']}
)
data_frame_2_cols_no_null = pd.DataFrame(
    {'name': ['name1', 'name2','name3', 'name4', 'name5' ],
    'col2': ['col21', 'col22','col23',  'col24', 'col25' ]}
)
data_frame_2_cols_all_null = pd.DataFrame(
    {'name': [None, None, None],
    'col2': [None, None, None]}
)
empty_df = pd.DataFrame({'col1': []})

#Expected output 
data_frame_1_col_2_nulls_output = pd.DataFrame(
    {'column': ['name'],
     'count': [2]}
)
data_frame_1_col_1_nulls_output = pd.DataFrame(
    {'column': ['name'],
     'count': [1]}
)
data_frame_2_cols_1_null_output = pd.DataFrame(
    {'column': ['name', 'col2'],
     'count': [1, 0]}
)
data_frame_2_cols_no_null_output  = pd.DataFrame(
    {'column': ['name', 'col2'],
     'count': [0, 0]}
)
data_frame_2_cols_all_null_output  = pd.DataFrame(
    {'column': ['name', 'col2'],
     'count': [3, 3]}
)
empty_df_output = pd.DataFrame(
    {'column': [],
     'count': []}
)

# Test for correct return type
def test_count_null_return_type():
    result = count_null(data_frame_2_cols_no_null)
    assert isinstance(result, pd.DataFrame), "check_null should return a pandas data frame"

#Test for correct counts for each columns
def test_count_null_return_correct_count_values():
    pd.testing.assert_frame_equal(count_null(data_frame_1_col_2_nulls), data_frame_1_col_2_nulls_output)
    pd.testing.assert_frame_equal(count_null(data_frame_1_col_1_nulls), data_frame_1_col_1_nulls_output)
    pd.testing.assert_frame_equal(count_null(data_frame_2_cols_1_null), data_frame_2_cols_1_null_output)
    pd.testing.assert_frame_equal(count_null(data_frame_2_cols_no_null), data_frame_2_cols_no_null_output)
    pd.testing.assert_frame_equal(count_null(data_frame_2_cols_all_null), data_frame_2_cols_all_null_output)

#Test for correct error handling type of column value
def test_count_null_error_handling():
    with pytest.raises(AttributeError, match="'str' object has no attribute 'isnull'"):
        count_null("not_a_dataframe_but_a_str")
    with pytest.raises(AttributeError, match="'NoneType' object has no attribute 'isnull'"):
        count_null(None)
    with pytest.raises(AttributeError, match="'list' object has no attribute 'isnull'"):
        count_null([])