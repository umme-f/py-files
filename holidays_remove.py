import pandas as pd

# Load the Excel file into a pandas DataFrame
file_path = r'cp-combine-ap.csv'

df = pd.read_csv(file_path)

# Assuming your DataFrame has a column named 'Date' containing datetime values
column_name = '(PDH-CSV 4.0) (Tokyo Standard Time)(-540)'

# List of Japanese holidays for the year 2023
japanese_holidays_2023 = ['2023-01-01', '2023-01-02', '2023-01-09', '2023-02-11', '2023-03-21', '2023-04-29', '2023-05-03', '2023-05-04', '2023-05-05', '2023-07-17', '2023-08-11', '2023-09-18', '2023-09-23', '2023-11-03', '2023-11-23', '2023-12-23']

# Removing data
df = df[~df[column_name].isin(japanese_holidays_2023)]

# Save the modified DataFrame back to the Excel file
df.to_csv('output_file_without_japanese_holidays_2023_cpu.csv', index=False)
