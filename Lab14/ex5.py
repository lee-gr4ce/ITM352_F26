# Get a JSON file from city of chicagos data portal and analyze driver types
import pandas as pd
import requests as req

url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"
response = req.get(url)

response_json = response.json()

print("Driver Types and Counts:")
print(response_json)

response_df = pd.DataFrame.from_records(response_json)
response_df.columns = ["driver_type", "count"]
response_df = response_df.set_index("driver_type")

print(response_df)