import pandas as pd
import pytest
import sys
import os

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyClassifier
from sklearn.neighbors import KNeighborsClassifier

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.model_cross_val import model_cross_val

#Test data
preprocessor = StandardScaler()
models_1 = {
    "Dummy": make_pipeline(preprocessor, DummyClassifier()),
    "Knn": make_pipeline(preprocessor, KNeighborsClassifier())
}

X_train = pd.DataFrame({'a' : [1,2,3, 4, 5, 6]*4, 'b': [2,1,4,2,1,4]*4, 'c' : [5,3,2,3,1,1]*4})
y_train = pd.Series(["classA", "classB"]*12)
result_1 = model_cross_val(models_1, X_train, y_train)


models_2 = {
    "Dummy": make_pipeline(preprocessor, DummyClassifier()),
}

X_train = pd.DataFrame({'a' : [1,2,3, 4, 5, 6]*4, 'b': [2,1,4,2,1,4]*4, 'c' : [5,3,2,3,1,1]*4})
y_train = pd.Series(["classA", "classB"]*12)
result_2 = model_cross_val(models_2, X_train, y_train)

# Expected outputs


# Test for correct return type
def test_model_cross_val_returns_dataframe():
    assert isinstance(result_1, pd.DataFrame), "model_cross_val` should return a pandas data frame"
    assert isinstance(result_2, pd.DataFrame), "model_cross_val` should return a pandas data frame"

#Test number of columns in return
def test_model_cross_val_columns():
    assert result_1.shape[1] == 4, "there should be 4 columns in the data frame (not including the index)"
    assert result_2.shape[1] == 4, "there should be 4 columns in the data frame (not including the index)"

#Test number of rows in return
def test_model_cross_val_rows():
    assert result_1.shape[0] == 2, "there should be 1 row for each item the models parameter"
    assert result_2.shape[0] == 1, "there should be 1 row for each item the models parameter"

#Test that the model name is correclty the index of the data frame
def test_model_cross_val_index():
    assert result_1.index[0] == result_2.index[0], "the model name should be the index of the data frame"

#Test index types within the dataframe
def test_model_cross_val_index_type():
    assert isinstance(result_1.index[0], object), "the index should be of type object"
    assert isinstance(result_1.index[1], object), "the index should be of type object"
    assert isinstance(result_2.index[0], object), "the index should be of type object"
