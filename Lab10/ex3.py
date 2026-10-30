# Create a dataframe from a dictionary

import pandas as pd

data = {
   'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
   'Age': [25, 30, 35, 40, 22],
   'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
   'Salary': [70000, 80000, 120000, 90000, 60000]
}

# Converting the dictionary into a DataFrame
df = pd.DataFrame(data) # df is common nickname for a dataframe

# Displaying the dataframe
print(df)

