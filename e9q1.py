import pandas as pd

# Creating a Pandas Series
s = pd.Series([10, 20, 30, 40, 50])

# Displaying the Series
print("Original Series:")
print(s)

# Accessing elements
print("\nFirst Element:", s[0])

# Adding 10 to each element
print("\nAfter adding 10:")
print(s + 10)

# Displaying maximum and minimum values
print("\nMaximum:", s.max())
print("Minimum:", s.min())

# Displaying sum and mean
print("Sum:", s.sum())
print("Mean:", s.mean())