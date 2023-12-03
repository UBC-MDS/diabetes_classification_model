import pandas as pd

def check_imbalance(df, feat_name):
    """
    Check for imbalances of a specific feature in a dataset.

    Parameters:
    - df (pd.DataFrame): The input DataFrame containing the dataset.
    - feat_name (str): The name of the feature to analyze for imbalances.

    Returns:
    pd.Series: The counts of each class in the specified feature.

    Steps:
    1. Remove duplicate rows from the DataFrame.
    2. Return a Series containing the count of each class in the specified feature.

    Example:
    --------
    >>> import pandas as pd
    >>> data = pd.DataFrame({"Diabetes_binary": [0, 1, 1, 0, 1, 0, 1]})
    >>> result = check_imbalance(data, "Diabetes_binary")
    >>> print(result)
    
    Notes:
    -----
    This function utilizes pandas to remove duplicate rows and calculate
    the count of each class in the specified feature.

    """
    feature_counts = df[feat_name].value_counts()

    return feature_counts
