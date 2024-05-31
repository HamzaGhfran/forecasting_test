import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/home/hamza/Downloads/archive (1)/Electric_Production.csv')
df['DATE'] = pd.to_datetime(df['DATE'])
df['DATE'] = df['DATE'].dt.strftime('%Y-%d-%m')
df['DATE'] = pd.to_datetime(df['DATE'])
def time_feature(df):
    """
    This function take dataframe as input.
    Function caluclate day_of_week, day_of_month and month_of_year
     and return dataframe
    """
    df['day'] = df['DATE'].dt.day
    df['day_of_week'] = df['DATE'].dt.dayofweek
    df['month'] = df['DATE'].dt.month
   
    return df




df = time_feature(df)

print(df.head())