import numpy as np
import pandas as pd

data=[[111,'anna'],
     [222,'fasmi'],
     [333,'asna']]


df=pd.DataFrame(data)
print(df)
print(df[1])


data={
    'name':['anna','fasmi','asna'],
    'age':[21,22,23],
    'place':['ekm','pkd','ekm']
}
df=pd.DataFrame(data)
print(df)
print(df['age'])
