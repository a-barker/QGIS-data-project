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

def plot_simple_features(column,img_name,description):
    """Plots features on a countplot, used for columns with binary values and for EDA datasets."""
    plt.figure(figsize = (16,10))
    plt.suptitle(description, fontsize=20)
    idx = 221
    while idx<225:
        for key,value in {'nm07':nm07_orig,'nm17':nm17_orig,'ne07':ne07_orig,'ne17':ne17_orig}.items():
            mean = value[column].mean()
            ax = plt.subplot(idx)
            plt.title(f'$\t{key.upper()}$')
            sns.countplot(x=value[column],palette="husl",hue=column, data=value) 
            ax.axhline(mean,linewidth=1,color='r')
            ax.set_xlabel('')
            #ax.set_xticklabels([0,1])
            idx +=1
    plt.savefig("../images/ind_features/" + str(img_name) + ".png")