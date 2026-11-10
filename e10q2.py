import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 30, 20]

subjects = ['Python', 'Java', 'C', 'DBMS']
marks = [85, 75, 90, 80]

# Creating two plots
plt.subplot(1, 2, 1)
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.subplot(1, 2, 2)
plt.bar(subjects, marks)
plt.title("Bar Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()