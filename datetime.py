import pandas as pd

# Read the CSV file
file_path = 'datetime.csv'  
df = pd.read_csv(file_path)

# Change column names
column_name_mapping = {
    '(PDH-CSV 4.0) (Tokyo Standard Time)(-540)': 'DateTime',
    '\\13SVNNAP\Memory\Committed Bytes': 'Memory Committed Bytes',
}
df.rename(columns=column_name_mapping, inplace=True)

# Convert 'Timestamp' column to datetime format
df['DateTime'] = pd.to_datetime(df['DateTime'])

# Convert 'Timestamp' to string
df['Timestamp_str'] = df['DateTime'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Split the DataFrame into two based on a condition (for example, time greater than noon)
condition = df['DateTime'].dt.hour >= 12
df['Timestamp_greater_than_noon'] = df['DateTime'][condition]
df['Timestamp_less_than_noon'] = df['DateTime'][~condition]

# Save the split columns to new columns
df['Timestamp_greater_than_noon_str'] = df['Timestamp_greater_than_noon'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['Timestamp_less_than_noon_str'] = df['Timestamp_less_than_noon'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Remove rows based on a given time range (for example, keep only rows between 2 PM and 4 PM)
start_time = pd.to_datetime('08:00:00')
end_time = pd.to_datetime('17:15:00')

df = df[(df['DateTime'] >= start_time) & (df['DateTime'] <= end_time)]

# Drop unnecessary columns if needed
df.drop(['Timestamp_greater_than_noon', 'Timestamp_less_than_noon'], axis=1, inplace=True)

# Save the modified DataFrame back to a new CSV file or overwrite the existing one
output_file_path = 'modified_file-apcpu.csv'  # Replace 'modified_file.csv' with the desired output file path
df.to_csv(output_file_path, index=False)

