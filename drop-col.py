# import pandas with shortcut 'pd' 
import pandas as pd 

excel_file_path = 'final-AP-ff.csv'  # Replace with the path to your Excel file
df = pd.read_csv(excel_file_path, encoding_errors='ignore')
df.drop(columns=df.columns[3:5], inplace=True)
df.to_csv('last-ap.csv', index=False)
