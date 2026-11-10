import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Rahul', 'Aman', 'Rohan', 'Priya'],
    'Age': [20, 21, 19, 22],
    'Marks': [85, 90, 78, 95]
}

df = pd.DataFrame(data)

# Displaying DataFrame
print("Original DataFrame:")
print(df)

# Adding a new column
df['City'] = ['Delhi', 'Mumbai', 'Pune', 'Bhubaneswar']

print("\nAfter adding a column:")
print(df)

# Adding a new row
df.loc[4] = ['Raj', 20, 88, 'Kolkata']

print("\nAfter adding a row:")
print(df)

# Updating a value
df.loc[0, 'Marks'] = 92

print("\nAfter updating marks:")
print(df)

# Deleting a column
df = df.drop('City', axis=1)

print("\nAfter deleting City column:")
print(df)