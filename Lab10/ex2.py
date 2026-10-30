# create a pandas dataframe
# do simple states from the lists
import pandas as pd

ages = [25, 30, 35, 40, 22]
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
gender = ["M", "F", "M", "M", "F"]

raw_data = zip(ages, gender)

# Create a Pandas DataFrame
df = pd.DataFrame(raw_data, columns=['Age', 'Gender'], index=names)

summary = df.describe() # Get summary statistics for the DataFrame
print(summary)

# Calculate average age by gender
average_age_by_gender = df.groupby('Gender')['Age'].mean()
print("\nAverage Age by Gender:")
print(average_age_by_gender)