# read a json file of taxi trip data anad create a dataframe from single stats
import pandas as pd

# Read the JSON file into a DataFrame
results_df = pd.read_json('Taxi_Trips.json')

# Display the first few rows of the DataFrame
print(results_df.head(6)) # default is 5 rows, but we can adjust the parameters

# Display basic statistics about the DataFrame
print(results_df.describe()) # this will give us basic statistics about the numeric columns in the dataframe

median = results_df['fare'].median()
print("The median fare value is: ", median)