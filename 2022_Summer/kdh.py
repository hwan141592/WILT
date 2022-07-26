##################
#### PACKAGES ####
# pip install warnings
# pip install fastparquet
# pip install pyarrow
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import fastparquet
# import pyarrow
import warnings
warnings.filterwarnings('ignore')



###################
#### VARIABLES ####
DF_TMP = pd.DataFrame({'col_a':[1,2,3,4], 'col_b':[5,6,7,8], 'col_c':[9,10,11,12]})



###################
#### FUNCTIONS ####
#### files ####
def saveAsParquet(df, fpath, p=True):
    tic = time.time()
    df.to_parquet(os.path.join(fpath), compression='gzip')
    toc = time.time()
    if p == True:
        print('*** It took {:4f} seconds to save dataframe as pickle file.'.format(toc-tic))
    else:
        pass
        
def readParquet(fpath, p=True):
    tic = time.time()
    df = pd.read_parquet(fpath)
    toc = time.time()
    if p==True:
        print('*** It took {:4f} seconds to read the pickle file.'.format(toc-tic))
    else:
        pass
    return df

def saveAsPickle(df, fpath, p=True):
    tic = time.time()
    df.to_pickle(os.path.join(fpath))
    toc = time.time()
    if p == True:
        print('*** It took {:4f} seconds to save dataframe as pickle file.'.format(toc-tic))
    else:
        pass
    
def readPickle(pkl_fpath, p=True):
    tic = time.time()
    df = pd.read_pickle(pkl_fpath)
    toc = time.time()
    if p==True:
        print('*** It took {:4f} seconds to read the pickle file.'.format(toc-tic))
    else:
        pass
    return df
    
def getKeyColCand(df):
    li_key_col_cand = []
    for col in df.columns:
        if df.shape[0] - df[col].nunique() == 0:
            li_key_col_cand.append(col)
        else:
            pass
    print('*** key column candidates: {}'.format(li_key_col_cand))
    return li_key_col_cand

def nullCheckForLoop(df):
    all_null_sum = 0
    for col in df.columns :        
        all_null_sum = all_null_sum + df[col].isnull().sum()
    if all_null_sum == 0:
        print('*** There is no null value in the DataFrame.')
    else:
        print("*** How many null values?")
        for col in df.columns :
            print("** column '{}' : {:.2f}%".format(col, 100*(df[col].isnull().sum() / df[col].shape[0])))

def colNameChange(df, lower=True, space_underbar=True): 
    cols = pd.Series(df.columns)
    if lower==True:
        cols = cols.apply(lambda x: x.lower())                      
    if space_underbar==True:
        cols = cols.apply(lambda x: x.replace(' ', '_'))
    df.columns = cols
    return df

#### Display ####
def h1(df):
    print(df.shape); display(df.head(1))
    
def t1(df):
    print(df.shape); display(df.tail(1))
    
def h1t1(df):
    print(df.shape); display(df.head(1), df.tail(1))
    
