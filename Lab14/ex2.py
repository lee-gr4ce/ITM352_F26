# Grab 3 month interest rate from the US treasury website

import pandas as pd
from urllib import request as req

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603" 

webpage = req.urlopen(url)
df = pd.read_html(webpage)
print("Columns:", df[0].columns)

int_rate_table = df[0] # even tho we only have 1 DF still need to specify it

# Print the 1 month interest rates
print("1 Month Interest Rates:")

for index, row in int_rate_table.iterrows():
    print(row["1 mo"])

