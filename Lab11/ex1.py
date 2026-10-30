sales_csv = 'https://drive.google.com/uc?export=download&id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K'

import pandas as pd
import pyarrow as pa

try:
    df = pd.read_csv(sales_csv, engine = 'pyarrow', on_bad_lines='skip')
    print(df.head())
except Exception as e:
    print(f"Error occurred while reading the CSV file: {e}")
