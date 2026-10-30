# Name: Grace Lee
# Date: 10/30/2026

import pandas as pd
import numpy as np

csv_file = 'https://drive.google.com/uc?export=download&id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K'

# Tell Pandas to print all columns when displaying a DataFrame
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format) # Format float values to 2 decimal places

# no need any for loops since this algorithm will run through every single row in the dataframe
try:
    df = pd.read_csv(csv_file, engine = 'python', on_bad_lines='skip')
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    print(df.head())

    # Calculate sales total per row
    df['sales'] = df['quantity'] * df['unit_price']

    # Create a pivot table aggregating sales by state and order type
    pivot_table = pd.pivot_table(df,
                                 values='sales',
                                 index='customer_state',
                                 columns=['order_type', 'customer_type'],
                                 aggfunc=np.sum,
                                 margins=True,
                                 margins_name='Average Sales')
    print(pivot_table)


except Exception as e:
    print(f"Error occurred while reading the CSV file: {e}")
