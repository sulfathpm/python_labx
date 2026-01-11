import pandas as pd
import numpy as np

data = np.array([np.sin(0), np.sin(30), np.sin(45), np.sin(60), np.sin(90)])
ser = pd.Series(data)
print(ser)

data = np.array(['Jennath','Jeremia','Jiphin','Joyal','Jyothish'])
ser = pd.Series(data)
print(ser)

