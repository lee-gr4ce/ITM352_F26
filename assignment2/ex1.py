# Load the CSV file and print the first 10 rows

csv_file = 'https://drive.google.com/file/d/1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA'

import pandas as pd
import pyarrow as pa

try:
    df = pd.read_csv(csv_file, engine = 'pyarrow', on_bad_lines='skip')
    outfile = 'sales_data_test.csv'
    df.head(10).to_csv(outfile, index=False)  
    print(f"First 10 rows of {csv_file} saved to {outfile}")
    
except Exception as e:
    print(f"Error occurred while reading the CSV file: {e}")
