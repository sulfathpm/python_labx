import numpy as np
import pandas as pd

data={
    'name':['anna','fasmi','asna','thasni','amri','afi','farsana'],
    'age':[21,22,23,34,45,56,32],
    'place':['ekm','pkd','klm','klm','idukki','tsr','kkd'],
    'salary':[20000,12000,2345,4535,3212,4643,3242]
}

df=pd.DataFrame(data)

# new_row={
#             'name':'farsana',
#             'age':25,
#             'place':'kkd',
#             'salary':3043
# }
# pos=2
# insert_row=pd.concat(df[:pos],
#             pd.DataFrame([new_row]),
#             df[pos:]).reset_index(drop=True)
# print(insert_row)

print(df.head())
# print("new-arr:",insert_row.head)

print(df.tail())
print("info:",df.info())
print("describe:",df.describe())
grp_df=df.groupby('place')['salary'].mean()
print(grp_df)

oldest_person = df.loc[df['age'].idxmax()]

# oldest_person=df.loc[df['age'].idxmax()]
print(oldest_person)