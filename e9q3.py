import pandas as pd

# Reading CSV file
df1 = pd.read_csv("data.csv")

print("CSV File Data:")
print(df1)

# Reading JSON file
df2 = pd.read_json("data.json")

print("\nJSON File Data:")
print(df2)