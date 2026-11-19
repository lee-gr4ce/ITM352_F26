import pandas as pd
from sodapy import Socrata

client = Socrata("data.cityofchicago.org", None)

# Specify the specific JSON file
json_file = "rr23-ymwb"

results = client.get(json_file, limit=500)

# Convert to Pandas DataFrame
df = pd.DataFrame.from_records(results)
df.head()

vehicles = df[["public_vehicle_number", "vehicle_fuel_source"]]
print("Public Vehicles and fuel sources:")

vehicles.info()
vehicles_by_fuel = vehicles.groupby("vehicle_fuel_source").count()
print(vehicles_by_fuel)