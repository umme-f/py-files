import pandas as pd
from datetime import datetime
# Load the Excel file into a pandas DataFrame
excel_file_path = 'modified_file-apcpu_2col.csv'  # Replace with the path to your Excel file
df = pd.read_csv(excel_file_path)


# Convert the 'DateTime' column to datetime format
df['DateTime'] = pd.to_datetime(df['DateTime'])
df['DateTime']=datetime.fromtimestamp('DateTime')

df