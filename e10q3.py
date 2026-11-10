import matplotlib.pyplot as plt

# Data
marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# Histogram
plt.subplot(1, 2, 1)
plt.hist(marks, bins=5)
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")

# Box Plot
plt.subplot(1, 2, 2)
plt.boxplot(marks)
plt.title("Box Plot")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()