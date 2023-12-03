from sklearn.model_selection import cross_validate
from sklearn.pipeline import make_pipeline
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyClassifier
from sklearn.neighbors import KNeighborsClassifier

#The below function is from DSCI 571
def mean_std_cross_val_scores(model, X_train, y_train, **kwargs):
    """
    Returns mean and std of cross validation

    Parameters
    ----------
    model :
        scikit-learn model
    X_train : numpy array or pandas DataFrame
        X in the training data
    y_train :
        y in the training data

    Returns
    ----------
        pandas Series with mean scores from cross_validation
    """

    scores = cross_validate(model, X_train, y_train, **kwargs)

    mean_scores = pd.DataFrame(scores).mean()
    std_scores = pd.DataFrame(scores).std()
    out_col = []

    for i in range(len(mean_scores)):
        out_col.append((f"%0.3f (+/- %0.3f)" % (mean_scores.iloc[i], std_scores.iloc[i])))

    return pd.Series(data=out_col, index=mean_scores.index)


def model_cross_val(models, X_train, y_train):
    """
    Returns the mean scores from 5-fold cross_validation for each model

    Parameters
    ----------
    models :
        dicionary where the key is the name of a model and the value is the pipeline for that model
 
    Returns
    ----------
        pandas dataframe containing mean scores from 5-fold cross_validation for each model 
    """
    results ={}
    for name, pipeline in models.items():
    # Cross-validation on training data
        results[name] = mean_std_cross_val_scores(
        pipeline, X_train, y_train, cv=10, return_train_score=True)

    return pd.DataFrame(results).T