import pandas as pd
import numpy as np
import csv

data=[
    ['name','rollno'],['anna',6],['fasmi',11],['amri',9]
]

csv_file_path='mod4/pandas/sample.txt'

with open(csv_file_path,mode='w') as file:
    writer=csv.writer(file)
    writer.writerows(data)
