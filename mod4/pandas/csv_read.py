import pandas as pd
import csv

df=pd.read_csv('mod4/pandas/sample.txt')
series1=pd.Series(df['name'])
print(series1)