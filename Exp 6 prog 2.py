
matrix = []

print("Enter the elements of the 3x3 matrix:")

for i in range(3):
    row = []
    for j in range(3):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

print("\nThe matrix is:")

for row in matrix:
    print(row)

print("\nSum of each row:")
for i in range(3):
    row_sum = sum(matrix[i])
    print("Row", i + 1, "=", row_sum)

print("\nSum of each column:")
for j in range(3):
    column_sum = 0
    for i in range(3):
        column_sum += matrix[i][j]
    print("Column", j + 1, "=", column_sum)
