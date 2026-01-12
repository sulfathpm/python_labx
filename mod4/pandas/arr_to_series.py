import numpy as np
import pandas as pd

data=np.array([np.sin(0),np.sin(30),np.sin(45),np.sin(60),np.sin(90)])
ser=pd.Series(data)
print(ser)
print(ser[:3])


data2=np.array(['anna','fasmi','asna','thasni','amri','afi'])
series1=pd.Series(data2)
print(series1)
series2=pd.Series(data2,index=range(101,107))
print(series2)