import matplotlib.pyplot as plt
import numpy as np

# Pie Chart Data
subjects = ['Python', 'Java', 'C', 'DBMS']
marks = [85, 75, 90, 80]

# Pie Chart
plt.subplot(1, 2, 1)
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Pie Chart")

# Contour Plot Data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Contour Plot
plt.subplot(1, 2, 2)
plt.contour(X, Y, Z)
plt.title("Contour Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.tight_layout()
plt.show()