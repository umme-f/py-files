# ======================= To change csv col name using python ========================

import pandas as pd

# Read the CSV file
# file_path = 'final-ap-cpu'  # Replace 'your_file.csv' with the actual file path
df = pd.read_csv('modified_file-apmem-time.csv', encoding_errors="ignore")

# Rename col
# df= df.rename(columns={'(PDH-CSV 4.0) (Tokyo Standard Time)(-540)':'DateTime'})
df= df.rename(columns={'Bytes Total/sec':'Memory Committed Bytes'})

# Save the modified DataFrame back to a new CSV file or overwrite the existing one
output_file_path = 'modified_file-apmem-time.csv'  # Replace 'modified_file.csv' with the desired output file path
df.to_csv(output_file_path, index=False)