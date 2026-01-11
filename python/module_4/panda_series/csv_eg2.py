import pandas as pd

# Read CSV file
df = pd.read_csv("abcPandas.csv")

# Create a Series from the Name column
ser = pd.Series(df['Name'])

# Get first 5 values
data = ser.head()

print(data)
