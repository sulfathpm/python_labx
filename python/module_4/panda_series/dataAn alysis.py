import pandas as pd

# Exploratory Data Analysis
data = {
    'Name': ['Sreekumar', 'Suparna', 'Surya', 'Thasneem', 'Tony', 'Vishnupriya'],
    'Age': [22, 20, 20, 21, 21, 22],
    'City': ['Washington', 'New York', 'Los Angeles', 'Chicago', 'Miami', 'Boston'],
    'Salary': [48000, 50000, 60000, 45000, 70000, 55000]
}

df = pd.DataFrame(data)

# First 5 rows
print(df.head())

# Last 5 rows
print(df.tail())

# Information about columns, data types, and missing values
print(df.info())

# Summary statistics
print(df.describe())

# Group by City and calculate average salary
grouped_df = df.groupby('City')['Salary'].mean()
print(grouped_df)

# Find the oldest person
oldest_person = df.loc[df['Age'].idxmax()]
print(oldest_person)
