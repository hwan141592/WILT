import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)

def map_many(iterable, function, *other):
    if other:
        return map_many(map(function, iterable), *other)
    return map(function, iterable)

def round2d(x):
    return round(x, 2)

def sigmoid(x):
    # lambda x: 1/(1+np.exp(-x))   # sigmoid
    return 1 / (1 + np.exp(-x))

def relu(x):
    return max(0.0, x)

def leaky_relu(x):
    # address the problem of zero gradients for negative value
    if x > 0:
        return x
    else:
        return 0.01 * x
    
def get_li_key_col_cand(df):
    li_key_col_cand = []
    for col in df.columns:
        if df.shape[0] - df[col].nunique() == 0:
            li_key_col_cand.append(col)
        else:
            pass
    print('*** key column candidates: {}'.format(li_key_col_cand))
    return li_key_col_cand

def get_year(dt):
    return str(pd.to_datetime(dt).year)

def get_month(dt):
    t = str(pd.to_datetime(dt).month)
    if len(t)==1:
        return '0'+t
    elif len(t)==2:
        return t
    else:
        return 'NA'
    
def get_date(dt):
    t = str(pd.to_datetime(dt).day)
    if len(t)==1:
        return '0'+t
    elif len(t)==2:
        return t
    else:
        return 'NA'

def get_group(val):
    x,y = val.split('T')
    return x

def get_team(val):
    x,y = val.split('T')
    return y.split(' ')[1]

def h1(df):
    print(df.shape)
    display(df.head(1))

def h2(df):
    print(df.shape)
    display(df.head(2))    
    
def h1t1(df):
    print(df.shape)
    display(df.head(1), df.tail(1))

def h2t2(df):
    print(df.shape)
    display(df.head(2), df.tail(2))