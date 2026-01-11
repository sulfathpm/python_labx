import pandas as pd
data={
    'name':['anna','fasmi','sulu'],
    'age':[20,21,22],
    'city':['ernakulam','palakad','ernakulam']
}

df=pd.DataFrame(data)
print(df)
print(df['name'])