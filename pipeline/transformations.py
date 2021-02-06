"""

Transformations for the pipeline

"""

import pandas as pd


def pandas_to_numpy(X):
    
    """
    Function to transform a pandas DataFrame into a numpy array
    It is needed because some machine learning methods do not accept
    DataFrames
    
    params: 
        - X: pandas DataFrame
    """
    
    if type(X) is pd.DataFrame:
        X = X.to_numpy()
    else:
        raise TypeError("X must be a DataFrame")
    return X


def change_column_name(X, dict_columns):
    
    """
    Function to change the name of the selected columns of a DataFrame
    
    params:
        - X: pandas DataFrame
        - dict_columns: Dictionary contaning the original columns and their
        new names
    """
    
    try:
        if type(X) is not pd.DataFrame:
            raise TypeError("X must be a DataFrame")
        else:
            X.rename(columns=dict_columns, inplace=True)
    except Exception as e:
        print("change_column_name has failed")
    return X
    

def remove_nans(X, axis):

    """
    Function ro remove nans from a DataFrame
    
    params:
        - X: pandas DataFrame
        - axis: axis (rows or columns)
    """    
    
    try:
        if type(X) is not pd.DataFrame:
            raise TypeError("X must be a DataFrame")  
        if axis not in (0,1):
            raise ValueError("axis must be 0 or 1")
        else:
            X.dropna(inplace = True, axis = axis)    
    except Exception as e:
        print("remove_nans has failed")
    return X   
    
def fill_gaps(X, method):
    
    """
    Function that fill missing data in a DataFrame
    
    params:
        -X: pandas DataFrame
        -method: Fill method. Can be backfill...
    """
    
    try:
        if type(X) is not pd.DataFrame:
            raise TypeError("X must be a DataFrame")
        if method not in ("backfill"):
            raise ValueError("method must be the ones in the documentation")
        else:
            if method == "backfill":
                X.fillna(method='backfill', inplace = True)
    except Exception as e:
        print("remove_nans has failed")                
    return X
    
    
    
    
    
