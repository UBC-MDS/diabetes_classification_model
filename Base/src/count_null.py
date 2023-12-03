import pandas as pd

def count_null(data_frame):
    """
    Count the number of null values in every columns of the data frame.

    Creates a new DataFrame with two columns consisting the column name
    and the number of null values entries in that column.

    Parameters:
    ----------
    data_frame: pandas.DataFrame
        The input DataFrame with the data to be analyzed.

    
    Returns:
    -------
    pandas.DataFrame
        A dataFrame with two columns:
        - 'column': List of column names in the input DataFrame.
        - 'count' : List of count of each null values in the corresponding
                    column.

    Examples:
    --------
    >>> import pandas as pd
    >>> data = pd.read_csv('data.csv') #Replace 'data.csv' with your dataset file
    >>> result = count_null(data)
    >>> print(result)

    Notes:
    -----
    This function uses the pandas library to perform the counting of null values
    in every column of the DataFrame and the sum function to count the total.

    """
    result = data_frame.isnull().sum()
    result = result.reset_index()
    result.columns = ['column','count']
    return result
