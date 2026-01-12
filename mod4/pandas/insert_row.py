import numpy as np
import pandas as pd

data={
    'name':['anna','fasmi','asna'],
    'age':[21,22,23],
    'place':['ekm','pkd','ekm']
}
df=pd.DataFrame(data)
# print(df)
# print(df['age'])

new_row={
    'name':'sulu',
    'age':23,
    'place':'ekm'
}

pos=1

insert_row=pd.concat([df[:pos],
                      pd.DataFrame([new_row]),
                      df[pos:]]).reset_index(drop=True)
# print(df)
print(insert_row)