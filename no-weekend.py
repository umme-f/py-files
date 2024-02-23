import pandas as pd
import numpy as np

# Load the Excel file into a pandas DataFrame
file_path = r'output_file_without_japanese_holidays_2023_mem.csv'
df = pd.read_csv(file_path)

# Assuming your DataFrame has a column named 'Date' containing datetime values
df['(PDH-CSV 4.0) (Tokyo Standard Time)(-540)'] = pd.to_datetime(df['(PDH-CSV 4.0) (Tokyo Standard Time)(-540)'])

# Identify weekends (Saturday and Sunday)
weekend_mask = (df['(PDH-CSV 4.0) (Tokyo Standard Time)(-540)'].dt.dayofweek == 5) | (df['(PDH-CSV 4.0) (Tokyo Standard Time)(-540)'].dt.dayofweek == 6)

# Filter out weekends
df = df[~weekend_mask]

# Save the modified DataFrame back to the Excel file
df.to_csv('output_file-noweekend.csv', index=False)