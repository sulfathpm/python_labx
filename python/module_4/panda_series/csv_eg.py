import csv

# Data
data = [
    ['Roll No', 'Name'],
    [1, 'Abhijith K Sajeev'],
    [2, 'Adhuljith T J'],
    [3, 'Alwyn Peter'],
    [4, 'Amaljoe'],
    [5, 'Anandu Dinesan']
]

# File path for the CSV file
csv_file_path = 'abcPandas.csv'

# Open the file in write mode
with open(csv_file_path, mode='w', newline='') as file:
    # Create a csv.writer object
    writer = csv.writer(file)

    # Write data to the CSV file
    writer.writerows(data)

print("CSV file created successfully!")
