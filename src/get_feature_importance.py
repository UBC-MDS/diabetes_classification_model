from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pandas as pd

def get_feature_importances(X_train, y_train, target_column_name):
    """
    Scales data using a standard scaler, runs logistic regression 
    on the training data and returns a dataframe of the feature names 
    along with their respective coefficients (as defined by logistic regression).

    Parameters
    ------
    X_train: numpy array or pandas DataFrame
        The X used for training
    y_train: numpy array or pandas Datarame
        The Y used for training
    target_column_name: string
        The name of the column where the target values are stored

    Returns:
    ------
        Pandas dataframe with two columns: features and coefficients

    Examples:
    ------
        get_feature_importance(X_train, y_train, "Diabetes_binary")
    
    """
    # Manually scaling the data
    scaler = StandardScaler()  
    scaler.fit(X_train)  
    X_train_scaled = scaler.transform(X_train)  
    
    # Fitting Logistic Regression
    lr = LogisticRegression()
    lr.fit(X_train_scaled, y_train)

    # Grab feature columns
    feature_columns = train_df.drop(columns=[target_column_name]).columns
    
    # Create a DataFrame to display coefficients
    data = {"features": feature_columns, "coefficients": lr.coef_[0]}
    coefficients_df = pd.DataFrame(data)
    
    return coefficients_df
