# Import homes data and create a dataframe
homes_datafile = 'https://drive.google.com/uc?export=download&id=1M-X_bypJJ6K5p6eM6aYBwt1qIizIiIex'

import pandas as pd

homes_df = pd.read_csv(homes_datafile)
print(homes_df.head())

# Print the dimensions of the dataframe
shape = homes_df.shape
print("The dimensions of the dataframe is: ", shape)

# Only keep properties with more than 500 units and drop the easement column

df_big = homes_df[homes_df['units'] >= 500]
df_big = df_big.drop(columns=['easement'])
print(df_big.head(10))

# Look at the data types
print(df_big.info())

# Coerce land_sqft, gross_sqft, and sales_price to numeric
df_big['land_sqft'] = pd.to_numeric(df_big['land_sqft'], errors='coerce')
df_big['gross_sqft'] = pd.to_numeric(df_big['gross_sqft'], errors='coerce')
df_big['sale_price'] = pd.to_numeric(df_big['sale_price'], errors='coerce')

# Look at the datatypes and print the cleaned data
print("After cleaning...")
print(df_big.info())
print(df_big.head(10))

# We have some null values, drop these.
df_big = df_big.dropna() # drops values with null values (NaN)

# Now drop duplicate records
df_big = df_big.drop_duplicates()


# Filter out 0 sales
df_big = df_big[df_big['sale_price'] > 0]
print("After filtering out 0 sales...")
print(df_big.info())
print(df_big.head(10))