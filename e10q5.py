import matplotlib.pyplot as plt

# Creating 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
z = [3, 6, 9, 12, 15]

# Drawing 3D plot
ax.plot(x, y, z)

ax.set_title("3D Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

plt.show()