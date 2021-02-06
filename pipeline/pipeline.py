import pandas as pd
import numpy as np
import sklearn
from sklearn.pipeline import Pipeline
import sys
import typing as t

class AutoMlPipeline(Pipeline):
    
    def fit(self, X: pd.DataFrame, y: pd.Series):
        
        """
        Method
        """
        
        if type(X) is not pd.DataFrame:
            raise TypeError(" X must be a DataFrame type")
        if type(y) is not pd.Series:
            raise TypeError(" y must be of Series type")  
        try:
            Pipeline.fit(X, y)  
        except Exception as e:
            print("Problem in running fit method")
            
    
    def predict(self, X: pd.DataFrame, y: pd.Series):
        
        """
        Method...
        """
        
        if type(X) is not pd.DataFrame:
            raise TypeError(" X must be a DataFrame type")  
        if type(y) is not pd.Series:
            raise TypeError(" y must be of Series type")
        try:
            Pipeline.predict(X, y)  
        except Exception as e:
            print("Problem in running predict method")
        

        