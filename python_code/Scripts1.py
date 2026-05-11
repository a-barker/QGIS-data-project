import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

from sklearn.impute import SimpleImputer


################
    #EDA
################

def impute_df(df):
    """Returns a dataframe with mean imputed values for NaN."""
    my_imputer = SimpleImputer(missing_values=np.nan)
    data_with_imputed_values = pd.DataFrame(my_imputer.fit_transform(df),columns = df.columns)
    return data_with_imputed_values

def only_zero(df):
    """Drops all columns that are all zero values and returns a Dataframe."""
    filter = pd.DataFrame(df.sum(axis=0)==0, columns=['value'])
    filter = filter.loc[filter['value']==True]
    col = list(filter.index)
    return df.drop(col,axis=1)
