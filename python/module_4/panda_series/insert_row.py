import pandas as pd
data={
    'name':['anna','fasmi','sulu'],
    'age':[20,21,22],
    'city':['ernakulam','palakad','ernakulam']
}

df=pd.DataFrame(data)
print(df)
print(df['name'])

new_row={'name':'Asna','age':21,'city':'idukki'}
position=2
df = pd.concat([df[:position], 
                pd.DataFrame([new_row]), 
                df[position:]]).reset_index(drop=True)
print(df)
