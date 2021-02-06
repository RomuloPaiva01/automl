"""

Template to run the automl
It contains a pipeline, a model and a postprocessing analysis

"""

#%% Imports

import pandas as pd
import numpy as np
import sys
import os

path_pipeline = "/home/romulo/projects/automl/pipeline/"
sys.path.append(os.path.abspath(path_pipeline))


from pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
#%% Read dataset

data_path = "/home/romulo/projects/automl/utils/data/dataset.xlsx"

df = pd.read_excel(data_path)

X = df[df.columns[~df.columns.isin(["Fail"])]]

y = df["Fail"]

#split train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

#%% Pipeline

pipeline = Pipeline([('StandardScaler', StandardScaler)])

pipeline.fit(X, y)

pipeline.predict(X, y)









