import pandas as pd
import numpy as np
df = pd.read_csv(r"D:\DEPI-Projects\DEPI_AIS2_ml\AMIT\src\Data Science\Session_3_Data-PreProcessing\train.csv")


def check_datatype(dtypes,n_unique):
    
    dtypes = df.dtypes
    n_unique = df.nunique()
    return pd.DataFrame({"Dtype":dtypes,
             "num_unique":n_unique}).T
    
def check_ratio_null(null,ratio):
    '''
    check null values and the percentage of each null row
    '''
    null = df.isnull().sum()
    ratio = (null /df.shape[0])*100
    return pd.DataFrame({"Null":null,
                "ratio %":ratio}).T
        
    