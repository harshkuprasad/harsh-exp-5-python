import pandas as pd

# Creating a DataFrame
data = {
    'Maths': [80, 85, 90, 95, 100],
    'Science': [75, 80, 85, 90, 95],
    'English': [60, 65, 70, 75, 80]
}

df = pd.DataFrame(data)

# Displaying DataFrame
print("DataFrame:")
print(df)

# Calculating correlation
correlation = df.corr()

print("\nCorrelation between columns:")
print(correlation)