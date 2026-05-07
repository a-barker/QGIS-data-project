import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

from sklearn.impute import SimpleImputer

################################
        #2007 Datasets
################################

unit07_demo= pd.read_csv('../data/07_DataDict/UNIT_Demo.csv')
unit07_assets=pd.read_csv('../data/07_DataDict/UNIT_Assets.csv')
unit07_exded=pd.read_csv('../data/07_DataDict/UNIT_ExDed.csv')
unit07_inc=pd.read_csv('../data/07_DataDict/UNIT_Inc.csv')
per07_char=pd.read_csv('../data/07_DataDict/PERS_Char.csv')
per07_inc=pd.read_csv('../data/07_DataDict/PERS_Inc.csv')

################################
        #2017 Datasets
################################

unit17_demo= pd.read_csv('../data/17_DataDict/UNIT_Demo.csv')
unit17_assets=pd.read_csv('../data/17_DataDict/UNIT_Assets.csv')
unit17_exded=pd.read_csv('../data/17_DataDict/UNIT_ExDed.csv')
unit17_inc=pd.read_csv('../data/17_DataDict/UNIT_Inc.csv')
per17_char=pd.read_csv('../data/17_DataDict/PERS_Char.csv')
per17_inc=pd.read_csv('../data/17_DataDict/PERS_Inc.csv')